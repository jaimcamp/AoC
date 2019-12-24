#!/usr/bin/python3

from collections import defaultdict

ex1 = """
....#
#..#.
#.?##
..#..
#....
"""


def n_bugs(pos, dic):
    a, b, c = pos
    bugs = 0
    if b == 0:
        nb = [(a, b + 1, c), (a - 1, 1, 2)]
    elif b == 4:
        nb = [(a, b - 1, c), (a - 1, 3, 2)]
    else:
        nb = [(a, b + 1, c), (a, b - 1, c)]
    if c == 0:
        nc = [(a, b, c + 1), (a - 1, 2, 1)]
    elif c == 4:
        nc = [(a, b, c - 1), (a - 1, 2, 3)]
    else:
        nc = [(a, b, c + 1), (a, b, c - 1)]
    neighbours = nb + nc

    if (b, c) == (1, 2):
        neighbours = [(a, 1, 3), (a, 1, 1), (a, 0, 2),
                      (a + 1, 0, 0), (a + 1, 0, 1), (a + 1, 0, 2),
                      (a + 1, 0, 3), (a + 1, 0, 4)]
    elif (b, c) == (2, 1):
        neighbours = [(a, 3, 1), (a, 1, 1), (a, 2, 0),
                      (a + 1, 0, 0), (a + 1, 1, 0), (a + 1, 2, 0),
                      (a + 1, 3, 0), (a + 1, 4, 0)]
    elif (b, c) == (3, 2):
        neighbours = [(a, 3, 1), (a, 3, 3), (a, 4, 2),
                      (a + 1, 4, 0), (a + 1, 4, 1), (a + 1, 4, 2),
                      (a + 1, 4, 3), (a + 1, 4, 4)]
    elif (b, c) == (2, 3):
        neighbours = [(a, 1, 3), (a, 3, 3), (a, 2, 4),
                      (a + 1, 0, 4), (a + 1, 1, 4), (a + 1, 2, 4),
                      (a + 1, 3, 4), (a + 1, 4, 4)]

    # if a == 0:
        # print((b, c), neighbours)
    bugs = sum([1 for x in neighbours if dic.get(x, " ") == "#"])
    if (b, c) == (2, 2):
        return 0
    return bugs


def new_status(status, n):
    if status == "#" and n != 1:
        return "."
    elif status == "." and n in [1, 2]:
        return "#"
    else:
        return status


if __name__ == "__main__":
    tiles = defaultdict(lambda: ".")
    # toread = ex1
    toread = open('input.txt').read()
    i, j = 0, 0
    map_in = [list(x) for x in toread.strip('\n').split('\n')]
    for val in map_in:
        j = 0
        for point in val:
            tiles[(0, i, j)] = point
            j += 1
        i += 1
    for k in range(-500, 501):
        for i in range(5):
            for j in range(5):
                if (i, j) == (2, 2):
                    tiles[(k, i, j)] = "?"
                tiles[(k, i, j)]
    for i in range(200):
        new_tiles = tiles.copy()
        for key, val in tiles.items():
            n = n_bugs(key, tiles)
            new_val = new_status(val, n)
            new_tiles[key] = new_val
        tiles = new_tiles

    total_bugs = 0
    for k in range(-200, 201):
        print(k)
        for i in range(5):
            for j in range(5):
                print(tiles[(k, i, j)], end="")
                if tiles[(k, i, j)] == "#":
                    total_bugs += 1
            print()

    print(total_bugs)
