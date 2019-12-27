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
    printit(tiles)
    intersections = get_inter(tiles)
    print("Part 1 ", sum([x * y for x, y in intersections]))

    # Part 2

    start = [key for key, value in tiles.items() if value == "^"][0]
    print(start)
    # A = Incode("input.txt")
    # A.input[0] = 2
    # program = "A,C,B\nR,6,L,10\n10,R,6\nR,8,R,8,R,12,L,8,L\nn\n"
    # run_codes = [ord(c) for c in program][::-1]
    # print(run_codes)
    # A.run(run_codes, False)
    # codes = A.output
    # positions = defaultdict(lambda: 32)
    # i, j = 0, 0
    # # out = codes.pop()
    # for code in codes:
        # if code == 10:
            # i = 0
            # j += 1
            # continue
        # positions[(i, j)] = code
        # i += 1
    # printit(positions)
