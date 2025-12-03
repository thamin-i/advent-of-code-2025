"""Common methods for the Day 02"""

import re
import typing as t
from pathlib import Path


def parse_id_ranges_file(file_name: str) -> t.List[t.Tuple[int, int]]:
    """Parse the ID ranges from the input file.

    Args:
        file_name (str): Name of the input file.

    Returns:
        t.List[t.Tuple[int, int]]: List of ID ranges as tuples.
    """
    id_ranges: t.List[t.Tuple[int, int]] = []
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        id_ranges = [
            (int(line.split("-")[0]), int(line.split("-")[1]))
            for line in input_fd.read().split(",")
        ]
    return id_ranges


def sum_invalid_ids(
    id_ranges: t.List[t.Tuple[int, int]], match_many: bool
) -> int:
    """Sum all invalid IDs based on the given ID ranges.

    Args:
        id_ranges (t.List[t.Tuple[int, int]]): List of ID ranges.
        match_many (bool): Whether to match many repetitions or just one.

    Returns:
        int: Sum of all invalid IDs.
    """
    return sum(
        id_number
        for range_start, range_end in id_ranges
        for id_number in range(range_start, range_end + 1)
        if re.fullmatch(
            r"(.+?)\1+" if match_many else r"(.+?)\1", str(id_number)
        )
    )
