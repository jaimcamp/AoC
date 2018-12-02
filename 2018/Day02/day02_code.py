twos = 0
threes = 0
with open("day02_input.txt", "r") as f:
    for line in f:
        any_2 = False
        any_3 = False
        chars = ''.join(set(line))
        for char in chars:
            times = line.count(char)
            if times == 2:
                any_2 = True
            elif times == 3:
                any_3 = True
        if any_2:
            twos += 1
        if any_3:
            threes += 1
print(twos)
print(threes)
print(twos * threes)

def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

r = open("day02_input.txt", "r")
lines = r.readlines()
for i1, line_1 in enumerate(lines):
    for i2, line_2 in enumerate(lines):
        if i1 == i2:
            continue
        d = hamming_distance(line_1, line_2)
        if d <= 1:
            print(i1, i2, line_1, line_2)
            out = [c1 for c1, c2 in zip(line_1, line_2) if c1 == c2]
            print(''.join(out))




        


