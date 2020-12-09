#!/usr/bin/env python3


def check_valid(numbers, preamble=5):
    for index, n in enumerate(numbers[preamble:]):
        start = index
        valid = False

        for index1, n1 in enumerate(numbers[start:index + preamble]):
            if valid is True:
                break
            for index2, n2 in enumerate(numbers[start:index + preamble]):
                if n1 + n2 == n:
                    valid = True
                    break
        if valid is False:
            return n


def part_2(numbers, p1):
    for start in range(len(numbers)):
        count = 0
        n = 2
        while count < p1:
            count = sum(numbers[start:n])
            if count == p1:
                return sum([min(numbers[start:n]), max(numbers[start:n])])
            n += 1


if __name__ == '__main__':

    with open('input9.txt') as f:
        for line in f:
            numbers = [int(line.strip()) for line in f]

    p1 = check_valid(numbers, preamble=25)
    print('Answer part 1: {}'.format(p1))

    print('Answer part 2: {}'.format(part_2(numbers, p1)))
