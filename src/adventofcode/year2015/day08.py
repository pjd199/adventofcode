"""Advent of Code 2015.

Day 8: Matchsticks

https://adventofcode.com/2015/day/8
"""

from re import findall

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(8, 2015)

    # solve part one
    puzzle.submit_answer_one(
        sum(
            len(x) - len(findall(r"\\x[0-9a-f]{2}|\\\"|\\\\|.", x[1:-1]))
            for x in puzzle.input.splitlines()
        )
    )

    # solve part two
    puzzle.submit_answer_two(
        sum(len(findall(r"\\|\"", x)) + 2 for x in puzzle.input.splitlines())
    )


if __name__ == "__main__":
    solve()
