"""Advent of Code 2015.

Day 12: JSAbacusFramework.io

https://adventofcode.com/2015/day/12
"""

from json import loads
from re import findall
from typing import Any

from adventus import Puzzle


def count(obj: Any) -> int:
    if isinstance(obj, int):
        return int(obj)
    if isinstance(obj, list):
        return sum(count(x) for x in obj)
    if isinstance(obj, dict) and "red" not in obj.values():
        return sum(count(x) for x in obj.values())
    return 0


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(12, 2015)

    # solve part one
    puzzle.submit_answer_one(sum(int(x) for x in findall(r"-?\d+", puzzle.input)))

    # solve part two
    puzzle.submit_answer_two(count(loads(puzzle.input)))


if __name__ == "__main__":
    solve()
