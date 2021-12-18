import math as m
from collections import namedtuple
from dataclasses import dataclass, field

Entry = namedtuple("Entry", "start_vel vel step")

traingular = lambda x:  sum(range( abs(x) + 1))
inv_traingular = lambda x: m.floor(m.sqrt(x*2))

# target_area = [ (116,161), (-154, -101) ]
target_area = [ (20,30), (-10, -5) ]

max_y_pos = traingular(target_area[1][0] - 1)

t = 1
valid_x_speeds = []
start_vel = 1
while start_vel <= target_area[0][1]:
    xpos = 0
    t = 0
    vel = start_vel
    while True:
        xpos += vel

        if target_area[0][0] <= xpos <= target_area[0][1]:
            print(Entry(start_vel, vel, t, ))
            valid_x_speeds.append( Entry(start_vel, vel, t,) )

        if vel == 0:
            break

        vel -= 1
        t += 1



    start_vel += 1

print(valid_x_speeds)
print(len(valid_x_speeds))

t = 0
ypos = 0
start_vel = target_area[1][0]
vel = start_vel
valid_y_speeds = []

for i in range(target_area[1][0]-1, abs(target_area[1][0]+1), 1):
    vel = start_vel

    max_y = 0
    ypos = 0
    t=0
    while ypos >= target_area[1][0]:
        ypos += vel

        if target_area[1][0] <= ypos <= target_area[1][1]:
            print(Entry(start_vel, vel, t,))
            valid_y_speeds.append(Entry(start_vel, vel, t,))

        vel -= 1
        t+=1

    start_vel+=1

print(len(valid_y_speeds))

# Find valid combinations
valid_combinations = set()
for x in valid_x_speeds:

    for y in valid_y_speeds:

        # If there are no
        if x.vel == 0 and y.step >= x.step:
            # print((x.start_vel, y.start_vel))
            valid_combinations.add((x.start_vel, y.start_vel))

        # Else only if
        elif x.step == y.step:
            # print((x.start_vel, y.start_vel))
            valid_combinations.add((x.start_vel, y.start_vel))

print(len(valid_combinations))



print(f"Answer 1: {max_y_pos:>5} ")
print(f"Answer 2: {len(valid_combinations):>5} ")

# Answer 1:   498
# Answer 2:  2901
