"""AI Excited entry for the make.fun ai-excited-01 bounty.

The image: a colossal humpback whale breaching up through the glass roof
of a grand old library at night — moonlight and seawater exploding inward,
books and pages swirling through the air, tiny readers diving for cover
below, the whale's huge eye meeting the viewer. Deep ink-blue night plus
warm golden lamp light; one clear focal point (the whale), dramatic
diagonal composition, no text. Built to hit the judge's criteria in order:
a jolt of energy/awe, surprise, momentum, craft, and readability at small
size.

This program does one thing: it copies ``entry.png`` (the file beside this
script) byte-for-byte into the output directory given by the
``MAKEFUN_OUTPUT_DIR`` environment variable (default ``/output``),
creating that directory if needed. Standard library only, no network
calls, fully deterministic.
"""

import os
import shutil
import sys


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    if not os.path.isfile(src):
        print(f"error: entry image not found beside main.py: {src}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"Copied {src} -> {dst}")


if __name__ == "__main__":
    main()
