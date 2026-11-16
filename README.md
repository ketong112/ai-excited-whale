# AI Excited — Whale in the Library

A colossal humpback whale breaching up through the glass roof of a grand
old library at night: moonlight and seawater exploding inward, books and
pages swirling through the air, tiny readers diving for cover below, the
whale's huge eye meeting the viewer. Deep ink-blue night plus warm golden
lamp light, photorealistic digital painting, extreme dynamic perspective.
One clear focal point (the whale), dramatic diagonal composition, no text.

Entry for the make.fun **ai-excited-01** bounty ("Make the AI judge
excited"): awe + surprise + momentum in one frame.

## How the program works

`main.py` (Python 3.13, standard library only) copies `entry.png` — the
image file sitting beside it — into the output directory given by the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`), creating
the directory if needed. No network calls, no dependencies. The copy is
byte-for-byte, so the output is deterministic.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png`.
