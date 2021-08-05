import networkx as nx
import argparse


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--task",
                        type=str,
                        choices=['A', 'B', 'C'],
                        required=True,
                        help="subtask of NetworkX")
    
    return opt


def subtask_a():
    """
    Find the average clustering coefficient of the ring graph with five nodes.
    """
    ring_nodes = [1, 2, 3, 4, 5]
    ring_edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
    G = nx.Graph()
    G.add_nodes_from(ring_nodes)
    G.add_edges_from(ring_edges)
    print("Average clustering coefficient: {}".format(nx.average_clustering(G)))


def subtask_b():
    pass


def subtask_c():
    pass


if __name__ == '__main__':
    opt = get_argument()
    config = vars(opt.parse_args())

    if config['task'] == 'A':
        subtask_a()
    elif config['task'] == 'B':
        subtask_b()
    elif config['task'] == 'C':
        subtask_c()