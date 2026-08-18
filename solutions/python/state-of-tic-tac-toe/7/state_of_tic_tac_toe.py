"""
This module provides a function to evaluate the state of de board.
"""

COMBOS = [
    (0,1,2), (3,4,5), (6,7,8), (0,3,6),
    (1,4,7), (2,5,8), (0,4,8), (2,4,6)
]

def gamestate(board: list[str]) -> str:
    """
    Evaluates the current state of board.
    Args:
        board (list[str]): A list of 3 strings representing the board rows-

    Returns:
        str: The state of the game. Can be "win", "draw" or "ongoing".

    Raises:
        ValueError: If the board is invalid, has the wrong turn order or has an impossible winning state.
    """

    board_plain = "".join(board)
    count_x = board_plain.count("X")
    count_o = board_plain.count("O")

    if count_o > count_x:
        raise ValueError("Wrong turn order: O started")

    if count_x > count_o+1:
        raise ValueError("Wrong turn order: X went twice")

    winners = set()

    for item1, item2, item3 in COMBOS:
        if board_plain[item1] == board_plain[item2] == board_plain[item3] != " ":
            winners.add(board_plain[item1])

    winners_count = len(winners)

    if winners_count > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")

    if winners_count == 1:
        return "win"

    if " " not in board_plain:
        return "draw"

    return "ongoing"
