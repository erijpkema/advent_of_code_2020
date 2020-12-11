#!/usr/bin/env python3

from copy import deepcopy


def calulate_1(grid):
    old_grid = deepcopy(grid)
    surrounds = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1),
                 (1, 1)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if old_grid[i][j] in ('L', '#'):
                neighbours = 0
                for direction in surrounds:
                    if old_grid[i + direction[0]][j + direction[1]] == '#':
                        neighbours += 1
                if old_grid[i][j] == '#' and neighbours >= 4:
                    grid[i][j] = 'L'
                elif old_grid[i][j] == 'L' and neighbours == 0:
                    grid[i][j] = '#'
    if grid == old_grid:
        return grid
    else:
        return calulate_1(grid)


def calulate_2(grid):

    old_grid = deepcopy(grid)
    surrounds = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1),
                 (1, 1)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if old_grid[i][j] in ('L', '#'):
                neighbours = 0
                for direction in surrounds:
                    n = 1
                    while True:
                        i_, j_ = i + n * direction[0], j + n * direction[1]
                        if old_grid[i_][j_] in (',', 'L'):
                            break
                        elif old_grid[i_][j_] == '#':
                            neighbours += 1
                            break
                        n += 1
                if old_grid[i][j] == '#' and neighbours >= 5:
                    grid[i][j] = 'L'
                elif old_grid[i][j] == 'L' and neighbours == 0:
                    grid[i][j] = '#'
    if grid == old_grid:
        return grid
    else:
        return calulate_2(grid)


if __name__ == '__main__':

    with open('input11.txt') as f:
        grid = [[c for c in ',' + line.strip('\n') + ','] for line in f]

    # add some padding
    width = len(grid[0])
    grid.insert(0, [',' for x in range(width)])
    grid.append([',' for x in range(width)])

    grid2 = deepcopy(grid)  # for part 2

    count = [j for sub in calulate_1(grid) for j in sub].count('#')
    print('Answer part 1: {}'.format(count))

    count = [j for sub in calulate_2(grid2) for j in sub].count('#')
    print('Answer part 2: {}'.format(count))
