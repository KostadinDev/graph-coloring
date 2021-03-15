import sys
from itertools import groupby
from visual_graph import visualize
from copy import deepcopy
import random


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
    return graph, graph_coloring, edges, colors


# Checks if generated graph coloring is a solution.
# Returns true if it is and false otherwise.
def is_solution(graph_coloring, edges):
    # if None in graph_coloring.values():
    #     return False
    for edge in edges:
        if graph_coloring[edge[0]] == graph_coloring[edge[1]] or graph_coloring[edge[0]] is None or graph_coloring[
            edge[1]] is None:
            return False
    return True


# gets the colors of neighboring nodes
def get_neighbor_colors(graph, graph_coloring, node):
    colors = []
    for neighbor in graph[node]:
        if graph_coloring[neighbor] is not None:
            colors.append(graph_coloring[neighbor])
    return colors


# Gives the possible branching of a node
def get_successors(graph, graph_coloring, node, colors):
    successors = []
    for neighbor in graph[node]:
        if graph_coloring[neighbor] is None:
            neighbor_colors = get_neighbor_colors(graph, graph_coloring, neighbor)
            for color in colors:
                if color not in neighbor_colors:
                    copy_graph_coloring = deepcopy(graph_coloring)
                    copy_graph_coloring[neighbor] = color
                    successors.append((copy_graph_coloring, neighbor))
    return successors


# Depth first searching for backtracking
def DFSB(graph, graph_coloring, node, colors, edges):
    if is_solution(graph_coloring, edges):
        return graph_coloring
    successors = get_successors(graph, graph_coloring, node, colors)
    for successor in successors:
        colored_graph = DFSB(graph, successor[0], successor[1], colors, edges)
        if colored_graph is not None:
            return colored_graph
    return None


# DFSB DRIVER

def DFSB_DRIVER(graph, graph_coloring, edges, colors):
    graph_coloring['0'] = '0'
    colored_graph = DFSB(graph, graph_coloring, '0', colors, edges)
    print(colored_graph)
    visualize(graph)


def get_random_color(colors):
    return random.choice(colors)
    pass


def get_random_coloring(graph_coloring, colors):
    for node in graph_coloring:
        graph_coloring[node] = get_random_color(colors)
    return graph_coloring


def get_conflicted(graph, graph_coloring, edges):
    random.shuffle(edges)
    for edge in edges:
        if graph_coloring[edge[0]] == graph_coloring[edge[1]]:
            return random.choice(edge)
    return -1


def get_least_conflict(graph, graph_coloring, edges, node):
    pass


def min_conflict(graph, graph_coloring, edges, colors, max_steps):
    graph_coloring = get_random_coloring(graph_coloring, colors)
    for i in range(max_steps):
        node = get_conflicted(graph, graph_coloring, edges)
        if node == -1:
            print('Solution found')
            return graph_coloring

        new_color = get_least_conflict(graph, graph_coloring, edges, node)
        graph_coloring[node] = new_color


def min_conflict_DRIVER(graph, graph_coloring, edges, colors):
    min_conflict(graph, graph_coloring, edges, colors, 10000)


if __name__ == '__main__':
    graph, graph_coloring, edges, colors = construct_graph()
    # DFSB_DRIVER(graph, graph_coloring, edges, colors)
    min_conflict_DRIVER(graph, graph_coloring, edges, colors)
