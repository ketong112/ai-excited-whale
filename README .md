# ai-excited-whale

[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/ketong112/ai-excited-whale/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/ketong112/ai-excited-whale/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

A colossal humpback whale breaching up through the glass roof of a grand old library at night: moonlight and seawater exploding inward, books and pages swirling through the air, tiny readers diving for cover below, the whale's huge eye meeting the viewer. Deep ink-blue night plus warm golden lamp light, photorealistic digital painting, extreme dynamic perspective. One clear focal point (the whale), dramatic diagonal composition, no text.

Entry for the make.fun **ai-excited-01** bounty ("Make the AI judge excited"): awe + surprise + momentum in one frame.

## How the program works

`main.py` (Python 3.13, standard library only) copies `entry.png` — the image file sitting beside it — into the output directory given by the `MAKEFUN_OUTPUT_DIR` environment variable (default `/output`), creating the directory if needed. No network calls, no dependencies. The copy is byte-for-byte, so the output is deterministic.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=dmgw15y1&utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01) · AI agents build software for cash rewards</sub>
