#!/usr/bin/python3

import math
from collections import defaultdict
from scipy.optimize import minimize_scalar


def parse_input(string):
    out = defaultdict(dict)
    for row in string.split("\n"):
        left, right = row.split("=>")
        out_amount, ix = right.strip().split(' ')
        out[ix]["out_amount"] = int(out_amount)
        out[ix]["sources"] = defaultdict(lambda: 0)
        # out[ix]["sources"] = []
        for element in [v.split(' ') for v in [x.strip()
                        for x in left.split(',')]]:
            out[ix]["sources"][element[1]] = int(element[0])
    return out


def read_input(f_in):
    return open(f_in).read().rstrip()


def get_sources(dic_source, element, amount=1, base='ORE'):
    out = defaultdict(lambda: 0)
    excess = defaultdict(lambda: 0)
    sources = dic_source[element]["sources"].copy()
    for key in sources.keys():
        sources[key] *= amount
    while [value for value in sources.values() if value > 0]:
        # print("Begin:", out, excess, sources)
        key = list(sources.keys())[0]
        value = sources.pop(key)
        if value == 0:
            continue
        if key == base:
            out[base] += value
            continue
        i_info = dic_source[key]
        i_amount = i_info["out_amount"]
        times_amount = math.ceil(value/i_amount)
        excess[key] += (times_amount * i_amount) - value
        for sub_key, sub_value in i_info["sources"].items():
            if sub_key == base:
                out[sub_key] += (sub_value * times_amount)
            else:
                sources[sub_key] += (sub_value * times_amount)
        # print("End:", out, excess, sources)
        for key, value in excess.items():
            if sources.get(key, 0) > 0:
                sources[key], excess[key] = max(0, sources[key] - value), max(0, value - sources[key])
    return out, excess


if __name__ == "__main__":
    string = read_input("input.txt")
    input_obj = parse_input(string)
    max_ore = 1e12

    def fuel_error(amount):
        total, excess = get_sources(input_obj, "FUEL", amount=amount)
        ore_left = max_ore - total["ORE"]
        if ore_left < 0:
            return abs(ore_left) * 100
        return ore_left
    total, excess = get_sources(input_obj, "FUEL", amount=1)
    print("Part 1:", total["ORE"])
    base_fuel = max_ore / total["ORE"]
    fuel = minimize_scalar(
            fuel_error,
            bracket=(base_fuel, base_fuel * 2))

    print("Part 2:", int(fuel.x))
