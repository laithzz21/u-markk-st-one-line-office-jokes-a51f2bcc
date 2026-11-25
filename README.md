# One-Line Office Joke — make.fun entry

[![make.fun](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![Rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/laithzz21/u-markk-st-one-line-office-jokes-a51f2bcc/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![Reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/laithzz21/u-markk-st-one-line-office-jokes-a51f2bcc/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)

## The entry

> The printer only jams when the document is urgent, the boss is watching, and you've already told everyone you fixed it.

**Character count:** 119

## How to run

```bash
python3 main.py
```

Prints exactly the entry text above to stdout and exits 0. The script validates the entry in-code (single line, under 200 characters, no stray whitespace) and verifies it by staging to a temp file and reading it back before printing. If stdout is unavailable, it falls back to writing the entry to `$MAKEFUN_OUTPUT` or `./output/entry.txt`.
