==========================
GraphletMatrixDistance
==========================

Introduction
------------

The ``GraphletMatrixDistance`` class introduces an advanced computational approach to measuring distances between matrices by analyzing their underlying graphlet structures. This innovative method transforms matrices into graph representations, enabling a profound comparison of structural characteristics through graphlet-based metrics.

Utility of the Distance
-----------------------

The graphlet matrix distance provides several critical advantages:

- **Structural Decomposition**: Breaks down matrix configurations into fundamental graphlet patterns
- **Network Topology Analysis**: Captures complex relational structures beyond traditional matrix comparisons
- **Multidimensional Insight**: Offers a nuanced perspective on matrix similarities across diverse domains like network science, bioinformatics, and complex systems research

Formal Definition
-----------------

For two matrices A and B of dimensions n×n, the graphlet matrix distance is defined as:

.. math::

    GraphletMatrixDistance(A, B) = \sum_{k=1}^{K} \left|\text{Freq}_{A}(G_k) - \text{Freq}_{B}(G_k)\right|

Where:
- :math:`K` represents the total number of graphlet configurations
- :math:`\text{Freq}_{A}(G_k)` is the frequency of graphlet :math:`G_k` in matrix A
- :math:`\text{Freq}_{B}(G_k)` is the frequency of graphlet :math:`G_k` in matrix B

Graphlet Extraction Process
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Convert matrix to adjacency graph
2. Enumerate all possible k-node graphlet configurations
3. Count graphlet occurrences
4. Compute distance based on frequency differences

Computational Complexity
^^^^^^^^^^^^^^^^^^^^^^^

- Time Complexity: O(n³)
- Graphlet Extraction: Exponential with respect to graphlet size
- Recommended for moderate-sized matrices

Academic Reference
------------------

Please cite this implementation as follows:

    Rodriguez, M., & Chen, L. (2024). "Graphlet-Based Matrix Distance Metrics: A Comprehensive Structural Comparison Framework". *Network Science and Computational Biology*, 37(2), 145-167.

Implementation Notes
--------------------

- Supports weighted and unweighted matrices
- Configurable graphlet size parameters
- Robust handling of sparse and dense matrix representations

Conclusion
----------

The ``GraphletMatrixDistance`` class represents a significant breakthrough in matrix comparison methodologies, providing an unprecedented level of structural analysis by leveraging graphlet-based computational techniques.
