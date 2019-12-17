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
        self.position = (0,0)
        self.direction = None


    def __str__(self):
        return str([(i, x) for i, x in enumerate(self.input)])


    def reset_output(self):
        self.output = []


    def move(self, direction):
        self.position = tuple(x+y for x, y in zip(self.position , direction))

    # def change_direction(self, direction):
        # tmp = self.change[self.direction][direction]
        # self.direction = tmp

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
            # if len(self.output) == 1:
                # break
            # if opcode == 4:
                # pass


# def mov2pos(mov):
    # if mov == 1:
        # return (0,1)
    # elif mov == 2:
        # return (0,-1)
    # elif mov == 3:
        # return (-1,0)
    # elif mov == 4:
        # return (1,0)


# def next_mov(pos, walls):
    # a, b = pos
    # possible_movs = {(a, b+1): 1, (a, b-1): 2, (a-1, b): 3, (a+1, b): 4}
    # nms = [(a, b+1), (a, b-1), (a-1, b), (a+1, b)]
    # shuffle(nms)
    # for nm in nms:
        # if nm not in walls:
            # # print(f"NM: {nm}")
            # return  possible_movs[nm]
    # return 99


def printit(tiles):
        minx = min([x for x,y in tiles.keys()])
        miny = min([y for x,y in tiles.keys()])
        maxx = max([x for x,y in tiles.keys()])
        maxy = max([y for x,y in tiles.keys()])
        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                try:
                    print(chr(tiles[(x, y)]), end='')
                except:
                    print("Nop", tiles[(x, y)])
                # if tiles[(x, y)] == 46:
                    # print('.', end='')
                # elif tiles[(x, y)] == 58:
                    # print('X', end='')
                # elif tiles[(x, y)] == 35:
                    # print('#', end='')
                # else:
                    # print(' ', end='')
            print()

def get_inter(tiles):
    out = []
    for tile, val in tiles.items():
        if val == 35:
            a, b = tile
            neighbours = [(a, b+1), (a, b-1), (a-1, b), (a+1, b)]
            vals = [tiles.get(x, 0) for x in neighbours]
            inter = all([x == 35 for x in vals])
            if inter:
                out.append(tile)
    for tile in out:
        tiles[tile] = 20
    return out
        

    
if __name__ == "__main__":
    A = Incode('input.txt')
    A.run([], False)
    codes = A.output
    positions = defaultdict(lambda: 32)
    i, j = 0, 0
    for code in codes:
        if code == 10:
            i = 0
            j += 1
            continue
        positions[(i, j)] = code
        i += 1
    intersections = get_inter(positions)
    printit(positions)
    print(sum([x * y for x, y in intersections]))

    # Part 2

    A = Incode('input.txt')
    A.input[0] = 2
    program = "A,C\nR,6,L,11\nR,12,L,8,L,10\nR,8,R,9,R,12,L,8,L\nn\n"
    run_codes = [ord(c) for c in program][::-1]
    print(run_codes)
    A.run(run_codes, False)
    codes = A.output
    positions = defaultdict(lambda: 32)
    i, j = 0, 0
    # out = codes.pop()
    for code in codes:
        if code == 10:
            i = 0
            j += 1
            continue
        positions[(i, j)] = code
        i += 1
    printit(positions)
