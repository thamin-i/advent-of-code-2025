"""Common methods for the Day 12"""

import typing as t
from pathlib import Path


class GiftShape:  # pylint: disable=too-few-public-methods
    """Gift 2D shape representation."""

    coordinates: t.List[t.Tuple[int, int]]
    width: int
    height: int
    area: int

    def __init__(self, raw_shape: t.List[t.List[str]]) -> None:
        """Initialize GiftShape with raw shape data.

        Args:
            raw_shape (t.List[t.List[str]]): Raw 2D shape.
        """
        self.coordinates = [
            (row_index, column_index)
            for row_index in range(len(raw_shape))
            for column_index in range(len(raw_shape[0]))
            if raw_shape[row_index][column_index] == "#"
        ]
        self.width = max(col for _, col in self.coordinates) + 1
        self.height = max(row for row, _ in self.coordinates) + 1
        self.area = len(self.coordinates)

    def __str__(self) -> str:
        """Generate string representation of the shape.

        Returns:
            str: String representation of the shape.
        """
        str_representation: str = ""
        for row in range(self.height):
            line: str = ""
            for col in range(self.width):
                if (row, col) in self.coordinates:
                    line += "#"
                else:
                    line += "."
            str_representation += line + "\n"
        return str_representation


class Gift:  # pylint: disable=too-few-public-methods
    """Gift representation."""

    id: int
    shapes: t.Dict[int, GiftShape]
    area: int

    def __init__(self, raw_data: t.List[str]) -> None:
        """Initialize Gift from raw data.

        Args:
            raw_data (t.List[str]): Raw gift.
        """
        self.id = int(raw_data[0].split(":")[0])
        self.__initialize_shapes(raw_data)
        self.area = self.shapes[0].area

    def __generate_rotated_shapes(
        self, shapes: t.Dict[int, t.List[t.List[str]]]
    ) -> None:
        """Generate rotated shapes and add them to the shapes dictionary.

        Args:
            shapes (t.Dict[int, t.List[t.List[str]]]): Existing shapes.
        """
        previous_shape: t.List[t.List[str]]
        new_shape: t.List[t.List[str]]
        for direction in range(1, 4):
            previous_shape = shapes[direction - 1]
            new_shape = []
            for column_index in range(len(previous_shape[0])):
                new_shape.append(
                    [
                        previous_shape[row_index][column_index]
                        for row_index in reversed(range(len(previous_shape)))
                    ]
                )
            shapes[direction] = new_shape

    def __generate_flipped_shapes(
        self, shapes: t.Dict[int, t.List[t.List[str]]]
    ) -> None:
        """Generate flipped shapes and add them to the shapes dictionary.

        Args:
            shapes (t.Dict[int, t.List[t.List[str]]]): Existing shapes.
        """
        flipped_shapes: t.List[t.List[t.List[str]]] = []
        new_shape: t.List[t.List[str]]
        for previous_shape in shapes.values():
            new_shape = []
            for row in previous_shape:
                new_shape.append(list(reversed(row)))
            flipped_shapes.append(new_shape)

        shapes_count: int = len(shapes.keys())
        for shape_id, new_shape in enumerate(flipped_shapes):
            shapes[shapes_count + shape_id] = new_shape

    def __initialize_shapes(self, raw_data: t.List[str]) -> None:
        """Initialize all possible shapes from raw data.

        Args:
            raw_data (t.List[str]): Raw gift shape data.
        """
        shapes: t.Dict[int, t.List[t.List[str]]] = {
            0: [list(line) for line in raw_data[1:]]
        }

        self.__generate_rotated_shapes(shapes)
        self.__generate_flipped_shapes(shapes)

        self.shapes = {
            key: GiftShape(value)
            for key, value in self.deduplicate_shapes(shapes).items()
        }

    @staticmethod
    def deduplicate_shapes(
        shapes: t.Dict[int, t.List[t.List[str]]]
    ) -> t.Dict[int, t.List[t.List[str]]]:
        """Deduplicate shapes.

        Args:
            shapes (t.Dict[int, t.List[t.List[str]]]): Raw shapes.

        Returns:
            t.Dict[int, t.List[t.List[str]]]: Deduplicated shapes.
        """
        deduplicated_shapes: t.Dict[str, t.List[t.List[str]]] = {}
        for direction in shapes:
            shape_str: str = "\n".join(
                ["".join(line) for line in shapes[direction]]
            )
            if shape_str not in deduplicated_shapes:
                deduplicated_shapes[shape_str] = shapes[direction]
        return {
            i: deduplicated_shapes[shape_str]
            for i, shape_str in enumerate(deduplicated_shapes)
        }

    def __str__(self) -> str:
        """Generate string representation of the gift.

        Returns:
            str: String representation of the gift.
        """
        return f"""
        Gift(
            id={self.id},
            shapes=
{self.__str__shapes()}
        )"""

    def __str__shapes(self) -> str:
        """Generate string representation of all shapes.

        Returns:
            str: String representation of all shapes.
        """
        return "".join(
            [
                f"- {key}:\n" f"{value}" + "\n"
                for key, value in self.shapes.items()
            ]
        )


class Region:  # pylint: disable=too-few-public-methods
    """Region representation."""

    id: int
    width: int
    height: int
    must_fit: t.List[int]

    def __init__(self, region_id: int, raw_data: str) -> None:
        """Initialize Region from raw data.

        Args:
            region_id (int): Region ID.
            raw_data (str): Raw region data.
        """
        self.id = region_id
        self.width = int(raw_data.split("x")[0])
        self.height = int(raw_data.split("x")[1].split(":")[0])
        self.must_fit = list(
            map(int, (x for x in raw_data.split(":")[1].split(" ") if len(x)))
        )

    def __str__(self) -> str:
        """Generate string representation of the region.

        Returns:
            str: String representation of the region.
        """
        return (
            f"Region(id={self.id}, "
            f"width={self.width}, "
            f"height={self.height}, "
            f"must_fit={self.must_fit})"
        )


def parse_gifts_and_regions_file(
    file_name: str,
) -> t.Tuple[t.List[Gift], t.List[Region]]:
    """Parse gifts and regions from file.

    Args:
        file_name (str): File name.

    Returns:
        t.Tuple[t.List[Gift], t.List[Region]]:
            Parsed gifts and regions.
    """
    gifts: t.List[Gift] = []
    regions: t.List[Region] = []
    file_path: Path = Path(__file__).parent / file_name
    with open(file_path, "r", encoding="utf-8") as input_fd:
        raw_blocks: t.List[str] = input_fd.read().split("\n\n")
        for raw_gift in raw_blocks[:-1]:
            gifts.append(Gift(raw_gift.split("\n")))
        for region_id, raw_region in enumerate(raw_blocks[-1].split("\n")):
            if len(raw_region):
                regions.append(Region(region_id, raw_region))
    return gifts, regions
