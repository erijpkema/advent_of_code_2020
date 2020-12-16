#!/usr/bin/env python3


def to_range(text):
    """
    Convert a-b string to range(a,b + 1)
    """
    return range(*[int(i) + 1 for i in text.split('-')])


if __name__ == '__main__':
    specs = {}
    other_tickets = []

    with open('input16.txt') as f:
        for line in f:
            if line == 'your ticket:\n':
                break
            elif line == '\n':
                continue
            key, value = line.strip().split(': ')
            ranges = [to_range(i) for i in value.split(' or ')]
            specs[key] = ranges
        my_ticket = [int(i) for i in f.readline().strip().split(',')]
        for line in f:
            if line == '\n':
                continue
            elif line == 'nearby tickets:\n':
                continue
            other_tickets.append([int(i) for i in line.strip().split(',')])

    invalids = []
    all_the_specs = [i for value in specs.values() for i in value]
    for ticket in other_tickets:
        for value in ticket:
            ok = False
            for spec in all_the_specs:

                if value in spec:
                    ok = True
                    break
            if not ok:
                invalids.append(value)


    print('Answer part 1: {}'.format(sum(invalids)))

    count = 0
    print('Answer part 2: {}'.format(count))
