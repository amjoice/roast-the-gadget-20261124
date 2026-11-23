#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original one-line roast (at most 200 characters) of an
everyday gadget to /output/entry.txt.

The line is a fixed string: no randomness, no network, no input, so every
run produces byte-identical output.
"""

import os

ROAST = (
    "My banking app crashed, then asked me to rate it \u2014 like a waiter "
    "asking how the meal was while I'm still choking."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
