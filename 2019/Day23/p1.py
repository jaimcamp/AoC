#!/usr/bin/python3

from Intcode import Intcode
from collections import deque


def create_network(n):
    comps = dict()
    queues = dict()
    for i in range(n):
        comps[str(i).zfill(2)] = Intcode("input.txt")
        queues[str(i).zfill(2)] = deque([-1])
    return comps, queues


def activate_network(network):
    for name, computer in network.items():
        computer.run([int(name)], False, halt_output=3)
        if computer.halt:
            print("Waiting")


if __name__ == "__main__":
    n = 50
    network, queues = create_network(n)
    activate_network(network)
    found = False
    while not found:
        for name, computer in network.items():
            if queues[name][0] == -1:
                queues[name].append(-1)
                code = [queues[name].popleft()]
            else:
                code = queues[name].popleft()
            computer.run(code, False, halt_output=3)
            if computer.halt:
                output = computer.output
                computer.reset_output()
                print(f"Output: {output}")
                target = str(output[0]).zfill(2)
                if target == "255":
                    print(f"Got to {target}. {output[1:]}")
                    found = True
                    break
                queues[target].appendleft(output[1:])

    # Part 2
    network, queues = create_network(n)
    activate_network(network)
    NAT = None
    idle = False
    to_zero = []
    found = False
    while not found:
        sleep = True
        halt = 0
        if idle:
            idle = False
            print("idle", NAT)
            target = "00"
            queues[target].appendleft(NAT)
            to_zero.append(NAT[1])
            if len(to_zero) > 2:
                if to_zero[-1] == to_zero[-2]:
                    print(to_zero)
                    found = True
                    break
        for name, computer in network.items():
            if queues[name][0] == -1:
                code = [-1]
            else:
                sleep = False
                code = queues[name].popleft()
            computer.run(code, False, halt_output=3)
            if computer.halt:
                output = computer.output
                computer.reset_output()
                target = str(output[0]).zfill(2)
                if target == "255":
                    NAT = output[1:]
                else:
                    queues[target].appendleft(output[1:])
            else:
                halt += 1

        if sleep:
            idle = True
