"""Advent of code - Day 11 - Part 02"""

import typing as t
from collections import defaultdict

from advent_of_code_2025.day_11.common import parse_mapping_file


def reverse_graph(graph: t.Dict[str, t.List[str]]) -> t.Dict[str, t.List[str]]:
    """Reverse the graph direction.

    Args:
        graph (t.Dict[str, t.List[str]]): Graph as a dictionary.

    Returns:
        t.Dict[str, t.List[str]]: Reversed graph as a dictionary.
    """
    reversed_graph: t.Dict[str, t.List[str]] = defaultdict(list)
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            reversed_graph[neighbor].append(node)
    return reversed_graph


def node_reachable_from(
    graph: t.Dict[str, t.List[str]], node: str
) -> t.Set[str]:
    """Return the set of nodes reachable from the given node in the graph.

    Args:
        graph (t.Dict[str, t.List[str]]): Graph as a dictionary.
        node (str): Starting node.

    Returns:
        t.Set[str]: Set of reachable nodes.
    """
    visited: t.Set[str] = set()
    stack: t.List[str] = [node]
    while stack:
        current_node: str = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            stack.extend(graph.get(current_node, []))
    return visited


def prune_non_used_nodes_in_graph(
    graph: t.Dict[str, t.List[str]], start_node: str, end_node: str
) -> t.Dict[str, t.List[str]]:
    """Prune nodes that are not reachable
        from the start node or cannot reach the end node.

    Args:
        graph (t.Dict[str, t.List[str]]): Graph as a dictionary.
        start_node (str): Start node.
        end_node (str): End node.

    Returns:
        t.Dict[str, t.List[str]]: Pruned graph as a dictionary.
    """
    from_start: t.Set[str] = node_reachable_from(graph, start_node)
    to_end: t.Set[str] = node_reachable_from(reverse_graph(graph), end_node)
    keep: t.Set[str] = from_start & to_end
    return {
        node: [n for n in neighbors if n in keep]
        for node, neighbors in graph.items()
        if node in keep
    }


def list_paths_in_graph(
    graph: t.Dict[str, t.List[str]], start: str, end: str
) -> t.Generator[t.List[str], None, None]:
    """List all paths in the graph from start to end.

    Args:
        graph (t.Dict[str, t.List[str]]): Graph as a dictionary.
        start (str): Starting node.
        end (str): Ending node.

    Returns:
        t.Generator[t.List[str], None, None]:
            Generator of paths from start to end.
    """
    stack: t.List[t.Tuple[str, t.List[str]]] = [(start, [start])]
    while stack:
        node, path = stack.pop()
        if node == end:
            yield list(path)
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))


def optimize_graph_and_count_paths(graph: t.Dict[str, t.List[str]]) -> int:
    """Optimize the graph and count valid paths that
        go from the start_node to the end_node
        passing through the two mandatory_nodes.

    Args:
        graph (t.Dict[str, t.List[str]]): Graph as a dictionary.

    Returns:
        int: Number of valid paths.
    """
    start_node: str = "svr"
    end_node: str = "out"
    mandatory_nodes: t.List[str] = ["fft", "dac"]

    # Step 1): prune nodes that cannot reach end or be reached from start
    graph = prune_non_used_nodes_in_graph(graph, start_node, end_node)

    # Step 2): List all possible paths for start<->A A<->B and B<->end
    # and multiply their counts to get the total number of valid paths
    paths_count: int = 1
    for start, end in list(
        zip([start_node] + mandatory_nodes, mandatory_nodes + [end_node])
    ):
        # Step 2.c): Multiply the number of paths for each segment
        paths_count *= len(
            list(
                # Step 2.b): List all paths between the two nodes
                list_paths_in_graph(
                    # Step 2.a): Prune the graph for the current start-end pair
                    prune_non_used_nodes_in_graph(graph, start, end),
                    start,
                    end,
                )
            )
        )

    return paths_count


def main() -> None:
    """Main function."""
    valid_paths_count: int
    valid_paths_count = optimize_graph_and_count_paths(
        parse_mapping_file(file_name="inputs/example_2.txt")
    )
    print(f"Example output: {valid_paths_count}")

    valid_paths_count = optimize_graph_and_count_paths(
        parse_mapping_file(file_name="inputs/real.txt")
    )
    print(f"Real output: {valid_paths_count}")


if __name__ == "__main__":
    main()
