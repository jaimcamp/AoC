#!/usr/bin/python3 

import numpy as np

with open('ex14.txt') as f:
    input_f = [list(x) for x in f.read().rstrip().split('\n')]
    input_f = [[1 if w=='#' else 0 for w in v] for v in input_f]
    input_f = np.array(input_f)

asteroids = [x for x in zip(*np.where(input_f.T > 0))]
in_view = {}

# print(input_f.T)

for i, x in enumerate(asteroids):
    to_check = asteroids[:i] + asteroids[i+1:]
    tmp = np.zeros((len(to_check)))
    for j, other in enumerate(to_check):
        a, b = other[0] - x[0], other[1] - x[1]
        rad = np.arctan2(b, a)
        tmp[j] = ( rad )
    x_num = len(np.unique(tmp))
    in_view[x] = x_num
max_asteroid = max(in_view, key=in_view.get)
print("Asteroid in {} with {}".format(max_asteroid, in_view[max_asteroid]))
