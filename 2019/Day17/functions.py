#!/usr/bin/python3


def get_params(l, i, self_v, a0, b0=None):
    if a0 == 0:
        a = l[l[i+1]]
    elif a0 == 1:
        a = l[i+1]
    elif a0 == 2:
        a = l[self_v.rel + l[i+1]]
    if b0 is not None:
        if b0 == 0:
            b = l[l[i+2]]
        elif b0 == 1:
            b = l[i+2] 
        elif b0 == 2:
            b = l[self_v.rel + l[i+2]]
        return (a, b)
    else:
        return (a)


def add_replace(l, i, a0, b0, c0, self_v):
    a, b = get_params(l, i, self_v, a0, b0)
    assign3(l, i, c0, (a+b), self_v)
    # l[l[i+3]] = a + b
    return i+4


def mul_replace(l, i, a0, b0, c0, self_v):
    a, b = get_params(l, i, self_v, a0, b0)
    assign3(l, i, c0, (a*b), self_v)
    # l[l[i+3]] = a * b
    return i+4


def save_p(l, i, a0, input_int, self_v):
    if a0 == 0:
        l[l[i+1]] = input_int
    elif a0 == 1:
        l[i+1] = input_int
    elif a0 == 2:
        l[self_v.rel + l[i+1]] = input_int
    return i + 2


def read_p(l, i, a0, self_v):
    a = get_params(l, i, self_v, a0)
    # print(a)
    self_v.output.append(a)
    return i + 2


def jit(l, i, a0, b0, self_v):
    a, b = get_params(l, i, self_v, a0, b0)
    if a != 0:
        return b
    else:
        return i + 3


def jif(l, i, a0, b0, self_v):
    a, b = get_params(l, i, self_v, a0, b0)
    if a == 0:
        return b
    else:
        return i + 3


def lesst(l, i, a0, b0, c0, self_v):
    a, b = get_params(l, i, self_v, a0, b0)
    if a < b:
        assign3(l, i, c0, 1, self_v)
        # l[l[i+3]] = 1
    else:
        assign3(l, i, c0, 0, self_v)
        # l[l[i+3]] = 0
    return i + 4


def assign3(l, i, c0, val, self_v):
    if c0 == 0:
        l[l[i+3]] = val
    elif c0 == 1:
        print("M3 == 1")
        l[i+1] = val
    elif c0 == 2:
        l[self_v.rel + l[i+3]] = val


def equals(l, i, a0, b0, c0, self_v):
    a, b = get_params(l, i, self_v, a0, b0)
    if a == b:
        assign3(l, i, c0, 1, self_v)
        # l[l[i+3]] = 1
    else:
        assign3(l, i, c0, 0, self_v)
        # l[l[i+3]] = 0
    return i + 4

def adjrel(l, i, m1, self_v):
    a = get_params(l, i, self_v, m1)
    self_v.rel += a
    return i + 2

def param_v(l, i, opcode, m1, m2, m3, input_int, self_v):
    if opcode == 1:
        return add_replace(l, i, m1, m2, m3, self_v)
    elif opcode == 2:
        return mul_replace(l, i, m1, m2, m3, self_v)
    elif opcode == 3:
        return save_p(l, i, m1, input_int, self_v)
    elif opcode == 4:
        return read_p(l, i, m1, self_v)
    elif opcode == 5:
        return jit(l, i, m1, m2, self_v)
    elif opcode == 6:
        return jif(l, i, m1, m2, self_v)
    elif opcode == 7:
        return lesst(l, i, m1, m2, m3, self_v)
    elif opcode == 8:
        return equals(l, i, m1, m2, m3, self_v)
    elif opcode == 9:
        return adjrel(l, i, m1, self_v)
    elif opcode == 99:
        return None
    else:
        print("r_opcode weird")
