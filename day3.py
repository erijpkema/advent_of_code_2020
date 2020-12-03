#!/usr/bin/env python3


from math import prod


def traverse_slope(right, down):
    with open('input3.txt') as f:
        x = 0
        y = 0
        trees = 0
        for line in f:
            if y % down != 0:
                y += 1
                continue
            line = line.strip('\n')
            trees += line[x % len(line)] == '#'
            y += 1
            x += right
    return trees


if __name__ == '__main__':

    print('Answer part 1: {}'.format(traverse_slope(3, 1)))

    inputs_2 = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = [traverse_slope(*i) for i in inputs_2]
    print('Answer part 2: {}'.format(prod(results)))
