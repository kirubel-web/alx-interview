#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
   if total <= 0:
        return 0 
    if not coins:
        return -1
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += total // coin
        total = total % coin
    if total != 0:
        return -1
    return count

