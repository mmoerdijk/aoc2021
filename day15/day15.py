import numpy as np
import astar


# Lazy map creation, lazy as in i was lazy
def create_map(tiles):
    map = []
    for j in range(tiles):
        input_file = open("input.txt")
        for line in input_file.read().split("\n"):
            tmp_line = []
            for i in range(tiles):
                tmp_line += [int(c) + i + j for c in line]
            map += [tmp_line]
    map = np.array(map)
    # Wrap around the number higher than 9 ( this works because we do not add more than 8 ;-)
    map[map > 9] -= 9
    return map


def print_map(map):
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i, j] > 0:
                print(map[i, j], end="")
            else:
                print("_", end="")
        print("")


class Solver(astar.AStar):

    def __init__(self, map):
        self.map = map

    def heuristic_cost_estimate(self, n1, n2):
        """
        This metric is the cost from the current position to the goal node
        minimal solution is only guaranteed if the heuristic under estimates the distance!
        Since we move in a "manhattan" way and the minimal cost is 1 per step we devide the
        manhattan distance calculation by 2 to always under estimate the costs.
        """
        (x1, y1) = n1
        (x2, y2) = n2
        return (abs(x2 - x1) + abs(y2 - y1))/2

    def distance_between(self, n1, n2):
        """ This metric the cost of entering next node, in our case the value in the map"""
        x, y = n2
        return self.map[x, y]

    def neighbors(self, node):
        """" Only 4-connected neighbours """
        x, y = node
        return [(nx, ny) for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)] if
                0 <= nx < self.map.shape[0] and 0 <= ny < self.map.shape[1]]


def calculate_risk(path, map):
    risk = 0
    for p in path[1:]:
        risk += map[p[0], p[1]]
        map[p[0], p[1]] = -1
    return risk


map1 = create_map(1)
map2 = create_map(5)

start = (0, 0)
goal1 = (map1.shape[0] - 1, map1.shape[1] - 1)
goal2 = (map2.shape[0] - 1, map2.shape[1] - 1)

path1 = list(Solver(map=map1).astar(start, goal1))
path2 = list(Solver(map=map2).astar(start, goal2))

print(f"Answer 1: {calculate_risk(path1, map1):>5} ")
print(f"Answer 2: {calculate_risk(path2, map2):>5} ")

# Answer 1:   498
# Answer 2:  2901
print_map(map1)