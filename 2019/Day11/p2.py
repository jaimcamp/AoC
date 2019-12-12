#!/usr/bin/python3


from functions import param_v
from collections import defaultdict

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
        self.direction = (0,1)
        self.change = {
                (0,1): [(-1,0),(1,0)],
                (0,-1): [(1,0),(-1,0)],
                (1,0): [(0,1),(0,-1)],
                (-1,0): [(0,-1),(0,1)]
                }


    def __str__(self):
        return str([(i, x) for i, x in enumerate(self.input)])


    def reset_output(self):
        self.output = []


    def move(self):
        self.position = tuple(x+y for x, y in zip(self.position , self.direction))

    def change_direction(self, direction):
        tmp = self.change[self.direction][direction]
        self.direction = tmp

    def run(self, inputs, opprint=False):
        print(inputs)
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
            if len(self.output) > 1:
                break
            # if opcode == 4:
                # pass


if __name__ == "__main__":
    maxx, minx = 100, -100
    maxy, miny = 100, -100
    A = Incode('input.txt')
    white_places = []
    old_positions = defaultdict(lambda: 1)
    colors = defaultdict(lambda: 0)
    color = 1
    while not A.stop:
        # print("Direction {}".format(A.direction))
        # print("Position {}".format(A.position))
        old_positions[A.position] = 1
        A.run([color], False)
        if A.stop:
            break
        out = A.output
        colors[A.position] = out[0]
        A.change_direction(direction=out[1])
        A.move()
        A.reset_output()
        color = colors[A.position]
    print(len(old_positions))
    minx = min([x for x,y in colors.keys()])
    miny = min([y for x,y in colors.keys()])
    maxx = max([x for x,y in colors.keys()])
    maxy = max([y for x,y in colors.keys()])
    print(minx, miny, maxx, maxy)
    for y in range(maxy, miny-1, -1):
        for x in range(minx, maxx+1):
            if colors[(x, y)] == 1:
                print('#', end="")
            else:
                print(' ', end="")
        print()
