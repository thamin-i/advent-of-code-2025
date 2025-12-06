"""Advent of code - Day 06 - Part 02"""

import re
import typing as t
from pathlib import Path

from advent_of_code_2025.day_06.common import (
    MathProblem,
    evaluate_and_sum_problems,
)


def parse_problems_file(file_name: str) -> t.List[MathProblem]:
    """Parse problems file and generate problems object

    Args:
        file_name (str): Name of the file to parse.

    Returns:
        t.List[MathProblem]: List of parsed problems.
    """
    problems: t.List[MathProblem] = []
    problems_idx: int = -1
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        lines: t.List[str] = input_fd.read().splitlines()

        # My pretty stupid linter is removing the spaces at the end of lines
        # So I need to pad them again :(
        width: int = max(len(line) for line in lines)
        lines = [line.ljust(width) for line in lines]

        columns: t.List[str] = [
            "".join(line[x] for line in lines) for x in range(len(lines[0]))
        ]

        for column in columns:
            number: re.Match[str] | None = re.search(r"\d+", column)
            operator: re.Match[str] | None = re.search(r"[\+\*]", column)

            if operator is not None:
                problems_idx += 1
                problems.append(MathProblem(operator=operator.group(0)))

            if number is not None:
                problems[problems_idx].add_operand(
                    int("".join(number.group(0)))
                )

    return problems


def main() -> None:
    """Main function."""
    solution: int

    solution = evaluate_and_sum_problems(
        parse_problems_file(
            file_name="inputs/example.txt",
        )
    )
    print(f"Example output: {solution}")

    solution = evaluate_and_sum_problems(
        parse_problems_file(
            file_name="inputs/real.txt",
        )
    )
    print(f"Real output: {solution}")


if __name__ == "__main__":
    main()
