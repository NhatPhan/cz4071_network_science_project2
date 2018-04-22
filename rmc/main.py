import networkx as nx
import init_G
import traditional_maxclique
import iscomplement

def main():
    print("Creating Graph \n")
    G = nx.barbell_graph(50, 50)

    print("Printing initialization values through Init algorithm \n")
    x = init_G.init(G)
    print(x)
    print("\n\n")

    print("Printing CompIS algorithm output\n\n")
    x = iscomplement.comp_is(G)
    print(x)
    print("\n\n")

    print("Printing Max Clique\n\n")
    maxclique = traditional_maxclique.traditional_maxclique(G)
    print("maxclique: {}\n".format(maxclique))

    print("Please refer to the source codes to check line by line implementation of the code according to the algo\n")
    print("Also refer to rmc.py to see line by line implementation of overall algorithm")
    print("We were unable to implement 3/8 algorithms from the paper: tciSeed, divSeed, and scSeed")
    print("As a result, could not run RMC in it's entirety, but our implementation closely matches the algorithm in the paper")
    print("_______END____________")

if __name__ == '__main__':
    main()