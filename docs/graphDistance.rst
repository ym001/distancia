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

.. _Betweenness Centrality: https://distancia.readthedocs.io/en/latest/BetweennessCentrality.html
.. _K-Core Number: https://distancia.readthedocs.io/en/latest/KCore.html
.. _Degree Centrality: https://distancia.readthedocs.io/en/latest/DegreeCentrality.html
.. _Closeness Centrality: https://distancia.readthedocs.io/en/latest/ClosenessCentrality.html
.. _Betweenness Centrality: https://distancia.readthedocs.io/en/latest/BetweennessCentrality.html
.. _Eigenvector Centrality: https://distancia.readthedocs.io/en/latest/EigenvectorCentrality.html
.. _Katz Centrality: https://distancia.readthedocs.io/en/latest/KatzCentrality.html
.. _PageRank: https://distancia.readthedocs.io/en/latest/PageRankCentrality.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html


Edge-Level Measures
-------------------

These measures assess the importance or characteristics of edges in a graph.

9. `Edge Betweenness`_: Measures the number of shortest paths that pass through an edge.
#. `Edge Weight`_: Represents the strength or capacity of a connection between nodes.

.. _Edge Betweenness: https://distancia.readthedocs.io/en/latest/EdgeBetweenness.html
.. _Edge Weight: https://distancia.readthedocs.io/en/latest/EdgeWeight.html

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

.. _Graph Density: https://distancia.readthedocs.io/en/latest/Graph Density.html
.. _Graph Diameter: https://distancia.readthedocs.io/en/latest/GraphDiameter.html
.. _Average Path Length: https://distancia.readthedocs.io/en/latest/AveragePathLength.html
.. _Clustering Coefficient: https://distancia.readthedocs.io/en/latest/ClusteringCoefficient.html
.. _Graph Assortativity: https://distancia.readthedocs.io/en/latest/GraphAssortativity.html
.. _Global Efficiency: https://distancia.readthedocs.io/en/latest/GlobalEfficiency.html
.. _Modularity: https://distancia.readthedocs.io/en/latest/Modularity.html
.. _GraphKernelDistance: https://distancia.readthedocs.io/en/latest/GraphKernelDistance.html

Community Detection Measures
----------------------------

These measures analyze groups of nodes within a graph.

19. `Community Detection`_: Identifies groups of nodes with dense internal connections and sparse external connections.
#. `Modularity Optimization`_: Quantifies the quality of community assignments.
#. `Modularity Score`_: Quantifies the quality of a graph's division into communities.
#. `Conductance`_: Measures the quality of a community by evaluating the ratio of inter-community edges to intra-community edges.
#. `Normalized Cut`_: Evaluates the separation quality of a graph into subgraphs.

.. _Community Detection: https://distancia.readthedocs.io/en/latest/CommunityDetection.html
.. _Modularity Optimization: https://distancia.readthedocs.io/en/latest/ModularityOptimization.html
.. _Modularity Score: https://distancia.readthedocs.io/en/latest/ModularityScore.html
.. _Conductance: https://distancia.readthedocs.io/en/latest/Conductance.html
.. _Normalized Cut: https://distancia.readthedocs.io/en/latest/NormalizedCut.html

Spectral Measures
-----------------

These measures are based on the eigenvalues and eigenvectors of matrices associated with the graph.

24. `Spectral Radius`_: The largest eigenvalue of the adjacency matrix.
#. `Graph Laplacian`_: Matrix representation used for analyzing graph properties.
#. `Algebraic Connectivity`_: The second smallest eigenvalue of the Laplacian, indicating graph robustness.
#. `SpectralDistance`_

.. _Spectral Radius: https://distancia.readthedocs.io/en/latest/SpectralRadius.html
.. _Graph Laplacian: https://distancia.readthedocs.io/en/latest/GraphLaplacian.html
.. _Algebraic Connectivity: https://distancia.readthedocs.io/en/latest/AlgebraicConnectivity.html
.. _SpectralDistance: https://distancia.readthedocs.io/en/latest/SpectralDistance.html

Dynamic Graph Measures
----------------------

These measures capture properties of evolving graphs over time.

28. `Temporal Reachability`_: Tracks the ability to connect nodes over time-varying edges.
#. `Dynamic Centrality`_: Adaptations of static centrality measures to dynamic networks.
#. `Temporal Clustering Coefficient`_: Evaluates clustering in temporal snapshots.
#. `Edge Persistence`_: Measures the stability of edges over time.

.. _Temporal Reachability: https://distancia.readthedocs.io/en/latest/TemporalReachability.html
.. _Dynamic Centrality: https://distancia.readthedocs.io/en/latest/DynamicCentrality.html
.. _Temporal Clustering Coefficient: https://distancia.readthedocs.io/en/latest/Temporal Clustering Coefficient.html
.. _Edge Persistence: https://distancia.readthedocs.io/en/latest/EdgePersistence.html

Application-Specific Measures
-----------------------------

Measures designed for specific types of graphs or applications.

32. `Shortest Path Length`_: Often used in transportation and communication networks.
#. `Resistance Distance`_: Measures connectivity in electrical networks.
#. `Network Flow`_: Models capacities and bottlenecks in flow-based networks.
#. `Random Walk Centrality`_: Related to the probability of visiting nodes during random walks.

.. _Shortest Path Length: https://distancia.readthedocs.io/en/latest/ShortestPathLength.html

.. _Network Flow: https://distancia.readthedocs.io/en/latest/NetworkFlow.html
.. _Random Walk Centrality: https://distancia.readthedocs.io/en/latest/RandomWalkCentrality.html

Graph-Level Measures
--------------------

36. `Graph Density`_: Proportion of observed edges to possible edges.
#. `Average Clustering Coefficient`_: Measures the likelihood of nodes forming tightly connected groups.
#. `Diameter`_: The longest shortest path between any two nodes in the graph.
#. `Radius`_: The shortest maximum distance from a central node to any other node.
#. `Modularity`_: Quantifies the strength of division of a network into communities.
#. `Assortativity`_: Measures the tendency of nodes to connect to other nodes with similar properties.

.. _Graph Density: https://distancia.readthedocs.io/en/latest/GraphDensity.html
.. _Average Clustering Coefficient: https://distancia.readthedocs.io/en/latest/AverageClusteringCoefficient.html
.. _Diameter: https://distancia.readthedocs.io/en/latest/Diameter.html
.. _Radius: https://distancia.readthedocs.io/en/latest/Radius.html
.. _Modularity: https://distancia.readthedocs.io/en/latest/Modularity.html
.. _Assortativity: https://distancia.readthedocs.io/en/latest/Assortativity.html

Shortest Path Measures
----------------------

42. `Shortest Path Length`_: Calculates the shortest path distance between nodes.
#. `Average Path Length`_: Computes the mean distance between all node pairs.
#. `Eccentricity`_: Measures the greatest distance from a node to all other nodes.
#. `Comparing Random Walk Stationary Distributions`_

.. _Average Path Length: https://distancia.readthedocs.io/en/latest/AveragePathLength.html
.. _Eccentricity: https://distancia.readthedocs.io/en/latest/Eccentricity.html
.. _Comparing Random Walk Stationary Distributions: https://distancia.readthedocs.io/en/latest/ComparingRandomWalkStationaryDistributions.html

Other Specialized Measures
--------------------------

46. `Random Walk Betweenness`_: Measures centrality based on random walk processes.
#. `Resistance Distance`_: Computes the effective electrical resistance between nodes.
#. `Graph Entropy`_: Quantifies the information content of a graph.
#. `Graph Edit Distance`_
#. `WeisfeilerLehmanSimilarity`_
#. `Diffusion`_
#. `FrobeniusDistance`_
#. `PatternBasedDistance`_
#. `GraphCompressionDistance`_

.. _Random Walk Betweenness: https://distancia.readthedocs.io/en/latest/RandomWalkBetweenness.html
.. _Resistance Distance: https://distancia.readthedocs.io/en/latest/Resistance.html
.. _Graph Entropy: https://distancia.readthedocs.io/en/latest/GraphEntropy.html
.. _Graph Edit Distance: https://distancia.readthedocs.io/en/latest/GraphEditDistance.html
.. _WeisfeilerLehmanSimilarity: https://distancia.readthedocs.io/en/latest/WeisfeilerLehmanSimilarity.html
.. _Diffusion: https://distancia.readthedocs.io/en/latest/Diffusion.html
.. _FrobeniusDistance: https://distancia.readthedocs.io/en/latest/FrobeniusDistance.html
.. _PatternBasedDistance: https://distancia.readthedocs.io/en/latest/PatternBasedDistance.html
.. _GraphCompressionDistance: https://distancia.readthedocs.io/en/latest/GraphCompressionDistance.html

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

