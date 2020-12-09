#!/usr/bin/env python3

from collections import namedtuple

Instruction = namedtuple('Instruction', ('operation', 'argument'))


def run_program(program, force_jmp=None, force_nop=None):
    index = 0
    acc = 0
    visited = set()
    while index not in visited:
        visited.add(index)
        try:
            instruction = program[index]
        except IndexError:
            print(f'Answer part 2: {acc}')
            return acc
        if force_jmp == index:
            index += instruction.argument
        elif force_nop == index:
            index += 1
        elif instruction.operation == 'nop':
            index += 1
        elif instruction.operation == 'acc':
            acc += instruction.argument
            index += 1
        elif instruction.operation == 'jmp':
            index += instruction.argument

    return acc


if __name__ == '__main__':

    program = []
    with open('input_8.txt') as f:
        for line in f:
            operation, argument = line.strip().split()
            program.append(Instruction(operation, int(argument)))

    print('Answer part 1: {}'.format(run_program(program)))

    nops = []
    jmps = []
    for index, instruction in enumerate(program):
        if instruction.operation == 'nop':
            nops.append(index)
        elif instruction.operation == 'jmp':
            jmps.append(index)

    for nop in nops:
        run_program(program, force_jmp=nop)
    for jmp in jmps:
        run_program(program, force_nop=jmp)
