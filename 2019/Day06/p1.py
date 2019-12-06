#!/usr/bin/python3

import pdb
import networkx as nx
import matplotlib.pyplot as plt


def read_graphdata(filei):
    with open(filei) as f:
        return [tuple(x.strip().split(')')) for x in f]


if __name__ == "__main__":
    in_graph = read_graphdata('input.txt')
    # in_graph = read_graphdata('example.txt')
    G = nx.DiGraph()
    G.add_edges_from(in_graph)
    # nx.draw(G)
    # plt.savefig('G.png')
    print(nx.transitive_closure(G).size())
    print((nx.shortest_path_length(G.to_undirected(), "YOU", "SAN")-2))
