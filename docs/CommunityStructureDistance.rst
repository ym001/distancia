CommunityStructureDistance
===========================

Introduction
------------
The `CommunityStructureDistance` class provides a method to measure the distance between the community structures of two graphs. Community detection is a fundamental aspect of graph analysis, aimed at uncovering the modular organization within networks. This class utilizes community detection algorithms to compare how nodes are grouped into communities in different graphs.

Idea
----
The primary objective of `CommunityStructureDistance` is to quantify the differences in community structures between two graphs. The distance metric is based on the comparison of detected communities, which are often represented as partitions or sets of nodes. By analyzing these structures, this distance metric can reveal how similar or different the underlying modular organizations of the graphs are.

Formal Definition
-----------------
The distance between the community structures of two graphs \( G_1 \) and \( G_2 \) is computed as follows:

1. **Community Detection**: Apply a community detection algorithm (e.g., Louvain method) to both graphs to identify the communities. Let \( C_1 \) and \( C_2 \) represent the detected communities in \( G_1 \) and \( G_2 \), respectively.

2. **Comparison Metric**: Use a comparison metric (e.g., Jaccard similarity, variation of information) to quantify the dissimilarity between the community structures \( C_1 \) and \( C_2 \).

For example, if \( C_1 \) and \( C_2 \) are partitions of the nodes, the distance can be computed as:
\[ \text{Distance}(G_1, G_2) = \text{ComparisonMetric}(C_1, C_2) \]

Here, `ComparisonMetric` could be a measure like the variation of information (VI) or normalized mutual information (NMI), depending on the specific implementation.

Significance
------------
Understanding the community structure of graphs is essential for various applications, including social network analysis, biological network study, and recommendation systems. The `CommunityStructureDistance` class helps in evaluating how changes in the graph's structure affect its modular organization. This can be particularly useful in scenarios where graphs evolve over time or when comparing different graph-based models.
Example
-------

.. code-block:: python

  import networkx as nx
  from community import community_louvain
      from distancia import CommunityStructureDistance

      graph1 = Graph(weighted=True)
      graph1.add_edge("A", "B", 1.0)
      graph1.add_edge("B", "C", 2.0)
      graph1.add_edge("C", "D", 1.5)
      graph1.add_edge("D", "A", 1.0)
      graph1.add_edge("A", "C", 2.0)

      graph2 = Graph(weighted=True)
      graph2.add_edge("A", "B", 1.0)
      graph2.add_edge("B", "C", 1.0)
      graph2.add_edge("C", "D", 1.0)
      # Compare community structures
      csd = CommunityStructureDistance()
      distance = csd.compute(graph1, graph2)
      print(f"Community structure distance: {distance}")

      # Get detected communities if needed
      communities1, communities2 = csd.get_communities()
      print("Communities in graph 1:", communities1)
      print("Communities in graph 2:", communities2)  

.. code-block:: bash

  Community structure distance: 0.75
  Communities in graph 1: {'B': 0, 'D': 0, 'C': 0, 'A': 0}
  Communities in graph 2: {'B': 1, 'D': 0, 'C': 0, 'A': 1}


Academic Reference
------------------
:footcite:t:`communitystructuredistance`:  
  
This reference describes the Louvain method, a popular algorithm for community detection, which can be used in conjunction with the `CommunityStructureDistance` class.

.. footbibliography::

Conclusion
----------
The `CommunityStructureDistance` class offers a valuable tool for analyzing and comparing community structures across different graphs. By leveraging community detection algorithms and various comparison metrics, it provides insights into the modular characteristics of networks. This distance measure is crucial for understanding structural similarities and differences in complex graph-based systems.

