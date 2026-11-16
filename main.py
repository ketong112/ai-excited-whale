#!/usr/bin/env python3
"""Whale in the Library — make.fun ai-excited-01 entry.

Copies entry.png byte-for-byte into the output directory named by the
MAKEFUN_OUTPUT_DIR environment variable (defaults to a local "out"
directory). The image itself is the entry: a colossal humpback whale
breaching up through the glass roof of a grand old library at night.
"""

import os
import shutil
import sys


def main() -> int:
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    if not os.path.isfile(source):
        print(f"error: entry image not found: {source}", file=sys.stderr)
        print("error: run from the repository directory containing entry.png",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, destination)
    print(f"copied {source} -> {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
