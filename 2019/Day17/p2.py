#!/usr/bin/python3


from Intcode import Intcode
from collections import defaultdict


def printit(tiles):
    minx = min([x for x, y in tiles.keys()])
    miny = min([y for x, y in tiles.keys()])
    maxx = max([x for x, y in tiles.keys()])
    maxy = max([y for x, y in tiles.keys()])
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            try:
                print(tiles[(x, y)], end="")
            except:
                print("Nop", tiles[(x, y)])
        print()


def get_inter(tiles):
    out = []
    for tile, val in tiles.items():
        if val == '#':
            a, b = tile
            neighbours = [(a, b + 1), (a, b - 1), (a - 1, b), (a + 1, b)]
            vals = [tiles.get(x, 0) for x in neighbours]
            inter = all([x == '#' for x in vals])
            if inter:
                out.append(tile)
    return out


def nobehind(pos, dire, dic):
    a, b = pos
    if dire[0]:
        neighbours = [(a, b-1), (a, b+1)]
    if dire[1]:
        neighbours = [(a-1, b), (a+1, b)]
    return neighbours


def canforward(pos, dire, dic):
    n_pos = pos = (pos[0] + dire[0], pos[1] + dire[1])
    if dic.get(n_pos) == "#":
        return True
    else:
        return False


def get_change(pos, dire, dic):
    change = {
            (0, 1): [(-1, 0), (1, 0)],
            (0, -1): [(1, 0), (-1, 0)],
            (1, 0): [(0, 1), (0, -1)],
            (-1, 0): [(0, -1), (0, 1)]
            }
    c, d = change[dire][0]
    e, f = change[dire][1]
    a, b = pos
    if dic.get((a + c, b + d)) == "#":
        return ((c, d), "R")
    elif dic.get((a + e, b + f)) == "#":
        return ((e, f), "L")
    else:
        print("ERROR", pos, dire)
        return (pos, 99)


if __name__ == "__main__":
    A = Intcode("input.txt")
    A.run([], False)
    codes = A.output
    tiles = defaultdict(lambda: chr(32))
    i, j = 0, 0
    for code in codes:
        if code == 10:
            i = 0
            j += 1
            continue
        tiles[(i, j)] = chr(code)
        i += 1
    # tiles[(10, 55)] = "O"
    # printit(tiles)
    intersections = get_inter(tiles)
    print("Part 1 ", sum([x * y for x, y in intersections]))

    # Part 2

    start = [key for key, value in tiles.items() if value == "^"][0]
    start_dire = (0, -1)
    pos, dire = start, start_dire
    print(start)
    nomore = False
    steps = 0
    path = []
    while not nomore:
        if canforward(pos, dire, tiles):
            pos = (pos[0] + dire[0], pos[1] + dire[1])
            steps += 1
        else:
            # print(pos, dire)
            path.append(str(steps))
            steps = 0
            dire, val = get_change(pos, dire, tiles)
            if val == 99:
                nomore = True
                continue
            path.append(str(val))
    print("".join(path[1:]))

    A = Intcode("input.txt")
    A.input[0] = 2
    program = "A,B,A,C,B,C,A,B,A,C\nR,6,L,10,R,8,R,8\nR,12,L,8,L,10\nR,12,L,10,R,6,L,10\nn\n"
    run_codes = [ord(c) for c in program]
    print(run_codes)
    A.run(run_codes, False)
    codes = A.output
    positions = defaultdict(lambda: " ")
    i, j = 0, 0
    # out = codes.pop()
    for code in codes[:-1]:
        if code == 10:
            i = 0
            j += 1
            continue
        positions[(i, j)] = chr(code)
        i += 1
    printit(positions)
    print(codes[-1])
