#!/usr/bin/python3 

import numpy as np
from itertools import cycle

with open('input.txt') as f:
    input_f = [list(x) for x in f.read().rstrip().split('\n')]
    input_f = [[1 if w=='#' else 0 for w in v] for v in input_f]
    input_f = np.array(input_f)

asteroids = [x for x in zip(*np.where(input_f.T > 0))]
in_view = {}

asteroid = (20, 18)
# asteroid = (11, 13)

ixasteroid = asteroids.index(asteroid)
to_check = asteroids[:ixasteroid] + asteroids[ixasteroid+1:]
other_asteroids = {}
deleted_asteroids = []
for j, other in enumerate(to_check):
    a, b = other[0] - asteroid[0], other[1] - asteroid[1]
    rad = np.arctan2(b, a)
    ang = rad * 180 / np.pi
    dist = abs(a) + abs(b)
    other_asteroids[other] = {"ang": ang, "dist": dist, "rad": rad}
u_ang = sorted(list(set(x['ang'] for x in other_asteroids.values())))
i_start = u_ang.index(-90)
u_ang = u_ang[i_start:] + u_ang[:i_start]
for val in cycle(u_ang):
    if len(other_asteroids) == 0:
        break
    tmp = {}
    for other, charac in other_asteroids.items():
        if charac['ang'] == val:
            tmp[other] = charac['dist']
    if len(tmp) == 0:
        continue
    out = min(tmp.items(), key=lambda x: x[1])
    del other_asteroids[out[0]]
    deleted_asteroids.append(out[0])

print(deleted_asteroids[199][0] * 100 + deleted_asteroids[199][1])
