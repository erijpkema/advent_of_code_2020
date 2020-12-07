#!/usr/bin/env python3


def parse_input():
    bags = {}
    with open('input7-t.txt') as f:
        for line in f:
            bag = line.strip().split(' contain ')
            bagname = bag[0].strip(' bags')

            if 'no other' in line:
                bags[bagname] = [(0, 'Na')]
                continue

            contents = bag[1][:-1].split(', ')
            contents = [(int(c.split(' ', 1)[0]),
                         c.split(' ', 1)[1].strip(' bags')) for c in contents]
            bags[bagname] = contents
    return bags


def calculate_1(bags, possibles=set(), last_possibles=None):
    last_possibles = possibles.copy()
    for bag in bags.keys():
        names = [c[1] for c in bags[bag]]
        if 'hiny gold' in names:
            possibles.add(bag)
        else:
            for possible in last_possibles:
                if possible in names:
                    possibles.add(bag)

    if possibles == last_possibles:
        return possibles
    else:
        return calculate_1(bags, possibles, last_possibles)


def calculate_2(bags, start='hiny gold'):
    global counter_2
    counter_2 += 1
    for child in bags[start]:
        for times in range(child[0]):
            calculate_2(bags, child[1])


if __name__ == '__main__':

    bags = parse_input()
    possibles = calculate_1(bags)
    print('Answer part 1: {}'.format(len(possibles)))

    counter_2 = 0
    calculate_2(bags)
    # I'm off by one and don't know why...
    print('Answer part 2: {}'.format(counter_2 - 1))
