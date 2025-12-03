"""Advent of code - Day 01 - Part 01"""

import typing as t

from advent_of_code_2025.day_01.common import parse_rotations_file


def compute_part_01_password(
    rotations: t.List[t.Tuple[int, int]], pointed_number: int = 50
) -> int:
    """Compute the password based on the rotations.

    Args:
        rotations (t.List[t.Tuple[int, int]]): List of rotations.
        pointed_number (int): Initial pointed number.

    Returns:
        int: The computed password.
    """
    password: int = 0
    for rotation in rotations:
        pointed_number = (pointed_number + rotation[0] * rotation[1]) % 100
        if pointed_number == 0:
            password += 1
    return password


def main() -> None:
    """Main function."""
    invalid_ids_sum: int
    invalid_ids_sum = compute_part_01_password(
        parse_rotations_file(file_name="inputs/example.txt")
    )
    print(f"Example output: {invalid_ids_sum}")

    invalid_ids_sum = compute_part_01_password(
        parse_rotations_file(file_name="inputs/real.txt")
    )
    print(f"Real output: {invalid_ids_sum}")


if __name__ == "__main__":
    main()
