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

      from distancia import GraphKernelDistance
      graph1 = Graph(weighted=True)
      graph1.add_edge("A", "B", 1.0)
      graph1.add_edge("B", "C", 2.0)
      graph1.add_edge("C", "A", 1.5)

      graph2 = Graph(weighted=True)
      graph2.add_edge("A", "B", 2.0)
      graph2.add_edge("B", "C", 1.0)
      graph2.add_edge("C", "A", 1.0)

      kernel_distance = GraphKernelDistance()
    
      # Compute single kernel distance
      distance = kernel_distance.compute_kernel_distance(graph1, graph2, 'heat', t=1.0)
      print(f"Heat kernel distance (t=1.0): {distance}")
    
      # Compute multiple kernel distances
      distances = kernel_distance.compute_multiple_kernel_distances(graph1, graph2)
      for name, dist in distances.items():
        print(f"{name}: {dist}")


.. code-block:: bash

      Heat kernel distance (t=1.0): 0.04792663944017091
      heat_kernel_t_1: 0.04792663944017091
      heat_kernel_t_0.1: 0.1739408309945977

Academic References
-------------------

:footcite:t:`graphkerneldistance1`, :footcite:t:`graphkerneldistance2`

.. footbibliography::

Conclusion
----------

The graph kernel distance provides a versatile tool for comparing and clustering graphs. This Python class offers a practical implementation of the concept, allowing users to easily compute kernel distances between graphs. Future work may explore more sophisticated kernel functions, efficient algorithms, and applications in specific domains.
