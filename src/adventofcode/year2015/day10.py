"""Advent of Code 2015.

Day 10: Elves Look, Elves Say

https://adventofcode.com/2015/day/10
"""

from itertools import groupby

from adventus import Puzzle


def look_and_say(digits: str, count: int) -> int:
    for _ in range(count):
        digits = "".join(
            f"{sum(1 for _ in group)}{key}" for key, group in groupby(digits)
        )
    return len(digits)


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(10, 2015)

    # solve part one
    puzzle.submit_answer_one(look_and_say(puzzle.input, 40))

    # solve part two
    puzzle.submit_answer_two(look_and_say(puzzle.input, 50))


if __name__ == "__main__":
    solve()
