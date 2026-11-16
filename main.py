#!/usr/bin/env python3
"""Whale in the Library — make.fun ai-excited-01 entry.

Copies entry.png byte-for-byte into the output directory named by the
MAKEFUN_OUTPUT_DIR environment variable (default /output).
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(
            f"error: entry.png is missing beside the script ({source})",
            file=sys.stderr,
        )
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(source, dest)
    print(f"copied {source} ({source.stat().st_size} bytes) -> {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
