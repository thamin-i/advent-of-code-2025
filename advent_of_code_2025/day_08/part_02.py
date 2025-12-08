"""Advent of code - Day 08 - Part 02"""

import typing as t
import uuid

from advent_of_code_2025.day_08.common import (
    Position,
    compute_sorted_distances,
    find_in_circuit,
    parse_positions_file,
)


def compute_result(
    positions: t.List[Position],
) -> int:  # pylint: disable=duplicate-code
    """Compute result based on positions

    Args:
        positions (t.List[Position]): List of 3D positions

    Returns:
        int: Product of the x-coordinates of the two
            points that complete the full circuit
    """
    sorted_distances: t.List[t.Tuple[float, Position, Position]] = (
        compute_sorted_distances(positions)
    )
    circuits: t.Dict[uuid.UUID, t.Set[Position]] = {}
    connections: int = 0
    for _, point_a, point_b in sorted_distances:
        circuit_a: uuid.UUID | None = find_in_circuit(circuits, point_a)
        circuit_b: uuid.UUID | None = find_in_circuit(circuits, point_b)

        # Points are not in any circuit -> Create a new circuit
        if circuit_a is None and circuit_b is None:
            circuits[uuid.uuid4()] = {point_a, point_b}
            connections += 1
        elif circuit_a is not None and circuit_b is not None:
            # Both points are already in the same circuit -> Skip
            if circuit_a == circuit_b:
                connections += 1
                continue
            # Both points are in different circuits -> Merge circuits
            if circuit_a != circuit_b:
                circuits[circuit_a].update(circuits[circuit_b])
                del circuits[circuit_b]
                connections += 1
        # Point A is in a circuit, point B is not -> Add B to A's circuit
        elif circuit_a is not None and circuit_b is None:
            circuits[circuit_a].add(point_b)
            connections += 1
        # Point B is in a circuit, point A is not -> Add A to B's circuit
        elif circuit_a is None and circuit_b is not None:
            circuits[circuit_b].add(point_a)
            connections += 1

        # Check if all points are now in a single circuit
        if len(circuits.keys()) == 1 and len(
            list(point for circuit in circuits.values() for point in circuit)
        ) == len(positions):
            return point_a.x * point_b.x

    return -1


def main() -> None:
    """Main function."""
    result: int
    result = compute_result(
        parse_positions_file(file_name="inputs/example.txt")
    )
    print(f"Example output: {result}")

    result = compute_result(parse_positions_file(file_name="inputs/real.txt"))
    print(f"Real output: {result}")


if __name__ == "__main__":
    main()
