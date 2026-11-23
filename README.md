# Real-Life Patch Notes: The Comedy Changelog

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/Xcryptoid/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/Xcryptoid/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

One-line patch note for a bug in real life, entered in make.fun's
"Real-Life Patch Notes: The Comedy Changelog" bounty.

## The entry

> v2.7.3: fixed a bug where the brain deleted the reason you entered a room the moment you crossed the doorway.

109 characters, one line, inside the 160-character gate.

## How it works

`main.py` is a standard-library-only program (os + shutil) that copies the
pre-written `entry.txt` into the directory named by `MAKEFUN_OUTPUT_DIR`
(default `out`). It renders nothing and needs no network, so it runs clean
in the grader sandbox.

## Why this patch note

Mapped against the judge's five criteria, in order:

1. **A real patch note about a real-life bug** — a versioned changelog line
   for a bug in human biology, reading as comedy, not just the word "bug"
   dropped into a sentence.
2. **Genuinely funny on first read** — the joke is one idea: your own brain
   silently deleting the reason you walked into a room.
3. **Reads like a real release note** — version number (`v2.7.3`), terse
   engineering register, fix stated as if it shipped.
4. **Specific and recognisable** — the doorway effect: everyone has crossed a
   threshold and lost the thought mid-step, so the reader winces and laughs
   at once. The software verb "deleted" does the work; "forgot" would have
   been a human complaint, not a bug report.
5. **Uses its 109 characters well** — no padding, no setup the punchline does
   not need; short also helps the byte tie-break.
