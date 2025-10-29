"""Advent of Code 2015.

Day 6: Probably a Fire Hazard

https://adventofcode.com/2015/day/6
"""

from re import findall

import numpy as np
from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(6, 2015)

    # solve part one
    lights = np.full((1000, 1000), False)
    for line in puzzle.input.splitlines():
        command, x1, y1, x2, y2 = map(
            lambda x: int(x) if x.isnumeric() else x,
            findall(r"([a-z ]*) (\d+),(\d+) through (\d+),(\d+)", line)[0],
        )
        region = lights[y1 : (y2 + 1), x1 : (x2 + 1)]
        match command:
            case "turn on":
                region[:] = True
            case "turn off":
                region[:] = False
            case "toggle":
                region[:] = ~region

    puzzle.answer_one = np.count_nonzero(lights)

    # solve part two
    lights = np.full((1000, 1000), 0)
    for line in puzzle.input.splitlines():
        command, x1, y1, x2, y2 = map(
            lambda x: int(x) if x.isnumeric() else x,
            findall(r"([a-z ]*) (\d+),(\d+) through (\d+),(\d+)", line)[0],
        )
        region = lights[y1 : (y2 + 1), x1 : (x2 + 1)]
        match command:
            case "turn on":
                region += 1
            case "turn off":
                region[:] = np.maximum(region - 1, 0)
            case "toggle":
                region += 2

    puzzle.answer_two = np.sum(lights)


if __name__ == "__main__":
    solve()
