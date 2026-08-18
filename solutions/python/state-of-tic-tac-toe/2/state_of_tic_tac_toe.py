COMBOS = [
    (0,1,2), (3,4,5), (6,7,8), (0,3,6),
    (1,4,7), (2,5,8), (0,4,8), (2,4,6)
]

def gamestate(board):
    """ Resolve state of gameboard. """
    board_plain = "".join(board)

    count_x = board_plain.count("X")
    count_o = board_plain.count("O")

    if count_o > count_x:
        raise ValueError("Wrong turn order: O started")

    if count_x > count_o+1:
        raise ValueError("Wrong turn order: X went twice")

    winners = set()

    for a, b, c in COMBOS:
        if board_plain[a] == board_plain[b] == board_plain[c] != " ":
            winners.add(board_plain[a])

    count_winners = len(winners)

    if count_winners > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if count_winners == 1:
        return "win"

    if " " not in board_plain:
        return "draw"

    return "ongoing"
