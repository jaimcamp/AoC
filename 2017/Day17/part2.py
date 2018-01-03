#!/bin/python3

import numpy as np

def insert_into(array, old_position, step, value):
    l = len(array)
    new_position = (old_position + step) % l
    tmp_array = np.insert(array, new_position + 1 , value)
   # np.copyto(array, tmp_array)
    return tmp_array, new_position + 1
    

part1 = np.array([0])
pos = 0
step = 312
val = 1
for i in range(50000000):
    part1, pos = insert_into(part1, pos, step, val)
    val += 1
print(part1[0:2])
