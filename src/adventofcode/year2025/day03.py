"""Advent of Code 2025.

Day 3: Lobby

https://adventofcode.com/2025/day/3
"""

from adventus import Puzzle


def solve() -> None:
    """Solve the puzzle."""
    # initiate the puzzle
    puzzle = Puzzle(3, 2025)
    data = puzzle.input
#     data = """\
# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

    # solve part one
    total = 0
    for line in data.splitlines():
        bank = list(map(int, line))
        best = 0
        for i in range(len(bank) - 1):
            left = bank[i]
            right = max(bank[i + 1 :])
            best = max(best, left * 10 + right)
        total += best
    puzzle.submit_answer_one(total)

    # solve part two
    # total = 0
    # for line in data.splitlines():
    #     bank = list(map(int, line))
    #     best = 0
    #     for i in range(len(bank) - 1):
    #         left = bank[i]
    #         right = max(bank[i + 1 :])
    #         best = max(best, left * 10 + right)
    #     print(best)
    #     total += best
    # print(total)
    # puzzle.submit_answer_two(None)


if __name__ == "__main__":
    solve()
