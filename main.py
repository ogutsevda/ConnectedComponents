import os
import torch
from torch_geometric.utils.convert import to_networkx
from graph_ops import GraphOps


def main():
    # === Example usage of GraphOps ===
    # ops = GraphOps(700, 600, "graphs/trial.pkl")
    # graph = ops.generate()
    # ops.visualize(graph)
    # ops.save(graph)
    # comp_dict = ops.BFS(graph)
    # ops.visualize_components(graph, comp_dict)

    # === Example usage of GraphOps with real data ===
    slides_list = [
        "2F1",
        "1E1",
        "1Q1",
        "1S1",
        "1Z2",
        "2B1",
        "2B2",
        "2C1",
        "2G1",
        "2H1",
        "2J1",
        "2R1",
        "2T2",
        "2U2",
        "2V1",
        "3A1",
        "3K1",
        "3N1",
        "3O1",
        "3P1",
        "1C1",
        "1C5",
        "1J1",
        "1J2",
        "1N1",
        "1O1",
        "1O2",
        "1P1",
        "1R1",
        "1R2",
        "1Y1",
        "2A1",
        "2Y1",
        "3H1",
        "4A1",
        "4B1",
        "4I1",
        "4Q1",
        "1D1",
        "1F1",
        "1G1",
        "1I1",
        "1L1",
        "1M1",
        "1U1",
        "1V2",
        "1W1",
        "1X3",
        "2D1",
        "2D2",
        "2E1",
        "2K3",
        "2L1",
        "2M1",
        "2N1",
        "2N2",
        "2O1",
        "2Q1",
        "2S1",
        "2U1",
        "2W1",
        "2X1",
        "2Z1",
        "3B1",
        "3E1",
        "3I1",
        "3J1",
        "4E1",
        "4G1",
        "4H1",
        "4J1",
        "4K1",
        "4L1",
        "4N1",
        "4P1",
    ]
    for slide_id in slides_list:
        data_path = os.path.join(
            os.getcwd(),
            f"../project_data/gnn_data_2/data_downstream/with_lymph/border/raw/{slide_id}.pt",
        )
        data = torch.load(data_path)
        graph = to_networkx(data, to_undirected=True)
        save_path = os.path.join(
            os.getcwd(),
            f"../../../Desktop/deepMEL-SSL-backup/connected_components/{slide_id}.png",
        )
        print(f"Slide ID: {slide_id}")
        ops = GraphOps(graph.number_of_nodes(), graph.number_of_edges(), None)
        comp_dict, comp_count_dict = ops.BFS(graph)
        ops.visualize_components(graph, comp_dict, save_path=save_path)


if __name__ == "__main__":
    main()
