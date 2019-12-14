#!/usr/bin/python3

def parse_input(string):
    out = {}
    for row in string.split("\n"):
        # print(row)
        left, right = row.split("=>")
        out_amount, ix = right.strip().split(' ')
        out[ix] = {"out_amount": out_amount}
        left_l = [x.strip() for x in left.split(',')]
        print(left_l)
        print([ix for ix in [x.split(' ') for x in left_l]])
        # for sides in row.split("=>"):
            # for solos in sides.strip().split(","):
                # print(solos)
    # dd = [solos for row in string.split("\n") for sides in row.split("=>") for solos in sides.strip().split(",")]
    # out = string.split("\n")
    # out = [x.split("=>") for x in out]
    # out = [[y.strip() for y in x] for x in out]
    # out = [x.strip() for x in string]
    return out

def read_input(f_in):
    return open(f_in).read().rstrip()

if __name__=="__main__":
    string = read_input("ex11.txt")
    input_obj = parse_input(string)
    print(input_obj)
