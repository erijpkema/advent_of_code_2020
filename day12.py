#!/usr/bin/env python3

import math


class Ship(object):

    to_vector = {0: [0, 1], 90: [1, 0], 180: [0, -1], 270: [-1, 0]}

    def __init__(self):
        # position in x, y
        self.pos = [0, 0]
        self.heading = 90
        self.waypoint = Waypoint()

    def vectorize_heading(self):
        """
        Calculate 2d vector from heading in degrees
        """
        self.heading %= 360
        return self.to_vector[self.heading]

    @property
    def manhattan_distance(self):
        return sum([abs(i) for i in self.pos])

    def follow_instruction(self, instruction):
        """
        Params:
            instruction (tuple)
        """
        if instruction[0] == 'R':
            self.heading += instruction[1]
        elif instruction[0] == 'L':
            self.heading -= instruction[1]

        else:
            movement = {
                'F': self.vectorize_heading(),
                'N': (0, 1),
                'S': (0, -1),
                'E': (1, 0),
                'W': (-1, 0)
            }
            self.pos[0] += instruction[1] * movement[instruction[0]][0]
            self.pos[1] += instruction[1] * movement[instruction[0]][1]

    def follow_instruction_2(self, instruction):
        """
        Params:
            instruction (tuple)
        """
        if instruction[0] == 'F':
            self.pos[0] += instruction[1] * self.waypoint.pos[0]
            self.pos[1] += instruction[1] * self.waypoint.pos[1]

        elif instruction[0] in ('L', 'R'):
            self.waypoint.rotate(instruction)

        else:
            self.waypoint.move(instruction)


class Waypoint(Ship):
    def __init__(self):
        # position in x, y
        self.pos = [10, 1]

    def move(self, instruction):
        movement = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        self.pos[0] += instruction[1] * movement[instruction[0]][0]
        self.pos[1] += instruction[1] * movement[instruction[0]][1]

    def rotate(self, instruction):
        """
        Not too proud of this one.
        I know it is possible not to use trigonomic functions (and floats)
        """
        angle = instruction[1]
        if instruction[0] == 'R':
            angle *= -1
        angle = 2 * math.pi * angle / 360
        px, py = self.pos
        qx = math.cos(angle) * px - math.sin(angle) * py
        qy = math.sin(angle) * px + math.cos(angle) * py
        self.pos = [int(round(qx)), int(round(qy))]


if __name__ == '__main__':

    with open('input12.txt') as f:
        instructions = [(line[0], int(line.strip('\n')[1:])) for line in f]

    boaty_mc_boatface = Ship()

    for instruction in instructions:
        boaty_mc_boatface.follow_instruction(instruction)

    print('Answer part 1: {}'.format(boaty_mc_boatface.manhattan_distance))

    boaty_mc_boatface = Ship()
    for instruction in instructions:
        boaty_mc_boatface.follow_instruction_2(instruction)

    print('Answer part 2: {}'.format(boaty_mc_boatface.manhattan_distance))
