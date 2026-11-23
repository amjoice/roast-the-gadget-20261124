"""One-line roast: the gadget/app used every day.

Writes a single original roast line to /output/entry.txt.
Standard library only, deterministic, no network.

The gate accepts 1 to 200 characters, so the line is checked
against that limit before anything is written.
"""

import os

ROAST = "My banking app crashed, then asked me to rate it \u2014 like a waiter asking how the meal was while I'm still choking."

MAX_CHARS = 200


def main() -> None:
    line = ROAST.strip()
    if not line or len(line) > MAX_CHARS:
        raise ValueError("roast line must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
