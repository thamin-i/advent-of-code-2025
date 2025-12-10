"""Advent of code - Day 10 - Part 02"""

import typing as t

import numpy as np
import pulp

from advent_of_code_2025.day_10.common import Machine, parse_machines_file


def list_min_buttons_pressed_count(machine: Machine) -> t.List[int]:
    """Find the minimum number of times each button needs to be pressed
    to achieve the target joltage levels.

    Uses integer linear programming to minimize total button presses while
    satisfying the constraint that each joltage level reaches its target.

    Args:
        machine (Machine): Machine with buttons and target joltage levels

    Returns:
        t.List[int]: Number of times each button should be pressed
    """
    joltage_count: int = len(machine.joltage)
    buttons_count: int = len(machine.buttons)

    # Build a matrix where each column represents a button and each row
    # represents a joltage level. 1 indicates that pressing the button
    # affects that joltage level.
    button_effects: np.ndarray = np.zeros(
        (joltage_count, buttons_count), dtype=int
    )
    for button_idx, affected_levels in enumerate(machine.buttons):
        for level_idx in affected_levels:
            button_effects[level_idx, button_idx] = 1

    # Target joltage levels
    target_joltage: np.ndarray = np.array(machine.joltage)

    # Set up the optimization problem using pulp: minimize total button presses
    optimization_problem: pulp.LpProblem = pulp.LpProblem(sense=pulp.LpMinimize)

    # Create variables for how many times each button is pressed
    button_press_counts: t.List[pulp.LpVariable] = [
        pulp.LpVariable(f"button_{i}_presses", lowBound=0, cat="Integer")
        for i in range(buttons_count)
    ]

    # Objective: minimize total button presses
    optimization_problem += pulp.lpSum(button_press_counts)

    # Constraints: for each joltage level,
    # the sum of button effects must equal target
    for level_idx in range(joltage_count):
        optimization_problem += (
            pulp.lpSum(
                button_effects[level_idx, button_idx]
                * button_press_counts[button_idx]
                for button_idx in range(buttons_count)
            )
            == target_joltage[level_idx]
        )

    # Solve the optimization problem
    optimization_problem.solve(pulp.PULP_CBC_CMD(msg=0))

    # Extract and return the minimum button press counts
    return [int(var.value()) for var in button_press_counts]


def compute_min_pressed_buttons_count_2(machines: t.List[Machine]) -> int:
    """Compute the minimum number of pressed buttons for a list of machines.

    Args:
        machines (t.List[Machine]): List of machines to process.

    Returns:
        int: Minimum number of pressed buttons across all machines.
    """
    pressed_count: int = 0
    pressed_buttons: t.List[int]
    for machine in machines:
        pressed_buttons = list_min_buttons_pressed_count(machine)
        pressed_count += sum(pressed_buttons)
    return pressed_count


def main() -> None:
    """Main function."""
    min_pressed_count: int
    min_pressed_count = compute_min_pressed_buttons_count_2(
        parse_machines_file(file_name="inputs/example.txt")
    )
    print(f"Example output: {min_pressed_count}")

    min_pressed_count = compute_min_pressed_buttons_count_2(
        parse_machines_file(file_name="inputs/real.txt")
    )
    print(f"Real output: {min_pressed_count}")


if __name__ == "__main__":
    main()
