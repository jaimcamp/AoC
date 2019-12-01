#!/bin/python3

from math import floor

def fuel_calc(mass):
    return floor(mass/3) - 2

def fuel_calc_adv(mass, total):
    fuel = fuel_calc(mass)
    if fuel <= 0:
        return total
    else:
        return fuel_calc_adv(fuel, fuel + total)

def test_fuel():
    mass_vals = [12,14,1969,100756]
    fuel_vals = [2,2,654,33583]
    result_vals = [fuel_calc(x) for x in mass_vals]
    print(result_vals)
    return fuel_vals == result_vals

def test_fuel_adv():
    mass_vals = [14,1969,100756]
    fuel_vals = [2,966,50346]
    result_vals = [fuel_calc_adv(x,0) for x in mass_vals]
    print(result_vals)
    return fuel_vals == result_vals

def input_proc(file_i):
    with open(file_i) as f:
        values = [int(x) for x in f.read().strip().split()]
    return values

if __name__=="__main__":
    values = input_proc('input.txt')
    # results = [fuel_calc(x) for x in values]
    results = [fuel_calc_adv(x,0) for x in values]
    print(sum(results))
