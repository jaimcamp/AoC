#!/usr/bin/python3

from cards import Cards

A = Cards(n=10007)

with open('input.txt') as f:
    for line in f:
        A.run(line.strip())

print("P1:", A.cards.index(2019))
