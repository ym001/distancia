Pattern-Based Distance
=======================

Introduction
------------

The Pattern-Based Distance is a graph distance metric that compares the frequency of specific motifs or sub-structures between two graphs. In graph theory, motifs are small, recurring, and significant sub-graphs that capture the essence of the graph's topology. This distance metric is particularly useful in domains such as bioinformatics, social network analysis, and chemistry, where the structure and connectivity patterns within graphs are critical.

Formal Definition
-----------------

.. math::

  Given two graphs \( G_1 \) and \( G_2 \), with their respective sets of nodes \( V_1, V_2 \) and edges \( E_1, E_2 \), the Pattern-  Based Distance between \( G_1 \) and \( G_2 \) is defined as:

  \[
  D_{\text{pattern}}(G_1, G_2) = \sum_{m \in M} \left| f_{G_1}(m) - f_{G_2}(m) \right|
  \]

  where:

  - \( M \) is the set of all possible motifs of a given size in the graphs.
  - \( f_{G_1}(m) \) and \( f_{G_2}(m) \) are the frequencies of motif \( m \) in \( G_1 \) and \( G_2 \) respectively.

Significance
------------

The Pattern-Based Distance provides a quantitative measure of the difference in structural motifs between two graphs. This metric is significant because it captures the topological essence of graphs beyond simple node and edge counts. By focusing on motifs, this distance metric allows us to understand the higher-order structure of graphs, which is often critical in applications like:

- **Bioinformatics**: Analyzing protein-protein interaction networks.
- **Social Networks**: Understanding the microstructures in social networks, such as communities or cliques.
- **Chemistry**: Comparing molecular structures where atoms and bonds are represented as nodes and edges, respectively.

.. code-block:: python

  from distancia import PatternBasedDistance

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
      graph2.add_edge("D", "A", 1.0)

      pattern_distance = PatternBasedDistance(max_pattern_size=4)
    
      # Compare all patterns
      distances = pattern_distance.compute(
        graph1, graph2,
        pattern_weights={'cycle': 1.5, 'path': 1.0, 'star': 0.5}
    )
      print("Overall distances:", distances)
    
      # Compare specific pattern type
      cycle_comparison = pattern_distance.compare_specific_patterns(
        graph1, graph2, 'cycle', 4
    )
      print("Cycle pattern comparison:", cycle_comparison)

.. code-block:: bash

  >>>Cycle pattern comparison: {'l1_distance': 0.0, 'l2_distance': 0.0, 'pattern_count_1': 1, 'pattern_count_2': 1}


Academic Reference
------------------

The concept of motif-based distance in graphs is rooted in the broader field of network science and graph theory. One key reference is the work on network motifs by Milo et al. (2002), which identifies and enumerates significant motifs in biological networks:

:footcite:t:`patternbaseddistance`

.. footbibliography::


Conclusion
----------

The Pattern-Based Distance is a powerful tool for comparing graphs based on their internal structure. By focusing on motifs, this distance metric captures the essence of a graph's topology, providing insights that are not available through simpler metrics. Its applications in various scientific fields highlight its versatility and importance. Future work may extend this metric to consider weighted motifs or dynamic graphs, further broadening its applicability.

