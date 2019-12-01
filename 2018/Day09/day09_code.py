#!/bin/env python3
from itertools import cycle
from collections import defaultdict

with open("day09_input.txt", "r") as f:
        input = f.read().strip().split()

# input = "10 players; last marble is worth 1618 points".split()
# input = "9 players; last marble is worth 25 points".split()
input = "13 players; last marble is worth 7999 points".split()
n_players = int(input[0])
n_marbles = int(input[6])

players = cycle(range(n_players))
marbles = iter(range(n_marbles + 1))
score = defaultdict(list)

results = [next(marbles)]

# Init:

player = next(players) + 1
current = results[0]
results.insert(1, next(marbles))


# print(player, results)
for marble in marbles:
    player = next(players) + 1
    if marble % 23 == 0:
        score[player].append(marble)
        i_out = current - 8
        # if i_out < 0:
        # i_out = k
        m_out = results.pop(i_out)
        score[player].append(m_out)
        current = i_out + 1
        continue

    new_pos = (current + 1)
    if new_pos > len(results):
        new_pos = new_pos % len(results)
    results.insert(new_pos, marble)
    current = new_pos + 1
    # print(player, results)

print(score)
final_score = {key: sum(score[key]) for key in score}
print(final_score)
print(max(final_score.values()))
