#!/usr/bin/env python3
"""Write the one-line office joke entry to /output/entry.txt.

Deterministic, stdlib-only, no network, no randomness.
"""

import os

ENTRY = (
    # One line, 95 characters: inside the competition's 1-200 character gate.
    "I finally got promoted: my title gained the word 'senior' "
    "and my salary gained the word 'soon'."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
