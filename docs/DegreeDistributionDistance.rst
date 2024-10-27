DegreeDistributionDistance
===========================

Introduction
------------

The `DegreeDistributionDistance` class is designed to compute the distance between two graphs based on their degree distributions. The degree distribution of a graph is a fundamental property that provides insight into the graph's topology by summarizing the distribution of node connections. This measure is particularly useful in comparing the structural similarities or differences between graphs, which is important in various applications such as social network analysis, biological network comparison, and more.

Formal Definition
-----------------

The degree distribution of a graph is a vector where each entry represents the fraction of nodes that have a specific degree. Formally, if :math:`G` is a graph with :math:`n` nodes, the degree distribution vector :math:`D(G)` is defined as:

.. math::
    D(G) = \left[ \frac{\text{number of nodes with degree } 0}{n}, \frac{\text{number of nodes with degree } 1}{n}, \ldots, \frac{\text{number of nodes with degree } k}{n} \right]

where :math:`k` is the maximum degree in the graph.

Given two graphs :math:`G1` and :math:`G2`, the distance between their degree distributions can be computed using a variety of distance metrics. A common choice is the L1-norm (Manhattan distance) or L2-norm (Euclidean distance) between the degree distribution vectors:

.. math::
    \text{Distance}(G1, G2) = || D(G1) - D(G2) ||

Where :math:`||.||` can be the L1 or L2 norm, depending on the application.

Significance
------------

The degree distribution captures the overall connectivity pattern in a graph. By comparing the degree distributions of two graphs, we can quantify how similar or different their topological structures are. This is particularly important in scenarios where the structure of a network has a direct impact on its function, such as in biological systems where the interaction patterns between proteins can determine cellular behavior, or in social networks where the connectivity patterns influence information spread.

.. code-block:: python

      from distancia import DegreeDistributionDistance

      graph1 = Graph(weighted=True)
      graph1.add_edge("A", "B", 1.0)
      graph1.add_edge("B", "C", 2.0)
      graph1.add_edge("C", "D", 1.5)
      graph1.add_edge("D", "A", 1.0)
      graph1.add_edge("A", "C", 2.0)

      graph2 = Graph(weighted=True)
      graph2.add_edge("A", "B", 1.0)
      graph2.add_edge("B", "C", 1.0)
      
      distance=self.compute(graph1,graph2)
      print(f"Graph DegreeDistributionDistance: {distance}")

.. code-block:: bash

    >>>Graph DegreeDistributionDistance: 1.3333333333333333




Academic Reference
------------------

For a deeper understanding of degree distributions and their importance in graph theory and network analysis, refer to the following academic sources: :footcite:t:`degreedistributiondistance1`: - :footcite:t:`degreedistributiondistance2`:

These papers provide a comprehensive overview of network structure analysis, including the significance of degree distributions.

.. footbibliography::

Conclusion
----------

The `DegreeDistributionDistance` class offers a robust way to compare graphs based on their degree distributions, providing a quantitative measure of structural similarity. This tool is invaluable for researchers and practitioners working in fields that require the comparison and analysis of complex networks. By leveraging this class, users can gain insights into the underlying structure of different graphs and make informed decisions based on their topological characteristics.
