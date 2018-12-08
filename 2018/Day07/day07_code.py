#!/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt
import string


input_val = [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.'
        ]

with open("day07_input.txt", "r") as f:
    input_val = f.readlines()


def process_input(list_input):
    out = []
    for line in list_input:
        _, first, *_, second, _, _ = line.strip().split(' ')
        out.append([first, second])
    return(out)


edges = process_input(input_val)
DG = nx.DiGraph()
for edge in edges:
    DG.add_edge(*edge)

nx.draw(DG, with_labels=True)
plt.savefig("plot.png")
lex_list = list(nx.lexicographical_topological_sort(DG))
print(''.join(lex_list))

times = {}
for char in string.ascii_uppercase:
    times[char] = ord(char) - 64 + 60

workers = 5
available = lex_list[:]
working = list(None * workes)
working[0] = 'M'
while True:
   DG.predecessors(working[0]) 
    
