card_pubkey = 11562782
door_pubkey = 18108497


def transform_subjectnr(subjectnr, loop_size):
    rv = 1
    for _ in range(loop_size):
        rv *= subjectnr
        rv %= 20201227
    return rv


def find_loop_size(pubkey):
    subjectnr = 7
    result = 1
    loop_size = 0
    while True:
        loop_size += 1
        result *= subjectnr
        result %= 20201227
        if result == pubkey:
            return loop_size


if __name__ == '__main__':
    assert transform_subjectnr(7, 8) == 5764801
    card_loopsize = find_loop_size(card_pubkey)

    secret_key = transform_subjectnr(door_pubkey, card_loopsize)
    print(f'Solution part 1: {secret_key}')
