"""Common methods for the Day 04"""

import itertools
import typing as t
from pathlib import Path


def parse_grid_file(file_name: str) -> t.List[t.List[str]]:
    """Parse a grid file into a 2D list of strings.

    Args:
        file_name (str): The name of the file to parse.

    Returns:
        t.List[t.List[str]]: A 2D list representing the grid.
    """
    grid: t.List[t.List[str]] = []
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        grid = [list(line.strip()) for line in input_fd.readlines()]
    return grid


def is_roll_accessible(grid: t.List[t.List[str]], row: int, col: int) -> bool:
    """Check if a roll at a given position is accessible.
    An accessible roll is defined as one that has less than 4 adjacent rolls.

    Args:
        grid (t.List[t.List[str]]): The grid representing the rolls.
        row (int): The row index of the roll.
        col (int): The column index of the roll.

    Returns:
        bool: True if the roll is accessible, False otherwise.
    """
    adjacent_rolls: int = 0
    directions: t.List[t.Tuple[int, int]] = [
        t.cast(t.Tuple[int, int], direction)
        for direction in itertools.product([-1, 0, 1], repeat=2)
        if direction != (0, 0)
    ]

    for row_direction, col_direction in directions:
        r, c = row + row_direction, col + col_direction
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == "@":
                adjacent_rolls += 1

    if adjacent_rolls >= 4:
        return False

    return True


def rec_compute_accessible_rolls(
    grid: t.List[t.List[str]], accessible_rolls: int = 0, part_01: bool = False
) -> int:
    """Recursively compute the number of accessible rolls in the grid.

    Args:
        grid (t.List[t.List[str]]):
            The grid representing the rolls.
        accessible_rolls (int, optional):
            The current count of accessible rolls. Defaults to 0.
        part_01 (bool, optional):
            If True, disables recursion. Defaults to False.

    Returns:
        int: The number of accessible rolls in the grid.
    """
    accessed_new_rolls: bool = False

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "@" and is_roll_accessible(grid, i, j):
                accessible_rolls += 1
                # In part two, we mark the roll as accessed
                if not part_01:
                    grid[i][j] = "X"
                accessed_new_rolls = True

    # In part one, we do not recurse
    if part_01:
        return accessible_rolls

    if accessed_new_rolls:
        return rec_compute_accessible_rolls(grid, accessible_rolls)

    return accessible_rolls
