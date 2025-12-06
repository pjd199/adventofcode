"""Advent of Code 2025.

Day 2: Gift Shop

https://adventofcode.com/2025/day/2
"""

from re import findall, fullmatch

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(2, 2025)
    data = puzzle.input

    # solve part one
    puzzle.submit_answer_one(
        sum(
            number
            for first, last in findall(r"(\d+)-(\d+)", data)
            for number in range(int(first), int(last) + 1)
            if fullmatch(r"(\d+)\1", str(number))
        )
    )

    # solve part two
    puzzle.submit_answer_two(
        sum(
            number
            for first, last in findall(r"(\d+)-(\d+)", data)
            for number in range(int(first), int(last) + 1)
            if fullmatch(r"(\d+)\1+", str(number))
        )
    )


if __name__ == "__main__":
    solve()
