=======================
Diffusion Distance Class
=======================

Introduction
============

The `DiffusionDistance` class is a Python implementation for comparing diffusion processes on graphs. Diffusion processes are a type of random walk where the walker can split and visit multiple nodes at each step, simulating the spread of information or influence through a network.

This class provides methods to compute and compare the diffusion processes on two different graphs, allowing researchers and data analysts to quantify the structural differences between the graphs based on their diffusion characteristics.

Mathematical Formulation of Diffusion Distance
==============================================

Let :math:`G1 = (V1, E1)` and :math:`G2 = (V2, E2)` be the two graphs being compared, where :math:`V` represents the set of nodes and :math:`E` represents the set of edges. The diffusion process on a graph :math:`G` starting from a source node :math:`s` and running for :math:`t` steps can be represented as a vector :math:`D(G, s, t)`, where :math:`D(G, s, t)[v]` represents the diffusion value at node :math:`v` after :math:`t` steps.

The Diffusion Distance between the two graphs :math:`G1` and :math:`G2` with respect to a source node :math:`s` and a number of steps :math:`t` can then be defined as:

.. math::

   d_{Diffusion}(G1, G2, s, t) = \|D(G1, s, t) - D(G2, s, t)\|_p

Where :math:`\|.\|_p` represents the L_p norm, and the most common choices are the L1 norm (Manhattan distance) and the L2 norm (Euclidean distance).

Sample
======
.. code-block:: python

      from distancia import DiffusionDistance

      graph1 = Graph(weighted=True)
      graph1.add_edge("A", "B", 1.0)
      graph1.add_edge("B", "C", 2.0)
      graph1.add_edge("C", "A", 1.5)

      graph2 = Graph(directed=False, weighted=True)
      graph2.add_edge("A", "B", 2.0)
      graph2.add_edge("B", "C", 1.0)
      graph2.add_edge("C", "D", 1.0)
      graph2.add_edge("D", "E", 1.0)

      comparator = DiffusionDistance()
    
      # Compare basic properties
      results = comparator.compare_graphs(graph1, graph2)
      print("Graph comparison results:", results)
    
      # Compare diffusion processes
      start_nodes = {"A"}
      diffusion_results = comparator.compare_diffusion_processes(
        graph1, graph2, start_nodes, steps=5, num_simulations=10
    )
      print("Diffusion comparison results:", diffusion_results)

.. code-block:: bash

   Graph comparison results: {'stationary_distance': 0.7999999999999999, 'hitting_time_distance': 2.3333333333333335, 'kernel_distance': 7.49216390608629e-11}
   Diffusion comparison results: {'average_difference': 1.1999999999999997, 'max_difference': 1.2, 'min_difference': 1.2}


=============================

The diffusion distance between two graphs measures the structural differences between the graphs in terms of how information or influence spreads through the network. A small diffusion distance indicates that the two graphs have similar diffusion characteristics, while a large diffusion distance implies that the graphs have very different patterns of information propagation.

This metric can be useful in a variety of applications, such as:

- Comparing the influence dynamics of different social networks
- Analyzing the spread of information or disease in different transportation or communication networks
- Quantifying the structural similarity of biological networks, such as neural networks or protein-protein interaction networks

Academic References
===================
::footcite:t:`diffusion1`,:footcite:t:`diffusion1`

.. footbibliography::



Conclusion
==========

The `DiffusionDistance` class provides a powerful tool for comparing the structural properties of graphs based on their diffusion characteristics. By quantifying the differences in how information or influence spreads through the networks, researchers and analysts can gain valuable insights into the underlying processes governing the graphs.

This class can be easily integrated into larger graph analysis frameworks or used as a standalone component for specialized applications. Future work could involve extending the class to handle directed, weighted, or time-varying graphs, as well as exploring more advanced diffusion models and distance metrics.
