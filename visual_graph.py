import networkx as nx
import matplotlib.pyplot as plt


def visualize(graph):
    G = nx.Graph(graph)
    nx.draw_networkx(G)
    plt.show()
