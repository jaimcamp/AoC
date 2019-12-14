#!/usr/bin/python3

from collections import defaultdict


def parse_input(string):
    out = defaultdict(dict)
    for row in string.split("\n"):
        left, right = row.split("=>")
        out_amount, ix = right.strip().split(' ')
        out[ix]["out_amount"] = int(out_amount)
        out[ix]["sources"] = []
        for element in [v.split(' ') for v in [x.strip()
                        for x in left.split(',')]]:
            out[ix]["sources"].append({"source": element[1],
                                       "amount": int(element[0])})
    return out


def read_input(f_in):
    return open(f_in).read().rstrip()


def get_sources(dic_source, element, base='ORE'):
    element_info = dic_source[element]
    out_amount = element_info['out_amount']
    total = 0
    for ingredient in element_info["sources"]:
        print(ingredient)
        if ingredient['source'] == base:
            total += ingredient['amount']
        else:
            total += (get_sources(dic_source, ingredient['source'], base)[0] * ingredient['amount'])
    return total, out_amount


if __name__ == "__main__":
    string = read_input("ex11.txt")
    input_obj = parse_input(string)
    print(get_sources(input_obj, "C"))
