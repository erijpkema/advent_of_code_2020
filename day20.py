#!/usr/bin/env python3

from collections import defaultdict
import numpy as np
import re


def parse_input():
    tiles = {}
    with open('input20-t.txt') as f:
        image_id = -1
        for line in f:
            if line == '\n':
                # Signals end of array definition.
                tiles[image_id] = np.array(tiles[image_id])
                continue
            m = re.match('(?:Tile )([0-9]+)', line)
            if m:
                image_id = int(m.groups()[0])
                tiles[image_id] = []
                continue
            else:
                tiles[image_id].append([c for c in line.strip('\n')])

    return tiles


def get_borders(arr, rotflip=True):
    """
    Return borders of the array
    """
    rv = []
    rv.append(arr[0])
    rv.append(arr[-1])
    rv.append(arr[:, 0])
    rv.append(arr[:, -1])
    if rotflip:
        for border in range(4):
            rv.append(np.flip(rv[border]))
    return rv


if __name__ == '__main__':

    tiles = parse_input()
    bordercounts = {}
    matches = defaultdict(list)

    for tile1 in tiles.keys():
        bordercounts[tile1] = 0
        for b1 in get_borders(tiles[tile1]):
            for tile2 in tiles.keys():
                if tile2 == tile1:
                    continue
                for b2 in get_borders(tiles[tile2], rotflip=False):
                    match = all(b1 == b2)
                    bordercounts[tile1] += match
                    if match:
                        matches[tile1].append(tile2)

    count = 1
    for tile in bordercounts.keys():
        if bordercounts[tile] == 2:
            count *= tile

    print('Answer part 1: {}'.format(count))
    import pprint
    pprint.pprint(matches)

    # build a new matrix with the ids of tiles
    side = int(np.sqrt(len(tiles)))
    image = [[0 for _ in range(side)] for _ in range(side)]

    # Top left is the first corner we find
    for tile in bordercounts.keys():
        if bordercounts[tile] == 2:
            image[0][0] = tile
            bordercounts.pop(tile)
            break

    # fill in the first row
    for c in range(side):
        for tile in bordercounts.keys():
            if bordercounts[tile] == 3 and image[0][0] in matches[tile]:
                image[0][1] = tile
                bordercounts.pop(tile)
                break

    print('Answer part 2: {}'.format(count))
