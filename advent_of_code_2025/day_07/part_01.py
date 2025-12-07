"""Advent of code - Day 07 - Part 01"""

import typing as t

from advent_of_code_2025.day_07.common import parse_diagram_file


def count_splits(diagram: t.List[t.List[str]]) -> int:
    """Count the number of beam splits in the input diagram

    Args:
        diagram (t.List[t.List[str]]): Input diagram.

    Returns:
        int: Number of beam splits in the diagram.
    """
    tachyons_idx: t.Set[int] = set()
    tachyons_idx.add(diagram[0].index("S"))
    splits: int = 0
    for line in diagram:
        for x, char in enumerate(line):
            if char == "^" and x in tachyons_idx:
                splits += 1
                tachyons_idx.remove(x)
                if x - 1 >= 0:
                    tachyons_idx.add(x - 1)
                if x + 1 < len(line):
                    tachyons_idx.add(x + 1)
    return splits


def main() -> None:
    """Main function."""
    splits_count: int
    splits_count = count_splits(
        parse_diagram_file(file_name="inputs/example.txt")
    )
    print(f"Example output: {splits_count}")

    splits_count = count_splits(parse_diagram_file(file_name="inputs/real.txt"))
    print(f"Real output: {splits_count}")


if __name__ == "__main__":
    main()
