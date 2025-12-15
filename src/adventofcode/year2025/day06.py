"""Advent of Code 2025.

Day 6: Trash Compactor

https://adventofcode.com/2025/day/6
"""

from math import prod
from re import finditer

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(6, 2025)
    data = puzzle.input

    functions = {"*": prod, "+": sum}

    # solve part one
    puzzle.submit_answer_one(
        sum(
            functions[op](map(int, numbers))
            for *numbers, op in zip(*(line.split() for line in data.splitlines()))
        )
    )

    # solve part two
    result = 0
    *digits, operators = data.splitlines()
    for m in finditer(r"([*+]) *", operators + " "):
        grid = [line[m.start() : m.end()] for line in digits]
        numbers = [
            int("".join(number).strip())
            for number in zip(*grid)
            if any(char.isnumeric() for char in number)
        ]
        result += functions[m[1]](numbers)

    puzzle.submit_answer_two(result)


if __name__ == "__main__":
    solve()
