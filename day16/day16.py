import math
from dataclasses import dataclass, field

transmisstion = open("input_debug.txt").readlines()[0]
print(transmisstion)
sum_id = 0

id_to_length = {0: 15, 1: 11, 4: 1}


@dataclass
class Package:
    version: int = 0
    type: int = 0
    value: int = 0


# Split packages
packages = []


def parse_literal(transmisstion, pos, scan_depth):
    # Scan forward max 6 position
    value = int(transmisstion[pos:pos + scan_depth], 16)
    positions = 0
    result = 0
    # scan forward to check if we reach the end
    for i in range(scan_depth * 4 - 7, 0, -5):
        positions += 1
        part = (value & 0xF << (i - 4)) >> (i - 4)
        result = (result << 4) + part
        if not value & (1 << i):
            break
    return result, positions

for pos in range(len(transmisstion)):
    header = int(transmisstion[pos:pos + 2], 16)
    print(f"{header:b}")
    # decode package
    p = Package()
    p.version = header >> 5
    p.type = (header & 0x1F) >> 2

    if p.type == 4:
        # We have Literal value
        p.value, positions = parse_literal(transmisstion=transmisstion, pos=pos, scan_depth=6)
        pos += (6 + positions * 5) // 4 + 1
        packages.append(p)
        continue

    else:  # Operator package

        # Get value of second bit of header
        length_type = (header & 0x02) >> 1
        value = int(transmisstion[pos:pos + 6], 16)
        length = 0
        if length_type == 0:
            # 15 bit number
            length = (value >> 2) & 0x7FFF
            scan_depth = (length // 4) + 1
            position = 0
            while position < length:
                header = int(transmisstion[pos+:pos + 2], 16)
                pack = Package()
                pack.type = header >> 5
                pack.version = (header & 0x1F) >> 2
                pack.value, inc = parse_literal(transmisstion=transmisstion, pos=pos, scan_depth=scan_depth)
                positions += inc*5

            pos = ((7 + 15 + length) // 4) + 1

        if length_type == 1:
            # 11 bit number
            length = (value >> 6) & 0x7FF
            # read length * 11 bit packages
            offset = 4
            bit_offset = 2
            # Read enough from buffer
            value = int(transmisstion[pos + offset:pos + offset + length * 3], 16) >> 1

            for p_num in range(length):
                tmp_val = (value >> (length - 1 - p_num) * 11) & 0x7FF
                p.value.append(tmp_val & 0xF)

            pos = (7 + 11 + length * 11) // 4 + 1


# print(f"Answer 1: {calculate_risk(path1, map1):>5} ")
# print(f"Answer 2: {calculate_risk(path2, map2):>5} ")

# Answer 1:   498
# Answer 2:  2901
