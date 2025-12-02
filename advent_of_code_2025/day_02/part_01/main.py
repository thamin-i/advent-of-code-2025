"""Advent of code - Day 02 - Part 01"""

import typing as t

from advent_of_code_2025.day_02.common import (
    parse_id_ranges_file,
    sum_invalid_ids,
)


def main() -> None:
    """Main function."""
    id_ranges: t.List[t.Tuple[int, int]] = parse_id_ranges_file(
        file_name="input.txt", from_file=__file__
    )
    invalid_ids_sum = sum_invalid_ids(id_ranges, match_many=False)
    print(invalid_ids_sum)


if __name__ == "__main__":
    main()
