""" This module help to get best change options for the avaiable coins for the target. """

def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """
    Find best change with less coins.

    Args:
        coins: List of coins avaible
        target: Money to return

    Returns:
        change: List of coins

    Raises:
        ValueError: if not possible give the change or target is negative
    """

    if target < 0:
        raise ValueError("target can't be negative")

    solutions = [[] if _ == 0 else None for _ in range(target+1)]

    for i in range(1, target+1):
        for coin in coins:
            if coin > i:
                continue
            if solutions[i-coin] is None:
                continue
            if solutions[i] is None:
                solutions[i] = solutions[i-coin] + [coin]
            elif len(solutions[i]) > len(solutions[i-coin]) + 1:
                solutions[i] = solutions[i-coin] + [coin]

    if solutions[target] is None:
        raise ValueError("can't make target with given coins")

    return solutions[target][::-1]
