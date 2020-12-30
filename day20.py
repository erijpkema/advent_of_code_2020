#!/usr/bin/env python3

from collections import defaultdict
import copy
import numpy as np
from pprint import pprint
import re


def parse_input():
    tiles = {}
    with open('input20.txt') as f:
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


def rot_flip(arr):
    for rot in arr, np.rot90(arr):
        yield rot
        yield np.flip(rot, 0)
        yield np.flip(rot, 1)
        yield np.flip(np.flip(rot, 1), 0)


def get_layout(matches):
    """
    Calculate a matrix of tile ids
    """
    id_matrix = np.zeros((side, side), dtype=int)
    matches2 = copy.deepcopy(matches)
    # Whichever image with two neighbours we find first is the top left corner.
    for tile in matches.keys():
        if len(matches[tile]) == 2:
            id_matrix[0][0] = tile
            matches2.pop(tile)
            break

    for i in range(len(id_matrix)):
        for j in range(len(id_matrix[0])):
            if i == 0 and j >= 1:

                for tile in matches.keys():
                    if len(matches2[tile]) in (
                            2, 3) and id_matrix[i][j - 1] in matches2[tile]:
                        id_matrix[i][j] = tile
                        matches2.pop(tile)
                        break
            elif i >= 1 and j == 0:
                for tile in matches2.keys():
                    if id_matrix[i - 1][j] in matches2[tile]:
                        id_matrix[i][j] = tile
                        matches2.pop(tile)
                        break
            elif i >= 1 and j >= 1:
                for tile in matches2.keys():
                    if id_matrix[i][j - 1] in matches2[tile] and \
                      id_matrix[i - 1][j] in matches2[tile]:
                        id_matrix[i][j] = tile
                        matches2.pop(tile)
                        break
    return id_matrix


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

    len_tile = len([i for i in tiles.values()][0]) - 2  # sides cut off..
    nr_tiles = len(tiles.keys())
    side = int(np.sqrt(nr_tiles))
    id_matrix = get_layout(matches)
    tile_matrix = [[None for _ in range(side)] for r in range(side)]

    len_image = side * len_tile  # The outer sides are also cut off..
    image = np.zeros((len_image, len_image), dtype="<U3")

    #  Add the first two tiles.
    tile1 = tiles[id_matrix[0][0]]
    tile2 = tiles[id_matrix[0][1]]

    # rotate/flip such that last column of tile1 = first column of tile2.
    found = False
    for rot in rot_flip(tile1):
        if found:
            break
        for rot2 in rot_flip(tile2):
            # check left right and if tile below could fit.
            if np.array_equal(rot[:, -1], rot2[:, 0]) and list(rot[-1]) in [
                    list(a) for a in get_borders(tiles[id_matrix[1][0]])
            ]:
                tile_matrix[0][0] = rot
                tile_matrix[0][1] = rot2
                left = rot[1:-1, 1:-1]
                right = rot2[1:-1, 1:-1]
                found = True
                break
    image[0:len_tile, 0:len_tile] = left
    image[0:len_tile, len_tile:2 * len_tile] = right
    # now we have an image with the two top left tiles added
    # And also a tile matrix with those added including the borders.

    for i in range(side):
        for j in range(side):
            if i == 0 and j <= 1:
                # already filed in
                continue
            elif i == 0:
                for rot in rot_flip(tiles[id_matrix[i][j]]):
                    # is the first column equal to last of tile to the left?
                    if np.array_equal(tile_matrix[i][j - 1][:, -1], rot[:, 0]):
                        tile_matrix[i][j] = rot
                        image[0:len_tile, j * len_tile:(j + 1) *
                              len_tile] = rot[1:-1, 1:-1]
            else:
                for rot in rot_flip(tiles[id_matrix[i][j]]):
                    # is the top row equal to bottom of tile above?
                    if np.array_equal(tile_matrix[i - 1][j][-1], rot[0]):
                        tile_matrix[i][j] = rot
                        image[i * len_tile:(i + 1) * len_tile, j *
                              len_tile:(j + 1) * len_tile] = rot[1:-1, 1:-1]

    print('\n'.join([''.join(line) for line in image]))

    sea_monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
    monster_coords = set()
    for i, line in enumerate(sea_monster.split('\n')):
        for j, c in enumerate(line):
            if c == '#':
                monster_coords.add((i, j))

    monster_found = False
    for form in rot_flip(image):
        if monster_found:
            break

        im_orient = form

        for i in range(len_image - 2):  # substract height of monster
            for j in range(len_image - 19):  # substract length of monster
                match = all([
                    im_orient[m[0] + i][m[1] + j] == '#'
                    for m in monster_coords
                ])
                if match:
                    print('Found a monster')
                    monster_found = True
                    for c in monster_coords:
                        im_orient[c[0] + i][c[1] + j] = 'O'

    print('\n\n', '\n'.join([''.join(line) for line in im_orient]))
    count = '\n'.join([''.join(line) for line in im_orient]).count('#')

    print('Answer part 2: {}'.format(count))
