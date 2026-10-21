#!/usr/bin/env python3
"""Compile the book from its project root, keeping all output in build/."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys


def find_compiler(engine, override):
    """Prefer an explicit compiler, then PATH, then the Windows user install."""
    if override:
        compiler = Path(override).expanduser().resolve()
        if not compiler.is_file():
            raise FileNotFoundError("Compiler does not exist: {}".format(compiler))
        return str(compiler)

    compiler = shutil.which(engine)
    if compiler:
        return compiler

    if engine == "tectonic" and os.name == "nt":
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            compiler = Path(local_app_data) / "Programs" / "Tectonic" / "tectonic.exe"
            if compiler.is_file():
                return str(compiler)

    raise FileNotFoundError(
        "Cannot find {}. Install it, add it to PATH, or pass --compiler PATH.".format(
            engine
        )
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--engine", choices=("tectonic", "xelatex"), default="tectonic"
    )
    parser.add_argument("--compiler", metavar="PATH", help="compiler executable path")
    args = parser.parse_args()

    project = Path(__file__).resolve().parents[1]
    output = project / "build"

    try:
        compiler = find_compiler(args.engine, args.compiler)
        output.mkdir(parents=True, exist_ok=True)

        if args.engine == "tectonic":
            command = [
                compiler,
                "--keep-logs",
                "--keep-intermediates",
                "--outdir",
                str(output),
                "main.tex",
            ]
            # Tectonic repeats typesetting automatically until references settle.
            subprocess.run(command, cwd=project, check=True)
        else:
            command = [
                compiler,
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                "-output-directory={}".format(output),
                "main.tex",
            ]
            # Three passes cover the table of contents and cross-references.
            for _ in range(3):
                subprocess.run(command, cwd=project, check=True)

        if not (output / "main.pdf").is_file():
            raise FileNotFoundError("The compiler did not produce build/main.pdf.")
    except subprocess.CalledProcessError as error:
        print(
            "Build failed. Check the compiler output above and build/main.log "
            "if the compiler produced one.",
            file=sys.stderr,
        )
        return error.returncode or 1
    except OSError as error:
        print("Build failed: {}".format(error), file=sys.stderr)
        return 1

    print("Built build/main.pdf", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
