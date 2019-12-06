#!/usr/bin/python3


def run_p1(l, input_int):
    i = 0
    while i <= len(l):
    # for i in range(0, len(l), 4):
        opcode = l[i]
        print("Opcode: {}".format(opcode))
        if opcode == 1:
            add_replace(l, i)
            i += 4
        elif opcode == 2:
            mul_replace(l, i)
            i += 4
        elif opcode == 3:
            save_p(l, i, input_int)
            i += 2
        elif opcode == 4:
            out = read_p(l, i)
            print(out)
            i += 2
        elif opcode == 5:
            i = jit(l, i, 0, 0)
            # i += 3
        elif opcode == 6:
            i = jif(l, i, 0, 0)
            # i += 3
        elif opcode == 7:
            lesst(l, i, 0, 0)
            i += 4
        elif opcode == 8:
            equals(l, i, 0, 0)
            i += 4
        elif opcode == 99:
            print("BREAKING")
            break
        else:
            s_opcode = str(opcode).zfill(5)
            r_opcode = int(s_opcode[-2:])
            m1 = int(s_opcode[-3])
            m2 = int(s_opcode[-4])
            m3 = int(s_opcode[-5])
            # m3 = 1 if len(s_opcode) > 4 else 0
            if m3:
                print("m3 weird")
            i_new = param_v(l, i, r_opcode, m1, m2, m3)
            if r_opcode in [1, 2, 7, 8]:
                i += 4
            elif r_opcode in [3, 4]:
                i += 2
            elif r_opcode in [5, 6]:
                i = i_new
            else:
                print("NO")
            # print(i)
    return l

def param_v(l, i, opcode, m1, m2, m3):
    v1 = l[i+1] if m1 == 1 else l[l[i+1]]
    if opcode == 1:
        v2 = l[i+2] if m2 == 1 else l[l[i+2]]
        v3 = l[i+3] if m3 == 1 else l[i+3]
        l[v3] = v1 + v2
        return(i)
    elif opcode == 2:
        v2 = l[i+2] if m2 == 1 else l[l[i+2]]
        v3 = l[i+3] if m3 == 1 else l[i+3]
        l[v3] = v1 * v2
        return(i)
    elif opcode == 4:
        print(l[v1])
        return(i)
    elif opcode == 5:
        i = jit(l, i, m1, m2)
        return(i)
    elif opcode == 6:
        i = jif(l, i, m1, m2)
        return(i)
    elif opcode == 7:
        lesst(l, i, m1, m2)
        return(i)
    elif opcode == 8:
        equals(l, i, m1, m2)
        return(i)
    else: 
        print("r_opcode weird")

def jit(l, i, a0=True, b0=True):
    a = l[i+1] if a0 else l[l[i+1]]
    b = l[i+2] if b0 else l[l[i+2]]
    if a != 0:
        return b
    else:
        return i + 3
def jif(l, i, a0=True, b0=True):
    a = l[i+1] if a0 else l[l[i+1]]
    b = l[i+2] if b0 else l[l[i+2]]
    if a == 0:
        return b
    else:
        return i + 3
    
def lesst(l, i, a0=True, b0=True):
    a = l[i+1] if a0 else l[l[i+1]]
    b = l[i+2] if b0 else l[l[i+2]]
    if a < b:
        l[i+2] = 1
    else:
        l[i+2] = 0

def equals(l, i, a0=True, b0=True):
    a = l[i+1] if a0 else l[l[i+1]]
    b = l[i+2] if b0 else l[l[i+2]]
    if a == b:
        l[i+2] = 1
    else:
        l[i+2] = 0

def save_p(l, i, input_int):
    l[l[i+1]] = input_int

def read_p(l, i):
    return l[l[i+1]]

def add_replace(l, i):
    tmp = l[l[i+1]] + l[l[i+2]]
    pos = l[i+3]
    l[pos] = tmp

def mul_replace(l, i):
    tmp = l[l[i+1]] * l[l[i+2]]
    pos = l[i+3]
    l[pos] = tmp

def input_proc(file_i):
    with open(file_i) as f:
        values = [int(x) for x in f.read().strip().split(',')]
    return values

if __name__=="__main__":
    input_l = input_proc('input.txt')
    out = run_p1(input_l, 5)
    print(out[0])
