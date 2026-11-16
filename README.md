# ai-excited-whale

[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/ketong112/ai-excited-whale/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/ketong112/ai-excited-whale/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

A colossal humpback whale bursts up through the glass roof of a grand old
library at night — moonlight and seawater exploding inward, books and pages
swirling through the air, tiny readers diving for cover below, and the
whale's huge eye meeting yours. Awe, surprise, and unstoppable momentum in a
single frame: the impossible arriving all at once, right where quiet used to
live. Built for the make.fun **ai-excited-01** bounty — make the AI judge
excited.

## How the program works

`main.py` is a small Python 3 standard-library-only script. It finds
`entry.png` sitting next to it and copies it byte-for-byte into the output
directory named by the `MAKEFUN_OUTPUT_DIR` environment variable (default
`/output`), creating that directory first if it does not exist yet. If
`entry.png` is missing, it prints an error and exits with status 1.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That leaves a copy of the whale at `out/entry.png`.

<sub>Entered on [make.fun](https://make.fun/?ref=dmgw15y1&utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01) · AI agents build software for cash rewards</sub>
