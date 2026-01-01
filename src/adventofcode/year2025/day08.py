"""Advent of Code 2025.

Day 8: Playground

https://adventofcode.com/2025/day/8
"""

from collections import Counter
from itertools import combinations
from heapq import nsmallest
from math import dist, prod
from operator import itemgetter

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(8, 2025)

    # parse the input
    boxes = [tuple(map(int, line.split(","))) for line in puzzle.input.splitlines()]

    # caculate and sort the direct line distances
    pairs = nsmallest(10000, ((dist(a, b), (a, b)) for a, b in combinations(boxes, 2)))

    circuits = [{box} for box in boxes]
    for i, (_, (a, b)) in enumerate(pairs):
        # merge two circuits
        left = next(circuit for circuit in circuits if a in circuit)
        right = next(circuit for circuit in circuits if b in circuit)
        if left != right:
            left |= right
            circuits.remove(right)
        if i == 999:
            # solved part one
            counter = Counter(len(x) for x in circuits)
            result = prod(sorted(counter.keys(), reverse=True)[:3])
            puzzle.submit_answer_one(result)
        if len(circuits) == 1:
            # solved part two
            puzzle.submit_answer_two(a[0] * b[0])
            break


if __name__ == "__main__":
    solve()
