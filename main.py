from graph_ops import GraphOps


def main():
    ops = GraphOps(20, 15, "graphs/trial.pkl")
    graph = ops.generate()
    ops.visualize(graph)
    ops.save(graph)
    comp_dict = ops.BFS(graph)
    ops.visualize_components(graph, comp_dict)


if __name__ == "__main__":
    main()
