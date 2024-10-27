Graph Compression Distance
===========================

Introduction
------------

The Graph Compression Distance is a metric that measures the similarity between two graphs based on the principles of information theory. This distance leverages the concept of data compression to quantify the complexity of a graph's structure. By comparing how well two graphs can be compressed, the distance provides insights into their structural similarities and differences. This approach is particularly useful in applications where the complexity of the graph's information content is a critical factor, such as in network analysis, data mining, and bioinformatics.

Formal Definition
-----------------


  Let :math:`G_1` and :math:`G_2` be two graphs. The compression function :math:`C(G)` denotes the size of the graph :math:`G` when compressed using a specific algorithm.

The Graph Compression Distance :math:`D_{compress}` between the graphs :math:`G_1` and :math:`G_2` is defined as:

.. math::

  D_{compress}(G_1, G_2) = \frac{C(G_1 \cup G_2) - \min(C(G_1), C(G_2))}{\max(C(G_1), C(G_2))}

  Where:

  - :math:`C(G_1 \cup G_2)`  represents the size of the compressed union of :math:`G_1` and :math:`G_2`.

  - :math:`\min(C(G_1), C(G_2))` and :math:`\max(C(G_1), C(G_2))` are the minimum and maximum compressed sizes of the individual graphs.

This formula provides a normalized distance metric that reflects how much additional information is needed to describe the union of the two graphs compared to describing each graph individually.

Significance
------------

The Graph Compression Distance is significant because it captures the inherent complexity and informational content of graphs. Unlike traditional graph distance metrics that focus on structural differences, this distance emphasizes the compressibility of the graph data, which is closely related to the amount of redundant or unique information contained within the graphs.

This metric is particularly useful in scenarios where the information content and structural complexity of the graphs are more relevant than simple topological comparisons. For example, in comparing different network models, the Graph Compression Distance can reveal how similar or distinct the informational content of the models is, based on their compressibility.

Example
-------

.. code-block:: python

      from distancia import GraphCompressionDistance

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
      
      distance_calculator = GraphCompressionDistance().compute(graph1, graph2)
      print(f"Graph Compression Distance: {distance_calculator}")
      

.. code-block:: bash

  >>>Graph Compression Distance: 16


Academic Reference
------------------

The concept of using compression-based methods to measure similarity has been explored in various fields, including bioinformatics and data mining. A key reference for this approach is: :footcite:t:`graphcompressiondistance`

.. footbibliography::


This paper introduces the idea of using data compression to cluster data and provides a foundation for applying compression-based metrics to graph comparison.

Conclusion
----------

The Graph Compression Distance offers a unique approach to graph comparison by focusing on the informational content and complexity of the graphs. By leveraging data compression techniques, this metric provides a meaningful way to measure the similarity between graphs in terms of their compressibility. This distance is especially valuable in contexts where the redundancy and uniqueness of information are critical factors, making it a powerful tool for analyzing complex networks and structures.

