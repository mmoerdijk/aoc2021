from dataclasses import dataclass, field
from collections.abc import Iterable
import numpy as np
import math as m


class SNumber:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self):
        while True:
            print("=====================")
            print(self)
            exploded = self.explode()
            print(self)
            splited = self.split()
            if not exploded and not splited:
                break

    def decompose(self, nest=0):

        result = []
        if isinstance(self.left, int) and isinstance(self.right, int):
            result += [[nest,self]]

        if isinstance(self.left, int) and not isinstance(self.right, int):
            result += [[nest, self]]
            result += self.right.decompose(nest=nest+1)

        if not isinstance(self.left, int) and isinstance(self.right, int):
            result += self.left.decompose(nest=nest+1)
            result += [[nest, self]]

        if not isinstance(self.left, int) and not isinstance(self.right, int):
            result += [[nest, self]]
            result += self.left.decompose(nest=nest+1)
            result += self.right.decompose(nest=nest+1)

        return result

    def contains(self, other: "SNumber"):

        if self.left == other.left and self.right == other.right:
            return True

        if self.left == other or self.right == other:
            return True

        if isinstance(self.left, int) and not isinstance(self.right, int):
            return self.right.contains(other)

        if not isinstance(self.left, int) and isinstance(self.right, int):
            return self.left.contains(other)

        if not isinstance(self.left, int) and not isinstance(self.right, int):
            return self.left.contains(other) or self.right.contains(other)

        return False

    def left_most_nested(self):

        if isinstance(self.left, int):
            return self

        left = self.left
        while True:

            if isinstance(left.left, int):
                return left

            left = left.left

    def right_most_nested(self):

        if isinstance(self.right, int):
            return self

        right = self.right
        while True:

            if isinstance(right.right, int):
                return right

            right = right.right

    def explode(self):
        decompose = self.decompose()
        exploded = False
        max_depth = max( max([ i for i,j in decompose]), 4)
        # Do explotions
        idx = 0
        for i in decompose:
            if i[0] == max_depth:
                exploded = True
                print("Explode!")
                # Explode !!!
                tmp = i[1]
                print(tmp)
                # Add left to left
                if idx - 1 >= 0:
                    for i in range(1,idx+1,1):
                        left = decompose[idx - i][1]
                        if isinstance(left.right, int):
                            left.right += tmp.left
                            break
                        elif left.right.contains(tmp):
                            if isinstance(left.left,int):
                                left.left += tmp.left
                                break
                            else:
                                left = left.left.right_most_nested()
                                left.right += tmp.left
                                break

                # Add right to right
                if idx + 1 <= len(decompose)-1:

                    # find left most number for right
                    for i in range(idx+1, len(decompose), 1):
                        right = decompose[i][1]
                        if isinstance(right.left, int):
                            right.left += tmp.right
                            break
                        elif right.left.contains(tmp):
                            if isinstance(right.right,int):
                                right.right += tmp.right
                                break
                            else:
                                right = right.right.left_most_nested()
                                right.left += tmp.right
                                break


                if idx - 1 >= 0:
                    if decompose[idx - 1][0] == max_depth-1:
                        if decompose[idx - 1][1].right == tmp:
                            decompose[idx - 1][1].right = 0
                            break
                        if decompose[idx - 1][1].left == tmp:
                            decompose[idx - 1][1].left = 0
                            break
                if idx + 1 <= len(decompose) - 1:
                    if decompose[idx + 1][0] == max_depth-1:
                        if decompose[idx + 1][1].left == tmp:
                            decompose[idx + 1][1].left = 0
                            break
                        if decompose[idx + 1][1].right == tmp:
                            decompose[idx + 1][1].right = 0
                            break
                break
            idx +=1
        # Should only be max 4 levels now
        return exploded


    def split(self):

        res = False
        if isinstance(self.left, int):
            if self.left > 9:
                tmp = self.left
                print(f"Split! {tmp} => left{m.floor(tmp/2)}, right={m.ceil(tmp/2)}")
                self.left = SNumber(left=m.floor(tmp/2), right=m.ceil(tmp/2))
                return True
        else:
            res = self.left.split()

        if not res:
            if isinstance(self.right, int):
                if self.right > 9:
                    tmp = self.right
                    print(f"Split! {tmp} => left{m.floor(tmp/2)}, right={m.ceil(tmp/2)}")
                    self.right = SNumber(left=m.floor(tmp/2), right=m.ceil(tmp/2))
                    return True
            else:
                return self.right.split()

        return res

    def __repr__(self):
        return f"[{self.left}, {self.right}]"

    def __add__(self, other):
        return SNumber(left=self, right=other).reduce()


homework_raw = open("input_debug.txt").readlines()
homework = []
for line in homework_raw:
    homework.append(eval(line[:-1].replace("[", "SNumber(").replace("]", ")")))

result = homework[0]
print(result)
for h in homework[1:]:
    result += h
    print(result)