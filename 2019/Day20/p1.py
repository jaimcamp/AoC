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


example1 = """
         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       
"""

tiles = defaultdict(lambda: ' ')
# for ix, line in enumerate(example1.split('\n')):
for ix, line in enumerate(open('input.txt').read().rstrip('\n').split('\n')):
    for iy, val in enumerate(line):
        if val == "." or val.isalpha():
            tiles[(ix, iy)] = val

G = nx.Graph()
for key, value in tiles.items():
    if value == ".":
        neighs = find_neighs(key, ["."], tiles)
        [G.add_edge(key, x) for x in neighs]
# print(G.nodes)

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
start = pairs[('A', 'A')][0]
end = pairs[('Z', 'Z')][0]
del pairs[('A', 'A')]
del pairs[('Z', 'Z')]
for key, value in pairs.items():
    G.add_edge(*value)


print(nx.shortest_path_length(G, start, end))
