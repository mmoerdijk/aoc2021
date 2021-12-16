import math
from dataclasses import dataclass

transmisstion = open("input_debug.txt").readlines()[0]
print(transmisstion)
sum_id = 0

id_to_length = { 0: 15, 1: 11, 4: 1}

@dataclass
class Package:
    version: int = 0
    type: int = 0

# Split packages
packages = []
for pos in range(len(transmisstion)):
    header = int(transmisstion[pos:pos+2], 16)
    print(f"{header:b}")
    # decode package
    p = Package()
    p.version = header >> 5
    p.type = (header & 0x1F) >> 2

    if p.type == 4:
        # We have Literal value
        scan_depth = 6
        # Scan forward max 10 position
        value = int(transmisstion[pos:pos + scan_depth], 16)
        number = 0
        positions = 0
        # scan forward to check if we reach the end
        for i in range(scan_depth*4-7, 0, -5):
            positions+=1

            if not value & (1 << i):
                break

        pos+= ( 6 + positions*5 ) // 4 + 1


    if p.type == 6 or p.type == 3:
        # Get value of second bit of header
        length_type = (header & 0x02) >> 1
        value = int(transmisstion[pos:pos + 6], 16)
        length = 0
        if length_type == 0:
            # 15 bit number
            length = (value >> 2) & 0x7FFF

        if length_type == 1:
            # 11 bit number
            length = (value >> 6) & 0x7FF


    packages.append(p)




# print(f"Answer 1: {calculate_risk(path1, map1):>5} ")
# print(f"Answer 2: {calculate_risk(path2, map2):>5} ")

# Answer 1:   498
# Answer 2:  2901