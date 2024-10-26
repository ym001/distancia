
import networkx as nx
from ../distancia/graphDistance import WeisfeilerLehmanSimilarity

def create_sample_graphs():
    # Create a cycle graph
    C5 = nx.cycle_graph(5)
    
    # Create a path graph
    P5 = nx.path_graph(5)
    
    # Create a complete graph
    K5 = nx.complete_graph(5)
    
    # Create a star graph
    S5 = nx.star_graph(4)
    
    # Create two random graphs
    G1 = nx.gnm_random_graph(5, 7)
    G2 = nx.gnm_random_graph(5, 7)
    
    return C5, P5, K5, S5, G1, G2

def compare_graphs(graphs, names):
    # Initialize WeisfeilerLehmanSimilarity object
    wl = WeisfeilerLehmanSimilarity(num_iterations=3)
    
    print("Weisfeiler-Lehman similarities between graphs:")
    for i, (G1, name1) in enumerate(zip(graphs, names)):
        for j, (G2, name2) in enumerate(zip(graphs[i+1:], names[i+1:])):
            similarity = wl.calculate(G1, G2)
            print(f"{name1} vs {name2}: {similarity:.4f}")
            
        # Check for potential isomorphism with itself (should always be true)
        is_iso = wl.is_isomorphic(G1, G1)
        print(f"Is {name1} isomorphic to itself? {is_iso}")
    
    # Check for potential isomorphism between different graphs
    print("\nChecking for potential isomorphism:")
    for i, (G1, name1) in enumerate(zip(graphs, names)):
        for j, (G2, name2) in enumerate(zip(graphs[i+1:], names[i+1:])):
            is_iso = wl.is_isomorphic(G1, G2)
            print(f"Are {name1} and {name2} potentially isomorphic? {is_iso}")

def main():
    # Create sample graphs
    C5, P5, K5, S5, G1, G2 = create_sample_graphs()
    graph_names = ["Cycle", "Path", "Complete", "Star", "Random1", "Random2"]
    
    # Compare the graphs
    compare_graphs([C5, P5, K5, S5, G1, G2], graph_names)

if __name__ == "__main__":
    main()
