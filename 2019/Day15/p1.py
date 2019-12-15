#!/usr/bin/python3


from functions import param_v
from collections import defaultdict
from random import shuffle
import networkx as nx
from matplotlib import pyplot as plt

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
            if len(self.output) == 1:
                break
            # if opcode == 4:
                # pass


def mov2pos(mov):
    if mov == 1:
        return (0,1)
    elif mov == 2:
        return (0,-1)
    elif mov == 3:
        return (-1,0)
    elif mov == 4:
        return (1,0)


def next_mov(pos, walls):
    a, b = pos
    possible_movs = {(a, b+1): 1, (a, b-1): 2, (a-1, b): 3, (a+1, b): 4}
    nms = [(a, b+1), (a, b-1), (a-1, b), (a+1, b)]
    shuffle(nms)
    for nm in nms:
        if nm not in walls:
            # print(f"NM: {nm}")
            return  possible_movs[nm]
    return 99


if __name__ == "__main__":
    A = Incode('input.txt')
    walls = []
    walked = set()
    pos = A.position
    found = False
    pos_o2 = None
    movement = 1
    while not found:
        walked.add(A.position)
        movement = next_mov(pos, walls)
        if movement == 99:
            print("No more directions")
            break
        # print("Mov", movement)
        A.run([movement], False)
        status = A.output[0]
        # print("S",status)
        if A.stop:
            print("Astop")
            break
        if status == 0:
            #Hit wall
            wall = tuple(x+y for x, y in zip(A.position , mov2pos(movement)))
            walls.append(wall)
        elif status == 1:
            #not wall
            A.move(mov2pos(movement))
            pos = A.position
        elif status == 2:
            #found it
            A.move(mov2pos(movement))
            walked.add(A.position)
            found = True
            # pos_o2 = tuple(x+y for x, y in zip(A.position , mov2pos(movement)))
            pos_o2 = A.position
        else:
            print(f"Weird Status: {status}")
        A.reset_output()
        # print("Position:", A.position, pos)
        # print("W", walls)
    # print(walked, len(walked))
    print(pos_o2)
    G = nx.Graph()
    for node in walked:
        G.add_node(node)
    for node in walked:
        a, b = node
        for neigh in [(a, b+1), (a, b-1), (a-1, b), (a+1, b)]:
            if neigh in walked:
                G.add_edge(node, neigh)
    nx.draw(G)
    plt.savefig('G1.png')
    print(nx.shortest_path_length(G.to_undirected(), (0,0), pos_o2))

