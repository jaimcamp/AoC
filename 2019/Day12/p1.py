#!/usr/bin/python3
import re
from itertools import combinations


class Planet:
    

    def __init__(self, initial_position):
        self.x, self.y, self.z = initial_position
        self.vx, self.vy, self.vz = [0]*3


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
    for x in data:
        planets.append(Planet(initial_position=x))
    [print(x) for x in planets]
    print()
    for i in range(1000):
        for ix in combinations(range(len(planets)), 2):
            change_g = get_gravity(planets[ix[0]], planets[ix[1]])
            planets[ix[0]].apply_gravity(change_g)
            planets[ix[1]].apply_gravity(tuple(-1 * w for w in change_g))

        [x.apply_velocity() for x in planets]

        # print(f"Step {i}")
        # [print(x) for x in planets]
    [x.get_total_e() for x in planets]
    print(sum([x.total_e for x in planets]))


