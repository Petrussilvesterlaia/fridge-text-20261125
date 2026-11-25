#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes the one line a smart fridge would text its owner at 3am to
/output/entry.txt. The line is a single line of at most 140 characters.
"""

import os
import sys

# The entry: one line, written by this program, nothing else.
ENTRY = "3am. I've been humming since 2019 and you still open me like I might have grown a pizza overnight."

MAX_CHARS = 140


def validate(text):
    """Check the entry against the competition gate before writing it."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for ch in text:
        if ord(ch) < 32 or ord(ch) == 127:
            raise ValueError("entry holds a control character: U+%04X" % ord(ch))


def main():
    validate(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read it back and confirm the file holds exactly the validated line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written file differs from the validated entry")
    validate(written)
    print("wrote %s (%d characters)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
