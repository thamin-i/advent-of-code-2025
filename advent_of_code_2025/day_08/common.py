"""Common methods for the Day 08"""

import itertools
import math
import typing as t
import uuid
from pathlib import Path


class Position(t.NamedTuple):
    """3D Position representation."""

    x: int
    y: int
    z: int


def parse_positions_file(file_name: str) -> t.List[Position]:
    """Parse list of 3D positions from a TXT file.

    Args:
        file_name (str): Name of the file containing 3D positions.

    Returns:
        t.List[Position]: List of Position objects representing 3D positions.
    """
    positions: t.List[Position] = []
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        positions = [
            Position(*map(int, line.split(",")))
            for line in input_fd.read().splitlines()
        ]
    return positions


def compute_distance(point_a: Position, point_b: Position) -> float:
    """Compute Euclidean distance between two 3D points.

    Args:
        point_a (Position): Coordinates of the first point (x1, y1, z1).
        point_b (Position): Coordinates of the second point (x2, y2, z2).

    Returns:
        float: Euclidean distance between point_a and point_b.
    """
    return math.sqrt(
        (point_b.x - point_a.x) ** 2
        + (point_b.y - point_a.y) ** 2
        + (point_b.z - point_a.z) ** 2
    )


def compute_sorted_distances(
    points: t.List[Position],
) -> t.List[t.Tuple[float, Position, Position]]:
    """Compute distances between all pairs of 3D points.

    Args:
        points (t.List[Position]): List of 3D points.

    Returns:
        t.List[t.Tuple[float, Position, Position]]:
            Sorted list of tuples containing distances and corresponding pairs.
    """
    return sorted(
        [
            (compute_distance(point_a, point_b), point_a, point_b)
            for point_a, point_b in itertools.combinations(points, 2)
        ],
        key=lambda x: x[0],
    )


def find_in_circuit(
    circuits: t.Dict[uuid.UUID, t.Set[Position]], point: Position
) -> t.Optional[uuid.UUID] | None:
    """Find a point in all circuits

    Args:
        circuits (t.Dict[uuid.UUID, t.Set[Position]]): All existing circuits
        point (Position): Point to find

    Returns:
        t.Optional[uuid.UUID] | None: Circuit ID if found, otherwise None.
    """
    return next(
        (k for k, circuit in circuits.items() if point in circuit), None
    )
