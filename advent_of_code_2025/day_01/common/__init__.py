"""Common methods for the Day 01"""

import os
import typing as t


def parse_rotations_file(
    file_name: str, from_file: str
) -> t.List[t.Tuple[int, int]]:
    """Parse TXT input file and generate list of rotations.

    Args:
        file_name (str): Name of the file to parse.
        from_file (str): Path to the file that calls this function.

    Returns:
        t.List[t.Tuple[int, int]]:
            List of tuples where the first element is the rotation
            (-1 for left, 1 for right) and the second element
            is the number of ticks to turn.
    """
    absolute_path_to_file: str = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(from_file), file_name)
    )
    rotations: t.List[t.Tuple[int, int]] = []
    with open(absolute_path_to_file, "r", encoding="utf-8") as input_fd:
        rotations = [
            (-1 if line[0] == "L" else 1, int(line[1:]))
            for line in input_fd.read().splitlines()
        ]
    return rotations
