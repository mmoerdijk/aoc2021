from copy import deepcopy
from collections import Counter

# Load data
input_file = open("input.txt")
nodes = {}
for line in input_file.read().split("\n"):
    current_nodes = line.split("-")
    for n in [i for i in current_nodes if i not in nodes]:
        nodes[n] = set()
    nodes[current_nodes[0]].add(current_nodes[1])
    nodes[current_nodes[1]].add(current_nodes[0])


def connect_path(paths, n):
    res = []
    for p in paths:
        # Get connections for node
        connections = nodes[p[-1]]
        valid_connections = []
        for c in connections:
            # Check if lower is maximum 1 lower case node that has n connections or start node
            if c.islower() and c in p and max(Counter([i for i in p if i.islower()]).values()) == n or c == "start":
                continue
            # end of the road for this path
            if c == "end":
                res.append(deepcopy(p) + [c])
                continue
            # valid connection
            valid_connections.append(c)
        # Make new paths
        new_paths = [deepcopy(p) + [vc] for vc in valid_connections]
        # and continue ...
        res += connect_path(paths=new_paths, n=n)
    return res


print(f"Answer 1: {len(connect_path(paths=[['start']], n=1))}")
print(f"Answer 2: {len(connect_path(paths=[['start']], n=2))}")
