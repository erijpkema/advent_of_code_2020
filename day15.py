#!/usr/bin/env python3


def calculate_next(seq):
    if seq[-1] not in seq[:-1]:
        return 0
    else:
        # find forlast occurence.
        # -1 because i chop the end of seq.
        previous = len(seq) - seq[-2::-1].index(seq[-1]) - 1
        return len(seq) - previous


def solve(seq, limit=2020):
    for _ in range(len(seq), limit):
        seq.append(calculate_next(seq))

        # let's chop the first bit off the list if possible.
        try:
            first = seq[:-1].index(seq[-1])
            seq = seq[first - 1:]
        except ValueError:
            continue

    return seq[-1]


if __name__ == '__main__':

    assert calculate_next([0, 3, 6, 0]) == 3
    assert solve([1, 3, 2]) == 1
    assert solve([2, 1, 3]) == 10
    assert solve([1, 2, 3]) == 27
    assert solve([2, 3, 1]) == 78
    assert solve([3, 2, 1]) == 438
    assert solve([3, 1, 2]) == 1836

    print('Answer part 1: {}'.format(solve([20, 0, 1, 11, 6, 3])))

    assert solve([0, 3, 6], 30000000) == 175594
    print('asserted 1')
    assert solve([1, 3, 2], 30000000) == 2578
    assert solve([2, 1, 3], 30000000) == 3544142
    assert solve([1, 2, 3], 30000000) == 261214
    assert solve([2, 3, 1], 30000000) == 6895259
    assert solve([3, 2, 1], 30000000) == 18
    assert solve([3, 1, 2], 30000000) == 362

    print('Answer part 2: {}'.format(solve([20, 0, 1, 11, 6, 3], 30000000)))
