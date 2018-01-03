#!/usr/bin/env python3

def parse_inst(inst, registers):
    # l = len(inst)
    if inst[0] == "snd":
        return snd_f(inst, registers)
    elif inst[0] == "add":
        return add_f(inst, registers)
    elif inst[0] == "mul":
        return mul_f(inst, registers)
    elif inst[0] == "mod":
        return mod_f(inst, registers)
    elif inst[0] == "set":
        return set_f(inst, registers)
    elif inst[0] == "rcv":
        return rcv_f(inst, registers)
    elif inst[0] == "jgz":
        return jgz_f(inst, registers)
    else:
        return -1

def set_f(inst, registers):
    if inst[2].isalpha():
        registers[inst[1]] = registers[inst[2]]
    else:
        registers[inst[1]] = int(inst[2])
    return 1

def add_f(inst, registers):
    if inst[2].isalpha():
        registers[inst[1]] += registers[inst[2]]
    else:
        registers[inst[1]] += int(inst[2])
    return 1

def mul_f(inst, registers):
    if inst[2].isalpha():
        registers[inst[1]] *= registers[inst[2]]
    else:
        registers[inst[1]] *= int(inst[2])
    return 1

def mod_f(inst, registers):
    if inst[2].isalpha():
        registers[inst[1]] = registers[inst[1]] % registers[inst[2]]
    else:
        registers[inst[1]] = registers[inst[1]] % int(inst[2])
    return 1

def snd_f(inst, registers):
    global lps
    lps = registers[inst[1]] 
    return 1

def jgz_f(inst, registers):
    global i
    if registers[inst[1]] > 0:
        i = i + int(inst[2]) - 1
    return 1

def rcv_f(inst, registers):
    global lps
    # print(registers[inst[1]])
    if registers[inst[1]] != 0:
        print(lps)
    return 1

if __name__ == "__main__":
    # Init objects
    lps = None #last played sound
    registers = {} # Dictionary of values for each register

    # Instuctions:
    instructions = open('input.txt').readlines()
    # instructions = [
            # "set a 1",
            # "add a 2",
            # "mul a a",
            # "mod a 5",
            # "snd a  ",
            # "set a 0",
            # "rcv a  ",
            # "jgz a -1",
            # "set a 1",
            # "jgz a -2"]

    registers =  {z :0 for z in set([x[4] for x in instructions])}

    range_inst = range(len(instructions))
    i = 0

    while True:
        # print(i)
        tmp = instructions[i].strip().split(' ')
        parse_inst(tmp, registers)
        i += 1
        if i > len(instructions):
            break


