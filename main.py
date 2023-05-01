from utils import create_valid_combo, bcolors

from simulated_annealing import simulated_annealing
from brute_force import brute_force


def main():
    # Create items
    combo, vals, caps = create_valid_combo()
    print(f"{bcolors.HEADER}Running BRUTE FORCE search for best result...{bcolors.ENDC}")
    val_brute_force, runtime_bt = brute_force(vals, caps)
    print(f"\n{bcolors.HEADER}Running SIMULATED ANNEALING algorith...{bcolors.ENDC}")
    val_sa, runtime_sa = simulated_annealing(combo, vals, caps)
    print(f"\n{bcolors.BOLD}Brute force runtime: {runtime_bt} s, SA runtime: {runtime_sa} s{bcolors.ENDC}")
    print(f"SA run {bcolors.BOLD}{round(runtime_bt/runtime_sa, 3)}{bcolors.ENDC} times faster to achieve result value "
          f"of {bcolors.BOLD}{(val_sa/val_brute_force)*100} %{bcolors.ENDC} in comparison with perfect brute force value")


if __name__ == '__main__':
    main()
