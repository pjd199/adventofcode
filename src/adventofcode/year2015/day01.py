from adventus import fetch

# load puzzle input
data = fetch(1, 2015)

# solve part one
print(data.count("(") - data.count(")"))

# solve part two
floor = 0
for i, move in enumerate(data, 1):
    floor += 1 if move == "(" else -1   
    if floor < 0:
        print(i)
        break
