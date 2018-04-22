import networkx as nx


def init(G):
    """
    Algorithm 2 that initializes the key variables for the RMC algorithm
    Checks if the input graph is already not a maximum clique
    If so, returns the max cliqu

    This is a line by line implementation of the algorithm in the paper
    :param G:
    :return: r, wc_min, wc_max, and the initial max_clique
    """
    lis_nodes = G.nodes()
    wc_min = 0
    max_core_number = -100
    core_number_dict = nx.core_number(G)
    for k, v in core_number_dict.items():
        if v > max_core_number:
            max_core_number = v
            print(max_core_number)

    wc_max = max_core_number + 1
    max_core = nx.k_core(G, max_core_number)

    # check if max-core is a clique
    num_nodes = len(max_core.nodes())
    num_edges = max_core.number_of_edges()
    if num_edges == (num_nodes * (num_nodes - 1)) // 2:
        print("max_core is a clique, hence must be maximum clique")
        print("returning maximum clique")
        wc_min = num_nodes
        wc_max = num_nodes + 1
        return (1, wc_min, wc_max, max_core)

    for k, v in core_number_dict.items():
        if v > wc_max:
            # find the maximal clique containing that node
            cliques = nx.cliques_containing_node(G, k)
            node_maximal_clique = max(cliques, key=lambda clique: clique.number_of_nodes())
            if node_maximal_clique.number_of_nodes() > wc_min:
                cmax = node_maximal_clique
                wc_min = cmax.number_of_nodes()
    if wc_min == wc_max:
        return 1, wc_min, wc_max, max_core
    d = nx.coloring.greedy_color(G, strategy='largest_first')  # color number of graph through graph coloring - line 12
    color_set = set()
    for _, v in d.items():
        color_set.add(v)
    cn = len(color_set)
    if wc_max > cn:
        wc_max = cn
    if wc_max == wc_min:
        return 1, wc_min, wc_max, max_core
    return 0, wc_min, wc_max, max_core


if __name__ == '__main__':
    G = nx.barbell_graph(10, 15)
    return_tuple = init(G)
    print(return_tuple)
