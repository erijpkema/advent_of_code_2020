#!/usr/bin/env python3

import numpy as np

if __name__ == '__main__':

    my_time = 1000434
    busses = [
        17, 'x', 'x', 'x', 'x', 'x', 'x', 41, 'x', 'x', 'x', 'x', 'x', 'x',
        'x', 'x', 'x', 983, 'x', 29, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
        'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 'x', 23, 'x',
        'x', 'x', 'x', 'x', 'x', 'x', 397, 'x', 'x', 'x', 'x', 'x', 37, 'x',
        'x', 'x', 'x', 'x', 'x', 13
    ]

    bus_nrs = [i for i in busses if i != 'x']
    wait_times = [bus - (my_time % bus) for bus in bus_nrs]
    shortest_wait = min(wait_times)
    bus_nr = bus_nrs[wait_times.index(shortest_wait)]

    print('Answer part 1: {}'.format(shortest_wait * bus_nr))

    delta = busses[0]
    timestamp = bus_nrs[0]
    for bus in bus_nrs[1:]:
        while (True):
            if (timestamp + busses.index(bus)) % bus == 0:
                # This bus is departing at the time we seek.
                break
            timestamp += delta
        delta = np.lcm(delta, bus)

    print('Answer part 2: {}'.format(timestamp))
