#!/usr/bin/python3


def get_params(l, i, a0, b0=None):
    a = l[i+1] if a0 else l[l[i+1]]
    if b0 is not None:
        b = l[i+2] if b0 else l[l[i+2]]
        return (a, b)
    else:
        return (a)


def add_replace(l, i, a0, b0):
    a, b = get_params(l, i, a0, b0)
    l[l[i+3]] = a + b
    return i+4


def mul_replace(l, i, a0, b0):
    a, b = get_params(l, i, a0, b0)
    l[l[i+3]] = a * b
    return i+4


def save_p(l, i, a0, input_int):
    if a0:
        l[i+1] = input_int
    else:
        l[l[i+1]] = input_int
    return i + 2


def read_p(l, i, a0, self_v):
    a = l[i+1] if a0 else l[l[i+1]]
    print(a)
    self_v.output = a
    return i + 2


def jit(l, i, a0, b0):
    a, b = get_params(l, i, a0, b0)
    if a != 0:
        return b
    else:
        return i + 3


def jif(l, i, a0, b0):
    a, b = get_params(l, i, a0, b0)
    if a == 0:
        return b
    else:
        return i + 3


def lesst(l, i, a0, b0):
    a, b = get_params(l, i, a0, b0)
    if a < b:
        l[l[i+3]] = 1
    else:
        l[l[i+3]] = 0
    return i + 4


def equals(l, i, a0, b0):
    a, b = get_params(l, i, a0, b0)
    if a == b:
        l[l[i+3]] = 1
    else:
        l[l[i+3]] = 0
    return i + 4


def param_v(l, i, opcode, m1, m2, m3, input_int, self_v):
    if opcode == 1:
        return add_replace(l, i, m1, m2)
    elif opcode == 2:
        return mul_replace(l, i, m1, m2)
    elif opcode == 3:
        return save_p(l, i, m1, input_int)
    elif opcode == 4:
        return read_p(l, i, m1, self_v)
    elif opcode == 5:
        return jit(l, i, m1, m2)
    elif opcode == 6:
        return jif(l, i, m1, m2)
    elif opcode == 7:
        return lesst(l, i, m1, m2)
    elif opcode == 8:
        return equals(l, i, m1, m2)
    elif opcode == 99:
        return None
    else:
        print("r_opcode weird")
