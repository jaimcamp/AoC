#!/usr/bin/python3

from itertools import cycle


def read_s(filei):
    return list(open(filei).read().strip())


def toint(string):
    return [int(x) for x in string]


def lastd(intt):
    return int(str(intt)[-1])


def repandix(string, times=10000):
    ix = int(string[:7])
    rep = string * times
    return rep, ix


if __name__ == "__main__":
    rin = read_s('input.txt')
    ex1 = "03036732577212944063491565474664"
    ex2 = "80871224585914546619083218645595"
    ex3 = "19617804207202209144916044189917"
    base = [int(x) for x in "0, 1, 0, -1".split(',')]
    rep, ix = repandix(ex1)
    inputt = toint(rep)
    tmp_input = inputt
    length = len(inputt)
    outputt = [0] * length
    for m in range(100):
        print("m", m)
        for i in range(length):
            base_it = cycle([x for x in base for k in range(i+1)])
            next(base_it)
            for j in range(length):
                nbase = next(base_it)
                # print(tmp_input[j], nbase)
                outputt[i] += (tmp_input[j] * nbase)
            outputt[i] = lastd(outputt[i])
            # print("out", outputt[i])
        tmp_input = outputt
        outputt = [0] * length
        print(tmp_input)
    print(tmp_input[ix:ix + 8])
