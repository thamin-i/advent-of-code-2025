"""Advent of code - Day 05 - Part 02"""

import typing as t

from advent_of_code_2025.day_05.common import parse_database_file


def count_fresh_ingredients(ranges: t.List[t.Tuple[int, int]]) -> int:
    """Count fresh ingredients within specified ranges.

    Args:
        ranges (t.List[t.Tuple[int, int]]):
            List of tuples representing ranges of fresh ingredients.

    Returns:
        int:
            The count of fresh ingredients within the specified ranges.
    """
    return sum(high - low + 1 for low, high in ranges)


def normalize_ranges(
    ranges: t.List[t.Tuple[int, int]],
) -> t.List[t.Tuple[int, int]]:
    """Normalize and merge overlapping ranges.
    First, sort the ranges by their starting values.
    Then, iterate through the sorted ranges
    and merge them if they overlap or are contiguous.

    Args:
        ranges (t.List[t.Tuple[int, int]]):
            List of tuples representing ranges.

    Returns:
        t.List[t.Tuple[int, int]]:
            Merged list of ranges.
    """
    sorted_ranges: t.List[t.Tuple[int, int]] = sorted(
        ranges, key=lambda range: range[0]
    )
    normalized_ranges: t.List[t.Tuple[int, int]] = []

    current_start, current_end = sorted_ranges[0]
    for start, end in sorted_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            normalized_ranges.append((current_start, current_end))
            current_start, current_end = start, end
    normalized_ranges.append((current_start, current_end))
    return normalized_ranges


def main() -> None:
    """Main function."""
    fresh_ingredients_count: int
    fresh_ingredients_count = count_fresh_ingredients(
        normalize_ranges(
            parse_database_file(
                file_name="inputs/example.txt",
            )[0]
        )
    )
    print(f"Example output: {fresh_ingredients_count}")

    fresh_ingredients_count = count_fresh_ingredients(
        normalize_ranges(
            parse_database_file(
                file_name="inputs/real.txt",
            )[0]
        )
    )
    print(f"Real output: {fresh_ingredients_count}")


if __name__ == "__main__":
    main()
