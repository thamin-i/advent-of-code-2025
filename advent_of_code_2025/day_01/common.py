"""Common methods for the Day 01"""

import typing as t
from pathlib import Path


def parse_rotations_file(file_name: str) -> t.List[t.Tuple[int, int]]:
    """Parse TXT input file and generate list of rotations.

    Args:
        file_name (str): Name of the file to parse.

    Returns:
        t.List[t.Tuple[int, int]]:
            List of tuples where the first element is the rotation
            (-1 for left, 1 for right) and the second element
            is the number of ticks to turn.
    """
    rotations: t.List[t.Tuple[int, int]] = []
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        rotations = [
            (-1 if line[0] == "L" else 1, int(line[1:]))
            for line in input_fd.read().splitlines()
        ]
    return rotations
