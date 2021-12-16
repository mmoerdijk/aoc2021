import math
from dataclasses import dataclass, field

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

transmisstion = open("input.txt").readlines()[0]
messsage = ""
for char in transmisstion:
    messsage += hex_to_bin[char]


@dataclass
class Package:
    version: int = 0
    id: int = 0
    value: int = 0
    children: list = field(default_factory=list)

    def sum_versions(self):
        sum_versions = self.version
        for c in self.children:
            sum_versions += c.sum_versions()
        return sum_versions

    def get_value(self):

        if self.id == 4:  # literal
            return self.value

        values = [c.get_value() for c in self.children]
        if self.id == 0:  # Sum
            return sum(values)

        if self.id == 1:  # Product
            return math.prod(values)

        if self.id == 2:  # min
            return min(values)

        if self.id == 3:  # max
            return max(values)

        if self.id == 5:  # 0 > 1
            return int(values[0] > values[1])

        if self.id == 6:  # 0 < 1
            return int(values[0] < values[1])

        if self.id == 7:  # 0 == 1
            return int(values[0] == values[1])


def read_int(buffer, start, length):
    value = int(buffer[start:start + length], 2)
    return value, start + length


def read_package(messsage, pos):
    p = Package()
    p.version, pos = read_int(messsage, pos, length=3)
    p.id, pos = read_int(messsage, pos, length=3)

    if p.id == 4:  # literal
        while True:
            # Check if we need to stop
            cnt, pos = read_int(messsage, pos, length=1)
            # Read value
            value, pos = read_int(messsage, pos, length=4)
            p.value = (p.value << 4) + value
            if cnt == 0:
                break

    else:  # Operator
        lenght_id, pos = read_int(messsage, pos, length=1)

        if lenght_id == 0:
            # 15 bits
            length, pos = read_int(messsage, pos, length=15)
            stop_pos = length + pos
            while pos < stop_pos:
                c, pos = read_package(messsage, pos)
                p.children.append(c)

        if lenght_id == 1:
            length, pos = read_int(messsage, pos, length=11)
            for child_idx in range(length):
                c, pos = read_package(messsage, pos)
                p.children.append(c)

    return p, pos


p, pos = read_package(messsage, 0)

print(f"Answer 1: {p.sum_versions():>20} ")
print(f"Answer 2: {p.get_value():>20} ")

# Answer 1:   498
# Answer 2:  2901
