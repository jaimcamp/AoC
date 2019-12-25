#!/usr/bin/python3

from Intcode import Intcode
from itertools import combinations
import sys


def out2char(l_out):
    for c in l_out:
        try:
            print(chr(c), end="")
        except:
            print(c)


def str2ord(s_in):
    return [ord(c) for c in s_in]


A = Intcode("input.txt")
A.run([])
out2char(A.output)
A.reset_output()

# while True:
    # act = input("Action")
    # act += "\n"
    # A.run(str2ord(act))
    # out2char(A.output)
    # A.reset_output()

with open("ins.txt") as f:
    for line in f.readlines():
        # input()
        instruction = line.strip() + "\n"
        print(instruction)
        A.run(str2ord(instruction))
        out2char(A.output)
        A.reset_output()
items = ["pointer", "mutex", "asterisk", "space law space brochure",
         "monolith", "mouse", "food ration", "sand"]
for i in range(1, len(items)):
    for c in combinations(items, i):
        # input()
        drops = ["drop " + x for x in c]
        drop_inst = "\n".join(drops) + "\neast\n"
        print("Will drop\n", drop_inst)
        A.run(str2ord(drop_inst))
        out2char(A.output)
        output = "".join([chr(x) for x in A.output])
        A.reset_output()
        if "lighter" not in output and \
           "heavier" not in output:
            print(c, output)
            sys.exit(0)
            break
        else:
            takes = ["take " + x for x in c]
            take_inst = "\n".join(takes) + "\n"
            print("Will take\n", take_inst)
            A.run(str2ord(take_inst))
            out2char(A.output)
            A.reset_output()
