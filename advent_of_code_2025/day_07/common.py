"""Common methods for the Day 07"""

import typing as t
from pathlib import Path


def parse_diagram_file(file_name: str) -> t.List[t.List[str]]:
    """Parse TXT input file and generate diagram.

    Args:
        file_name (str): Name of the file to parse.

    Returns:
        t.List[t.List[str]]: Diagram as a list of list of characters.
    """
    diagram: t.List[t.List[str]] = []
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        diagram = list(
            list(line) for line in map(str.strip, input_fd.readlines())
        )
    return diagram
