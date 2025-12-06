"""Advent of Code 2025.

Day 4: Printing Department

https://adventofcode.com/2025/day/4
"""

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(4, 2025)
    data = puzzle.input

    locations = {
        (x, y)
        for y, row in enumerate(list(data.splitlines()))
        for x, item in enumerate(row)
        if item == "@"
    }
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    # solve part one
    puzzle.answer_one = sum(
        1
        for x, y in locations
        if sum(1 for dx, dy in offsets if (x + dx, y + dy) in locations) < 4
    )

    # solve part two
    result = 0
    while True:
        accessible = {
            (x, y)
            for x, y in locations
            if sum(1 for dx, dy in offsets if (x + dx, y + dy) in locations) < 4
        }
        result += len(accessible)
        locations -= accessible
        if not accessible:
            break
    puzzle.answer_two = result


if __name__ == "__main__":
    solve()
