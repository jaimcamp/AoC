#!/usr/bin/python3

def split_in(list_in, n):
    return(list_in[i:i+n] for i in range(0, len(list_in), n))

def add_replace(l, i):
    tmp = l[l[i+1]] + l[l[i+2]]
    pos = l[i+3]
    l[pos] = tmp

def mul_replace(l, i):
    tmp = l[l[i+1]] * l[l[i+2]]
    pos = l[i+3]
    l[pos] = tmp

def test_p1():
    test_list = [1,9,10,3,2,3,11,0,99,30,40,50]

    for i in range(0, len(test_list), 4):
        opcode = test_list[i]
        print(opcode)
        if opcode == 1:
            add_replace(test_list, i)
        elif opcode == 2:
            mul_replace(test_list, i)
        elif opcode == 99:
            break
        else:
            print("Wrong OPCODE")
            break
        print(test_list)
    print(test_list)
    
def run_p1(l):
    for i in range(0, len(l), 4):
        opcode = l[i]
        if opcode == 1:
            add_replace(l, i)
        elif opcode == 2:
            mul_replace(l, i)
        elif opcode == 99:
            break
        else:
            # print("Wrong OPCODE")
            break
    return l

def input_proc(file_i):
    with open(file_i) as f:
        values = [int(x) for x in f.read().strip().split(',')]
    return values

if __name__=="__main__":
    # Part 2
    for noun in range(0,100):
        for verb in range(0,100):
            input_l = input_proc('input.txt')
            print((noun, verb))
            input_l[1] = noun
            input_l[2] = verb
            out = run_p1(input_l)
            if out[0] == 19690720:
                print(noun*100 + verb)
                break
        else:
            continue
        break


    # Part 1
    # input_l[1] = 12
    # input_l[2] = 2
    # out = run_p1(input_l)
    # print(out[0])

