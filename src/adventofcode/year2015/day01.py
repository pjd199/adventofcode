"""Advent of Code 2015.

Day 1: Not Quite Lisp

https://adventofcode.com/2015/day/1
"""

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(1, 2015)

    # solve part one
    puzzle.submit_answer_one(puzzle.input.count("(") - puzzle.input.count(")"))

    # solve part two
    floor = 0
    for i, move in enumerate(puzzle.input, 1):
        floor += 1 if move == "(" else -1
        if floor < 0:
            puzzle.submit_answer_two(i)
            break


if __name__ == "__main__":
    solve()
