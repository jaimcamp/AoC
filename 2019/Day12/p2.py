#!/usr/bin/python3
import re
from itertools import combinations
import numpy as np


class Planet:
    

    def __init__(self, initial_position):
        self.x0, self.y0, self.z0 = initial_position
        self.vx0, self.vy0, self.vz0 = [0]*3
        self.x, self.y, self.z = initial_position
        self.vx, self.vy, self.vz = [0]*3

    def __eq__(self, other): 
        if not isinstance(other, Planet):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z and self.vx==other.vx and self.vy == other.vy and self.vz == self.vz

    def samex(self, other): 
        if not isinstance(other, Planet):
            return NotImplemented
        return self.x == other.x and self.vx==other.vx 

    def samey(self, other): 
        if not isinstance(other, Planet):
            return NotImplemented
        return self.y == other.y and self.vy==other.vy 

    def samez(self, other): 
        if not isinstance(other, Planet):
            return NotImplemented
        return self.z == other.z and self.vz==other.vz 


    def __str__(self):
        return "Position {}, {}, {}\nVel {} {} {}".format(
                self.x, self.y, self.z,
                self.vx, self.vy, self.vz)
    
    def apply_gravity(self, gravity):
        self.vx += gravity[0]
        self.vy += gravity[1]
        self.vz += gravity[2]


    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_total_e(self):
        self.potential = abs(self.x) + abs(self.y) + abs(self.z)  
        self.kinetic = abs(self.vx) + abs(self.vy) + abs(self.vz)  
        self.total_e = self.potential * self.kinetic

def read_d(path):
    with open(path) as f:
        tmp = [re.findall(r'-?\d+', line) for line in f]
        return [[int(v) for v in d] for d in tmp]


def sign(val):
    return (val>0) - (val<0)


def get_gravity(p1, p2):
    diffx = sign(p2.x - p1.x)
    diffy = sign(p2.y - p1.y)
    diffz = sign(p2.z - p1.z)

    return (diffx, diffy, diffz)

if __name__=="__main__":
    data = read_d("input.txt")
    planets = []
    originals = []
    for x in data:
        planets.append(Planet(initial_position=x))
        originals.append(Planet(initial_position=x))
    [print(x) for x in planets]
    print()
    same_x, same_y, same_z = [True] * 3
    i = 1
    while any([same_x, same_y, same_z]):
        for ix in combinations(range(len(planets)), 2):
            change_g = get_gravity(planets[ix[0]], planets[ix[1]])
            planets[ix[0]].apply_gravity(change_g)
            planets[ix[1]].apply_gravity(tuple(-1 * w for w in change_g))

        [x.apply_velocity() for x in planets]

        # print([x.samey(y) for x, y in zip(planets, originals)])
        comparison_x = all([x.samex(y) for x, y in zip(planets, originals)])
        comparison_y = all([x.samey(y) for x, y in zip(planets, originals)])
        comparison_z = all([x.samez(y) for x, y in zip(planets, originals)])
        if same_x:
            if comparison_x:
                same_x = False
                print(f"X: {i}")
                xf = i
        if same_y:
            if comparison_y:
                same_y = False
                print(f"Y: {i}")
                yf = i
        if same_z:
            if comparison_z:
                same_z = False
                print(f"Z: {i}")
                zf = i
        i += 1
    lcm = np.lcm.reduce([xf, yf, zf])
    print("Total {}".format(lcm))


