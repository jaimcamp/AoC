#!/usr/bin/python3


def run_p1(l, input_int):
    i = 0
    while i <= len(l):
        opcode = l[i]
        print("Opcode: {}".format(opcode))
        s_opcode = str(opcode).zfill(5)
        r_opcode = int(s_opcode[-2:])
        m1 = int(s_opcode[-3])
        m2 = int(s_opcode[-4])
        m3 = int(s_opcode[-5])
        if m3:
            print("m3 weird")
        i_new = param_v(l, i, r_opcode, m1, m2, m3, input_int)
        if r_opcode in [1, 2, 7, 8]:
            i += 4
        elif r_opcode in [3, 4]:
            i += 2
        elif r_opcode in [5, 6]:
            i = i_new
        elif r_opcode == 99:
            break
        else:
            print("NO")
    return l

def param_v(l, i, opcode, m1, m2, m3, input_int):
    if opcode == 1:
        add_replace(l, i, m1, m2)
        return(i)
    elif opcode == 2:
        mul_replace(l, i, m1, m2)
        return(i)
    elif opcode == 3:
        save_p(l, i, m1, input_int)
        return(i)
    elif opcode == 4:
        read_p(l, i, m1)
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
    elif opcode == 99:
        return None
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

def save_p(l, i, a0, input_int):
    if a0:
        l[i+1] = input_int
    else:
        l[l[i+1]] = input_int

def read_p(l, i, a0):
    a = l[i+1] if a0 else l[l[i+1]]
    print(a)
    return i

def add_replace(l, i, a0, b0):
    a = l[i+1] if a0 else l[l[i+1]]
    b = l[i+2] if b0 else l[l[i+2]]
    l[l[i+3]] = a + b

def mul_replace(l, i):
    a = l[i+1] if a0 else l[l[i+1]]
    b = l[i+2] if b0 else l[l[i+2]]
    l[l[i+3]] = a * b

def input_proc(file_i):
    with open(file_i) as f:
        values = [int(x) for x in f.read().strip().split(',')]
    return values

if __name__=="__main__":
    input_l = input_proc('input.txt')
    tmp = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
    example = [int(x) for x in tmp.split(',')]
    out = run_p1(example, 100)
    # out = run_p1(input_l, 5)
    print(out[0])
