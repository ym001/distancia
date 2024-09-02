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

   # Exemple d'utilisation
   graph1 = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
   graph2 = {'X': ['Y', 'Z'], 'Y': ['X'], 'Z': ['X']}

   distance = GraphKernelDistance(graph1, graph2)
   random_walk_value = distance.compute_kernel(distance.random_walk_kernel)
   subgraph_value = distance.compute_kernel(distance.subgraph_kernel)

   print("Noyau de marche aléatoire:", random_walk_value)
   print("Noyau de sous-graphes:", subgraph_value)

.. code-block:: bash

Academic References
-------------------


* Gärtner, T., Flach, P., & Wrobel, S. (2003). On graph kernels: Hardness results and efficient alternatives. In *Proceedings of the 16th annual conference on learning theory* (pp. 129-143). Springer.

Implementation
----------------

**[Insert detailed explanation of your Python class here, including:**
* Class structure and attributes
* Methods and their functionalities
* Code examples and usage

**Example:**

```python
class GraphKernel:
    # ... class definition ...

    def compute_kernel(self, graph1, graph2):
        # ... implementation ...
