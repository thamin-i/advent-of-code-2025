"""Common methods for the Day 03"""

import typing as t
from pathlib import Path


def parse_battery_banks_file(file_name: str) -> t.List[str]:
    """Parse battery banks from file.

    Args:
        file_name (str): File name to parse from.

    Returns:
        t.List[str]: List of battery banks.
    """
    battery_banks: t.List[str] = []
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        battery_banks = [line.strip() for line in input_fd.readlines()]
    return battery_banks


def compute_largest_voltage(battery_bank: str, battery_size: int) -> int:
    """Use a greedy algorithm to find the largest number that can be formed
    by removing digits from the battery bank.

    Args:
        battery_bank (str): Battery bank as a string of digits.
        battery_size (int): Number of batteries to use.

    Returns:
        int: Largest voltage that can be formed from two batteries.
    """
    removable_banks: int = len(battery_bank) - battery_size
    largest_voltage: t.List[int] = []

    for digit in battery_bank:
        while removable_banks > 0:
            # Stop if there is nothing to remove in the stack
            if len(largest_voltage) == 0:
                break
            # Stop if current digit is less than the last one in the stack
            if largest_voltage[-1] >= int(digit):
                break
            # Remove the last digit from the stack
            largest_voltage = largest_voltage[:-1]
            removable_banks -= 1
        largest_voltage.append(int(digit))

    return int("".join(map(str, largest_voltage[:battery_size])))


def sum_largest_voltages(battery_banks: t.List[str], battery_size: int) -> int:
    """Sum the largest voltages from a list of battery banks.

    Args:
        battery_banks (t.List[str]): List of battery banks.
        battery_size (int): Number of batteries to use for each bank.

    Returns:
        int: Sum of the largest voltages from each battery bank.
    """
    largest_voltage: int = 0
    for battery_bank in battery_banks:
        largest_voltage += compute_largest_voltage(
            battery_bank, battery_size=battery_size
        )
    return largest_voltage
