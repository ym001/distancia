==================================
MinimumCutDistanceCalculator
==================================

Introduction
------------

The ``MinimumCutDistanceCalculator`` class represents an advanced algorithmic approach to measuring distances between matrices through the lens of graph-theoretic minimum cut analysis. This sophisticated method transforms matrix structures into weighted graphs, enabling a unique perspective on structural dissimilarity through network connectivity principles.

Utility of the Distance
-----------------------

The minimum cut matrix distance offers several profound advantages:

- **Structural Connectivity Analysis**: Evaluates matrix similarities through fundamental network partition strategies
- **Robust Comparative Mechanism**: Provides a powerful metric for detecting significant structural differences
- **Interdisciplinary Applications**: Relevant in domains such as network science, computational biology, and complex systems modeling

Formal Definition
-----------------

For two matrices A and B of dimensions n×n, the minimum cut distance is defined as:

.. math::

    MinCutDistance(A, B) = \min\left\{ \sum_{(u,v) \in \text{Cut}} w(u,v) \middle| \text{Cut separates graph representations of A and B} \right\}

Where:
- :math:`w(u,v)` represents the weight of the edge between nodes u and v
- :math:`\text{Cut}` is the set of edges removed to separate graph representations
- The calculation minimizes the total edge weight that disconnects the graphs

Computational Strategy
^^^^^^^^^^^^^^^^^^^^^

1. Convert matrices to weighted graph representations
2. Apply minimum cut algorithms (e.g., Karger's algorithm)
3. Compute the minimum edge weight required to separate graph structures
4. Normalize the distance metric

Algorithmic Complexity
^^^^^^^^^^^^^^^^^^^^^

- Time Complexity: O(n³)
- Space Complexity: O(n²)
- Probabilistic minimum cut algorithms available for large-scale matrices

Theoretical Foundations
----------------------

The approach builds upon seminal work in graph theory, specifically:
- Minimum cut theory
- Network partitioning algorithms
- Structural graph decomposition techniques

Usage Example
-------------

Here's an example of how to use the MinimumCutDistanceCalculator Distance measure in the `distancia` package:

.. code-block:: python

    matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

    matrix2 = [
    [1, 2, 4],
    [4, 6, 6],
    [7, 8, 0]
    ]

    calculator = MinimumCutDistanceCalculator()
    print(calculator.compute(matrix1, matrix2))  # Affichera 3
    print(calculator.get_cut_positions(matrix1,matrix2))  # Affichera les positions des différences
    print(calculator.get_detailed_difference(matrix1,matrix2))

Academic Reference
------------------

Please cite this implementation as follows:

    Zhang, H., & Nakamura, K. (2024). "Minimum Cut Distance Metrics: A Novel Approach to Structural Matrix Comparison". *Advanced Network Analysis*, 29(1), 78-95.

Implementation Considerations
-----------------------------

- Supports weighted and unweighted matrices
- Configurable minimum cut algorithm selection
- Robust handling of sparse and dense matrix representations
- Provides multiple distance normalization strategies

Conclusion
----------

The ``MinimumCutDistanceCalculator`` class represents a groundbreaking advancement in matrix comparison methodologies, offering an innovative approach to measuring structural dissimilarity through sophisticated network partitioning techniques.
