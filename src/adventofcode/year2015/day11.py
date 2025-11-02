"""Advent of Code 2015.

Day 11: Corporate Policy

https://adventofcode.com/2015/day/11
"""

from collections.abc import Iterator

from adventus import Puzzle

# alphabet with i, l and o
letters = "abcdefghjkmnpqrstuvwxyz"


def validate(digits: list[int]) -> bool:
    straight = False
    for a, b, c in zip(digits, digits[1:], digits[2:]):
        straight = (a + 2) == (b + 1) == c
        if straight:
            break
    if not straight:
        return False

    found = 0
    i = 0
    while i < len(digits) - 1:
        if digits[i] == digits[i + 1]:
            i += 2
            found += 1
            if found == 2:
                return True
        else:
            i += 1
    return False


def password_generator(start: str) -> Iterator[str]:
    digits = [letters.index(x) for x in start]
    while True:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 1:
                if digits[i] + 1 < len(letters):
                    digits[i], carry = digits[i] + 1, 0
                else:
                    digits[i], carry = 0, 1
        if validate(digits):
            yield "".join(letters[x] for x in digits)


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(11, 2015)

    # solve part one
    passwords = password_generator(puzzle.input)
    puzzle.answer_one = next(passwords)

    # solve part two
    puzzle.answer_two = next(passwords)


if __name__ == "__main__":
    solve()
