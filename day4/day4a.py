# load data
import numpy as np
import copy

input_file = open("input_debug.txt")
numbers = [int(i) for i in input_file.readline().split(",")]
input_file.readline()
puzzel_idx = 0
puzzels = np.array([])

for line in input_file.readlines():
    if line == "\n":
        puzzel_idx += 1
        continue
    print(np.array([int(n) for n in line[:-1].split(" ") if n != ""], "int"))
    np.append(puzzels, np.array([int(n) for n in line[:-1].split(" ") if n != ""], "int") )
    print(puzzels)
    exit(0)

print(puzzels[0])
exit(0)


def sum_puzzle(puzzle):
    s = 0
    for n in puzzle:
        s += sum([m[0] for m in n if m[1] == 0])
    return s


# play game
def play_puzzle(stop_condition, pin):

    found = [False for _ in range(len(pin))]

    for num in numbers:
        # mark
        for p in pin:
            for n in p:
                for i in n:
                    if i[0] == num:
                        i[1] = 1
        puzzle_nr = 0
        for p in pin:
            size = len(p)
            # rows
            for n in p:
                marked = [m[1] for m in n]
                if sum(marked) == size:
                    found[puzzle_nr] = True
                    if stop_condition(found):
                        return puzzle_nr, num, sum_puzzle(p)
            # cols
            for col in range(size):
                marked = [i[col][1] for i in p]
                if sum(marked) == size:
                    found[puzzle_nr] = True
                    if stop_condition(found):
                        return puzzle_nr, num, sum_puzzle(p)

            puzzle_nr += 1


puzzle_nr, winning_number, sum_p = play_puzzle(any, copy.deepcopy(puzzels))
print(f"Answer 1: {sum_p * winning_number}")


puzzle_nr, winning_number, sum_p = play_puzzle(all, copy.deepcopy(puzzels))
print(f"Answer 2: {sum_p * winning_number}")
