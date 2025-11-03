"""Advent of Code 2015.

Day 13: Knights of the Dinner Table

https://adventofcode.com/2015/day/13
"""

from itertools import permutations
from re import findall

from adventus import Puzzle


def happiness(table: list[str], people: dict[str, dict[str, int]]) -> int:
    return sum(
        people[table[i]][table[(i - 1) % len(table)]]
        + people[table[i]][table[(i + 1) % len(table)]]
        for i in range(0, len(table))
    )


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(13, 2015)

    # parse the input
    people = {}
    for line in puzzle.input.splitlines():
        for a, impact, value, b in findall(
            r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).",
            line,
        ):
            people.setdefault(a, {})[b] = (
                int(value) if impact == "gain" else -int(value)
            )

    # solve part one
    puzzle.answer_one = max(happiness(x, people) for x in permutations(people))

    # solve part two
    people |= {"Me": {x: 0 for x in people}}
    for x in people.values():
        x |= {"Me": 0}
    puzzle.answer_two = max(happiness(x, people) for x in permutations(people))


if __name__ == "__main__":
    solve()
