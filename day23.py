from dataclasses import dataclass
import datetime

input23 = '583976241'


@dataclass
class Cup(object):
    value: int
    next_cup: "Cup" = None


def rotate_cups(first_cup, cups, rotations):
    max_key = max(cups.keys())
    cur_cup = first_cup
    for _ in range(rotations):
        a = cur_cup.next_cup
        b = a.next_cup
        c = b.next_cup
        dest = cur_cup.value - 1
        while True:
            if dest in [a.value, b.value, c.value]:
                pass
            elif dest < 0:
                dest = max_key
                continue
            elif dest in cups:
                dest_cup = cups[dest]
                break
            dest -= 1
        break_cup = dest_cup.next_cup
        cur_cup.next_cup = c.next_cup
        dest_cup.next_cup = a
        c.next_cup = break_cup
        cur_cup = cur_cup.next_cup

    return cups


def prepare_game(extra_cups: int = 0) -> tuple:
    """
    Install the cups in a circle
    Returns a the first cup and a dict of cup objects with ids as key.
    """
    cups = {}
    labeling = [int(i) for i in input23]

    last_cup = Cup(labeling.pop(0))

    first_cup = last_cup
    cups[last_cup.value] = last_cup
    for i in labeling:
        cup = Cup(i)
        last_cup.next_cup = cup
        cups[cup.value] = cup
        last_cup = cup
    for i in range(max(cups.keys()) + 1, extra_cups + 1):
        cup = Cup(i)
        last_cup.next_cup = cup
        cups[cup.value] = cup
        last_cup = cup
    last_cup.next_cup = first_cup
    return first_cup, cups


if __name__ == '__main__':
    start = datetime.datetime.now()

    first_cup, cups = prepare_game()

    cups = rotate_cups(first_cup, cups, 100)
    cup = cups[1]
    ans = []
    for _ in range(len(cups)):
        ans.append(cup.value)
        cup = cup.next_cup
    ans.pop(0)
    print('Part 1: ', ''.join(map(str, ans)))

    first_cup, cups = prepare_game(int(1e6))

    cups = rotate_cups(first_cup, cups, int(1e7))
    cup1 = cups[1].next_cup
    cup2 = cup1.next_cup
    print('Part 2: ', cup1.value * cup2.value)
    print('this took: ', datetime.datetime.now() - start)
