#!/bin/env python3

def rec_pop(list_v, meta, let):
    children = list_v.pop(0)
    meta_vals = list_v.pop(0)
    if children == 0:
        while meta_vals > 0:
            meta += list_v.pop(0)
            meta_vals -= 1
        print(let + ": ", children, meta_vals, list_v, meta)
        return(list_v, meta)
    else:
        metas = [None] * children
        for child in range(children):
            list_v, metas[child] = rec_pop(list_v, meta, chr(ord(let)+1))
        while meta_vals > 0:
            meta_tmp = list_v.pop(0)
            if meta_tmp <= len(metas):
                meta += metas[meta_tmp - 1]
            meta_vals -= 1
        print(let + ": ", children, metas, list_v, meta)
        return(list_v, meta)
        # while children > 0:
            # list_v, meta = rec_pop(list_v, meta)
            # children -= 1
        # # list_v, meta = rec_pop(list_v, meta)
        # while meta_vals > 0:
            # meta += list_v.pop(0)
            # meta_vals -= 1
        # return(list_v, meta)


input_vals = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()
with open("day08_input.txt", "r") as f:
    input_vals = f.readline().split()
input_vals = list(map(int, input_vals))
print(input_vals)

meta_count = 0
final_list, meta_count = rec_pop(input_vals, meta_count, 'A')
print(final_list)
print(meta_count)


