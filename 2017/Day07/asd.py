import re, collections

with open("input.txt") as fp:
    text = fp.read()

weight = {}
children = {}
for line in text.strip().splitlines():
    label, n, *xs = re.findall(r'\w+', line)
    weight[label] = int(n)
    children[label] = tuple(xs)

root, = set(weight) - {c for cs in children.values() for c in cs}

def total_weight(label):
    sub = [total_weight(c) for c in children[label]]
    if len(set(sub)) > 1:
        (target, _), (failure, _) = collections.Counter(sub).most_common()
        print(target - failure + weight[children[label][sub.index(failure)]])
        return weight[label] + sum(sub)
    return weight[label] + sum(sub)

print(total_weight(root))

