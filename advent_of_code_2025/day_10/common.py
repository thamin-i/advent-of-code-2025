"""Common methods for the Day 10"""

import re
import typing as t
from pathlib import Path


class Machine:  # pylint: disable=too-few-public-methods
    """Class representing a machine
    with indicator lights, buttons, and joltage.
    """

    indicator_lights_diagram: t.List[int]
    buttons: t.List[t.Set[int]]
    joltage: t.List[int]

    def __init__(self, raw_line: str) -> None:
        """Initialize Machine instance.

        Args:
            raw_line (str):
                Raw input line representing the machine configuration.
        """
        self.indicator_lights_diagram = [
            int(c == "#") for c in re.findall(r"\[(.*?)\]", raw_line)[0]
        ]
        self.buttons = [
            set(int(b) for b in button_group.split(","))
            for button_group in re.findall(r"\(([^()]*)\)", raw_line)
        ]
        self.joltage = [
            int(j) for j in re.findall(r"\{(.*?)\}", raw_line)[0].split(",")
        ]

    def __str__(self) -> str:
        """Return string representation.

        Returns:
            str: String representation of the Machine instance.
        """
        return (
            f"Machine(lights={self.indicator_lights_diagram}, "
            f"buttons={self.buttons}, joltage={self.joltage})"
        )


def parse_machines_file(file_name: str) -> t.List[Machine]:
    """Parse TXT input file and generate list of machines.

    Args:
        file_name (str): Name of the file to parse.

    Returns:
        t.List[Machine]: List of Machine instances.
    """
    machines: t.List[Machine]
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        machines = [Machine(line) for line in input_fd.read().splitlines()]
    return machines
