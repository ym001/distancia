Weisfeiler-Lehman Similarity Class
==================================

Introduction
------------

The Weisfeiler-Lehman Similarity class is a Python implementation for measuring the structural similarity between graphs based on the Weisfeiler-Lehman (WL) isomorphism test. This method is particularly useful in various fields such as social network analysis, chemoinformatics, and machine learning on graphs, where comparing graph structures is essential.

Understanding Weisfeiler-Lehman Similarity
------------------------------------------

The Weisfeiler-Lehman similarity is based on the WL graph isomorphism test, which iteratively refines node labels based on their neighborhoods. The similarity between two graphs is then computed by comparing these refined label sets.

The process works as follows:

1. Initialize node labels (e.g., with degree or a constant).
2. For each iteration:
   a. For each node, aggregate labels of its neighbors.
   b. Hash this aggregated label to create a new label for the node.
3. After a fixed number of iterations, compare the resulting label sets.

The similarity is typically computed as the average Jaccard similarity between the label multisets at each iteration:

.. math::

   Similarity(G1, G2) = \frac{1}{k} \sum_{i=0}^{k-1} \frac{|L_i(G1) \cap L_i(G2)|}{|L_i(G1) \cup L_i(G2)|}

Where:
- k is the number of iterations
- L_i(G) is the multiset of labels for graph G at iteration i

Key properties:
- It's sensitive to structural differences in graphs.
- It can distinguish many (but not all) non-isomorphic graphs.
- It's computationally efficient compared to exact isomorphism tests.

Usage Example
-------------

Here's a basic example of how to use the WeisfeilerLehmanSimilarity class:

.. code-block:: python

  
   import networkx as nx

   from distancia import *

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

.. code-block:: bash

   Weisfeiler-Lehman similarities between graphs:
   Cycle vs Path: 0.3849
   Cycle vs Complete: 0.2500
   Cycle vs Star: 0.2500
   Cycle vs Random1: 0.2500
   Cycle vs Random2: 0.2778
   Is Cycle isomorphic to itself? True
   Path vs Complete: 0.2500
   Path vs Star: 0.3125
   Path vs Random1: 0.2778
   Path vs Random2: 0.2778
   Is Path isomorphic to itself? True
   Complete vs Star: 0.2778
   Complete vs Random1: 0.2778
   Complete vs Random2: 0.2500
   Is Complete isomorphic to itself? True
   Star vs Random1: 0.3403
   Star vs Random2: 0.2500
   Is Star isomorphic to itself? True
   Random1 vs Random2: 0.3571
   Is Random1 isomorphic to itself? True
   Is Random2 isomorphic to itself? True

   Checking for potential isomorphism:
   Are Cycle and Path potentially isomorphic? False
   Are Cycle and Complete potentially isomorphic? False
   Are Cycle and Star potentially isomorphic? False
   Are Cycle and Random1 potentially isomorphic? False
   Are Cycle and Random2 potentially isomorphic? False
   Are Path and Complete potentially isomorphic? False
   Are Path and Star potentially isomorphic? False
   Are Path and Random1 potentially isomorphic? False
   Are Path and Random2 potentially isomorphic? False
   Are Complete and Star potentially isomorphic? False
   Are Complete and Random1 potentially isomorphic? False
   Are Complete and Random2 potentially isomorphic? False
   Are Star and Random1 potentially isomorphic? False
   Are Star and Random2 potentially isomorphic? False
   Are Random1 and Random2 potentially isomorphic? False



This example compares a cycle graph with a path graph, both having 5 nodes. The Weisfeiler-Lehman similarity quantifies how structurally similar these graphs are.

Academic Citations
------------------

When using this implementation in academic work, please cite the following papers:

1. For the original Weisfeiler-Lehman test: :footcite:t:`weisfeilerlehmansimilarity1`



2. For the use of WL in graph kernels and similarity measures:  :footcite:t:`weisfeilerlehmansimilarity2`


.. footbibliography::

Conclusion
----------

The Weisfeiler-Lehman Similarity class provides an efficient and powerful tool for comparing graph structures. Its strengths lie in its ability to capture fine-grained structural similarities and differences between graphs, making it valuable in various applications of network analysis and graph-based machine learning.

Key advantages:
1. Efficient computation, even for large graphs
2. Captures structural similarities beyond simple graph statistics
3. Can be used as a fast approximation for graph isomorphism testing

However, users should be aware of its limitations:
1. Cannot distinguish all non-isomorphic graphs (known as the "WL test's blindness")
2. Sensitive to initial node labeling in some cases
3. May require tuning of the number of iterations for optimal performance

Future work could explore extensions to edge-labeled graphs, adaptations for directed graphs, or combinations with other graph comparison techniques to overcome some of these limitations. Despite these considerations, the Weisfeiler-Lehman similarity remains a fundamental and widely-used method in the field of graph analysis and comparison, offering a good balance between computational efficiency and discriminative power.
