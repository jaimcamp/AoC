#!/usr/bin/python3

from Intcode import Intcode


A = Intcode("input.txt")

while not A.stop:
    A.run([], False, halt_output=1)
    if not A.stop:
        print(chr(A.output[0]), end="")
        A.halt = False
        A.reset_output()

instructions = [
    ord(x)
    for x in "NOT C T\nAND D T\nOR T J\nNOT F T\nOR H T\nAND T J\nNOT A T\nOR T J\nNOT B T\nAND A T\nAND D T\nOR T J\nRUN\n"
]
A.run(instructions)
for l in A.output:
    try:
        print(chr(l), end="")
    except:
        print(l)
# print(''.join([chr(x) for x in A.output]))
