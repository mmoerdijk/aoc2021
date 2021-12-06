import copy
import numpy as np


def check_neighbours(i, j, map):

    low_point = [True] * 4
    direction = [True] * 4
    ni, nj = i - 1, j
    if ni >= 0:
        if map[i][j] >= map[ni][nj]:
            low_point[0] = False
    else:
        direction[0] = False
    # check right
    ni, nj = i + 1, j
    if ni < max_i:
        if map[i][j] >= map[ni][nj]:
            low_point[1] = False
    else:
        direction[1] = False
    # check up
    ni, nj = i, j - 1
    if nj >= 0:
        if map[i][j] >= map[ni][nj]:
            low_point[2] = False
    else:
        direction[2] = False
    # check down
    ni, nj = i, j + 1
    if nj < max_j:
        if map[i][j] >= map[ni][nj]:
            low_point[3] = False
    else:
        direction[3] = False

    return low_point, direction


def make_basin(
    i, j, map, basin_size,
):

    low_point, directions = check_neighbours(i, j, map)
    map[i][j] = 9
    if any(low_point):
        basin_size += 1
        if directions[0] and map[i - 1][j] != 9:
            basin_size = make_basin(i - 1, j, map, basin_size,)
        if directions[1] and map[i + 1][j] != 9:
            basin_size = make_basin(i + 1, j, map, basin_size,)
        if directions[2] and map[i][j - 1] != 9:
            basin_size = make_basin(i, j - 1, map, basin_size,)
        if directions[3] and map[i][j + 1] != 9:
            basin_size = make_basin(i, j + 1, map, basin_size,)

    return basin_size


input_file = open("input.txt")
map = []
all_values = []
for line in input_file.readlines():
    map.append([int(a) for a in line[:-1]])
    all_values += [int(a) for a in line[:-1]]


map = np.array(map, dtype=int)
min_values = []
size_basin = []
max_i = len(map)
max_j = len(map[0])
for i in range(len(map)):
    for j in range(len(map[i])):
        low_point, directions = check_neighbours(i, j, map)
        if all(low_point):
            print([i, j])
            size = make_basin(i, j, copy.deepcopy(map), 0)
            size_basin.append(size)
            min_values.append(copy.deepcopy(map[i][j]))


values = np.array(min_values) + 1
size_basin = sorted(size_basin, reverse=True)
print(f"Answer 1: {values.sum()}")
print(f"Answer 2: {size_basin[0]*size_basin[1]*size_basin[2]}")
