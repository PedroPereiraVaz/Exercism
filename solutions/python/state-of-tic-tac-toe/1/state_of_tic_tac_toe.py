def gamestate(board):

    board_plain = ""
    for line in board:
        board_plain += line

    count_x = board_plain.count("X")
    count_o = board_plain.count("O")

    if len(board_plain) != 9:
        return ValueError

    if count_o > count_x:
        raise ValueError("Wrong turn order: O started")

    if count_x > count_o+1:
        raise ValueError("Wrong turn order: X went twice")


    combos = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]

    winners = ""

    for combo in combos:
        if board_plain[combo[0]] == board_plain[combo[1]] == board_plain[combo[2]] != " ":
            winners += board_plain[combo[0]]

    if len(set(winners)) > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if len(set(winners)) == 1:
        return "win"

    if len(set(winners)) == 0 and len(board_plain.replace(" ","")) == 9:
        return "draw"

    return "ongoing"


