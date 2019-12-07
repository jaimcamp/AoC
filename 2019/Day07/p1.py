#!/usr/bin/python3


from functions import param_v
from itertools import permutations


class Incode:

    def __init__(self, input_file):
        self.input = [int(x) for x in
                      open(input_file).read().strip().split(',')]
        self.i = 0
        self.output = None

    def __str__(self):
        return str([(i, x) for i, x in enumerate(self.input)])

    def run(self, inputs, opprint=False):
        while self.i <= len(self.input):
            code = self.input[self.i]
            s_code = str(code).zfill(5)
            opcode = int(s_code[-2:])
            if opprint:
                print("Opcode: {}, Pos: {}".format(s_code, self.i))
            m1 = int(s_code[-3])
            m2 = int(s_code[-4])
            m3 = int(s_code[-5])
            if m3 == 1:
                print("m3 weird")
                break
            if opcode == 3:
                input_int = inputs.pop()
            elif opcode == 99:
                break
            self.i = param_v(self.input, self.i, opcode, m1, m2, m3,
                             input_int, self)


if __name__ == "__main__":
    # seq = [4, 3, 2, 1, 0][::-1]
    # seq = [1, 0, 4, 3, 2]
    max_val = 0
    seq_m = None
    for seq in permutations([0, 1, 2, 3, 4]):
        output = 0
        for i in seq:
            run_input = [output, i]
            tmp = Incode('input.txt')
            tmp.run(run_input, False)
            output = tmp.output
        if output > max_val:
            max_val = output
            seq_m = seq
    print("The max is: {}, with the seq {}".format(max_val, seq_m))
