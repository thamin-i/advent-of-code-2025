"""Advent of code - Day 05 - Part 01"""

import typing as t

from advent_of_code_2025.day_05.common import parse_database_file


def count_fresh_ingredients(
    ranges: t.List[t.Tuple[int, int]], ingredients: t.List[int]
) -> int:
    """Count fresh ingredients within specified ranges.

    Args:
        ranges (t.List[t.Tuple[int, int]]):
            List of tuples representing ranges of fresh ingredients.
        ingredients (t.List[int]):
            List of ingredient identifiers.

    Returns:
        int:
            The count of fresh ingredients within the specified ranges.
    """
    return len(
        {
            ingredient
            for ingredient in ingredients
            for low, high in ranges
            if low <= ingredient <= high
        }
    )


def main() -> None:
    """Main function."""
    fresh_ingredients_count: int
    ranges, ingredients = parse_database_file(
        file_name="inputs/example.txt",
    )
    fresh_ingredients_count = count_fresh_ingredients(ranges, ingredients)
    print(f"Example output: {fresh_ingredients_count}")

    ranges, ingredients = parse_database_file(
        file_name="inputs/real.txt",
    )
    fresh_ingredients_count = count_fresh_ingredients(ranges, ingredients)
    print(f"Real output: {fresh_ingredients_count}")


if __name__ == "__main__":
    main()
