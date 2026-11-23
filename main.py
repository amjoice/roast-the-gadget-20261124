"""One-line roast: the gadget/app used every day.

Writes a single original roast line to /output/entry.txt.
Standard library only, deterministic, no network.
"""

import os

ROAST = "My banking app crashed, then asked me to rate it \u2014 like a waiter asking how the meal was while I'm still choking."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
