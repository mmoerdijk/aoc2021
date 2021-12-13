import time

# Load data
input_file = open("input.txt")
nodes = {}
for line in input_file.read().split("\n"):
    current_nodes = line.split("-")
    for n in [i for i in current_nodes if i not in nodes]:
        nodes[n] = set()
    nodes[current_nodes[0]].add(current_nodes[1])
    nodes[current_nodes[1]].add(current_nodes[0])


def connect_path(paths, one_double=True):
    res = []
    for p, double in paths:
        # Get connections for node
        connections = nodes[p[-1]]
        valid_connections = []
        for c in connections:
            d = double
            if c == "start":
                continue
            # Check if lower is maximum 1 lower case node that has n connections or start node
            if c.islower() and c in p:
                if d or not one_double:
                    continue
                d = True

            # end of the road for this path
            if c == "end":
                res.append(([], d))
                # res.append([])
                continue
            # valid connection
            valid_connections.append((c, d))
        # Make new paths
        new_paths = [(p + [vc], dc) for vc, dc in valid_connections]
        # and continue ...
        res += connect_path(paths=new_paths, one_double=one_double)
    return res




ts = time.time()
print(
    f"Answer 1: {len(connect_path(paths=[(['start'], False)], one_double=False)) : >10} Duration:{round(time.time() - ts, 2): >5} ")
ts = time.time()
print(f"Answer 2: {len(connect_path(paths=[(['start'], False)], one_double=True)) : > 10} Duration:{round(time.time()-ts,2) : >5}")

# Output
# Answer 1:       4411 Duration: 0.02
# Answer 2:     136767 Duration: 0.85
