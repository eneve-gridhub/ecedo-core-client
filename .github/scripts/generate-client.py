"""Run Gridbot's Swagger pipeline with this repository's development setup."""

import os
import re
import shutil
import subprocess
import sys
from functools import partial
from pathlib import Path

from gridbot.ecedo_swagger.pipeline import (
    CODEGEN_TIMEOUT_SECONDS,
    MAX_JAVA_HEAP,
    PipelineError,
    PipelineInputs,
    run_pipeline,
)


LEGACY_BASE_CLASS = rb"extends \PHPUnit_Framework_TestCase"
LIFECYCLE_SIGNATURE = re.compile(
    rb"(function (?:setUpBeforeClass|setUp|tearDown|tearDownAfterClass)\(\))(?=[ \t]*\r?$)",
    re.MULTILINE,
)


def modernize_generated_tests(test_dir: Path) -> None:
    for path in test_dir.rglob("*Test.php"):
        source = path.read_bytes()
        if LEGACY_BASE_CLASS in source:
            updated = source.replace(LEGACY_BASE_CLASS, rb"extends \PHPUnit\Framework\TestCase")
            updated = LIFECYCLE_SIGNATURE.sub(rb"\1: void", updated)
            path.write_bytes(updated)


def generate(repo: Path, jar: Path, spec: Path, output: Path) -> None:
    java = shutil.which("java")
    if java is None:
        raise PipelineError("Java is not available.")

    # Set the package path explicitly so Gridbot can find lib/ at the output root.
    command = [
        java,
        f"-Xmx{MAX_JAVA_HEAP}",
        "-jar", str(jar),
        "generate",
        "-i", str(spec),
        "-l", "php",
        "--additional-properties", "packagePath=.",
        "-o", str(output),
    ]
    java_env = {
        key: value
        for key, value in os.environ.items()
        if key in {"PATH", "HOME", "JAVA_HOME", "LANG"}
    }
    try:
        subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            timeout=CODEGEN_TIMEOUT_SECONDS,
            env=java_env,
        )
    except subprocess.CalledProcessError as error:
        raise PipelineError(f"Swagger Codegen failed: {error.stderr.strip()[-300:]}") from None
    except subprocess.TimeoutExpired:
        raise PipelineError("Swagger Codegen timed out.") from None
    if not (output / "lib").is_dir():
        raise PipelineError("Swagger Codegen produced no lib/ folder.")

    # Gridbot checks out the requested base branch before invoking the generator.
    if (repo / "phpunit.dist.xml").is_file():
        modernize_generated_tests(output / "test")
        (output / ".travis.yml").unlink(missing_ok=True)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: generate-client.py <repo-dir> <codegen-jar>", file=sys.stderr)
        return 2

    repo, jar = map(Path, sys.argv[1:])
    try:
        result = run_pipeline(
            repo, jar, PipelineInputs.from_env(), generator=partial(generate, repo)
        )
    except Exception as error:
        print(f"::error::{type(error).__name__}: {error}")
        return 1

    print(result.as_json())
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with Path(summary).open("a", encoding="utf-8") as handle:
            handle.write(f"Branch `{result.branch}` pushed ({result.files_changed} files).\n")
            handle.writelines(f"- {note}\n" for note in result.notes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
