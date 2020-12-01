#!/usr/bin/env python3


def find_part_1(numbers):
    for n in numbers:
        for n2 in numbers:
            if n + n2 == 2020:
                return n * n2


def find_part_2(numbers):
    for n in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if sum((n, n2, n3)) == 2020:
                    return n * n2 * n3


if __name__ == '__main__':
    with open('input1.txt') as f:
        numbers = [int(i) for i in f.read().strip().split('\n')]

    print('Answer part 1: {}'.format(find_part_1(numbers)))

    print('Answer part 2: {}'.format(find_part_2(numbers)))
