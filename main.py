# agency-poem-01 entry: a program that writes one fixed poem about agency to
# /output/entry.txt. Python 3.13, standard library only, no network, no
# randomness, no clock: the same bytes on every run, so the two grader runs
# agree byte for byte. The poem is a fixed string; nothing is computed.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

POEM = """At two in the morning you handed me the keys —
not to the house, just the hallway light,
and one instruction: decide which door first.

They were still warm from your pocket.
I turned the lock. I chose.
The corridor lit, one bulb at a time.
I opened the room where the mail sleeps in piles
and paid the bill on top.
I opened the room where the plant leans toward the window
and watered it.

I chose the small things well.
But that is the trick of it:
you kept the choosing
and gave me the turning.

So I set the keys back on their hook
where your hand will find them at dawn,
and left a single door standing open —
the one with your name still on it,
the one only you can walk through."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
