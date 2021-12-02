input = open("input.txt").readlines()
horizontal = 0
depth = 0
for command in input:
    action, value = command.split(" ")
    value = int(value)
    if action == "forward":
        horizontal += value
    if action == "up":
        depth -= value
    if action == "down":
        depth += value

print(f"Answer 1 {depth*horizontal}")

aim = 0
depth = 0
horizontal = 0
for command in input:
    action, value = command.split(" ")
    value = int(value)
    if action == "forward":
        horizontal += value
        depth += value*aim
    if action == "up":
        aim -= value

    if action == "down":
        aim += value

print(f"Answer 2 {depth*horizontal}")