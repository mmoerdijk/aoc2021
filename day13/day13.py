import numpy as np

# Load data
input_file = open("input.txt")
dots_raw, folds_raw = input_file.read().split("==")

dots = []
for dot in dots_raw.split("\n"):
    if dot not in ["", "\n"]:
        dots += [[int(x) for x in dot.split(",")]]

folds = []
for fold in folds_raw.split("\n"):
    if fold not in ["", "\n"]:
        fold = fold.replace("fold along ", "").split("=")
        folds += [[fold[0], int(fold[1])]]

dots = np.array(dots)
grid_size = dots.max(axis=0) + 1

grid = np.zeros((grid_size[1], grid_size[0]))

# mark dots
for dot in dots:
    grid[dot[1], dot[0]] = 1

# fold
for axis, line in folds:

    if axis == "x":
        flap = np.flip(grid[:, line + 1 :], axis=1)
        grid[:, :line] += flap[:, :line]
        grid = grid[:, :line]

    if axis == "y":
        flap = np.flip(grid[line + 1 :, :], axis=0)
        grid[:line, :] += flap[:line, :]
        grid = grid[:line, :]


grid[grid > 0] = 1

print(f"Answer 1: {grid.sum()} ")
print(f"Answer 2: ")
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        print(" " if grid[i,j] == 0 else "#", end="")
    print("")

# Answer 1: 95.0
# Answer 2:
###  #### #  # ###   ##    ## #### #  #
#  # #    # #  #  # #  #    #    # #  #
###  ###  ##   #  # #       #   #  #  #
#  # #    # #  ###  #       #  #   #  #
#  # #    # #  # #  #  # #  # #    #  #
###  #    #  # #  #  ##   ##  ####  ##