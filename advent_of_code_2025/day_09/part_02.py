"""Advent of code - Day 09 - Part 02"""

import itertools
import typing as t

from advent_of_code_2025.day_09.common import (
    Position,
    Segment,
    compute_rectangle_area,
    parse_tiles_positions_file,
)

SHAPE_EDGES: t.Set[Position] = set()


def is_point_inside_shape(  # pylint: disable=too-many-return-statements
    point: Position,
) -> bool:
    """Check if point X, Y is inside the `SHAPE_EDGES` global
        (surrounded on all four sides by at least one shape points).

    Args:
        point (Position): 2D position of the point to check

    Returns:
        bool: True if the point is inside the shape, False otherwise
    """
    # Point is part of the shape edges
    if point in SHAPE_EDGES:
        return True

    # Check for shape points on the same X and Y axes
    same_x = [p for p in SHAPE_EDGES if p[0] == point[0]]
    if not same_x:
        return False

    # Check for shape points on the same Y axis
    same_y = [p for p in SHAPE_EDGES if p[1] == point[1]]
    if not same_y:
        return False

    # Check for shape points above the point
    above = any(p[1] < point[1] for p in same_x)
    if not above:
        return False

    # Check for shape points below the point
    below = any(p[1] > point[1] for p in same_x)
    if not below:
        return False

    # Check for shape points to the left of the point
    left = any(p[0] < point[0] for p in same_y)
    if not left:
        return False

    # Check for shape points to the right of the point
    right = any(p[0] > point[0] for p in same_y)
    if not right:
        return False

    return True


def compute_rectangle_corners(
    corner1: Position, corner2: Position
) -> t.List[Position]:
    """Compute the 4 corners of a rectangle
        where corner1 and corner2 are opposite corners.

    Args:
        corner1 (Position): 2D position of the corner1
        corner2 (Position): 2D position of the corner2

    Returns:
        t.List[Position]: Tuple of the 4 rectangle corners
    """
    corners: t.List[Position] = t.cast(
        t.List[Position],
        (corner1, (corner1[0], corner2[1]), corner2, (corner2[0], corner1[1])),
    )
    return sorted(corners, key=lambda p: (p[1], p[0]))


def compute_lines_and_columns(
    corners: t.List[Position],
) -> t.Tuple[t.List[Segment], t.List[Segment]]:
    """Compute the lines and columns defined by the rectangle corners.

    Args:
        corners (t.List[Position]):
            List of ordered rectangle corners
            (top-left, top-right, bottom-left, bottom-right)

    Returns:
        t.Tuple[t.List[Segment], t.List[Segment]]:
        Tuple containing two lists:
            - List of lines (each line is a list of two points)
            - List of columns (each column is a list of two points)
    """
    top_row: Segment = t.cast(
        Segment,
        (
            (corners[0][0] + 1, corners[0][1] + 1),
            (corners[1][0] - 1, corners[1][1] + 1),
        ),
    )
    bottom_row: Segment = t.cast(
        Segment,
        (
            (corners[2][0] + 1, corners[2][1] - 1),
            (corners[3][0] - 1, corners[3][1] - 1),
        ),
    )
    left_col: Segment = t.cast(
        Segment,
        (
            (corners[0][0] + 1, corners[0][1] + 1),
            (corners[2][0] + 1, corners[2][1] - 1),
        ),
    )
    right_col: Segment = t.cast(
        Segment,
        (
            (corners[1][0] - 1, corners[1][1] + 1),
            (corners[3][0] - 1, corners[3][1] - 1),
        ),
    )
    return [top_row, bottom_row], [left_col, right_col]


def compute_shape_edges(red_points: t.List[Position]) -> None:
    """Compute edges of the shape defined by all red points.

    Args:
        red_points (t.List[Position]): List of 2D positions of red points
    """
    global SHAPE_EDGES  # pylint: disable=global-statement

    for point_a, point_b in itertools.combinations(red_points, 2):
        if point_a[1] == point_b[1]:
            min_x_pair = min(point_a[0], point_b[0])
            max_x_pair = max(point_a[0], point_b[0])
            SHAPE_EDGES = SHAPE_EDGES | {
                Position(x, point_a[1])
                for x in range(min_x_pair, max_x_pair + 1)
            }
        elif point_a[0] == point_b[0]:
            min_y_pair = min(point_a[1], point_b[1])
            max_y_pair = max(point_a[1], point_b[1])
            SHAPE_EDGES = SHAPE_EDGES | {
                Position(point_a[0], y)
                for y in range(min_y_pair, max_y_pair + 1)
            }


def compute_biggest_rectangle_area_in_shape(
    red_points: t.List[Position],
) -> int:
    """Compute the biggest rectangle area fully
        inside the shape defined by red points.

    Args:
        red_points (t.List[Position]): List of 2D positions of red points

    Returns:
        int: Area of the biggest rectangle fully inside the shape
    """
    compute_shape_edges(red_points)

    sorted_areas: t.List[t.Tuple[int, Position, Position]] = sorted(
        [
            (compute_rectangle_area(point_a, point_b), point_a, point_b)
            for point_a, point_b in itertools.combinations(red_points, 2)
        ],
        reverse=True,
        key=lambda x: x[0],
    )

    for area in sorted_areas:

        corners: t.List[Position] = compute_rectangle_corners(area[1], area[2])

        # Check that all corners are inside the shape
        broken_area: bool = False
        for corner in corners:
            if not is_point_inside_shape(corner):
                broken_area = True
        if broken_area:
            continue

        # Check that there is no shape point crossing
        # lines or columns defined by rectangle corners -1
        for line, column in zip(*compute_lines_and_columns(corners)):
            crossed_lines = [
                p
                for p in SHAPE_EDGES
                if p[1] == line[0][1]
                and p[0] >= min(line[0][0], line[1][0])
                and p[0] <= max(line[0][0], line[1][0])
            ]
            crossed_corners = [
                p
                for p in SHAPE_EDGES
                if p[0] == column[0][0]
                and p[1] >= min(column[0][1], column[1][1])
                and p[1] <= max(column[0][1], column[1][1])
            ]
            if any(crossed_lines) or any(crossed_corners):
                broken_area = True
        if broken_area:
            continue

        return area[0]

    return -1


def main() -> None:
    """Main function."""
    biggest_rectangle_area_in_shape: int
    biggest_rectangle_area_in_shape = compute_biggest_rectangle_area_in_shape(
        parse_tiles_positions_file(file_name="inputs/example.txt")
    )
    print(f"Example output: {biggest_rectangle_area_in_shape}")

    biggest_rectangle_area_in_shape = compute_biggest_rectangle_area_in_shape(
        parse_tiles_positions_file(file_name="inputs/real.txt")
    )
    print(f"Real output: {biggest_rectangle_area_in_shape}")
    # Result is 1652344888


if __name__ == "__main__":
    main()
