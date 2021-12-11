import numpy as np
# Load data
input_file = open("input.txt")
grid = []
for line in input_file.readlines():
    grid.append([int(c) for c in line[:-1]])
grid = np.array(grid)
# Process data
mask = np.array([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
sum_flashes, step = 0, 0
while len((grid == 0).nonzero()[0]) != grid.size:
    grid += 1
    while True:
        nines = (grid > 9).nonzero()
        if nines[0].size == 0:
            break
        if step <= 100:
            sum_flashes += nines[0].size
        # increase all neighbours of nines
        for x, y in zip(*nines):
            grid[x, y] = -1
            for nx, ny in mask + (x, y):
                if all(j in range(grid.shape[0]) for j in [nx, ny]) and grid[nx, ny] != -1:
                    grid[nx, ny] += 1

    grid[grid == -1] = 0
    step += 1

print(f"Answer 1: {sum_flashes}")
print(f"Answer 2: {step}")
