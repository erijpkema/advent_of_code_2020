#!/usr/bin/env python3

import re

if __name__ == '__main__':

    passports = [{}]

    with open('input4.txt') as f:
        for line in f:
            if line == '\n':
                passports.append({})
                continue
            # convert line into list of key value tuples.
            items = [tuple(i.split(':')) for i in line.strip('\n').split(' ')]
            for k, v in items:
                passports[-1][k] = v

    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    count = 0
    for passport in passports:
        count += required_keys.issubset(set(passport.keys()))

    print('Answer part 1: {}'.format(count))

    count = 0
    for passport in passports:
        try:
            if not 2002 >= int(passport['byr']) >= 1920:
                continue
            if 2020 < int(passport['iyr']) < 2010:
                continue
            if not 2020 <= int(passport['eyr']) <= 2030:
                continue
            if passport['hgt'][-2:] not in ('cm', 'in'):
                continue
            elif passport['hgt'][-2:] == 'cm' and int(
                    passport['hgt'][:-2]) not in range(150, 193):
                continue
            elif passport['hgt'][-2:] == 'in' and int(
                    passport['hgt'][:-2]) not in range(59, 76):
                continue
            if not re.match('#([a-f]|[0-9]){6}', passport['hcl']):
                continue
            if not passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn',
                                       'hzl', 'oth'):
                continue
            if not re.match('[0-9]{9}', passport['pid']):
                continue

            count += 1
        except KeyError:
            pass

    print('Answer part 2: {}'.format(count))
