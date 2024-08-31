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
   from weisfeiler_lehman_similarity import WeisfeilerLehmanSimilarity

   # Create two sample graphs
   G1 = nx.cycle_graph(5)
   G2 = nx.path_graph(5)

   # Initialize WeisfeilerLehmanSimilarity object
   wl = WeisfeilerLehmanSimilarity(num_iterations=3)

   # Calculate the WL similarity
   similarity = wl.calculate(G1, G2)
   print(f"The Weisfeiler-Lehman similarity between G1 and G2 is: {similarity}")

   # Check if the graphs are potentially isomorphic
   isomorphic = wl.is_isomorphic(G1, G2)
   print(f"Are G1 and G2 potentially isomorphic? {isomorphic}")

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
