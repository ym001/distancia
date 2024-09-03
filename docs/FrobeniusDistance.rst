FrobeniusDistance
==================

Introduction
------------
The `FrobeniusDistance` class implements a method to measure the similarity between two graphs based on their adjacency matrices. The Frobenius distance is a matrix norm that quantifies the difference between two matrices by computing the square root of the sum of the absolute squares of their elements. When applied to graph adjacency matrices, this distance provides a straightforward way to compare the overall structure of two graphs.

Formal Definition
-----------------
Let \( A_1 \) and \( A_2 \) be the adjacency matrices of two graphs \( G_1 \) and \( G_2 \), respectively. The Frobenius distance \( D_F \) between these two graphs is defined as:

\[
D_F(G_1, G_2) = \|A_1 - A_2\|_F = \sqrt{\sum_{i=1}^{n} \sum_{j=1}^{n} (A_1(i, j) - A_2(i, j))^2}
\]

Where:
- \( A_1(i, j) \) and \( A_2(i, j) \) represent the elements of the adjacency matrices \( A_1 \) and \( A_2 \) at position \( (i, j) \).
- \( \| \cdot \|_F \) denotes the Frobenius norm of a matrix.

This formula essentially sums up the squared differences between corresponding elements in the two adjacency matrices and takes the square root of the result.

Significance
------------
The Frobenius distance is widely used in graph theory and network analysis due to its simplicity and computational efficiency. It captures the overall difference between two graphs by considering all pairwise connections. This distance is particularly useful when comparing graphs of the same size and when the primary concern is the global structure rather than specific substructures or node properties.

The Frobenius distance is applicable in various domains, including:
- **Social network analysis:** Comparing social graphs to detect changes in social structures over time.
- **Biological network analysis:** Assessing similarities between protein-protein interaction networks.
- **Data clustering:** Grouping graphs based on structural similarities.

Example
-------
.. code-block:: python

  from distancia import FrobeniusDistance

  nodes1 = ["A", "B", "C"]
  edges1 = [("A", "B"), ("B", "C")]

  nodes2 = ["A", "B", "C"]
  edges2 = [("A", "B"), ("A", "C")]

  graph1 = Graph(nodes1, edges1)
  graph2 = Graph(nodes2, edges2)

  frobenius_distance = FrobeniusDistance(graph1, graph2)
  distance = frobenius_distance.compute()

  print(f"La distance de Frobenius entre les deux graphes est: {distance}")

.. code-block:: bash

  >>>La distance de Frobenius entre les deux graphes est: 2.0

Academic Reference
------------------


This reference provides a comprehensive treatment of matrix norms, including the Frobenius norm, which underpins the Frobenius distance metric used in this class.

Conclusion
----------
The `FrobeniusDistance` class offers a robust and intuitive method for comparing graphs based on their adjacency matrices. By focusing on the global structural differences between graphs, this distance measure is a valuable tool for a wide range of applications in network analysis and related fields. Its computational simplicity and effectiveness make it a popular choice for graph comparison tasks.
