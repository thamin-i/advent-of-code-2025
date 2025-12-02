"""Common methods for the Day 02"""

import os
import typing as t


def parse_id_ranges_file(
    file_name: str, from_file: str
) -> t.List[t.Tuple[int, int]]:
    """Parse the ID ranges from the input file.

    Args:
        file_name (str): Name of the input file.
        from_file (str): Reference file to determine the path.

    Returns:
        t.List[t.Tuple[int, int]]: List of ID ranges as tuples.
    """
    absolute_path_to_file: str = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(from_file), file_name)
    )
    id_ranges: t.List[t.Tuple[int, int]] = []
    with open(absolute_path_to_file, "r", encoding="utf-8") as input_fd:
        id_ranges = [
            (int(line.split("-")[0]), int(line.split("-")[1]))
            for line in input_fd.read().split(",")
        ]
    return id_ranges
