"""Advent of Code 2015.

Day 3: Perfectly Spherical Houses in a Vacuum

https://adventofcode.com/2015/day/3
"""

from adventus import Puzzle


# visit function
def visit(moves):
    x, y = (0, 0)
    houses = set([(x, y)])
    delta_x = {">": 1, "v": 0, "<": -1, "^": 0}
    delta_y = {">": 0, "v": 1, "<": 0, "^": -1}
    for move in moves:
        x += delta_x[move]
        y += delta_y[move]
        houses.add((x, y))
    return houses


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(3, 2015)

    # solve part one
    puzzle.answer_one = len(visit(puzzle.input))

    # solve part two
    puzzle.answer_two = len(visit(puzzle.input[::2]) | visit(puzzle.input[1::2]))


if __name__ == "__main__":
    solve()


# solve part one
print()

# solve part two
print()
