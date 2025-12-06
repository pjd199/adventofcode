"""Advent of Code 2015.

Day 4: The Ideal Stocking Stuffer

https://adventofcode.com/2015/day/4
"""

from hashlib import md5
from itertools import count

from adventus import Puzzle


# solver function
def search(key: str, zeros: int):
    for i in count():
        hash = md5(f"{key}{i}".encode(), usedforsecurity=False).hexdigest()
        if hash.startswith("0" * zeros):
            return i


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(4, 2015)

    # solve part one
    puzzle.submit_answer_one(search(puzzle.input, 5))

    # solve part two
    puzzle.submit_answer_two(search(puzzle.input, 6))


if __name__ == "__main__":
    solve()
