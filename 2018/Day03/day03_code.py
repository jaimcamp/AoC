#!/bin/env python3
import numpy as np


def find_coords():
    return True


def translate_coords(line):
    l_split = line.split(" ")
    l_id = l_split[0][1:]
    l_xy = l_split[2][:-1].split(",")
    l_y, l_x = l_xy
    l_wh = l_split[3].split("x")
    l_h, l_w = l_wh
    l_out = {'id': l_id,
             'x': l_x,
             'y': l_y,
             'width': l_w,
             'height': l_h
             }
    l_out = {k: int(v) for k, v in l_out.items()}
    return l_out


def create_canvas(n=1000):
    canvas = np.zeros((n, n), 'int')
    return canvas


def add_to_canvas(canvas, in_dic):
    canvas[in_dic['x']:in_dic['x'] + in_dic['width'],
           in_dic['y']:in_dic['y'] + in_dic['height']] += 1


def check_canvas(canvas, in_dic):
    is_one = np.all(
        canvas[in_dic['x']:in_dic['x'] + in_dic['width'],
               in_dic['y']:in_dic['y'] + in_dic['height']] == 1)
    if is_one:
        print(in_dic['id'])


with open("day03_input.txt", "r") as f:
# with open("example.txt", "r") as f:
    canvas = create_canvas(1000)
    for line in f:
        in_dic = translate_coords(line.strip())
        add_to_canvas(canvas, in_dic)
print(canvas)
print(np.sum(canvas > 1))


with open("day03_input.txt", "r") as f:
# with open("example.txt", "r") as f:
    for line in f:
        in_dic = translate_coords(line.strip())
        check_canvas(canvas, in_dic)
