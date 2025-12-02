"""Advent of code - Day 02 - Part 01"""

import typing as t

from advent_of_code_2025.day_02.common import parse_id_ranges_file


def find_invalid_ids(id_range: t.Tuple[int, int]) -> t.List[int]:
    """Find all invalid IDs within the given ID range.

    Args:
        id_range (t.Tuple[int, int]): The ID range as a tuple.

    Returns:
        t.List[int]: List of invalid IDs.
    """
    invalid_ids: t.List[int] = []
    for id_number in range(id_range[0], id_range[1] + 1):
        str_id_number: str = str(id_number)
        if len(str_id_number) % 2 != 0:
            continue
        if (
            str_id_number[len(str_id_number) // 2 :]
            == str_id_number[: len(str_id_number) // 2]
        ):
            invalid_ids.append(id_number)
    return invalid_ids


def sum_invalid_ids(id_ranges: t.List[t.Tuple[int, int]]) -> int:
    """Sum all invalid IDs based on the given ID ranges.

    Args:
        id_ranges (t.List[t.Tuple[int, int]]): List of ID ranges.

    Returns:
        int: Sum of all invalid IDs.
    """
    invalid_ids: t.List[int] = []
    for id_range in id_ranges:
        invalid_ids += find_invalid_ids(id_range)
    return sum(invalid_ids)


def main() -> None:
    """Main function."""
    id_ranges: t.List[t.Tuple[int, int]] = parse_id_ranges_file(
        file_name="input.txt", from_file=__file__
    )
    invalid_ids_sum: int = sum_invalid_ids(id_ranges)
    print(invalid_ids_sum)


if __name__ == "__main__":
    main()
