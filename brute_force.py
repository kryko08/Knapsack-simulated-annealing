from utils import create_valid_combo, print_combo
from cost_func import get_combination_value

import time

from itertools import product

NUM_BF_ITEMS = 15


def brute_force(vals=None, caps=None):
    if vals is None:
        _, vals, caps = create_valid_combo()

    best_combo = 0
    best_value = 0

    # Time brute force search
    start = time.time()
    tf = [True, False]
    for combo in product(tf, repeat=10):
        value = get_combination_value(combo, vals, caps)
        if value > best_value:
            best_combo, best_value = combo, value

    time_to_complete = time.time() - start

    print("Best result for this set of knapsack items:")

    print_combo(best_combo, vals, caps)

    return best_value, time_to_complete
