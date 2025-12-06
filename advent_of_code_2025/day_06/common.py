"""Common methods for the Day 06"""

import typing as t


class MathProblem:
    """Class representing a mathematical problem
    with an operator and a list of operands.
    """

    operator: str | None
    operands: t.List[int]

    def __init__(
        self, operator: str | None = None, operands: t.List[int] | None = None
    ) -> None:
        self.operator = operator
        self.operands = operands if operands is not None else []

    @staticmethod
    def available_operators() -> t.List[str]:
        """List of supported operators.

        Returns:
            t.List[str]: Supported operators.
        """
        return ["+", "*"]

    def set_operator(self, operator: str) -> None:
        """Set the operator for the problem.

        Args:
            operator (str): Operator to set.
        """
        if operator not in self.available_operators():
            raise ValueError(f"Unsupported operator: {operator}")
        self.operator = operator

    def add_operand(self, operand: int) -> None:
        """Add an operand to the problem.

        Args:
            operand (int): Operand to add.
        """
        self.operands.append(operand)

    def evaluate(self) -> int:
        """Evaluate the mathematical problem.

        Returns:
            int: Result of the evaluation.
        """
        if self.operator is None:
            raise ValueError("Operator is not set.")
        return t.cast(
            int,
            eval(  # pylint: disable=eval-used
                f"{self.operator}".join(map(str, self.operands))
            ),
        )


def evaluate_and_sum_problems(problems: t.List[MathProblem]) -> int:
    """Evaluate and sum a list of mathematical problems.

    Args:
        problems (t.List[MathProblem]): List of mathematical problems.

    Returns:
        int: Sum of evaluated problems.
    """
    return sum(problem.evaluate() for problem in problems)
