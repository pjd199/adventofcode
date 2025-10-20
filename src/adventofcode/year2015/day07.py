"""Advent of Code 2015.

Day 7: Some Assembly Required

https://adventofcode.com/2015/day/7
"""

from functools import cache
from re import fullmatch

from adventus import Puzzle

instructions = {}


@cache
def find(wire: str) -> int:
    if wire.isnumeric():
        return int(wire)
    if instructions[wire].isnumeric():
        return int(instructions[wire])
    m = fullmatch(
        r"([a-z0-9]+)? ?([A-Z]+) ?([a-z0-9]+)|([a-z]+)", instructions[wire])
    left, gate, right, link = m.groups()
    match gate:
        case "AND":
            return int(find(left)) & int(find(right))
        case "OR":
            return int(find(left)) | int(find(right))
        case "LSHIFT":
            return int(find(left)) << int(right)
        case "RSHIFT":
            return int(find(left)) >> int(right)
        case "NOT":
            return ~int(find(right)) & 0xFFFF
        case None:
            return int(find(link))


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(7, 2015)
    for line in puzzle.input.splitlines():
        ins, wire = line.split(" -> ")
        instructions[wire] = ins

    # solve part one
    puzzle.answer_one = find("a")

    # solve part two
    find.cache_clear()
    instructions["b"] = puzzle.answer_one
    puzzle.answer_two = find("a")


if __name__ == "__main__":
    solve()
