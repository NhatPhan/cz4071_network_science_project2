import networkx as nx
import iscomplement
import init_G
import traditional_maxclique
import tciSeed
import scSeed
import divSeed
THETA = 0


def rmc(G):
    """
    This is the overall algorithm of the paper
    unfortunately, we were unable to complete the tciSeed, scSeed, and divSeed algorithms
    We were able to complete all other algorithms
    You can run these algorithms by using:
        python filename.py
    Each algo has it's own if __name__ == 'main' section that will execute on the above command
    :param G:
    :return: maxclique
    """
    r, wc_min, wc_max, maxclique = init_G.init(G)
    if r == 1:
        return maxclique
    S = None

    while wc_max - wc_min > THETA:
        wt = (wc_min + wc_max) // 2
        wp_max = wc_max
        wp_min = wc_min
        (wc_min, wc_max, maxclique, S) = scSeed.scSeed(G, wt)
        # case statements
        if not S:
            if wc_min >= wt:
                return maxclique
            else:
                wc_max = wt - 1
        else:
            wc_min, wc_max, maxclique, S = tciSeed.tci_seed(G, S, wt)
            if not S:
                if wc_min >= wt:
                    return maxclique
                elif wc_min < wt:
                    wc_max = wt - 1
                elif (wc_min == wp_min) and (wc_max == wp_max):
                    break

    wt = wc_min + 1
    (wc_min, wc_max, maxclique, S) = scSeed.scSeed(G, wt)
    if not S:
        return maxclique
    (wc_min, wc_max, maxclique, S) = tciSeed.tci_seed(G, S, wc_min + 1)
    while S:
        (wc_min, wc_max, maxclique, S) = divSeed.divSeed(G, S, wc_min + 1)
    return  maxclique

