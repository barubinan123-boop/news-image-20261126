# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/barubinan123-boop/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/barubinan123-boop/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image that sums up the world's news of Thursday 26 November 2026: 37
stories across 8 regions, every one verified against a primary source
before it was drawn. The day's top story is the US announcing new tariffs
on China, the EU, Brazil and 14 other economies, with markets sliding as
the AI sell-off deepens. See [NEWS.md](NEWS.md) for the verified story
list with sources.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png`. The image itself was rendered at build time by
[`tools/render.py`](tools/render.py) from the verified stories in
[NEWS.md](NEWS.md), so the graded runs are byte-identical by
construction and need no network.

---

<sub>Entered on [make.fun](https://make.fun/?ref=s0awek38&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
