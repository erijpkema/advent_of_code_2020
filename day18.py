#!/usr/bin/env python3


class Infix(object):
    """
    Hacked new operator.
    https://code.activestate.com/recipes/384122/
    """

    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __or__(self, other):
        return self.function(other)


mul = Infix(lambda x, y: x * y)
add = Infix(lambda x, y: x + y)


def process(line, part=1):
    line = line.replace('*', '|mul|')
    if part == 1:
        line = line.replace('+', '|add|')
    return eval(line)


if __name__ == '__main__':
    assert process('2 * 3 + (4 * 5)') == 26

    count = 0
    count2 = 0
    with open('input18.txt') as f:
        for line in f:
            count += process(line, part=1)
            count2 += process(line, part=2)

    print('Answer part 1: {}'.format(count))

    print('Answer part 2: {}'.format(count2))
