"""Advent of code - Day 12 - Part 01"""

import typing as t

from advent_of_code_2025.day_12.common import (
    Gift,
    GiftShape,
    Region,
    parse_gifts_and_regions_file,
)


def print_board(board: t.List[t.List[int]]) -> None:
    """Print the board.

    Args:
        board (t.List[t.List[int]]): Board to print.
    """
    for row in board:
        print("".join(str(cell) for cell in row))
    print()


def fits(board: t.List[t.List[int]], shape: GiftShape, x: int, y: int) -> bool:
    """Check if shape fits at position.

    Args:
        board (t.List[t.List[int]]): Board to check.
        shape (GiftShape): Shape to place.
        x (int): X coordinate.
        y (int): Y coordinate.

    Returns:
        bool: True if shape fits, False otherwise.
    """
    for pos_x, pos_y in shape.coordinates:
        if board[y + pos_y][x + pos_x] == 1:
            return False
    return True


def place(board: t.List[t.List[int]], shape: GiftShape, x: int, y: int) -> None:
    """Place shape on board at position.

    Args:
        board (t.List[t.List[int]]): Board to place on.
        shape (GiftShape): Shape to place.
        x (int): X coordinate.
        y (int): Y coordinate.
    """
    for pos_x, pos_y in shape.coordinates:
        board[y + pos_y][x + pos_x] = 1


def remove(
    board: t.List[t.List[int]], shape: GiftShape, x: int, y: int
) -> None:
    """Remove shape from board.

    Args:
        board (t.List[t.List[int]]): Board to remove from.
        shape (GiftShape): Shape to remove.
        x (int): X coordinate of the placed shape.
        y (int): Y coordinate of the placed shape.
    """
    for pos_x, pos_y in shape.coordinates:
        board[y + pos_y][x + pos_x] = 0


def free_cells(board: t.List[t.List[int]]) -> int:
    """Return count of empty cells on the board.

    Args:
        board (t.List[t.List[int]]): Board to check.

    Returns:
        int: Count of empty cells.
    """
    return sum(1 for row in board for cell in row if cell == 0)


def sort_gifts_by_area_and_shapes(
    gifts: t.Dict[int, Gift], gifts_to_place: t.List[int]
) -> None:
    """Sort gifts by area and number of shapes.

    Args:
        gifts (t.Dict[int, Gift]): Dictionary of gifts.
        gifts_to_place (t.List[int]): List of gift IDs to sort.
    """

    def __sort(gift_id: int) -> tuple[int, int]:
        """Sorting function for gifts.

        Args:
            gift_id (int): Gift ID.

        Returns:
            tuple[int, int]:
                Sorting key as a tuple of
                - [0] negative max area
                - [1] shapes count
        """
        gift: Gift = gifts[gift_id]
        max_area: int = max(shape.area for shape in gift.shapes.values())
        shapes_count: int = len(gift.shapes)
        return (-max_area, shapes_count)

    gifts_to_place.sort(key=__sort)


def rec_backtrack_fits(
    region: Region,
    gifts: t.Dict[int, Gift],
    board: t.List[t.List[int]],
    remaining: t.List[int],
) -> bool:
    """Backtracking algorithm to fit gifts into the region.

    Args:
        region (Region): Region to fill.
        gifts (t.Dict[int, Gift]): Gifts to place.
        board (t.List[t.List[int]]): Current state of the board.
        remaining (t.List[int]): Remaining gift IDs to place.

    Returns:
        bool: True all gifts fit, False otherwise.
    """
    if not remaining:
        return True

    shape_id: int = remaining[0]
    gift: Gift = gifts[shape_id]

    for shape in gift.shapes.values():  # pylint: disable=too-many-nested-blocks
        for pos_y in range(region.height - shape.height + 1):
            for pos_x in range(region.width - shape.width + 1):
                if fits(board, shape, pos_x, pos_y):
                    place(board, shape, pos_x, pos_y)

                    if free_cells(board) >= sum(
                        gifts[gid].area for gid in remaining[1:]
                    ):
                        if rec_backtrack_fits(
                            region, gifts, board, remaining[1:]
                        ):
                            return True

                    remove(board, shape, pos_x, pos_y)
    return False


def is_region_valid(region: Region, gifts: t.Dict[int, Gift]) -> bool:
    """Check if a given set of gifts can fit into a given region.

    Args:
        region (Region): Region to check.
        gifts (t.Dict[int, Gift]): Gifts to place.

    Returns:
        bool: True if region is valid, False otherwise.
    """
    board: t.List[t.List[int]] = [
        [0] * region.width for _ in range(region.height)
    ]

    gifts_to_place: t.List[int] = []
    for gift_id, count in enumerate(region.must_fit):
        gifts_to_place.extend([gift_id] * count)

    sort_gifts_by_area_and_shapes(gifts, gifts_to_place)

    return rec_backtrack_fits(region, gifts, board, gifts_to_place)


def count_valid_regions(gifts: t.List[Gift], regions: t.List[Region]) -> int:
    """Count regions that can be validly filled with gifts.

    Args:
        gifts (list[Gift]): List of gifts.
        regions (list[Region]): List of regions.

    Returns:
        int: Count of valid regions.
    """
    valid_regions: int = 0
    for region in regions:
        if is_region_valid(region, {gift.id: gift for gift in gifts}):
            valid_regions += 1
    return valid_regions


def main() -> None:
    """Main function."""
    invalid_ids_sum: int
    invalid_ids_sum = count_valid_regions(
        *parse_gifts_and_regions_file(file_name="inputs/example.txt")
    )
    print(f"Example output: {invalid_ids_sum}")

    invalid_ids_sum = count_valid_regions(
        *parse_gifts_and_regions_file(file_name="inputs/real.txt")
    )
    print(f"Real output: {invalid_ids_sum}")


if __name__ == "__main__":
    main()
