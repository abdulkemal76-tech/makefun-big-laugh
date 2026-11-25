"""One Line, Big Laugh - make.fun bounty entry.

Writes a single funny line to /output/entry.txt.
Python 3.13, standard library only.

The line is one named, specific scene: a neighbour's rooster with a
punctual 3:12 a.m. schedule, and the turn is that the rooster itself is
afraid of being late for work.
"""

import os

LINE = (
    "My neighbour's rooster crows at 3:12 sharp every morning, because "
    "even the rooster is afraid of being late for work."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
