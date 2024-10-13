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

   import networkx as nx
   from distancia import DiffusionDistance

   # Créer deux graphes
   G1 = nx.erdos_renyi_graph(10, 0.3, seed=42)
   G2 = nx.erdos_renyi_graph(10, 0.35, seed=42)
   steps = 5

   # Initialiser l'objet DiffusionDistance
   diffusion_distance = DiffusionDistance(steps)

   # Comparer les processus de diffusion
   source_node = 0
   l1_distance = diffusion_distance.compute(G1, G2,source_node)
   diffusion_distance = DiffusionDistance(steps,metric='l2')

   l2_distance = diffusion_distance.compute(G1, G2,source_node)

   print(f"L1 distance between diffusion processes: {l1_distance:.4f}")
   print(f"L2 distance between diffusion processes: {l2_distance:.4f}")

.. code-block:: bash

   >>>L1 distance between diffusion processes: 557124462311584.2500
   >>>L2 distance between diffusion processes: 186791387234450.2188

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
