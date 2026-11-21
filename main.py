"""The joke about the demo (make.fun bounty the-joke-about-the-demo-20261121-0551).

Writes a single one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, no network, no randomness, no input:
the same joke, byte for byte, on every run.
"""

import os

JOKE = (
    "My coding agent wrote the fix, had another agent review it, "
    "and they both agreed the bug was me."
)


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 280, "joke must be 1-280 Unicode code points"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
