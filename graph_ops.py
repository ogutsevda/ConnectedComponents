import pickle
import random
import networkx as nx
import matplotlib.pyplot as plt


class GraphOps:
    def __init__(self, num_nodes, num_edges, filename):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.filename = filename

    def generate(self):
        G = nx.Graph()
        G.add_nodes_from(range(self.num_nodes))
        G.add_edges_from([(random.randint(0, self.num_nodes), random.randint(0, self.num_nodes))
                              for _ in range(self.num_edges)])

        return G

    @staticmethod
    def visualize(G):
        nx.draw(G, with_labels=True)
        plt.show()


    def save(self, G):
        with open(self.filename, 'wb') as f:
            pickle.dump(G, f)
