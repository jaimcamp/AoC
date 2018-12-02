value = 0
with open("day01input.txt", "r") as f:
    for line in f:
        if not line:
            break
        tmp = "value + " + line
        value = eval(tmp)
    print(value)


freqs = []
value = 0
found = False
while True:
    with open("day01input.txt", "r") as f:
        for line in f:
            if not line:
                break
            tmp = eval("value + " + line)
            if tmp in freqs:
                print(tmp)
                found = True
                break
            freqs.append(tmp)
            value = tmp
    if found:
        break
