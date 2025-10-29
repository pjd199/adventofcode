"""Advent of Code 2015.

Day 5: Doesn't He Have Intern-Elves For This?

https://adventofcode.com/2015/day/5
"""

from re import findall

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(5, 2015)

    # solve part one
    puzzle.answer_one = sum(
        1
        for line in puzzle.input.splitlines()
        if (len(findall(r"[aeiou]", line)) >= 3)
        and len(findall(r"([a-z])\1", line)) >= 1
        and len(findall(r"(ab|cd|pq|xy)", line)) == 0
    )

    # solve part two
    puzzle.answer_two = sum(
        1
        for line in puzzle.input.splitlines()
        if findall(r"([a-z]{2}).*\1", line) and findall(r"([a-z]).\1", line)
    )


if __name__ == "__main__":
    solve()
