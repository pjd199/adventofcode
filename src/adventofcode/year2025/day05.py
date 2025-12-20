"""Advent of Code 2025.

Day 5: Cafeteria

https://adventofcode.com/2025/day/5
"""

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(5, 2025)
    data = puzzle.input
    #     data = """3-5
    # 10-14
    # 16-20
    # 12-18

    # 1
    # 5
    # 8
    # 11
    # 17
    # 32"""

    first_section, second_section = data.split("\n\n")
    ranges = [tuple(map(int, line.split("-"))) for line in first_section.split()]
    items = list(map(int, second_section.split()))
    print(ranges)
    print(items)

    # solve part one
    fresh = sum(
        1 for item in items if any(lower <= item <= upper for lower, upper in ranges)
    )
    print(fresh)
    puzzle.submit_answer_one(
        sum(
            1
            for item in items
            if any(lower <= item <= upper for lower, upper in ranges)
        )
    )

    # solve part two
    puzzle.submit_answer_two(None)


if __name__ == "__main__":
    solve()
