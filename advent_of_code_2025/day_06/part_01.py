"""Advent of code - Day 06 - Part 01"""

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
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        for line in input_fd.read().splitlines():
            line = re.sub(r"\s+", " ", line.strip())
            for idx, value in enumerate(line.split(" ")):
                if len(problems) <= idx:
                    problems.append(MathProblem())
                if not value.isdigit():
                    problems[idx].set_operator(value)
                else:
                    problems[idx].add_operand(int(value))
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
