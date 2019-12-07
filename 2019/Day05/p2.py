#!/usr/bin/python3


def run_p1(l, input_int):
    i = 0
    while i <= len(l):
        opcode = l[i]
        s_opcode = str(opcode).zfill(5)
        r_opcode = int(s_opcode[-2:])
        print("Opcode: {}, Pos: {}".format(s_opcode, i))
        m1 = int(s_opcode[-3])
        m2 = int(s_opcode[-4])
        m3 = int(s_opcode[-5])
        if m3 == 1:
            print("m3 weird")
            break
        i_new = param_v(l, i, r_opcode, m1, m2, m3, input_int)
        i = i_new
        if r_opcode == 99:
            break
    return l

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

def read_p(l, i, a0):
    a = l[i+1] if a0 else l[l[i+1]]
    print(a)
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

def param_v(l, i, opcode, m1, m2, m3, input_int):
    if opcode == 1:
        return add_replace(l, i, m1, m2)
    elif opcode == 2:
        return mul_replace(l, i, m1, m2)
    elif opcode == 3:
        return save_p(l, i, m1, input_int)
    elif opcode == 4:
        return read_p(l, i, m1)
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

    

def input_proc(file_i):
    with open(file_i) as f:
        values = [int(x) for x in f.read().strip().split(',')]
    return values

if __name__=="__main__":
    input_l = input_proc('input.txt')
    tmp = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
    example = [int(x) for x in tmp.split(',')]
    # out = run_p1(example, 81)
    out = run_p1(input_l, 5)
    # print([(i, x) for i, x in enumerate(out)])
