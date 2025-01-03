Graph Distances
===============

Introduction
============
Graphs are fundamental structures used to represent relationships between objects, making them indispensable in fields like computer science, biology, and network analysis. Comparing two graphs is a complex task that can involve structural, topological, and feature-based analysis. The **Distancia** package offers several distance measures tailored for graph comparison, helping users analyze differences in structure, node properties, and overall connectivity.

Graph Measures
===============

This section provides a comprehensive list of graph measures supported by our package. These measures are grouped into categories to aid understanding and selection based on specific graph analysis tasks.

Node-Level Measures
-------------------

These measures describe the importance, influence, or role of individual nodes within the graph.

#. `Betweenness Centrality`_: Measures how often a node acts as a bridge along the shortest path between two other nodes.
#. `K-Core Number`_: Indicates the largest subgraph in which all nodes have at least \(k\) neighbors.
#. `Degree Centrality`_: Measures the number of edges connected to a node.
#. `Closeness Centrality`_: Evaluates how close a node is to all other nodes in the graph.
#. `Betweenness Centrality`_: Quantifies the number of times a node acts as a bridge along the shortest path between two other nodes.
#. `Eigenvector Centrality`_: Indicates the influence of a node in a network based on its connections to other high-scoring nodes.
#. `Katz Centrality`_: A variant of eigenvector centrality that incorporates a damping factor.
#. `PageRank`_: A probabilistic algorithm to measure the importance of nodes.

Edge-Level Measures
-------------------

These measures assess the importance or characteristics of edges in a graph.

9. `Edge Betweenness`_: Measures the number of shortest paths that pass through an edge.
#. `Edge Weight`_: Represents the strength or capacity of a connection between nodes.


Global Graph Measures
---------------------

These measures provide insights into the overall structure and properties of a graph.

11. `Graph Density`_: Ratio of actual edges to the maximum possible edges in the graph.
#. `Graph Diameter`_: The longest shortest path between any two nodes in the graph.
#. `Average Path Length`_: The mean of all shortest paths in the graph.
#. `Clustering Coefficient`_: Measures the degree to which nodes in a graph tend to cluster together.
#. `Graph Assortativity`_: Indicates the tendency of nodes to connect with similar nodes.
#. `Global Efficiency`_: Measures how efficiently information is exchanged over the graph.
#. `Modularity`_: Quantifies the strength of division of a graph into modules or communities.
#. `GraphKernelDistance`_

Community Detection Measures
----------------------------

These measures analyze groups of nodes within a graph.

19. `Community Detection`_: Identifies groups of nodes with dense internal connections and sparse external connections.
#. `Modularity Optimization`_: Quantifies the quality of community assignments.
#. `Modularity Score`_: Quantifies the quality of a graph's division into communities.
#. `Conductance`_: Measures the quality of a community by evaluating the ratio of inter-community edges to intra-community edges.
#. `Normalized Cut`_: Evaluates the separation quality of a graph into subgraphs.

Spectral Measures
-----------------

These measures are based on the eigenvalues and eigenvectors of matrices associated with the graph.

24. `Spectral Radius`_: The largest eigenvalue of the adjacency matrix.
#. `Graph Laplacian`_: Matrix representation used for analyzing graph properties.
#. `Algebraic Connectivity`_: The second smallest eigenvalue of the Laplacian, indicating graph robustness.
#. `SpectralDistance`_

Dynamic Graph Measures
----------------------

These measures capture properties of evolving graphs over time.

28. `Temporal Reachability`_: Tracks the ability to connect nodes over time-varying edges.
#. `Dynamic Centrality`_: Adaptations of static centrality measures to dynamic networks.
#. `Temporal Clustering Coefficient`_: Evaluates clustering in temporal snapshots.
#. `Edge Persistence`_: Measures the stability of edges over time.

Application-Specific Measures
-----------------------------

Measures designed for specific types of graphs or applications.

32. `Shortest Path Length`_: Often used in transportation and communication networks.
#. `Resistance Distance`_: Measures connectivity in electrical networks.
#. `Network Flow`_: Models capacities and bottlenecks in flow-based networks.
#. `Random Walk Centrality`_: Related to the probability of visiting nodes during random walks.

Graph-Level Measures
--------------------

36. `Graph Density`_: Proportion of observed edges to possible edges.
#. `Average Clustering Coefficient`_: Measures the likelihood of nodes forming tightly connected groups.
#. `Diameter`_: The longest shortest path between any two nodes in the graph.
#. `Radius`_: The shortest maximum distance from a central node to any other node.
#. `Modularity`_: Quantifies the strength of division of a network into communities.
#. `Assortativity`_: Measures the tendency of nodes to connect to other nodes with similar properties.

Shortest Path Measures
----------------------

42. `Shortest Path Length`_: Calculates the shortest path distance between nodes.
#. `Average Path Length`_: Computes the mean distance between all node pairs.
#. `Eccentricity`_: Measures the greatest distance from a node to all other nodes.
#. `ComparingRandomWalkStationaryDistributions`_

Other Specialized Measures
--------------------------

46. `Random Walk Betweenness`_: Measures centrality based on random walk processes.
#. `Resistance Distance`_: Computes the effective electrical resistance between nodes.
#. `Graph Entropy`_: Quantifies the information content of a graph.
#. `GraphEditDistance`_
#. `WeisfeilerLehmanSimilarity`_
#. `Diffusion`_
#. `FrobeniusDistance`_
#. `PatternBasedDistance`_
#. `GraphCompressionDistance`_

Conclusion
==========
The variety of graph distance measures provided by **Distancia** allows for comprehensive comparisons across different dimensions of graph structure and properties. Whether you're interested in structural differences, node-level comparisons, or the spectral characteristics of graphs, **Distancia** offers the right tools for a detailed and insightful analysis. These distances are applicable in numerous fields, from social network analysis to biology, offering flexibility and depth in graph comparison tasks.

.. _Shortest Path Length: https://distancia.readthedocs.io/en/latest/ShortestPath.html
.. _GraphEditDistance: https://distancia.readthedocs.io/en/latest/GraphEditDistance.html
.. _SpectralDistance: https://distancia.readthedocs.io/en/latest/SpectralDistance.html
.. _WeisfeilerLehmanSimilarity: https://distancia.readthedocs.io/en/latest/WeisfeilerLehmanSimilarity.html
.. _ComparingRandomWalkStationaryDistributions: https://distancia.readthedocs.io/en/latest/ComparingRandomWalkStationaryDistributions.html
.. _Diffusion: https://distancia.readthedocs.io/en/latest/Diffusion.html
.. _FrobeniusDistance: https://distancia.readthedocs.io/en/latest/FrobeniusDistance.html
.. _GraphKernelDistance: https://distancia.readthedocs.io/en/latest/GraphKernelDistance.html
.. _PatternBasedDistance: https://distancia.readthedocs.io/en/latest/PatternBasedDistance.html
.. _GraphCompressionDistance: https://distancia.readthedocs.io/en/latest/GraphCompressionDistance.html
.. _Degree Centrality: https://distancia.readthedocs.io/en/latest/DegreeDistributionDistance.html
.. _Community Detection: https://distancia.readthedocs.io/en/latest/CommunityStructureDistance.html

