#!/bin/env python3
import numpy as np

# def search_neighbours(point, others):
    # if all([point[0] > x for x, y in others]) or
       # all([point[0] < x for x, y in others]) or
       # all([point[1] < y for x, y in others]) or
       # all([point[1] > y for x, y in others]):
           # k`


# def area(point, list_points):
    # others = list_points[:]
    # others.remove(point)




def is_inside(list_points):
    out = []
    for idx, point in enumerate(list_points):
        others = list_points[:idx] + list_points[idx + 1:]
        # print(idx, point, others)
        if (any([point[0] > x for x, y in others]) and
            any([point[0] < x for x, y in others])) and \
           (any([point[1] < y for x, y in others]) and
            any([point[1] > y for x, y in others])):
            out.append(point)
    return(out)


with open("day06_input.txt", "r") as f:
    input = f.readlines()
# input = ['1, 1', '1, 6', '8, 3',
         # '3, 4', '5, 5', '8, 9']

clean = []
for inp in input:
    inp = inp.strip().split(', ')
    inp = list(map(int, inp))
    clean.append(inp)
inside_list = is_inside(clean)

min_x = min([x for x, y in clean])
max_x = max([x for x, y in clean])
min_y = min([y for x, y in clean])
max_y = max([y for x, y in clean])
xv, yv = np.meshgrid(range(min_x, max_x), range(min_y, max_y))
np.dstack(xv, yv).reshape(-1, 2)
print(xv)
# value_area = []

# for element in inside_list:
    # a = area(element, clean)
    # value_area.append({'point': element, 'area': a})
