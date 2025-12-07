"""Advent of code - Day 07 - Part 02"""

import typing as t

import networkx as nx

from advent_of_code_2025.day_07.common import parse_diagram_file


def rec_count_paths(
    graph: nx.DiGraph,
    current: t.Tuple[int, int],
    targets: t.Set[t.Tuple[int, int]],
    cache: t.Dict[t.Tuple[int, int], int] | None = None,
) -> int:
    """Recursively count all possible paths
        from the current node to any of the target nodes.

    Args:
        graph (nx.DiGraph):
            Directed graph representing all possible paths.
        current (t.Tuple[int, int]):
            Current node in the graph.
        targets (t.Set[t.Tuple[int, int]]):
            Set of target nodes.
        cache (t.Dict[t.Tuple[int, int], int], optional):
            Cache to store previously computed results.
            Defaults to None.

    Returns:
        int:
            Number of possible paths from the current node to any target node.
    """
    if cache is None:
        cache = {}

    if current in cache:
        return cache[current]

    if current in targets:
        return 1

    paths_count: int = 0
    for successor in graph.successors(current):
        paths_count += rec_count_paths(graph, successor, targets, cache)

    cache[current] = paths_count
    return paths_count


def count_timelines(diagram: t.List[t.List[str]]) -> int:
    """Count the number of possible timelines through the diagram.

    Args:
        diagram (t.List[t.List[str]]):
            Input diagram.

    Returns:
        int:
            Number of possible timelines through the diagram.
    """
    rows: int = len(diagram)
    columns: int = len(diagram[0])
    start_node: t.Tuple[int, int] = (diagram[0].index("S"), 0)

    # Graph of all possible paths
    graph: nx.DiGraph = nx.DiGraph()
    graph.add_node(start_node)

    # Set of current active nodes indexes
    tachyons_idx: t.Set[int] = set()
    tachyons_idx.add(start_node[0])

    # Compute all possible paths through the diagram
    for y, line in enumerate(diagram):
        for x, char in enumerate(line):
            if char == "^" and x in tachyons_idx:
                tachyons_idx.remove(x)
                if x - 1 >= 0:
                    graph.add_edge((x, y), (x - 1, y + 1))
                    tachyons_idx.add(x - 1)
                if x + 1 < columns:
                    graph.add_edge((x, y), (x + 1, y + 1))
                    tachyons_idx.add(x + 1)
            else:
                graph.add_edge((x, y), (x, y + 1))

    # List of all the bottom nodes
    bottom_nodes: t.Set[t.Tuple[int, int]] = {
        (x, rows - 1) for x in tachyons_idx
    }

    return rec_count_paths(graph, start_node, bottom_nodes)


def main() -> None:
    """Main function."""
    timelines_count: int
    timelines_count = count_timelines(
        parse_diagram_file(file_name="inputs/example.txt")
    )
    print(f"Example output: {timelines_count}")

    timelines_count = count_timelines(
        parse_diagram_file(file_name="inputs/real.txt")
    )
    print(f"Real output: {timelines_count}")


if __name__ == "__main__":
    main()
