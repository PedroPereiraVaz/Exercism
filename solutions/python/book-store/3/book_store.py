"""Module for get price of the basket"""
from functools import cache

prices = {1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}

def total(basket):
    """Function for calculate best price discount"""

    @cache
    def find_min_price(actual_state):
        if not actual_state:
            return 0

        return min(
            prices[group_size] + find_min_price(
                tuple(sorted([x - 1 for x in actual_state[:group_size] if x > 1] + list(actual_state[group_size:]), reverse=True))
            )
            for group_size in range(1, len(actual_state) + 1)
        )

    frequency = tuple(sorted((basket.count(book) for book in set(basket)), reverse=True))
    return find_min_price(frequency)