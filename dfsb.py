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
    return graph, graph_coloring, M, K


def is_solution(graph_coloring):
    pass

def DFS(graph, graph_coloring):
    pass


if __name__ == '__main__':
    graph, graph_coloring, num_edges, num_colors = construct_graph()

    # DFS(graph, '0')
