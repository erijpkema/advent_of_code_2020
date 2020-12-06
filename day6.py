#!/usr/bin/env python3

if __name__ == '__main__':

    groups = [set()]
    with open('input6.txt') as f:
        for line in f:
            if line == '\n':
                groups.append(set())
                continue
            for question in {c for c in line.strip()}:
                groups[-1].add(question)

    count = sum([len(s) for s in groups])

    print('Answer part 1: {}'.format(count))

    groups = [set()]
    new_group = True

    with open('input6.txt') as f:
        for line in f:
            if line == '\n':
                groups.append(set())
                new_group = True
                continue
            questions = {c for c in line.strip()}
            if new_group:
                groups[-1] = questions
                new_group = False
            else:
                groups[-1] = groups[-1].intersection(questions)

    count = sum([len(s) for s in groups])

    print('Answer part 2: {}'.format(count))
