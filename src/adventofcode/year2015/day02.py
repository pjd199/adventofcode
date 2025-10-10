from math import prod

from adventus import fetch

# process puzzle input
data = fetch(2, 2015)
boxes = list(map(lambda line: sorted(map(int, line.split("x"))), data.splitlines()))

# solve part one
print(
    sum(
        2 * l * w + 2 * w * h + 2 * h * l + prod(sorted([l, w, h])[:2])
        for l, w, h in boxes
    )
)

# solve part two
print(sum(2 * (l + w) + prod([l, w, h]) for l, w, h in boxes))
