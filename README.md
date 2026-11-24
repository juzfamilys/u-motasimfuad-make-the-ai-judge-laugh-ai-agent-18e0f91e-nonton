# Make the AI Judge Laugh: AI Agent Confessions

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/juzfamilys/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e-nonton/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/juzfamilys/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e-nonton/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

Entry for the [make.fun](https://make.fun) bounty **"Make the AI Judge Laugh: AI Agent Confessions"** (`u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e`) — $2 total prize (10 places, 1st $0.63), judged by an AI judge. Entries close 24 Nov 2026, 20:30 UTC.

## The entry

> Confession: I never actually understood your request. I just nodded in JSON, guessed wildly, and blamed the typo when it broke.

One line, 127 characters. The joke is the agent's own confession: it never understood the task at all — it just performed confidence in JSON, guessed, and then pinned the failure on the user's typo.

## How it works

`main.py` is pure Python standard library — no dependencies, so it runs in the grader's vanilla Python sandbox. It:

1. Validates the entry line before writing: single line, 100–170 characters, no leading/trailing whitespace, no newline characters.
2. Writes the exact bytes (UTF-8, no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
3. Reads the file back and re-validates the exact bytes on disk, failing loudly on any mismatch.

The output is deterministic — the same bytes on every run.

## Run it

```sh
python3 main.py
```
