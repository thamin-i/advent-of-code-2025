"""Common methods for the Day 11"""

import typing as t
from pathlib import Path


def parse_mapping_file(file_name: str) -> t.Dict[str, t.List[str]]:
    """Parse TXT input file and generate a mapping of nodes to their neighbors.

    Args:
        file_name (str): Name of the file to parse.

    Returns:
        t.Dict[str, t.List[str]]:
            Dictionary where keys are node names
            and values are lists of neighboring node names.
    """
    mapping: t.Dict[str, t.List[str]] = {}
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        mapping = {
            line.split(": ")[0]: list(line.split(": ")[1].split(" "))
            for line in input_fd.read().splitlines()
        }
    return mapping
