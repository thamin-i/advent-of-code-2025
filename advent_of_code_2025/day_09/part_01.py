"""Advent of code - Day 09 - Part 01"""

import itertools
import typing as t

from advent_of_code_2025.day_09.common import (
    Position,
    compute_rectangle_area,
    parse_tiles_positions_file,
)


def compute_biggest_rectangle_area(positions: t.List[Position]) -> int:
    """Compute the area of the biggest rectangle
        defined by any two positions in the list.

    Args:
        positions (t.List[Position]): List of 2D positions

    Returns:
        int: Area of the biggest rectangle
    """
    sorted_areas: t.List[t.Tuple[int, Position, Position]] = sorted(
        [
            (compute_rectangle_area(point_a, point_b), point_a, point_b)
            for point_a, point_b in itertools.combinations(positions, 2)
        ],
        reverse=True,
        key=lambda x: x[0],
    )
    return sorted_areas[0][0]


def main() -> None:
    """Main function."""
    biggest_rectangle_area: int
    biggest_rectangle_area = compute_biggest_rectangle_area(
        parse_tiles_positions_file(file_name="inputs/example.txt")
    )
    print(f"Example output: {biggest_rectangle_area}")

    biggest_rectangle_area = compute_biggest_rectangle_area(
        parse_tiles_positions_file(file_name="inputs/real.txt")
    )
    print(f"Real output: {biggest_rectangle_area}")


if __name__ == "__main__":
    main()
