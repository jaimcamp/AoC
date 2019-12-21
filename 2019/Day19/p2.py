#!/usr/bin/python3


from functions import param_v
from collections import defaultdict
# from random import shuffle
# import networkx as nx
# from matplotlib import pyplot as plt

class Incode:

    def __init__(self, input_file):
        temp = [int(x) for x in
                open(input_file).read().strip().split(',')]
        self.input = temp + [0] * (10000 - len(temp))
        self.i = 0
        self.output = []
        self.stop = False
        self.rel = 0


    def __str__(self):
        return str([(i, x) for i, x in enumerate(self.input)])


    def reset_output(self):
        self.output = []



    def run(self, inputs, opprint=False):
        # print(inputs)
        input_int = None
        while self.i <= len(self.input):
            code = self.input[self.i]
            s_code = str(code).zfill(5)
            opcode = int(s_code[-2:])
            if opprint:
                print("Opcode: {}, Pos: {}, Rel: {}".format(s_code, self.i, self.rel))
            m1 = int(s_code[-3])
            m2 = int(s_code[-4])
            m3 = int(s_code[-5])
            if m3 == 1:
                print("m3 weird")
                break
            if opcode == 3:
                input_int = inputs.pop()
            elif opcode == 99:
                self.stop = True
                break
            self.i = param_v(self.input, self.i, opcode, m1, m2, m3,
                             input_int, self)
            if len(self.output) == 1:
                break
            # if opcode == 4:
                # pass


def printit(tiles):
        minx = min([x for x,y in tiles.keys()])
        miny = min([y for x,y in tiles.keys()])
        maxx = max([x for x,y in tiles.keys()])
        maxy = max([y for x,y in tiles.keys()])
        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                if tiles[(x, y)] == 1:
                    print('#', end='')
                elif tiles[(x, y)] == 0:
                    print('.', end='')
                else:
                    print(' ', end='')
            print()


def getbeam(x, y):
    A = Incode('input.txt')
    A.run([x, y])
    return A.output[0]


def test_sq(x, y):
    return getbeam(x, y) and \
            getbeam(x, y + 99) and \
            getbeam(x - 99, y) and \
            getbeam(x - 99, y + 99)


def find_miny(x):
    y, maxy = 0, x
    while True:
        m = (maxy + y) // 2
        if getbeam(x, m):
            maxy = m
        else:
            y = m

        if y == maxy - 1:
            return maxy

# if __name__ == "__main__":
    # x, maxx = 0, 10000
    # while True:
        # midx = (maxx + x) // 2
        # y = find_miny(midx)
        # print(maxx, y)
        # if test_sq(midx, y):
            # maxx = midx
        # else:
            # x = midx
        # if x == maxx-1:
            # print(maxx)
            # print((maxx-99) * 10000 + find_miny(maxx))
            # break


def find_max_y(x):
    y, Y = 0, x/0.6
    while True:
        m = (y+Y)//2
        if getbeam(x, m):
            Y = m
        else:
            y = m
        if y == Y-1:
            return Y

def is_good(x, y):
    return getbeam(x, y) and \
        getbeam(x, y+99) and \
        getbeam(x-99, y+99) and \
        getbeam(x-99, y)

def part_two():
    x, X = 0, 10000
    while True:
        m = (x+X)//2
        y = find_max_y(m)
        if is_good(m, y):
            X = m
        else:
            x = m
        if x == X-1:
            return (X-99)*10000+find_max_y(X)

print(f"Part two: {part_two()}")
