"""Advent of Code 2025.

Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""

from collections import deque
from functools import cache
from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(7, 2025)
    data = puzzle.input
    data = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

    grid = {
        (x, y): value
        for y, row in enumerate(data.splitlines())
        for x, value in enumerate(row)
    }
    start_x, start_y = next((x, y) for (x, y), value in grid.items() if value == "S")
    grid[(start_x, start_y + 1)] = "|"

    # solve part one
    queue = deque([(start_x, start_y + 1)])
    active = set()
    while queue:
        x, y = queue.pop()
        if (x, y + 1) in grid:
            if grid[(x, y + 1)] == ".":
                grid[(x, y + 1)] = "|"
                queue.appendleft((x, y + 1))
            elif grid[(x, y + 1)] == "^":
                for dx in (-1, 1):
                    if grid[(x + dx, y + 1)] == ".":
                        grid[(x + dx, y + 1)] = "|"
                        queue.appendleft((x + dx, y + 1))
                        active.add((x, y + 1))

    max_x, max_y = ((max(a)) for a in zip(*grid.keys()))
    print(
        "\n".join(
            "".join(grid[(x, y)] for x in range(0, max_x + 1))
            for y in range(0, max_y + 1)
        )
    )
    puzzle.submit_answer_one(len(active))

    # solve part two
    grid = {
        (x, y): value
        for y, row in enumerate(data.splitlines())
        for x, value in enumerate(row)
    }

    @cache
    def search(x: int, y: int) -> int:
        grid[(x, y)] = "|"
        if (x, y + 1) not in grid:
            return 1
        if grid[(x, y + 1)] == "^":
            q = 0
            for dx in (-1, 1):
                if grid[(x + dx, y + 1)] == ".":
                    grid[(x + dx, y + 1)] = "|"
                    q += 1 + search(x + dx, y + 1)
            return q
        return search(x, y + 1)

    print(search(start_x, start_y + 1))

    puzzle.submit_answer_two(None)


if __name__ == "__main__":
    solve()
