"""Advent of Code 2025.

Day 1: Secret Entrance

https://adventofcode.com/2025/day/1
"""

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(1, 2025)

    directions = {"R": 1, "L": -1}

    # solve part one
    dial = 50
    count = 0
    for line in puzzle.input.splitlines():
        rotation = int(line[1:]) * directions[line[0]]
        dial = (dial + rotation) % 100
        if dial == 0:
            count += 1
    puzzle.answer_one = count

    # # solve part two
    dial = 50
    count = 0
    for line in puzzle.input.splitlines():
        turns, rotation = divmod(int(line[1:]), 100)
        count += turns
        if line[0] == "R":
            if dial + rotation >= 100:
                count += 1
        else:
            if dial > 0 and (dial - rotation) <= 0:
                count += 1
        dial = (dial + rotation * directions[line[0]]) % 100
    puzzle.answer_two = count


if __name__ == "__main__":
    solve()
