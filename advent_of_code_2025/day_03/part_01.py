"""Advent of code - Day 03 - Part 01"""

from advent_of_code_2025.day_03.common import (
    parse_battery_banks_file,
    sum_largest_voltages,
)


def main() -> None:
    """Main function."""
    largest_voltages_sum: int
    largest_voltages_sum = sum_largest_voltages(
        parse_battery_banks_file(file_name="inputs/example.txt"), battery_size=2
    )
    print(f"Example output: {largest_voltages_sum}")

    largest_voltages_sum = sum_largest_voltages(
        parse_battery_banks_file(file_name="inputs/real.txt"), battery_size=2
    )
    print(f"Real output: {largest_voltages_sum}")


if __name__ == "__main__":
    main()
