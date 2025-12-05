"""Common methods for the Day 05"""

import typing as t
from enum import Enum
from pathlib import Path


class ParsingMode(Enum):
    """Parsing modes enumeration."""

    RANGES = 1
    INGREDIENTS = 2


def parse_database_file(
    file_name: str,
) -> t.Tuple[t.List[t.Tuple[int, int]], t.List[int]]:
    """Parse the database file into ranges and ingredients.

    Args:
        file_name (str):
            The name of the file to parse.

    Returns:
        t.Tuple[t.List[t.Tuple[int, int]], t.List[int]]:
            The parsed ranges and ingredients.
    """
    mode: ParsingMode = ParsingMode.RANGES
    ingredients: t.List[int] = []
    ranges: t.List[t.Tuple[int, int]] = []
    file_path: Path = Path(__file__).parent / file_name

    with open(file_path, "r", encoding="utf-8") as input_fd:
        for line in input_fd.readlines():
            if len(line.strip()) == 0:
                mode = ParsingMode.INGREDIENTS
                continue
            if mode == ParsingMode.RANGES:
                ranges.append(
                    t.cast(
                        t.Tuple[int, int],
                        tuple(int(x) for x in line.strip().split("-")),
                    )
                )
            elif mode == ParsingMode.INGREDIENTS:
                ingredients.append(int(line.strip()))

    return ranges, ingredients
