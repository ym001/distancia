Frobenius
=========

Introduction
------------
The `FrobeniusDistance` class implements a method to measure the similarity between two graphs based on their adjacency matrices. The Frobenius distance is a matrix norm that quantifies the difference between two matrices by computing the square root of the sum of the absolute squares of their elements. When applied to graph adjacency matrices, this distance provides a straightforward way to compare the overall structure of two graphs.

Formal Definition
-----------------
 

Let :math:`A_1` and :math:`A_2` be the adjacency matrices of two graphs :math:`G_1` and :math:`G_2`, respectively. The Frobenius distance :math:`D_F` between these two graphs is defined as:

.. math::

  D_F(G_1, G_2) = \|A_1 - A_2\|_F = \sqrt{\sum_{i=1}^{n} \sum_{j=1}^{n} (A_1(i, j) - A_2(i, j))^2}


Where:
- :math:`A_1(i, j)` and :math:`A_2(i, j)` represent the elements of the adjacency matrices :math:`A_1` and :math:`A_2` at position :math:`(i, j)`.
- :math:`\| \cdot \|_F` denotes the Frobenius norm of a matrix.

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

      from distancia import FrobeniusDistance, Graph

      """
      Test the Frobenius distance calculation between graphs
      """
      # Test 1: Identical graphs
      print("Test 1: Identical graphs")
      g1 = Graph(weighted=True)
      g1.add_edge('A', 'B', 1.0)
      g1.add_edge('B', 'C', 2.0)
    
      g2 = Graph(weighted=True)
      g2.add_edge('A', 'B', 1.0)
      g2.add_edge('B', 'C', 2.0)
    
      distance = FrobeniusDistance().compute(g1,g2)
      print(f"Distance between identical graphs: {distance}")  # Should be 0.0
    
      # Test 2: Different edge weights
      print("\nTest 2: Different edge weights")
      g3 = Graph(weighted=True)
      g3.add_edge('A', 'B', 2.0)
      g3.add_edge('B', 'C', 3.0)
    
      distance = FrobeniusDistance().compute(g1,g3)
      print(f"Distance between graphs with different weights: {distance}")
    
      # Test 3: Different structure
      print("\nTest 3: Different structure")
      g4 = Graph(weighted=True)
      g4.add_edge('A', 'B', 1.0)
      g4.add_edge('B', 'C', 2.0)
      g4.add_edge('A', 'C', 1.5)  # Additional edge
    
      g1.add_node('C')  # Ensure both graphs have same nodes
      distance = FrobeniusDistance().compute(g1,g4)
      print(f"Distance between graphs with different structure: {distance}")


.. code-block:: bash

  >>>Test 1: Identical graphs
  >>>Distance between identical graphs: 0.0

  >>>Test 2: Different edge weights
  >>>Distance between graphs with different weights: 2.0

  >>>Test 3: Different structure
  >>>Distance between graphs with different structure: 2.1213203435596424


Academic Reference
------------------

:footcite:t:`frobeniusdistance`

.. footbibliography::

This reference provides a comprehensive treatment of matrix norms, including the Frobenius norm, which underpins the Frobenius distance metric used in this class.

Conclusion
----------
The `FrobeniusDistance` class offers a robust and intuitive method for comparing graphs based on their adjacency matrices. By focusing on the global structural differences between graphs, this distance measure is a valuable tool for a wide range of applications in network analysis and related fields. Its computational simplicity and effectiveness make it a popular choice for graph comparison tasks.
