#!/usr/bin/env python3

from collections import defaultdict


class Tile(object):
    def __init__(self):
        """
        mapping
        Black: True, White: False
        """
        self.color = False

    def flip(self):
        self.color = self.color is False


# axial directions
directions = {
    'e': (1, 0),
    'se': (0, 1),
    'sw': (-1, 1),
    'w': (-1, 0),
    'nw': (0, -1),
    'ne': (1, -1)
}

floor = defaultdict(Tile)


def get_neighbours(coords):
    """
    Return a list of neighbouring coordinates
    """
    rv = []
    for offset in directions.values():
        rv.append((coords[0] + offset[0], coords[1] + offset[1]))
    return rv


def neighbouring_black_tiles(coords):
    """
    Return the number of black tiles around position.
    """
    return sum([floor[c].color for c in get_neighbours(coords)])


def daily_flip(floor):
    to_be_flipped = set()
    known_tiles = list(floor.keys())
    for coords in known_tiles:
        if floor[coords].color:  # is Black
            count = neighbouring_black_tiles(coords)
            if count > 2 or count == 0:
                to_be_flipped.add(coords)
            for neighbour in get_neighbours(coords):
                if not floor[neighbour].color and neighbouring_black_tiles(
                        neighbour) == 2:
                    to_be_flipped.add(neighbour)
    for coord in to_be_flipped:
        floor[coord].flip()


if __name__ == '__main__':

    with open('input24.txt') as f:
        for line in f:
            line = line.strip()
            coords = [0, 0]
            while len(line) != 0:
                if line[0] in ('e', 'w'):
                    direction = line[0]
                    line = line[1:]
                else:
                    direction = line[:2]
                    line = line[2:]
                coords[0] += directions[direction][0]
                coords[1] += directions[direction][1]
            floor[tuple(coords)].flip()

    count = sum([tile.color for tile in floor.values()])
    print('Answer part 1: {}'.format(count))

    for _ in range(100):
        daily_flip(floor)

    count = sum([tile.color for tile in floor.values()])
    print('Answer part 2: {}'.format(count))
