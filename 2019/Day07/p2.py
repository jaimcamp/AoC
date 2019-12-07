#!/usr/bin/python3


from functions import param_v
from itertools import permutations


class Incode:

    def __init__(self, input_file):
        self.input = [int(x) for x in
                      open(input_file).read().strip().split(',')]
        self.i = 0
        self.output = None
        self.stop = False

    def __str__(self):
        return str([(i, x) for i, x in enumerate(self.input)])

    def run(self, inputs, opprint=False):
        print(inputs)
        input_int = None
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
                self.stop = True
                break
            self.i = param_v(self.input, self.i, opcode, m1, m2, m3,
                             input_int, self)
            if opcode == 4:
                break


if __name__ == "__main__":
    max_val = 0
    seq_m = None
    for seq in permutations([5, 6, 7, 8, 9]):
        A = Incode('input.txt')
        B = Incode('input.txt')
        C = Incode('input.txt')
        D = Incode('input.txt')
        E = Incode('input.txt')
        output = 0
        A.run([output, seq[0]], True)
        B.run([A.output, seq[1]])
        C.run([B.output, seq[2]])
        D.run([C.output, seq[3]])
        E.run([D.output, seq[4]])
        output = E.output
        while all([not A.stop, not B.stop, not C.stop, not D.stop, not E.stop]):
            A.run([output])
            B.run([A.output])
            C.run([B.output])
            D.run([C.output])
            E.run([D.output])
            output = E.output
        if output > max_val:
            max_val = output
            seq_m = seq
    print("The max is: {}, with the seq {}".format(max_val, seq_m))
