import networkx as nx
import matplotlib.pyplot as plt


def visualize(graph):
    print("hello")
    G = nx.Graph(graph)
    nx.draw_spring(G)
    plt.show()
