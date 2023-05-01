import numpy as np
import random
import matplotlib.pyplot as plt

from cost_func import CAPACITY


NUM_ITEMS = 10


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def tweak(pack):
    cc = np.copy(pack)
    for ind in range(len(pack)):
        p = random.random()
        if p < 1/(len(pack)):
            cc[ind] = not cc[ind]
    return cc


def create_valid_combo():
    while True:
        pack = [random.choice([True, False]) for _ in range(NUM_ITEMS)]
        caps = [random.randint(1, 50) for _ in range(NUM_ITEMS)]
        vals = [random.randint(1, 50) for _ in range(NUM_ITEMS)]

        if np.sum(caps, where=pack) <= CAPACITY:
            return pack, vals, caps


def print_combo(combo, vals, caps):
    for i in range(NUM_ITEMS):
        if combo[i]:
            print(f"{bcolors.OKGREEN}Item {i+1}, \tvalue: {vals[i]}, \tcapacity: {caps[i]}, \tselected: {combo[i]}{bcolors.ENDC}")
        else:
            print(
                f"{bcolors.FAIL}Item {i + 1}, \tvalue: {vals[i]}, \tcapacity: {caps[i]}, \tselected: {combo[i]}{bcolors.ENDC}")

    print(f"{bcolors.BOLD}Of selected items - CAPACITY TOTAL: {np.sum(caps, where=combo)}, VALUE TOTAL: {np.sum( vals, where=combo)}{bcolors.ENDC}")


def plot_result(x, y):
    plt.plot(x, y, label="Reference")
    plt.xlabel("Iterations")
    plt.ylabel("Value")
    plt.show()

