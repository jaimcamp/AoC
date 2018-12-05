#!/bin/env python3
import re

def compare_duo(string_i):
    assert(len(string_i) == 2)
    tmp = string_i.lower()
    if tmp[0] != tmp[1]:
        return(False)
    if string_i[0].isupper() == string_i[1].isupper():
        return(False)
    else:
        return(True)


def go_over(linea):
    for i in range(0, len(linea) - 1, 1):
        tmp = linea[i:i+2]
        out = compare_duo(tmp)
        if out:
            return linea[0:i] + linea[i+2:]
    return linea


r = open("day05_input.txt", "r")
line = r.readline().strip()
r.close()

# line = "dabAcCaCBAcCcaDA"
# print(line)

# l = len(line)
# for i in range(len(line)):
    # line = go_over(line)
    # l_new = len(line)
    # if l_new == l:
        # break
    # l = l_new
    # # print(line)
# print(l)

chars = set(line.lower())

for char in chars:
    tmp_line = re.sub(char, '',  line, flags=re.IGNORECASE)
    l = len(tmp_line)
    for i in range(len(tmp_line)):
        tmp_line = go_over(tmp_line)
        l_new = len(tmp_line)
        if l_new == l:
            break
        l = l_new
    print(char, l)
