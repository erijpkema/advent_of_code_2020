#!/usr/bin/env python3

from collections import namedtuple

Seats = namedtuple('Seats', ['min', 'max'])


def calc_seat_id(spec):
    return calc_row(spec[:7], Seats(0, 127)) * 8 + calc_row(
        spec[7:], Seats(0, 7))


def calc_row(spec, rows):
    """
    Misleadingly now also used for the column.
    Args:
        spec (string): F and B
        rows (tuple): min ans max possible rows.
    """
    # print(f'spec: {spec}\n rows: {rows}')
    if spec[0] in ['F', 'L']:
        max_seat = (rows.max - rows.min) // 2 + rows.min
        min_seat = rows.min
    else:
        min_seat = (rows.max - rows.min) // 2 + rows.min + (
            (rows.max - rows.min) % 2 > 0)
        max_seat = rows.max
    if max_seat == min_seat:
        return min_seat
    else:
        return calc_row(spec[1:], Seats(min_seat, max_seat))


def possible_ids():
    ids = set()
    for row in range(1, 110):
        for column in range(0, 8):
            ids.add(row * 8 + column)
    return ids


if __name__ == '__main__':
    assert calc_row('FBFBBFFRLR', Seats(0, 127)) == 44
    assert calc_row('BFFFBBFRRR', Seats(0, 127)) == 70
    assert calc_seat_id('BFFFBBFRRR') == 567
    assert calc_seat_id('FFFBBBFRRR') == 119
    assert calc_seat_id('BBFFBBFRLL') == 820

    max_seat_id = 0
    with open('input5.txt') as f:
        for line in f:
            seat_id = calc_seat_id(line.strip())
            max_seat_id = max(seat_id, max_seat_id)

    print('Answer part 1: {}'.format(max_seat_id))

    ids = possible_ids()

    with open('input5.txt') as f:
        for line in f:
            seat_id = calc_seat_id(line.strip())
            ids.remove(seat_id)
    print('Answer part 2: {}'.format(ids))
