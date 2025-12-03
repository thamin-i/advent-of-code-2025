"""Advent of code - Day 02 - Part 02"""

from advent_of_code_2025.day_02.common import (
    parse_id_ranges_file,
    sum_invalid_ids,
)


def main() -> None:
    """Main function."""
    invalid_ids_sum: int
    invalid_ids_sum = sum_invalid_ids(
        parse_id_ranges_file(file_name="inputs/example.txt"), match_many=True
    )
    print(f"Example output: {invalid_ids_sum}")

    invalid_ids_sum = sum_invalid_ids(
        parse_id_ranges_file(file_name="inputs/real.txt"), match_many=True
    )
    print(f"Real output: {invalid_ids_sum}")


if __name__ == "__main__":
    main()
