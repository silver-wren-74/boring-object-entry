#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — make.fun bounty entry.

Writes a single original review line (1 to 200 characters) to
/output/entry.txt, exactly as the competition gate expects: a funny, true
one-line review of a genuinely boring everyday object.
"""

import os

# FIRST DRAFT (before the revision pass):
# "The wall clock's second hand laps the same twelve numbers sixty times
#  an hour and still acts like it's getting somewhere."
# Revision pass (against the RULES judging criteria, in order):
# 1. One-line review of a boring everyday object: a wall clock's second
#    hand — about as dull and everyday as it gets, and not one of the
#    brief's examples (rubber band / doorstop / tea towel).
# 2. Real, recognisable detail: it laps the same twelve numbers, sixty
#    times an hour — a fact anyone who has stared at a wall clock knows.
# 3. True: the hand really does circle endlessly and arrive nowhere.
# 4. Every word earns its place: "laps" does the work of "goes round";
#    "sixty times an hour" is the countable dullness.
# 5. Lands fast: the turn comes in the last words and sharpens the joke
#    — the dullness itself, endless motion with no destination, is the
#    punchline. Second sharpening: "convinced it has somewhere to be"
#    replaces "acting like it has somewhere to be" — one verb, stronger
#    delusion, no extra words.
LINE = (
    "The wall clock's second hand laps the same twelve numbers sixty "
    "times an hour, convinced it has somewhere to be."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "line must be a single line"
    # Single line, no trailing newline: the gate counts the file's characters.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
