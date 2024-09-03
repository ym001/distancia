.. _graph_kernel_distance

Graph Kernel Distance
======================

Introduction
------------

The graph kernel distance is a measure of similarity between two graphs. It quantifies how similar the structural patterns of two graphs are. By computing a kernel, we can measure the degree of shared substructures between the graphs. Graph kernel distances are widely used in various domains, such as cheminformatics, bioinformatics, and social network analysis.

Formal Definition
-----------------

Let G₁ and G₂ be two graphs. The graph kernel distance, K(G₁, G₂), is defined as:

.. math::
   K(G_1, G_2) = \sum_{s \in S} \phi(G_1, s) \cdot \phi(G_2, s)

where:

* S is the set of all possible substructures of a graph (e.g., subgraphs, walks, cycles).
* φ(G, s) is the feature vector representing the presence or frequency of substructure s in graph G.

Intuitive Meaning
-----------------
A higher graph kernel distance indicates that the two graphs share more common structural patterns. Conversely, a lower distance implies that the graphs are less similar. By comparing the kernel values of different pairs of graphs, we can identify groups of similar graphs and potentially discover underlying patterns.

Example
------

.. code-block:: python

   # Example usage
   from distancia import GraphKernelDistance
   edges1 = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
   nodes1 = ["A", "B", "C", "D"]

   edges2 = [("A", "B"), ("B", "C"), ("C", "D")]
   nodes2 = ["A", "B", "C", "D"]

   graph1 = Graph(nodes1, edges1)
   graph2 = Graph(nodes2, edges2)

   kernel_distance = GraphKernelDistance(graph1, graph2)
   distance = kernel_distance.compute(method="random_walk", depth=3)

   print(f"The Graph Kernel Distance between the two graphs is: {distance}")


.. code-block:: bash

   >>>The Graph Kernel Distance between the two graphs is: 0.001949317738791423

Academic References
-------------------

:footcite:t:`graphkerneldistance1`, :footcite:t:`graphkerneldistance2`

.. footbibliography::

Conclusion
----------

The graph kernel distance provides a versatile tool for comparing and clustering graphs. This Python class offers a practical implementation of the concept, allowing users to easily compute kernel distances between graphs. Future work may explore more sophisticated kernel functions, efficient algorithms, and applications in specific domains.
