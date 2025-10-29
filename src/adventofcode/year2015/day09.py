"""Advent of Code 2015.

Day 9: All in a Single Night

https://adventofcode.com/2015/day/9
"""

from itertools import pairwise, permutations
from re import findall

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(9, 2015)

    routes = {}
    cities = set()

    for a, b, distance in findall(r"(\w+) to (\w+) = (\d+)", puzzle.input):
        routes |= {(a, b): int(distance), (b, a): int(distance)}
        cities |= {a, b}

    # solve part one
    puzzle.answer_one = min(
        sum(routes[x] for x in pairwise(path))
        for path in permutations(cities, len(cities))
    )

    # solve part two
    puzzle.answer_two = max(
        sum(routes[x] for x in pairwise(path))
        for path in permutations(cities, len(cities))
    )


if __name__ == "__main__":
    solve()
