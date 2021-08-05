import networkx as nx
import matplotlib.pyplot as plt
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


def subtask_b(node_number):
    """
    Given a complete graph, find the average degree and plot the graph with no label.

    Args:
        node_number ([int]): number of nodes
    """
    G = nx.complete_graph(node_number)

    # calculate average degree
    node_degree = nx.degree(G)
    sum_degree = 0
    for node, degree in node_degree:
        sum_degree += degree

    avg_degree = sum_degree / len(G.nodes)
    print("Average degree: {}".format(avg_degree))

    # plot the graph
    nx.draw(G)
    plt.draw()
    plt.savefig('task_1_b.png')
    plt.close()


def subtask_c(filename):
    """
    Load graph data and:
    1. Model as a directed graph
    2. Get the number of nodes and edges
    3. Get the number of weakly connected component
    4. Plot the top three smallest weakly connected component

    Args:
        filename ([string]): Filename of graph data
    """
    # remove header
    graph_data = open(filename, 'r').read().splitlines()[1:]

    G = nx.read_edgelist(graph_data, delimiter=',', create_using=nx.DiGraph())
    
    wcc = nx.weakly_connected_components(G)
    smallest_wcc = [c for c in sorted(wcc, key=len, reverse=False)]

    print("Number of nodes: {}".format(len(G.nodes)))
    print("Number of edges: {}".format(len(G.edges)))
    print("Number of weakly connected components: {}".format(len(smallest_wcc)))

    # plot the top three smallest wcc
    for i in range(3):
        plt.title('{} Smallest Weakly Connected Components'.format(i+1))
        nx.draw(G.subgraph(smallest_wcc[i]), node_size=12)
        plt.draw()
        plt.savefig('task_1_c_{}.png'.format(i))
        plt.close()


if __name__ == '__main__':
    opt = get_argument()
    config = vars(opt.parse_args())

    if config['task'] == 'A':
        subtask_a()
    elif config['task'] == 'B':
        subtask_b(5)
    elif config['task'] == 'C':
        subtask_c('elliptic_txs_edgelist.csv')