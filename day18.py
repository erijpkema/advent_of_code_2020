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

    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __rshift__(self, other):
        return self.function(other)

    def __call__(self, value1, value2):
        return self.function(value1, value2)


mul = Infix(lambda x, y: x * y)
add = Infix(lambda x, y: x + y)


def process(line):
    return eval(line.replace('*', '|mul|').replace('+', '|add|'))


def process2(line):
    return eval(line.replace('*', '|mul|'))


if __name__ == '__main__':
    assert process('2 * 3 + (4 * 5)') == 26

    count = 0
    with open('input18.txt') as f:
        for line in f:
            count += process(line)

    print('Answer part 1: {}'.format(count))

    count = 0
    with open('input18.txt') as f:
        for line in f:
            count += process2(line)

    print('Answer part 2: {}'.format(count))
