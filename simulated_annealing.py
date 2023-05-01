from utils import (
    create_valid_combo,
    plot_result,
    tweak,
    print_combo
    )
from cost_func import get_combination_value

import random
import math
import time

from utils import NUM_ITEMS

ITERS = 200
MAX_TEMP = 1000
MIN_TEMP = 1
COOLING_DECR = 0.96
METROPOLISE_PER_TEMPERATURE = 10
P = 1 / NUM_ITEMS


def simulated_annealing(combo=None, vals=None, caps=None, temp=MAX_TEMP, min_temp=MIN_TEMP, cooling_decr=COOLING_DECR,
                        metro_per_iter=METROPOLISE_PER_TEMPERATURE):
    # set up
    if combo is None:
        combo, vals, caps = create_valid_combo()

    value_list = []
    t = temp
    value = get_combination_value(combo, vals, caps)
    best_combo, best_value = combo, value

    start = time.time()
    for i in range(ITERS//metro_per_iter):
        # nt loop
        for ii in range(metro_per_iter):

            candidate_combo = tweak(combo)
            candidate_value = get_combination_value(candidate_combo, vals, caps)

            # Move towards better solution
            if candidate_value > value:
                combo, value = candidate_combo, candidate_value
            # Move towards worse solution
            elif random.random() < math.e ** -((candidate_value - value)/t):
                combo, value = candidate_combo, candidate_value

            # Best solution
            if value > best_value:
                best_combo, best_value = combo, value

            value_list.append(best_value)

        # Stop alg if temperature drops below limit
        t *= cooling_decr
        if t < min_temp:
            break

    finish = time.time() - start

    print("Result of Simulated annealing:")
    print_combo(best_combo, vals, caps)

    plot_result(list(range(ITERS)), value_list)
    return best_value, finish

