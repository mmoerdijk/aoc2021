# Now optimized for speed, not clarity :-D
import time
script_start = time.time()
# Load data
from copy import copy

input_file = open("input.txt")
nodes = {}
for line in input_file.read().split("\n"):
    current_nodes = line.split("-")
    for n in [i for i in current_nodes if i not in nodes]:
        nodes[n] = set()

    if current_nodes[1] != "start":
        if current_nodes[1] == "end":
            nodes[current_nodes[0]].add((False, True))
        else:
            nodes[current_nodes[0]].add((current_nodes[1], current_nodes[1].islower()))

    if current_nodes[0] != "start":
        if current_nodes[0] == "end":
            nodes[current_nodes[1]].add((False, True))
        else:
            nodes[current_nodes[1]].add((current_nodes[0],current_nodes[0].islower()))

def connect_path(paths, one_double=True):
    res = 0
    for p, double, last in paths:
        # Get connections for node
        connections = nodes[last]
        new_paths = []

        for c, islower in connections:
            # end of the road for this path
            if not c:
                res += 1
                continue

            if islower:
                if c in p:
                    if double or not one_double:
                        continue
                    new = copy(p)
                    new.add(c)
                    new_paths += [(new, True, c)]
                else:
                    new = copy(p)
                    new.add(c)
                    new_paths += [(new, double, c)]

            else:
                new_paths += [(p, double, c)]

        # and continue ...
        res += connect_path(paths=new_paths, one_double=one_double)
    return res


ts = time.time()
p = connect_path(paths=[(set(), False, 'start')], one_double=False)
ct = time.time() - ts
print(f"Answer 1: {p : >10} Duration: {ct: >5} ")

ts = time.time()
p = connect_path(paths=[(set(), False, 'start')], one_double=True)
ct = time.time() - ts
print( f"Answer 2: {p : >10} Duration: {ct: >5} ")

print( f"Total time: {time.time() - script_start } ")

# Output
# Answer 1:       4411 Duration: 0.015621423721313477
# Answer 2:     136767 Duration: 0.3280768394470215
# Total time: 0.34369826316833496

# Line profiler
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     25                                           @profile
#     26                                           def connect_path(paths, one_double=True):
#     27    499151     136580.3      0.3      3.1      res = 0
#     28    998300     323019.5      0.3      7.3      for p, double, last in paths:
#     29                                                   # Get connections for node
#     30    499149     161083.5      0.3      3.6          connections = nodes[last]
#     31    499149     151795.0      0.3      3.4          new_paths = []
#     32
#     33   2358007     737582.0      0.3     16.6          for c, islower in connections:
#     34                                                       # end of the road for this path
#     35   1858858     518024.1      0.3     11.6              if not c:
#     36    141178      43193.5      0.3      1.0                  res += 1
#     37    141178      37512.4      0.3      0.8                  continue
#     38
#     39   1717680     487549.3      0.3     11.0              if islower:
#     40   1374365     431050.7      0.3      9.7                  if c in p:
#     41   1256845     352345.0      0.3      7.9                      if double or not one_double:
#     42     38312       9856.4      0.3      0.2                          continue
#     43     38312      49331.6      1.3      1.1                      new = copy(p)
#     44     38312      15993.1      0.4      0.4                      new.add(c)
#     45     38312      17975.6      0.5      0.4                      new_paths += [(new, True, c)]
#     46                                                           else:
#     47    117520     153539.1      1.3      3.5                      new = copy(p)
#     48    117520      50351.8      0.4      1.1                      new.add(c)
#     49    117520      50551.4      0.4      1.1                      new_paths += [(new, double, c)]
#     50
#     51                                                       else:
#     52    343315     143818.8      0.4      3.2                  new_paths += [(p, double, c)]
#     53
#     54                                                   # and continue ...
#     55    499149     452215.9      0.9     10.2          res += connect_path(paths=new_paths, one_double=one_double)
#     56    499151     125562.7      0.3      2.8      return res
