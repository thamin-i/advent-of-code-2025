"""Advent of code - Day 04 - Part 01"""

from advent_of_code_2025.day_04.common import (
    parse_grid_file,
    rec_compute_accessible_rolls,
)


def main() -> None:
    """Main function."""
    largest_voltages_sum: int
    largest_voltages_sum = rec_compute_accessible_rolls(
        parse_grid_file(file_name="inputs/example.txt"),
        part_01=True,
    )
    print(f"Example output: {largest_voltages_sum}")

    largest_voltages_sum = rec_compute_accessible_rolls(
        parse_grid_file(file_name="inputs/real.txt"),
        part_01=True,
    )
    print(f"Real output: {largest_voltages_sum}")


if __name__ == "__main__":
    main()
