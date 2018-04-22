import networkx as nx
import heapq


def comp_is(G):
    """
    Line by line implementation of Algorithm 7 called CompIS
    :param G:
    :return: Candidate set P, and the Independent Set I
    """
    # lines 1-3 initial setup
    P = set()
    I = set()
    min_heap = []
    node_degree_dict = dict()
    for node in G.nodes():
        node_degree_dict[node] = G.degree(node)
    for node, degree in node_degree_dict.items():
        heapq.heappush(min_heap, (node, degree)) # line2 of algorithm
    t = True
    state = dict()
    for node in G.nodes:
        state[node] = 0
    # line 4 of the algorithm
    while min_heap:
        v = heapq.heappop(min_heap)[0] # line 5
        if state[v] == 0:
            state[v] = 1
            I.add(v)
            if node_degree_dict[v] > 1:
                t = False
            if t:
                P.add(v)
            for u in G.neighbors(v):
                if state[u] == 0:
                    state[u] = 1
                    for w in G.neighbors(u):
                        if state[w] == 0:
                            node_degree_dict[w] -= 1
    return P,I

if __name__ == '__main__':

    G = nx.barbell_graph(10, 130)
    P_I = comp_is(G)
    print(P_I)
