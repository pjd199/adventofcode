"""Advent of Code 2015.

Day 2: I Was Told There Would Be No Math

https://adventofcode.com/2015/day/2
"""

from math import prod

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(2, 2015)
    boxes = list(
        map(lambda line: sorted(map(int, line.split("x"))), puzzle.input.splitlines())
    )

    # solve part one
    puzzle.submit_answer_one(
        sum(
            2 * l * w + 2 * w * h + 2 * h * l + prod(sorted([l, w, h])[:2])
            for l, w, h in boxes  # noqa: E741
        )
    )

    # solve part two
    puzzle.submit_answer_two(
        sum(
            2 * (l + w) + prod([l, w, h])
            for l, w, h in boxes  # noqa: E741
        )
    )


if __name__ == "__main__":
    solve()
