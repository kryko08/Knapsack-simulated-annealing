import numpy as np

CAPACITY = 100


def get_combination_value(coord, vals, caps):
    """
    This function gets value of given list of knapsack items

    :param coord: List[bool], items that should be included for this specific set Up
    """

    # No items in knapsack

    total_val = np.sum(vals, where=coord)
    total_cap = np.sum(caps, where=coord)

    if total_cap > CAPACITY:
        total_val = 0

    return total_val
