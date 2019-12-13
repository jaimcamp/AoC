#!/usr/bin/python3


from functions import param_v
from collections import defaultdict
import time

class Incode:

    def __init__(self, input_file):
        temp = [int(x) for x in
                open(input_file).read().strip().split(',')]
        self.input = temp + [0] * (10000 - len(temp))
        self.i = 0
        self.output = []
        self.stop = False
        self.rel = 0
        # self.position = (0,0)
        # self.direction = (0,1)
        # self.change = {
                # (0,1): [(-1,0),(1,0)],
                # (0,-1): [(1,0),(-1,0)],
                # (1,0): [(0,1),(0,-1)],
                # (-1,0): [(0,-1),(0,1)]
                # }


    def __str__(self):
        return str([(i, x) for i, x in enumerate(self.input)])


    def reset_output(self):
        self.output = []


    # def move(self):
        # self.position = tuple(x+y for x, y in zip(self.position , self.direction))

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
            if len(self.output) > 2:
                break
            # if opcode == 4:
                # pass


if __name__ == "__main__":
    A = Incode('input.txt')
    A.input[0] = 2
    tiles = defaultdict(lambda: ' ')
    buffer_size = 1
    joystick = []
    while True:
        with open('screen.txt', 'a') as screen:
            joystick = [int(input("Move it! "))]
            while True:
                A.run(joystick, False)
                if A.stop:
                    break
                out = A.output
                print(out[:50])
                tiles[(out[0], out[1])] = out[2]
                A.reset_output()
        # print([pos for  pos, val in tiles.items() if val == 3])
        # minx = min([x for x,y in tiles.keys()])
        # miny = min([y for x,y in tiles.keys()])
            minx = 0
            miny = 0
            maxx = max([x for x,y in tiles.keys()])
            maxy = max([y for x,y in tiles.keys()])
        # print(minx, miny, maxx, maxy)
            info = "Part 1: {}\n".format(sum([z==2 for  z in tiles.values()]))
            screen.write(info)
            screen.write("Score: {} \n".format(tiles[(-1,0)]))
                
            for y in range(miny, maxy):
                for x in range(minx, maxx+1):
                    if tiles[(x, y)] == 1:
                        screen.write('॥')
                    elif tiles[(x, y)] == 2:
                        screen.write('#')
                    elif tiles[(x, y)] == 3:
                        screen.write('=')
                    elif tiles[(x, y)] == 4:
                        screen.write('O')
                    else:
                        screen.write(' ')
                screen.write("\n")
        # screen.close()
