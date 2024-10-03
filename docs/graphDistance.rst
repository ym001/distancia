Graph Distances in Distancia
============================

Introduction
============
Graphs are fundamental structures used to represent relationships between objects, making them indispensable in fields like computer science, biology, and network analysis. Comparing two graphs is a complex task that can involve structural, topological, and feature-based analysis. The **Distancia** package offers several distance measures tailored for graph comparison, helping users analyze differences in structure, node properties, and overall connectivity.

Categories 
==========

1. **Structural Distances**
2. **Node-Based Distances**
3. **Spectral Distances**

List of Graph Distances
=======================

**Structural Distances**
------------------------

  These distances focus on comparing the overall structure of the graphs, including their connectivity, edge relationships, and graph topology. They help determine how similar or different the structural frameworks of two graphs are.

1. :doc:`GraphEditDistance`

   - Measures the minimum number of operations (additions, deletions, substitutions) needed to transform one graph into another.

2. :doc:`Hamming`

   - Compares two graphs by calculating the number of differing edges between them, providing a simple structural comparison.

3. :doc:`Jaccard`

   - Measures the dissimilarity between two graphs by comparing the sets of edges, using the ratio of the intersection to the union of edges.

**Node-Based Distances**
------------------------

Node-based distances compare graphs by analyzing the properties and relationships of individual nodes. They are particularly useful when you need to compare graphs based on local node attributes or node connections.

1. :doc:`DegreeDistribution`

   - Compares the degree distributions of two graphs, capturing differences in the number of connections per node.

2. :doc:`MatchingDistance`

   - Analyzes the alignment of node labels or node features between two graphs, measuring how well the nodes match.

3. :doc:`GraphletDistribution`

   - Compares small subgraph (graphlet) occurrences within two graphs, capturing local structural similarities.

**Spectral Distances**
----------------------

Spectral distances focus on comparing the eigenvalues or spectral properties of the graphs' adjacency or Laplacian matrices. These measures capture differences in the overall connectivity and flow within the graphs.

1. :doc:`SpectralDistance`

   - Compares the eigenvalues of the adjacency or Laplacian matrices of the two graphs, highlighting differences in graph connectivity and flow.

2. :doc:`HeatKernel`

   - Uses the heat kernel representation of the graph's Laplacian matrix to measure the diffusion of information between nodes, capturing connectivity patterns.

3. :doc:`Resistance`

   - Based on the effective resistance between nodes, this distance measures how difficult it is for information to travel between different parts of the graph.

Conclusion
==========
The variety of graph distance measures provided by **Distancia** allows for comprehensive comparisons across different dimensions of graph structure and properties. Whether you're interested in structural differences, node-level comparisons, or the spectral characteristics of graphs, **Distancia** offers the right tools for a detailed and insightful analysis. These distances are applicable in numerous fields, from social network analysis to biology, offering flexibility and depth in graph comparison tasks.
