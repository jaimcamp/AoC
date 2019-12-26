#!/usr/bin/python3


from Intcode import Intcode

from collections import defaultdict

# from random import shuffle
# import networkx as nx
# from matplotlib import pyplot as plt


def printit(tiles):
    minx = min([x for x, y in tiles.keys()])
    miny = min([y for x, y in tiles.keys()])
    maxx = max([x for x, y in tiles.keys()])
    maxy = max([y for x, y in tiles.keys()])
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            if tiles[(x, y)] == 1:
                print("#", end="")
            elif tiles[(x, y)] == 0:
                print(".", end="")
            else:
                print(" ", end="")
        print()


def getbeam(x, y, input_f):
    A = Intcode(input_f)
    A.run([x, y], halt_output=1)
    return A.output[0]


def find_miny(x, input_f):
    y, maxy = 0, (x * 0.6)
    while True:
        m = (maxy + y) // 2
        if getbeam(x, m, input_f):
            maxy = m
        else:
            y = m

        if y == (maxy - 1):
            return maxy


def test_sq(x, y, input_f):
    return (
        getbeam(x, y, input_f)
        and getbeam(x, y + 99, input_f)
        and getbeam(x - 99, y, input_f)
        and getbeam(x - 99, y + 99, input_f)
    )


def part_two(input_f):
    x, maxx = 0, 10000
    while True:
        m = (x + maxx) // 2
        y = find_miny(m, input_f)
        print(f"M: {m}", test_sq(m, y, input_f))
        if test_sq(m, y, input_f):
            maxx = m
        else:
            x = m
        if x == maxx - 1:
            print((maxx - 99) * 10000 + find_miny(maxx, input_f))
            return 0


def part_one(input_f):
    total = 0
    for i in range(50):
        for j in range(50):
            total += getbeam(i, j, input_f)
    print(f"Part one: {total}")


if __name__ == "__main__":
    part_one("input.txt")
    part_two("input.txt")
