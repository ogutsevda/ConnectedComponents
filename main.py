# Find the connected components in random graphs with the following algorithm:
# -- Start from random node and perform BFS
# -- Label the nodes that BFS visits
# -- If all nodes are visited, the network is connected
# -- Otherwise find an unvisited node and repeat BFS
# NOTE: ChatGPT is not allowed but GitHub Copilot is fine :)

from graph_ops import GraphOps


def main():
    ops = GraphOps(10, 15, "graphs/trial.pkl")
    graph = ops.generate()
    ops.visualize(graph)
    ops.save(graph)

    # TODO 3) write the BFS algorithm
    # TODO 4) find the connected components
    # TODO 5) visualize the connected components


if __name__ == '__main__':
    main()
