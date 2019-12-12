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
    A = Incode('input.txt')
    white_places = []
    old_positions = defaultdict(lambda: 1)
    colors = defaultdict(lambda: 0)
    color = 0
    while not A.stop:
        print("Direction {}".format(A.direction))
        print("Position {}".format(A.position))
        old_positions[A.position] = 1
        A.run([color], False)
        if A.stop:
            break
        out = A.output
        colors[A.position] = out[0]
        # if out[0] == 1:
            # white_places.append(A.position)
            # print("Added {}".format(white_places[-1]))
        A.change_direction(direction=out[1])
        A.move()
        A.reset_output()
        color = colors[A.position]
        # if A.position in white_places:
            # color = 1
        # else:
            # color = 0
            # print("white")
        # color = 1 if A.position in white_places else 0
    print(len(old_positions))
    print(colors)
