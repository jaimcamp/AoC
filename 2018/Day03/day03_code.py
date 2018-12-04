#!/bin/env python3
import numpy as np


def find_coords():
    return True


def translate_coords(line):
    l_split = line.split(" ")
    l_id = l_split[0][1:]
    l_xy = l_split[2][:-1].split(",")
    l_x, l_y = l_xy
    l_wh = l_split[3].split("x")
    l_w, l_h = l_wh
    # l_out = [l_id, l_x, l_y, l_w, l_h]
    l_out = {'id': l_id,
             'x': l_x,
             'y': l_y,
             'width': l_w,
             'height': l_h
             }
    return l_out


cloth = np.zeros((1000, 1000))
with open("day03_input.txt", "r") as f:
    for line in f:
        print(translate_coords(line.strip()))
