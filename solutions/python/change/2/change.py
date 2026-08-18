"""This module helps to get the best change options using the fewest available coins."""

def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """
    Finds the best change using the fewest coins possible.

    Args:
        coins: List of available coin values.
        target: Target amount of money to return.

    Returns:
        List of coins that make up the change, ordered from smallest to largest.

    Raises:
        ValueError: If it's not possible to make the exact change, or if the target is negative.
    """

    if target < 0:
        raise ValueError("target can't be negative")

    solutions = [[] if index == 0 else None for index in range(target+1)]

    for amount in range(1, target+1):
        for coin in coins:
            if coin > amount:
                continue
            if solutions[amount-coin] is None:
                continue
            if solutions[amount] is None:
                solutions[amount] = solutions[amount-coin] + [coin]
            elif len(solutions[amount]) > len(solutions[amount-coin]) + 1:
                solutions[amount] = solutions[amount-coin] + [coin]

    if solutions[target] is None:
        raise ValueError("can't make target with given coins")

    return sorted(solutions[target])


