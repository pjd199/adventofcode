from adventus import fetch

# import puzzle import
data = fetch(3, 2015)

# solver function
def solver(moves):
    x, y = (0, 0)
    houses = set([(x, y)])
    delta_x = {">": 1, "v": 0, "<": -1, "^": 0}
    delta_y = {">": 0, "v": 1, "<": 0, "^": -1}
    for move in moves:
        x += delta_x[move]
        y += delta_y[move]
        houses.add((x, y))
    return houses


# solve part one
print(len(solver(data)))

# solve part two
print(len(solver(data[::2]) | solver(data[1::2])))
