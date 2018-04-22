import networkx as nx
from networkx.algorithms.approximation import ramsey


def traditional_maxclique(G, name=None):
    # complement
    if name is None:
        name = "complement(%s)" % G.name
    R = G.fresh_copy()
    R.add_nodes_from(G)
    R.add_edges_from(((n, n2)
                      for n, nbrs in G.adjacency()
                      for n2 in G if n2 not in nbrs
                      if n != n2))
    graph = G.copy()
    c_i, i_i = ramsey.ramsey_R2(graph)
    cliques = [c_i]
    isets = [i_i]
    while graph:
        graph.remove_nodes_from(c_i)
        c_i, i_i = ramsey.ramsey_R2(graph)
        if c_i:
            cliques.append(c_i)
        if i_i:
            isets.append(i_i)
    # Determine the largest independent set as measured by cardinality.
    maxiset = max(isets, key=len)
    return maxiset


def traditional_maxclique_algo_1(G):
    def sorting_heuristic(node):
        return G.degree(node)

    def build_candidate_set(G, C):
        clique_nodes = C.nodes()
        graph_nodes = G.nodes()
        common_nodes = set()
        if not clique_nodes:
            return []
        # populate the set of common nodes not already in the clique
        first_node = list(common_nodes)[0]
        for neighbour in G.neighbors(first_node):
            if neighbour not in clique_nodes:
                common_nodes.add(neighbour)

        if not clique_nodes[1:]:
            return list(common_nodes)

        for node in clique_nodes[1:]:
            neighbour_set = set()
            for neighbour in G.neighbors(node):
                if neighbour not in clique_nodes:
                    neighbour_set.add(neighbour)
            common_nodes = common_nodes.intersection(neighbour_set)

        return list(common_nodes)

    def U(G, C, P):
        pass  # implement your U(C,P) here to find the lower bound

    def clique_recursive(G, C, candidate_set, node):
        global Cmax
        C.add_node(node)
        if not candidate_set:
            if C.number_of_nodes() > Cmax.number_of_nodes():
                Cmax = C
        elif U(G, C, candidate_set) > Cmax.number_of_node():
            candidate_set = sorted(candidate_set, key=sorting_heuristic, reverse=True)
            for node in candidate_set:
                clique_recursive(G, C, candidate_set, node)
        return

    lis_nodes = G.nodes()
    sorted_lis_nodes = sorted(lis_nodes, key=sorting_heuristic, reverse=True)
    candidate_set = [node for node in G.nodes() if node != sorted_lis_nodes[0]]
    C = nx.Graph()
    Cmax = nx.Graph()
    for node in candidate_set:
        clique_recursive(G, C, candidate_set, node)


if __name__ == '__main__':
    G = nx.barbell_graph(10, 10)
    max_clique = traditional_maxclique(G)
    print(max_clique)
