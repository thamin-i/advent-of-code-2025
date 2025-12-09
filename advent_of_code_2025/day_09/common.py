"""Common methods for the Day 09"""

import typing as t
from pathlib import Path


class Position(t.NamedTuple):
    """2D Position representation."""

    x: int
    y: int


class Segment(t.NamedTuple):
    """2D Segment representation."""

    a: Position
    b: Position


def parse_tiles_positions_file(file_name: str) -> t.List[Position]:
    """Parse list of 2D positions from a TXT file.

    Args:
        file_name (str): Name of the file containing 2D positions.

    Returns:
        t.List[Position]: List of Position objects representing 2D positions.
    """
    tiles_positions: t.List[Position] = []
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        tiles_positions = [
            Position(*map(int, line.split(",")))
            for line in input_fd.read().splitlines()
        ]
    return tiles_positions


def compute_rectangle_area(point_a: Position, point_b: Position) -> int:
    """Compute the area of the rectangle where
        point_a and point_b are opposite corners.

    Args:
        point_a (Position): 2D position of the point_a
        point_b (Position): 2D position of the point_b

    Returns:
        int: Area of the rectangle
    """
    width: int = abs(point_b[0] - point_a[0]) + 1
    height: int = abs(point_b[1] - point_a[1]) + 1
    return width * height
