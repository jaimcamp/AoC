#!/usr/bin/python3


class Intcode:

    def __init__(self, input_file):
        temp = [int(x) for x in
                open(input_file).read().strip().split(',')]
        self.input = temp + [0] * (10000 - len(temp))
        self.i = 0
        self.output = []
        self.stop = False
        self.halt = False
        self.rel = 0


    def __str__(self):
        return str([(i, x) for i, x in enumerate(self.input)])


    def reset_output(self):
        self.output = []


    def run(self, inputs, opprint=False, halt_output=None):
        if opprint:
            print(f"Inputs: {inputs}")
        input_int = None
        while self.i <= len(self.input):
            code = self.input[self.i]
            s_code = str(code).zfill(5)
            opcode = int(s_code[-2:])
            if opprint:
                print("Opcode: {}, Pos: {}, Rel: {}".format(s_code, self.i, self.rel))
            m1 = int(s_code[-3])
            m2 = int(s_code[-4])
            m3 = int(s_code[-5])
            if m3 == 1:
                print("m3 weird")
                self.halt = True
                break
            if opcode == 3:
                if not len(inputs):
                    print("No inputs, halt!")
                    self.stop = True
                    break
                else:
                    input_int = inputs.pop(0)
            elif opcode == 99:
                self.stop = True
                break
            self.i = param_v(self.input, self.i, opcode, m1, m2, m3,
                             input_int, self)
            if halt_output:
                if len(self.output) == halt_output:
                    self.halt = True
                    break


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
    # a = l[i+1] if a0 else l[l[i+1]]
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
