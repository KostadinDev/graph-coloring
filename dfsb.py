import sys
from itertools import groupby
from visual_graph import visualize
from copy import deepcopy


# Constructs an adjacency list representation of a graph from the input
def construct_graph():
    input_file, output_file, mode_flag = sys.argv[1:4]
    edges = []
    with open(input_file) as fp:
        line = fp.readline()
        # N - number of nodes
        # M - number of constraints
        # K - number of colors
        N, M, K = line.split()
        vertices = [str(i) for i in range(int(N))]
        colors = [str(i) for i in range(int(K))]
        while line:
            line = fp.readline()
            if line:
                edges.append(line.split())

    graph = {}
    graph_coloring = {}
    for vertex in vertices:
        graph[vertex] = []
        graph_coloring[vertex] = None
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph, graph_coloring, edges, K


# Checks if generated graph coloring is a solution.
# Returns true if it is and false otherwise.
def is_solution(graph_coloring, edges):
    for node in graph_coloring:
        for edge in edges:
            if graph_coloring[edge[0]] == graph_coloring[edge[1]] or graph_coloring[edge[0]] is not None:
                return False
    return True


# gets the colors of neighboring nodes
def get_neighbor_colors(graph, graph_coloring, node):
    colors = []
    for neighbor in graph[node]:
        if graph_coloring[neighbor] is not None:
            colors.append(graph_coloring[neighbor])
    return colors


def get_successors(graph, graph_coloring, node, colors):
    successors = []
    for neighbor in graph[node]:
        if graph_coloring[neighbor] is None:
            neighbor_colors = get_neighbor_colors(graph, graph_coloring, neighbor)
            for color in colors:
                if color not in neighbor_colors:
                    copy_graph_coloring = deepcopy(graph_coloring)
                    copy_graph_coloring[neighbor] = color
                    successors.append((graph, copy_graph_coloring, neighbor, colors))
    return successors


def DFS(graph, graph_coloring, node, colors):
    if is_solution(graph_coloring):
        return graph_coloring

    for successor in get_successors(graph, graph_coloring, node, colors):
        DFS(successor)


if __name__ == '__main__':
    graph, graph_coloring, edges, colors = construct_graph()
    graph_coloring['0'] = '0'
    graph_coloring['1'] = '1'
    print(get_successors(graph, graph_coloring, '5', ['0', '1', '2', '3'])[3][1:3])
# visualize(graph)

# DFS(graph, '0')
