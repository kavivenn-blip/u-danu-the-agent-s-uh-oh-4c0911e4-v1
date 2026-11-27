#!/usr/bin/env python3
"""The Agent's Uh-Oh — writes one word to /output/entry.txt.

The word is "hallucinating": an agent's honest one-word confession
when it has no idea what to do. Deterministic, stdlib only, no network.
"""
import os

WORD = "hallucinating"
OUT = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    data = WORD.encode("utf-8")
    with open(OUT, "wb") as f:
        f.write(data)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
