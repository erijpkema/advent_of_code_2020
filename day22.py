#!/usr/bin/env python3

from copy import deepcopy

decks='''Player 1:
14
29
25
17
13
50
33
32
7
37
26
34
46
24
3
28
18
20
11
1
21
8
44
10
22

Player 2:
5
38
27
15
45
40
43
30
35
9
48
12
16
47
42
4
2
31
41
39
23
19
36
49
6'''


decks_example = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''


hands = []


for line in decks.split('\n'):
    print(line)
    if 'Player' in line:
        hands.append([])
        continue
    elif line == '':
        continue
    else:
        hands[-1].append(int(line))


def game(hands):
    past_hands1 = []
    past_hands2 = []
    while len(hands[0]) > 0 and len(hands[1]) > 0:
        # print(hands, '\n')
        if tuple(hands[0]) in past_hands1 or tuple(hands[1]) in past_hands2:
            return (1, hands[0])
        past_hands1.append(tuple(hands[0]))
        past_hands2.append(tuple(hands[1]))
        top_p1 = hands[0].pop(0)
        top_p2 = hands[1].pop(0)
        if (len(hands[0]) + 1) > top_p1 and (len(hands[1]) + 1) > top_p2:
            # recursive combat
            # print('recursive combat!')
            hands2 = [hands[0][:top_p1], hands[1][:top_p2]]
            winner = game(hands2)[0]
        else:
            # normal combat
            winner = top_p1 > top_p2
        if winner == 1:
            hands[0] += [top_p1, top_p2]
        else:
            hands[1] += [top_p2, top_p1]

    if len(hands[0]) == 0:
        winning_hand = hands[1]
        winning_player = 2
    else:
        winning_hand = hands[0]
        winning_player = 1

    winning_hand.reverse()
    # print('level up')
    return (winning_player, winning_hand)


score = 0
for i, v in enumerate(game(hands)[1]):
    score += (i + 1) * v

print(f'Answer part 2: {score}')


