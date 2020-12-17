from collections import namedtuple


start = '''.#.
..#
###
'''

start = '''..#..##.
#.....##
##.#.#.#
..#...#.
.###....
######..
.###..#.
..#..##.
'''

Point = namedtuple('Point', ['x', 'y', 'z', 'w'])



def get_neighbours(points, point, hyper=False):
    """
    return a set of points around point.
    """
    neighbours = set()
    for x in range(point.x - 1, point.x + 2):
        for y in range(point.y - 1, point.y + 2):
            for z in range(point.z - 1, point.z + 2):
                if not hyper:
                    neighbours.add(Point(x, y, z, 0))
                else:
                    for w in range(point.w - 1, point.w + 2):
                        neighbours.add(Point(x, y, z, w))

    # Remove point itself again
    neighbours.remove(point)
    return neighbours


def count_neighbours(points, point, hyper):
    rv = 0
    for neighbour in get_neighbours(points, point, hyper):
        if neighbour in points:
            rv += 1
    return rv


def cycle(points, hyper=False):
    points2 = set()
    for point in points:
        count = count_neighbours(points, point, hyper)
        if count in (2, 3):
            points2.add(point)
        for neighbour in get_neighbours(points, point, hyper):
            if neighbour not in points:
                count = count_neighbours(points, neighbour, hyper)
                if count == 3:
                    points2.add(neighbour)
    return points2


if __name__ == '__main__':
    # list of points in active state.
    points = set()
    for y, line in enumerate(start.split('\n')):
        for x, c in enumerate(line.strip()):
            if c == '#':
                points.add(Point(x, y, 0, 0))

    for _ in range(6):
        points = cycle(points)

    print('answer to part 1: {}'.format(len(points)))

    # list of points in active state.
    points = set()
    for y, line in enumerate(start.split('\n')):
        for x, c in enumerate(line.strip()):
            if c == '#':
                points.add(Point(x, y, 0, 0))

    for _ in range(6):
        points = cycle(points, hyper=True)

    print('answer to part 2: {}'.format(len(points)))
