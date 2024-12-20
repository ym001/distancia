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
- **Degree Centrality**: Measures the number of edges connected to a node.
- **Closeness Centrality**: Evaluates how close a node is to all other nodes in the graph.
- **Betweenness Centrality**: Quantifies the number of times a node acts as a bridge along the shortest path between two other nodes.
- **Eigenvector Centrality**: Indicates the influence of a node in a network based on its connections to other high-scoring nodes.
- **Katz Centrality**: A variant of eigenvector centrality that incorporates a damping factor.
- **PageRank**: A probabilistic algorithm to measure the importance of nodes.

Edge-Level Measures
-------------------
- **Edge Betweenness**: Measures the extent to which an edge lies on the shortest paths between nodes.
- **Jaccard Similarity**: Measures the similarity between the neighborhoods of two nodes connected by an edge.

Global Graph Measures
---------------------
These measures provide insights into the overall structure and properties of a graph.

- **Graph Density**: Ratio of actual edges to the maximum possible edges in the graph.
- **Graph Diameter**: The longest shortest path between any two nodes in the graph.
- **Average Path Length**: The mean of all shortest paths in the graph.
- **Clustering Coefficient**: Measures the degree to which nodes in a graph tend to cluster together.
- **Graph Assortativity**: Indicates the tendency of nodes to connect with similar nodes.
- **Global Efficiency**: Measures how efficiently information is exchanged over the graph.
- **Modularity**: Quantifies the strength of division of a graph into modules or communities.

Node-Level Measures
-------------------
These measures describe the importance, influence, or role of individual nodes within the graph.

- **Degree Centrality**: Number of direct connections a node has.
- **Betweenness Centrality**: Measures how often a node acts as a bridge along the shortest path between two other nodes.
- **Closeness Centrality**: Inverse of the average length of the shortest path from a node to all other nodes.
- **Eigenvector Centrality**: Assigns scores to nodes based on their connections and the influence of their neighbors.
- **PageRank**: A variant of eigenvector centrality originally designed for ranking web pages.
- **K-Core Number**: Indicates the largest subgraph in which all nodes have at least \(k\) neighbors.

Edge-Level Measures
-------------------
These measures assess the importance or characteristics of edges in a graph.

- **Edge Betweenness**: Measures the number of shortest paths that pass through an edge.
- **Edge Weight**: Represents the strength or capacity of a connection between nodes.

Community-Level Measures
------------------------
These measures analyze groups of nodes within a graph.

- **Community Detection**: Identifies groups of nodes with dense internal connections and sparse external connections.
- **Modularity Optimization**: Quantifies the quality of community assignments.

Spectral Measures
-----------------
These measures are based on the eigenvalues and eigenvectors of matrices associated with the graph.

- **Spectral Radius**: The largest eigenvalue of the adjacency matrix.
- **Graph Laplacian**: Matrix representation used for analyzing graph properties.
- **Algebraic Connectivity**: The second smallest eigenvalue of the Laplacian, indicating graph robustness.

Dynamic Graph Measures
----------------------
These measures capture properties of evolving graphs over time.

- **Temporal Reachability**: Tracks the ability to connect nodes over time-varying edges.
- **Dynamic Centrality**: Adaptations of static centrality measures to dynamic networks.

Application-Specific Measures
-----------------------------
Measures designed for specific types of graphs or applications.

- **Shortest Path Length**: Often used in transportation and communication networks.
- **Resistance Distance**: Measures connectivity in electrical networks.
- **Network Flow**: Models capacities and bottlenecks in flow-based networks.
- **Random Walk Centrality**: Related to the probability of visiting nodes during random walks.

Graph-Level Measures
--------------------
- **Graph Density**: Proportion of observed edges to possible edges.
- **Average Clustering Coefficient**: Measures the likelihood of nodes forming tightly connected groups.
- **Diameter**: The longest shortest path between any two nodes in the graph.
- **Radius**: The shortest maximum distance from a central node to any other node.
- **Modularity**: Quantifies the strength of division of a network into communities.
- **Assortativity**: Measures the tendency of nodes to connect to other nodes with similar properties.

Community Detection Measures
----------------------------
- **Modularity Score**: Quantifies the quality of a graph's division into communities.
- **Conductance**: Measures the quality of a community by evaluating the ratio of inter-community edges to intra-community edges.
- **Normalized Cut**: Evaluates the separation quality of a graph into subgraphs.

Dynamic Graph Measures
----------------------
- **Temporal Betweenness**: Extends betweenness centrality to dynamic graphs.
- **Temporal Clustering Coefficient**: Evaluates clustering in temporal snapshots.
- **Edge Persistence**: Measures the stability of edges over time.

Shortest Path Measures
----------------------
- **Shortest Path Length**: Calculates the shortest path distance between nodes.
- **Average Path Length**: Computes the mean distance between all node pairs.
- **Eccentricity**: Measures the greatest distance from a node to all other nodes.

Spectral Measures
-----------------
- **Spectral Radius**: The largest eigenvalue of the adjacency matrix.
- **Graph Laplacian Eigenvalues**: Encodes various structural properties of the graph.
- **Algebraic Connectivity**: The second smallest eigenvalue of the Laplacian matrix, indicating the graph's connectivity.

Other Specialized Measures
--------------------------
- **Random Walk Betweenness**: Measures centrality based on random walk processes.
- **Resistance Distance**: Computes the effective electrical resistance between nodes.
- **Graph Entropy**: Quantifies the information content of a graph.

Conclusion
==========
The variety of graph distance measures provided by **Distancia** allows for comprehensive comparisons across different dimensions of graph structure and properties. Whether you're interested in structural differences, node-level comparisons, or the spectral characteristics of graphs, **Distancia** offers the right tools for a detailed and insightful analysis. These distances are applicable in numerous fields, from social network analysis to biology, offering flexibility and depth in graph comparison tasks.

.. _ShortestPath: https://distancia.readthedocs.io/en/latest/ShortestPath.html
.. _GraphEditDistance: https://distancia.readthedocs.io/en/latest/GraphEditDistance.html
.. _SpectralDistance: https://distancia.readthedocs.io/en/latest/SpectralDistance.html
.. _WeisfeilerLehmanSimilarity: https://distancia.readthedocs.io/en/latest/WeisfeilerLehmanSimilarity.html
.. _ComparingRandomWalkStationaryDistributions: https://distancia.readthedocs.io/en/latest/ComparingRandomWalkStationaryDistributions.html
.. _Diffusion: https://distancia.readthedocs.io/en/latest/Diffusion.html
.. _FrobeniusDistance: https://distancia.readthedocs.io/en/latest/FrobeniusDistance.html
.. _GraphKernelDistance: https://distancia.readthedocs.io/en/latest/GraphKernelDistance.html
.. _PatternBasedDistance: https://distancia.readthedocs.io/en/latest/PatternBasedDistance.html
.. _GraphCompressionDistance: https://distancia.readthedocs.io/en/latest/GraphCompressionDistance.html
.. _DegreeDistributionDistance: https://distancia.readthedocs.io/en/latest/DegreeDistributionDistance.html
.. _CommunityStructureDistance: https://distancia.readthedocs.io/en/latest/CommunityStructureDistance.html

