from hashlib import md5
from itertools import count

from adventus import fetch

# load input
key = fetch(4, 2015).strip()


# solver function
def solver(zeros: int):
    for i in count():
        hash = md5(f"{key}{i}".encode(), usedforsecurity=False).hexdigest()
        if hash.startswith("0" * zeros):
            return i


# solve part one
print(solver(5))

# solve part two
print(solver(6))
