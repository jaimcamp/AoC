#!/usr/bin/python3

import networkx as nx
from collections import defaultdict


def find_neighs(pos, what, dic):
    out = []
    a, b = pos
    neighbours = [(a, b+1), (a, b-1), (a-1, b), (a+1, b)]
    for neigh in neighbours:
        if dic.get(neigh) and (dic.get(neigh) in what):
            out.append(neigh)
    return out


tiles = defaultdict(lambda: ' ')
for ix, line in enumerate(open('input.txt').read().rstrip('\n').split('\n')):
    for iy, val in enumerate(line):
        if val == "." or val.isalpha():
            tiles[(ix, iy)] = val
maxi = max([i for i, j in tiles.keys()])
maxj = max([j for i, j in tiles.keys()])

pairs = defaultdict(list)
letters = [(key, value) for key, value in tiles.items() if value.isalpha()]
for key, value in letters:
    exitpos = find_neighs(key, ["."], tiles)
    if not exitpos:
        continue
    diff_a = key[0] - exitpos[0][0]
    diff_b = key[1] - exitpos[0][1]
    pair = (key[0] + diff_a, key[1] + diff_b)
    if tiles[key] <= tiles[pair]:
        pairs[(tiles[key], tiles[pair])].append(exitpos[0])
    else:
        pairs[(tiles[pair], tiles[key])].append(exitpos[0])
# print(pairs)
start = (0, *pairs[('A', 'A')][0])
end = (0, *pairs[('Z', 'Z')][0])
# print(start, end)
del pairs[('A', 'A')]
del pairs[('Z', 'Z')]
print(pairs)
G = nx.Graph()
for k in range(100):
    for key, value in tiles.items():
        if value == ".":
            neighs = find_neighs(key, ["."], tiles)
            key = (k, *key)
            neighs = [(k, *x) for x in neighs]
            [G.add_edge(key, x) for x in neighs]
    for key, values in pairs.items():
        if (values[0][0] in [2, maxi-2]) or \
                (values[0][1] in [2, maxj-2]):
            toadd = [(k, *values[1]), (k+1, *values[0])]
        elif (values[1][0] in [2, maxi-2]) or \
                (values[1][1] in [2, maxj-2]):
            toadd = [(k, *values[0]), (k+1, *values[1])]
        G.add_edge(*toadd)
# print(G.edges)


print(nx.shortest_path_length(G, start, end))
