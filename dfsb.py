import sys
from itertools import groupby


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
    print(graph)
    return graph, graph_coloring, edges, K


# Checks if generated graph coloring is a solution.
# Returns true if it is and false otherwise.
def is_solution(graph_coloring, edges):
    for node in graph_coloring:
        if node is None:
            return False
    for edge in edges:
        if graph_coloring[edge[0]] == graph_coloring[edge[1]]:
            return False
    return True


def DFS(graph, graph_coloring):
    pass


if __name__ == '__main__':
    graph, graph_coloring, edges, num_colors = construct_graph()
    print(is_solution(graph_coloring, edges))

    # DFS(graph, '0')
