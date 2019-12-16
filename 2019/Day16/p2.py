#!/usr/bin/python3

from itertools import cycle
import numpy as np


def read_s(filei):
    return list(open(filei).read().strip())


def toint(string):
    return np.array([int(x) for x in string])


def lastd(intt):
    return int(str(intt)[-1])


# def repandix(string, times=10000):
    # ix = int(string[:7])
    # rep = string * times
    # return rep, ix


if __name__ == "__main__":
    rin = read_s('input.txt')
    ex1 = "03036732577212944063491565474664"
    ex2 = "80871224585914546619083218645595"
    ex3 = "19617804207202209144916044189917"

    base = np.array([int(x) for x in "0, 1, 0, -1".split(',')])
    inputt = toint(rin * 10000)
    offset = int(''.join(inputt[:7].astype(str)))
    n = len(inputt)
    print(offset, n)
    xx = inputt.copy()
    STEPS = 100
    for i in range(10):
        print(xx)
        xx = xx[::-1].cumsum()[n//2-1::-1] % 10
        print(xx)

    newoffset = offset - len(xx)
    print("Part 2:", ''.join(xx[newoffset:newoffset+8].astype(str)))

    # for i in range(n):
        # np.rol

    # tmp_input = inputt
    # length = len(inputt)
    # outputt = [0] * length
    # for m in range(100):
        # print("m", m)
        # for i in range(length):
            # base_it = cycle([x for x in base for k in range(i+1)])
            # next(base_it)
            # for j in range(length):
                # nbase = next(base_it)
                # # print(tmp_input[j], nbase)
                # outputt[i] += (tmp_input[j] * nbase)
            # outputt[i] = lastd(outputt[i])
            # # print("out", outputt[i])
        # tmp_input = outputt
        # outputt = [0] * length
        # print(tmp_input)
    # print(tmp_input[ix:ix + 8])
