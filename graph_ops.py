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
        G.add_edges_from(
            [
                (random.randint(0, self.num_nodes), random.randint(0, self.num_nodes))
                for _ in range(self.num_edges)
            ]
        )

        return G

    @staticmethod
    def visualize(G):
        nx.draw(G, with_labels=True)
        plt.show()

    def save(self, G):
        with open(self.filename, "wb") as f:
            pickle.dump(G, f)

    def BFS(self, G):
        all_nodes = set(G.nodes())
        visited_nodes = set()
        comp_dict = dict()

        comp_count = 0
        while visited_nodes != all_nodes:
            current_neighbors = set()
            visited = set()

            non_visited_nodes = all_nodes - visited_nodes
            random_node = random.choice(list(non_visited_nodes))

            visited.add(random_node)
            for node in G.neighbors(random_node):
                current_neighbors.add(node)

            while bool(current_neighbors - visited):
                visited.update(current_neighbors)
                neighbors = set()

                for node in current_neighbors:
                    neighbors.update(i for i in G.neighbors(node))
                current_neighbors.update(neighbors)

            comp_count += 1
            comp_dict[f"Connected Component {comp_count}"] = visited
            visited_nodes.update(visited)

        return comp_dict
