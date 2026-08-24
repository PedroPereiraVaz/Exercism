VALUES = {"J": 11, "Q": 12, "K": 13, "A": 14}

def best_hands(hands):

    best_tuple = evaluate_hand(max(hands, key=evaluate_hand))

    winner_hands = [hand for hand in hands if evaluate_hand(hand) == best_tuple]

    return winner_hands

def evaluate_hand(hand):
    cards = hand.split()

    values = []
    suits = [] 

    for card in cards:
        suits.append(card[-1])
        value_str = card[:-1]

        if value_str in VALUES:
            values.append(VALUES[value_str])
        else:
            values.append(int(value_str))

    groups = [(values.count(value), value) for value in set(values)]
    groups.sort(reverse=True)

    counts = [count for count, value in groups]
    sorted_cards = [value for count, value in groups]

    is_flush = len(set(suits)) == 1

    is_straight = (len(counts) == 5) and (max(sorted_cards) - min(sorted_cards) == 4)

    if sorted_cards == [14,5,4,3,2]:
        is_straight = True

        sorted_cards = [5,4,3,2,1]


    # Points

    if is_straight and is_flush:
        return (8, sorted_cards)

    if counts == [4,1]:
        return (7, sorted_cards)

    if counts == [3,2]:
        return (6, sorted_cards)

    if is_flush:
        return (5, sorted_cards)

    if is_straight:
        return (4, sorted_cards)

    if counts == [3,1,1]:
        return (3, sorted_cards)

    if counts == [2,2,1]:
        return (2, sorted_cards)

    if counts == [2,1,1,1]:
        return (1, sorted_cards)

    return (0, sorted_cards)