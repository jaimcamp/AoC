#!/usr/bin/python3

L = 119315717514047


def rev_newstack(i):
    return L - 1 - i


def rev_cutn(i, n):
    return (i + n + L) % L


def rev_todead(i, n):
    return modinv(n, L) * i % L


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


def parse_inst(instruction):
    inst, val = None, None
    if "new stack" in instruction:
        inst = 0
    elif "cut" in instruction:
        inst = 1
        val = int(instruction.split(" ")[-1])
    elif "increment" in instruction:
        inst = 2
        val = int(instruction.split(" ")[-1])

    return inst, val


lines = open("input.txt").read().strip().split("\n")
lines.reverse()
X = 2020
pos = X
for line in lines:
    inst, val = parse_inst(line)
    if inst == 0:
        pos = rev_newstack(pos)
    elif inst == 1:
        pos = rev_cutn(pos, val)
    elif inst == 2:
        pos = rev_todead(pos, val)
    else:
        print("Wrong Instruction")
Y = pos

lines = open("input.txt").read().strip().split("\n")
lines.reverse()
pos = Y
for line in lines:
    inst, val = parse_inst(line)
    if inst == 0:
        pos = rev_newstack(pos)
    elif inst == 1:
        pos = rev_cutn(pos, val)
    elif inst == 2:
        pos = rev_todead(pos, val)
    else:
        print("Wrong Instruction")
Z = pos

print(X, Y, Z)
A = (Y - Z) * modinv(X - Y + L, L) % L
B = (Y - A * X) % L

n = 101741582076661
print((pow(A, n, L) * X + (pow(A, n, L) - 1) * modinv(A - 1, L) * B) % L)
