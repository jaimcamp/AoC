#!/usr/bin/python3

from collections import deque


def parse_inst(instruction):
    inst, val = None, None
    if "new stack" in instruction:
        inst = 0
    elif "cut" in instruction:
        inst = 1
        val = int(instruction.split(" ")[-1])
    elif "increment" in instruction:
        inst = 2
        val = int(instruction.split(" ")[-1])

    return inst, val


class Cards:
    def __init__(self, n):
        self.n = n
        self.cards = deque(range(n))

    def run(self, instruction):
        inst, val = parse_inst(instruction)
        if inst == 0:
            self.new_stack()
        elif inst == 1:
            self.cutn(val)
        elif inst == 2:
            self.todeal(val)
        else:
            print("Wrong Instruction")

    def __repr__(self):
        return str(self.cards)

    def new_stack(self):
        self.cards.reverse()

    def cutn(self, n):
        self.cards.rotate(-1 * n)

    def todeal(self, n):
        new = deque([0] * self.n)
        for ix, val in enumerate(self.cards):
            pos = (ix * n) % self.n
            new[pos] = val
        self.cards = new
