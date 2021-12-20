import math as m
from collections import namedtuple

Entry = namedtuple("Entry", "start_vel vel step")

traingular = lambda x: sum(range(abs(x) + 1))
inv_traingular = lambda x: m.floor(m.sqrt(x * 2))

target_area = [ (111,161), (-154, -101) ]
# target_area = [(20, 30), (-10, -5)]


t = 0
valid_x_speeds = []
x_start_vel = inv_traingular(target_area[0][0])
# find all x start speeds
while x_start_vel <= target_area[0][1]:
    xpos = 0
    t = 0
    x_vel = x_start_vel
    while x_vel >= 0:
        xpos += x_vel
        if target_area[0][0] <= xpos <= target_area[0][1]:
            valid_x_speeds.append(Entry(x_start_vel, x_vel, t, ))
        x_vel -= 1
        t += 1
    x_start_vel += 1

t = 0
ypos = 0
y_start_vel = target_area[1][0]
y_vel = y_start_vel
valid_y_speeds = []
# Find all y start speeds
for i in range(target_area[1][0] - 1, abs(target_area[1][0])+1, 1):
    y_vel = y_start_vel
    ypos = 0
    t = 0
    while ypos >= target_area[1][0]:
        ypos += y_vel
        if target_area[1][0] <= ypos <= target_area[1][1]:
            print(Entry(y_start_vel, y_vel, t, ))
            valid_y_speeds.append(Entry(y_start_vel, y_vel, t, ))
        y_vel -= 1
        t += 1
    y_start_vel += 1

# Find valid combinations
valid_combinations = set()
for x in valid_x_speeds:
    for y in valid_y_speeds:
        # If there are no
        if x.vel == 0 and y.step >= x.step:
            valid_combinations.add((x.start_vel, y.start_vel))

        # Else only if they are there in the same step
        if x.step == y.step:
            valid_combinations.add((x.start_vel, y.start_vel))


print(f"Answer 1: {traingular(target_area[1][0]+1):>5} ")
print(f"Answer 2: {len(valid_combinations):>5} ")

# Answer 1: 11781
# Answer 2:  4531
