"""Advent of code - Day 11 - Part 01"""

import typing as t

from advent_of_code_2025.day_11.common import parse_mapping_file


def rec_count_valid_paths(
    mapping: dict[str, list[str]],
    validated_paths: t.List[t.List[str]],
    current_path: t.List[str],
) -> int:
    """Recursively count valid paths from the current node to the "out" node.

    Args:
        mapping (dict[str, list[str]]): Mapping of nodes to their neighbors.
        validated_paths (t.List[t.List[str]]): List to store validated paths.
        current_path (t.List[str]): Current path being explored.

    Returns:
        int: The number of valid paths found.
    """
    for neighbor in mapping[current_path[-1]]:
        if neighbor == "out":
            validated_paths.append(current_path + [neighbor])
        elif neighbor not in current_path:
            rec_count_valid_paths(
                mapping,
                validated_paths,
                current_path + [neighbor],
            )
    return len(validated_paths)


def main() -> None:
    """Main function."""
    valid_paths_count: int
    valid_paths_count = rec_count_valid_paths(
        parse_mapping_file(file_name="inputs/example_1.txt"), [], ["you"]
    )
    print(f"Example output: {valid_paths_count}")

    valid_paths_count = rec_count_valid_paths(
        parse_mapping_file(file_name="inputs/real.txt"), [], ["you"]
    )
    print(f"Real output: {valid_paths_count}")


if __name__ == "__main__":
    main()
