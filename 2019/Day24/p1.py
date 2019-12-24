#!/usr/bin/python3

from collections import defaultdict

tiles = defaultdict(lambda: " ")

ex1 = """
....#
#..#.
#..##
..#..
#....
"""

# toread = ex1
toread = open('input.txt').read()
i, j = 0, 0
map_in = [list(x) for x in toread.strip('\n').split('\n')]
for val in map_in:
    j = 0
    for point in val:
        tiles[(i, j)] = point
        j += 1
    i += 1


def n_bugs(pos, dic):
    a, b = pos
    neighbours = [(a, b+1), (a + 1, b), (a, b - 1), (a - 1, b)]
    return sum([1 for x in neighbours if dic.get(x, " ") == "#"])


def new_status(status, n):
    if status == "#" and n != 1:
        return "."
    elif status == "." and n in [1, 2]:
        return "#"
    else:
        return status


old_tiles = [tiles]
while True:
    new_tiles = tiles.copy()
    for key, val in tiles.items():
        n = n_bugs(key, tiles)
        new_val = new_status(val, n)
        new_tiles[key] = new_val
    if sum([1 for x in old_tiles if x == new_tiles]):
        print("found", new_tiles)
        break
    tiles = new_tiles
    old_tiles.append(tiles)

bugs = [key for key, val in new_tiles.items() if val == "#"]
print(bugs)
diversity = 0
for bug in bugs:
    p = (bug[0] * 5) + bug[1]
    diversity += 2 ** p
print(diversity)

