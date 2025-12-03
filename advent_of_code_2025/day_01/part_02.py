"""Advent of code - Day 01 - Part 02"""

from advent_of_code_2025.day_01.common import (
    compute_password,
    parse_rotations_file,
)


def main() -> None:
    """Main function."""
    invalid_ids_sum: int
    invalid_ids_sum = compute_password(
        parse_rotations_file(file_name="inputs/example.txt"),
        only_count_pointed=False,
    )
    print(f"Example output: {invalid_ids_sum}")

    invalid_ids_sum = compute_password(
        parse_rotations_file(file_name="inputs/real.txt"),
        only_count_pointed=False,
    )
    print(f"Real output: {invalid_ids_sum}")


if __name__ == "__main__":
    main()
