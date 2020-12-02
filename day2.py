#!/usr/bin/env python3


class Password(object):
    def __init__(self, line):
        """
        Parses an input line.
        """
        instructions, self.passwd = line.split(': ')
        self.min_max, self.letter = instructions.split(' ')
        self.min_c, self.max_c = self.min_max.split('-')
        self.min_c = int(self.min_c)
        self.max_c = int(self.max_c)

    def is_valid(self):

        return self.passwd.count(self.letter) in range(self.min_c,
                                                       self.max_c + 1)

    def is_valid_2(self):
        return (self.passwd[self.min_c - 1] == self.letter) ^ (
            self.passwd[self.max_c - 1] == self.letter)


if __name__ == '__main__':
    p = Password('2-9 c: ccccccccc')
    assert p.is_valid()

    p = Password('1-3 a: abcde')
    assert p.is_valid_2()

    count = 0
    with open('input2.txt') as f:
        for line in f:
            p = Password(line)
            count += p.is_valid()

    print('Answer part 1: {}'.format(count))

    count = 0
    with open('input2.txt') as f:
        for line in f:
            p = Password(line)
            count += p.is_valid_2()

    print('Answer part 2: {}'.format(count))
