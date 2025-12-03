"""Interactive CLI for running Advent of Code 2025 solutions."""

import importlib
import sys
import typing as t
from pathlib import Path

import click


def get_available_days() -> t.List[t.Tuple[int, str]]:
    """Get list of available day folders.

    Returns:
        t.List[t.Tuple[int, str]]:
            List of tuples containing day number and folder name.
    """
    base_path: Path = Path(__file__).parent
    available_days: t.List[t.Tuple[int, str]] = []
    for item in sorted(base_path.iterdir()):
        if item.is_dir() and item.name.startswith("day_"):
            available_days.append((int(item.name.split("_")[1]), item.name))
    return available_days


def get_available_parts(day_folder: str) -> t.List[t.Tuple[int, str]]:
    """Get list of available parts for a given day.

    Args:
        day_folder (str): Day folder name.

    Returns:
        t.List[t.Tuple[int, str]]:
            List of tuples containing part number and file name.
    """
    base_path: Path = Path(__file__).parent / day_folder
    available_parts: t.List[t.Tuple[int, str]] = []
    for item in sorted(base_path.iterdir()):
        if (
            item.is_file()
            and item.name.startswith("part_")
            and item.name.endswith(".py")
        ):
            available_parts.append((int(item.stem.split("_")[1]), item.stem))
    return available_parts


@click.command()
@click.option(
    "--day",
    type=int,
    help="Day number to run (e.g., 1 for day_01)",
)
@click.option(
    "--part",
    type=int,
    help="Part number to run (1 or 2)",
)
def main(day: int | None = None, part: int | None = None) -> None:
    """Interactive CLI for running Advent of Code 2025 solutions.

    Run without arguments for interactive mode, or specify --day and --part.
    """
    # Interactive day selection if not provided
    if day is None:
        available_days: t.List[t.Tuple[int, str]] = get_available_days()
        click.echo("\n📅 Available Days:")
        for day_num, day_folder in available_days:
            click.echo(f"  {day_num}. {day_folder}")
        day = click.prompt(
            "\nSelect a day",
            type=click.IntRange(min=1, max=25),
        )

    # Validate day folder existence
    day_folder = f"day_{day:02d}"
    if not (Path(__file__).parent / day_folder).exists():
        click.echo(f"❌ Day {day} ({day_folder}) not found!", err=True)
        sys.exit(1)

    # Interactive part selection if not provided
    if part is None:
        available_parts: t.List[t.Tuple[int, str]] = get_available_parts(
            day_folder
        )
        click.echo(f"\n🧩 Available Parts for Day {day}:")
        for part_num, part_file in available_parts:
            click.echo(f"  {part_num}. {part_file}")

        part = click.prompt(
            "\nSelect a part",
            type=click.IntRange(min=1, max=2),
        )

    # Validate part file existence
    part_file = f"part_{part:02d}"
    if not (Path(__file__).parent / day_folder / f"{part_file}.py").exists():
        click.echo(
            f"❌ Part {part} ({part_file}.py) not found in {day_folder}!",
            err=True,
        )
        sys.exit(1)

    # Run the selected solution
    click.echo(f"\n🚀 Running Day {day}, Part {part}...\n")
    click.echo("=" * 50)

    module_path = f"advent_of_code_2025.{day_folder}.{part_file}"
    module = importlib.import_module(module_path)

    if hasattr(module, "main"):
        module.main()
    else:
        click.echo(f"⚠️  No main() function found in {part_file}.py", err=True)
        sys.exit(1)

    click.echo("=" * 50)
    click.echo("\n✅ Done!")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
