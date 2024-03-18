import pickle
import random
import numpy as np
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
        G.add_edges_from(
            [
                (random.randint(0, self.num_nodes), random.randint(0, self.num_nodes))
                for _ in range(self.num_edges)
            ]
        )

        return G

    @staticmethod
    def visualize(G, with_labels=False):
        plt.figure(figsize=(20, 16))
        nx.draw(G, with_labels=with_labels, font_size=3, node_size=25)
        plt.show()

    def save(self, G):
        with open(self.filename, "wb") as f:
            pickle.dump(G, f)

    @staticmethod
    def BFS(G):
        all_nodes = set(G.nodes())
        visited_nodes = set()
        comp_dict = dict()
        comp_count_dict = dict()

        comp_count = 0
        while visited_nodes != all_nodes:
            current_neighbors = set()
            visited_neighbors = set()

            non_visited_nodes = all_nodes - visited_nodes
            random_node = random.choice(list(non_visited_nodes))

            visited_neighbors.add(random_node)
            for node in G.neighbors(random_node):
                current_neighbors.add(node)

            while bool(current_neighbors - visited_neighbors):

                neighbors = set()
                for node in current_neighbors - visited_neighbors:
                    neighbors.update(i for i in G.neighbors(node))

                visited_neighbors.update(current_neighbors)
                current_neighbors.update(neighbors)

            comp_count += 1
            comp_dict[f"Connected Component {comp_count}"] = visited_neighbors
            comp_count_dict[f"Connected Component {comp_count}"] = len(
                visited_neighbors
            )
            visited_nodes.update(visited_neighbors)

        print(f"There are {comp_count} connected components in the graph!")
        print(comp_count_dict)

        return comp_dict, comp_count_dict

    @staticmethod
    def visualize_components(G, comp_dict, with_labels=False, save_path=None):
        color_map = [0] * len(G.nodes())
        for key in comp_dict:
            # Very unlikely but the same color can be generated
            # with different connected components (unimportant bug)
            color = tuple(np.random.rand(3))
            idx = list(comp_dict[key])
            for i in idx:
                color_map[i] = color

        plt.figure(figsize=(20, 16))
        nx.draw(
            G, node_color=color_map, with_labels=with_labels, font_size=3, node_size=25
        )

        if save_path:
            plt.savefig(save_path)

        plt.show()
