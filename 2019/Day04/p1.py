#!/usr/bin/python3

s_input = [264360,746325]
count = 0
for num in range(s_input[0], s_input[1] + 1):
    nstr = str(num)
    if nstr == ''.join(sorted(nstr)):
        if any([i==j for i, j in zip(nstr, nstr[1:])]):
            count += 1
print("Number of passwords: {}".format(count))

from collections import Counter
count = 0
for num in range(s_input[0], s_input[1] + 1):
    nstr = str(num)
    if nstr == ''.join(sorted(nstr)):
        if 2 in Counter(nstr).values():
            count += 1
print("Number of passwords in p2: {}".format(count))
    
    
