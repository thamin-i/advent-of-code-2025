"""Advent of code - Day 10 - Part 01"""

import typing as t
from itertools import product

from advent_of_code_2025.day_10.common import Machine, parse_machines_file


def bruteforce_min_pressed_buttons(machine: Machine) -> int:
    """Bruteforce approach to find the minimum set of buttons to press
        to match the indicator lights diagram.

    Args:
        machine (Machine): Machine instance

    Returns:
        int: Minimum number of buttons to press.
    """
    pressed_buttons: t.List[int] = []
    for solution in product([0, 1], repeat=len(machine.buttons)):
        initial_state = [0] * len(machine.indicator_lights_diagram)
        for button_index, pressed in enumerate(solution):
            if pressed:
                for light in machine.buttons[button_index]:
                    initial_state[light] ^= 1
        if initial_state == machine.indicator_lights_diagram:
            pressed_buttons.append(len([v for v in solution if v]))
    sorted_pressed_buttons = sorted(pressed_buttons)
    return sorted_pressed_buttons[0]


def compute_min_pressed_sum(machines: t.List[Machine]) -> int:
    """Compute the sum of minimum number
        of pressed buttons for a list of machines.

    Args:
        machines (t.List[Machine]): List of machines to process.

    Returns:
        int: Minimum number of pressed buttons across all machines.
    """
    return sum(bruteforce_min_pressed_buttons(machine) for machine in machines)


def main() -> None:
    """Main function."""
    min_pressed_sum: int
    min_pressed_sum = compute_min_pressed_sum(
        parse_machines_file(file_name="inputs/example.txt")
    )
    print(f"Example output: {min_pressed_sum}")

    min_pressed_sum = compute_min_pressed_sum(
        parse_machines_file(file_name="inputs/real.txt")
    )
    print(f"Real output: {min_pressed_sum}")


if __name__ == "__main__":
    main()
