# load data
import numpy as np

fishes_arr=np.array("3,1,5,4,4,4,5,3,4,4,1,4,2,3,1,3,3,2,3,2,5,1,1,4,4,3,2,4,2,4,1,5,3,3,2,2,2,5,5,1,3,4,5,1,5,5,1,1,1,4,3,2,3,3,3,4,4,4,5,5,1,3,3,5,4,5,5,5,1,1,2,4,3,4,5,4,5,2,2,3,5,2,1,2,4,3,5,1,3,1,4,4,1,3,2,3,2,4,5,2,4,1,4,3,1,3,1,5,1,3,5,4,3,1,5,3,3,5,4,2,3,4,1,2,1,1,4,4,4,3,1,1,1,1,1,4,2,5,1,1,2,1,5,3,4,1,5,4,1,3,3,1,4,4,5,3,1,1,3,3,3,1,1,5,4,2,5,1,1,5,5,1,4,2,2,5,3,1,1,3,3,5,3,3,2,4,3,2,5,2,5,4,5,4,3,2,4,3,5,1,2,2,4,3,1,5,5,1,3,1,3,2,2,4,5,4,2,3,2,3,4,1,3,4,2,5,4,4,2,2,1,4,1,5,1,5,4,3,3,3,3,3,5,2,1,5,5,3,5,2,1,1,4,2,2,5,1,4,3,3,4,4,2,3,2,1,3,1,5,2,1,5,1,3,1,4,2,4,5,1,4,5,5,3,5,1,5,4,1,3,4,1,1,4,5,5,2,1,3,3".split(","), dtype=int)
# fishes_arr=np.array("3,4,3,1,2".split(","), dtype=int)

def transform_state(f):
    res = np.zeros(9)
    for i in range(9):
        res[i] = len(f[f==i])
    return res

number_of_fishes_per_number = transform_state(fishes_arr)

for d in range(80):
    # print(number_of_fishes_per_number)
    zeros = number_of_fishes_per_number[0]
    number_of_fishes_per_number = number_of_fishes_per_number[1:]
    number_of_fishes_per_number[6] += zeros
    number_of_fishes_per_number = np.append(number_of_fishes_per_number, zeros)

print(f"Answer1: {number_of_fishes_per_number.sum()}")

for d in range(256-80):
    # print(number_of_fishes_per_number)
    zeros = number_of_fishes_per_number[0]
    number_of_fishes_per_number = number_of_fishes_per_number[1:]
    number_of_fishes_per_number[6] += zeros
    number_of_fishes_per_number = np.append(number_of_fishes_per_number, zeros)


print(f"Answer1: {number_of_fishes_per_number.sum()}")