from astar_python.astar import Astar
import numpy as np

# load
input_file = open("input_debug.txt")
map = []
for line in input_file.read().split("\n"):
    map += [[int(c) for c in line]]

map = np.array(map)
print(map)

def calculate_risk(path, map):
    risk=0
    for p in path[1:]:
        risk+=map[p[0],p[1]]
        map[p[0], p[1]] = -1
    return risk

start_path = []
x=0
y=0
for i in range(map.shape[0]*2-1):
    start_path.append([x,y])
    if i%2:
        x+=1
    else:
        y+=1
print(calculate_risk(start_path, map))




print(map)
