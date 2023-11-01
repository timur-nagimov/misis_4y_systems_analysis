from typing import Dict, List, Tuple
import csv
import io


def get_edges_from_csv(csv_content: str, delimiter=';') -> List[Tuple[int, int]]:
    edge_list = []
    buffer = io.StringIO(csv_content)
    csv_reader = csv.reader(buffer, delimiter=delimiter)
    for line in csv_reader:
        if len(line) == 2:
            edge_list.append((int(line[0]), int(line[1])))
    return edge_list


def construct_graph(edge_list: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    adjacency_list = {}
    for start, end in edge_list:
        if start not in adjacency_list:
            adjacency_list[start] = []
        adjacency_list[start].append(end)
    return adjacency_list


def recursive_dfs(graph: Dict[int, List[int]], node: int, current_depth: int, node_depths: Dict[int, int]) -> None:
    node_depths[node] = current_depth
    if node in graph:
        for neighbor in graph[node]:
            recursive_dfs(graph, neighbor, current_depth + 1, node_depths)


def calculate_subtree_sizes(graph: Dict[int, List[int]], node: int, subtree_sizes: Dict[int, int]) -> int:
    if node not in graph:
        subtree_sizes[node] = 1
        return 1
    size = 1
    for child in graph[node]:
        size += calculate_subtree_sizes(graph, child, subtree_sizes)
    subtree_sizes[node] = size
    return size


def group_nodes_by_depth(depths: Dict[int, int]) -> Dict[int, List[int]]:
    levels = {}
    for node, depth in depths.items():
        if depth not in levels:
            levels[depth] = []
        levels[depth].append(node)
    return levels


def task(csv_input: str) -> str:
    edges = get_edges_from_csv(csv_input)

    graph = construct_graph(edges)
    reverse_graph = {child: parent for parent,
                     children in graph.items() for child in children}

    num_children = {node: len(children) for node, children in graph.items()}
    depths = {}
    subtree_sizes = {}
    same_level = {}

    for node in graph:
        if node not in depths:
            recursive_dfs(graph, node, 0, depths)
        if node not in subtree_sizes:
            calculate_subtree_sizes(graph, node, subtree_sizes)

    levels = group_nodes_by_depth(depths)

    for depth, nodes in levels.items():
        for node in nodes:
            same_level[node] = len(nodes) - 1

    all_nodes = set(graph.keys()) | {
        child for children in graph.values() for child in children}

    output_buffer = io.StringIO()
    csv_writer = csv.writer(output_buffer, delimiter='\t')

    for node in sorted(all_nodes):
        r1 = num_children.get(node, 0)
        r2 = 1 if node in reverse_graph else 0
        r3 = subtree_sizes.get(node, 1) - r1 - 1
        r4 = depths.get(node, 0) - 1 if node in reverse_graph else 0
        r5 = same_level.get(node, 0)
        csv_writer.writerow([r1, r2, r3, r4, r5])

    return output_buffer.getvalue().strip()


def save_csv_data_to_file(csv_data: str, file_path: str) -> None:
    formatted_data = csv_data.replace('\t', ';')
    with open(file_path, 'w', newline='') as file:
        file.write(formatted_data)


csv_data = "1;2\n1;3\n3;4\n3;5"
csv_output = task(csv_data)

output_file_path = "./task3.csv"
save_csv_data_to_file(csv_output, output_file_path)
