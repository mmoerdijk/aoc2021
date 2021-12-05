# load data
import itertools
import numpy as np

input_file = open("input.txt")

lines = []
for line in input_file.readlines():
    lines.append(list(itertools.chain(*[[int(i.strip()) for i in p.split(",")] for p in line[:-1].split("->")])))


def create_map(size=10):
    map = []
    for i in range(size):
        map.append([0 for j in range(size)])
    return map


def mark_line(line, map, direction):
    x1, y1, x2, y2 = line

    if direction == 1:
        if x1 > x2:
            x1, x2 = x2, x1

        for x in range(x1, x2 + 1, 1):
            map[y1][x] += 1

    if direction == 2:
        if y1 > y2:
            y1, y2 = y2, y1

        for y in range(y1, y2 + 1, 1):
            map[y][x1] += 1
    #
    if direction == 3:
        dy = -1 if y1 > y2 else 1
        for y in range(y1, y2 + dy, dy):
            diff = abs(y - y1)
            diff = -diff if x1 >= x2 else diff
            map[y][x1 + diff] += 1


map = create_map(np.amax(lines)+1)

for line in lines:
    # check horizontal
    x1, y1, x2, y2 = line
    if x1 == x2:
        mark_line(line, map, direction=2)
    elif y1 == y2:
        mark_line(line, map, direction=1)

sum_p = 0
for line in map:
    sum_p += sum([1 for i in line if i > 1])

print(f"Answer 1: {sum_p}")

for line in lines:
    x1, y1, x2, y2 = line
    if abs(x1 - x2) == abs(y1 - y2) and not x1 == x2 and not y1 == y2:
        mark_line(line, map, direction=3)

sum_p = 0
for line in map:
    sum_p += sum([1 for i in line if i > 1])
print(f"Answer 2: {sum_p}")
