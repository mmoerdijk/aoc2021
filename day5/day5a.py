# load data
import itertools
import numpy as np

input_file = open("input.txt")

lines = []
for line in input_file.readlines():
    lines.append(list(itertools.chain(*[[int(i.strip()) for i in p.split(",")] for p in line[:-1].split("->")])))

lines = np.array(lines)
gz = np.amax(lines) + 1
map = np.zeros((gz, gz))


for x1, y1, x2, y2 in lines:
    if x1 == x2 or y1 == y2:
        map[min(y1, y2): max(y1, y2) + 1, min(x1, x2): max(x1, x2) + 1] += 1

print(f"Answer 1: {np.sum(map[:]>=2)}")
#
for x1, y1, x2, y2 in lines:
    if abs(x1 - x2) == abs(y1 - y2):
        for step in range(abs(y2-y1)+1):
            dx = np.sign(x2-x1)
            dy = np.sign(y2-y1)
            map[y1+step*dy, x1+step*dx] += 1

print(f"Answer 2: {np.sum(map[:]>=2)}")
