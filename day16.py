#!/usr/bin/env python3

from copy import deepcopy


def to_range(text):
    """
    Convert a-b string to range(a,b + 1)
    """
    return range(*[int(i) + 1 for i in text.split('-')])


def in_spec(specname, value):
    """
    See if value is within the spec of <specname>
    """
    for spec in specs[specname]:
        if value in spec:
            return True
    return False


def sanitize(possible_specs):
    """
    A bit like sudoku:
    if there is a position with one possible spec.
    remove that spec from other positions.
    """
    sanitize2(possible_specs)
    solid_postion = None
    for index, specs in enumerate(possible_specs):
        if type(specs) == str:
            continue  # Already sanitized
        elif len(specs) == 1:
            solid_postion = specs[0]
            possible_specs[index] = solid_postion
            remove_from_options(possible_specs, solid_postion)
    if solid_postion is None:
        return
    else:
        sanitize(possible_specs)


def sanitize2(possible_specs):
    """
    If a name is unique for a set of possible_specs,
    make that one definitive.
    """
    all_the_specs = [i for value in possible_specs for i in value]
    for name in set(all_the_specs):
        import ipdb; ipdb.set_trace()

        # flatten possible_specs
        if all_the_specs.count(name) == 1:
            for index, specs in enumerate(possible_specs):
                if name in specs:
                    possible_specs[index] = spec


def remove_from_options(possible_specs, solid_postion):
    for index, specs in enumerate(possible_specs):

        if type(specs) == str:
            continue  # Already sanitized
        elif solid_postion is not None and solid_postion in specs:
            if len(specs) == 1:
                import ipdb
                ipdb.set_trace()

            possible_specs[index].remove(solid_postion)


if __name__ == '__main__':
    specs = {}
    other_tickets = []
    valid_tickets = []

    with open('input16.txt') as f:
        for line in f:
            if line == 'your ticket:\n':
                break
            elif line == '\n':
                continue
            key, value = line.strip().split(': ')
            ranges = [to_range(i) for i in value.split(' or ')]
            specs[key] = ranges
        my_ticket = [int(i) for i in f.readline().strip().split(',')]
        for line in f:
            if line == '\n':
                continue
            elif line == 'nearby tickets:\n':
                continue
            other_tickets.append([int(i) for i in line.strip().split(',')])

    invalids = []
    all_the_specs = [i for value in specs.values() for i in value]
    for ticket in other_tickets:
        ticket_ok = True
        for value in ticket:
            ok = False
            for spec in all_the_specs:
                if value in spec:
                    ok = True
                    break
            if not ok:
                ticket_ok = False
                invalids.append(value)
        if ticket_ok:
            valid_tickets.append(ticket)

    print('Answer part 1: {}'.format(sum(invalids)))

    # possible specs for each position in the ticket
    possible_specs = [list(specs.keys()) for _ in range(len(valid_tickets[0]))]

    for index, values in enumerate(zip(*valid_tickets)):
        for name in possible_specs[index]:
            for value in values:
                if not in_spec(name, value):
                    possible_specs[index].remove(name)
                    break

    #possible_specs = possible_specs2
    sanitize(possible_specs)
    import ipdb
    ipdb.set_trace()

    part2 = 1
    for i, field in enumerate(possible_specs):
        print(field)
        if field[:9] == 'departure':
            part2 *= my_ticket[i]

    print('Answer part 2: {}'.format(part2))
