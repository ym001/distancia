===================================
Edge Weight Distance
===================================

Introduction
-----------
Edge Weight Distance is a fundamental graph similarity metric that compares two graphs based on their edge weight distributions. This measure is particularly valuable when dealing with weighted networks where the strength of connections between nodes carries significant meaning, such as in social networks (relationship strength), transportation networks (capacity/distance), or neural networks (synaptic strength).

Formal Definition
---------------
For two weighted graphs G1 and G2 with the same number of edges, the edge weight distance is defined as:

Let w1(e) be the weight of edge e in G1
Let w2(e) be the weight of edge e in G2
Let W(G) be the normalized distribution of edge weights for graph G

The distance is computed as:

D(G1, G2) = Σ |w1(e) - w2(e)| / |E|

where |E| is the total number of edges.

Intuition and Significance
------------------------
The edge weight distance measures how different the connection strengths are between two networks. It captures:
* Variations in interaction intensities
* Differences in network capacity
* Changes in relationship strength patterns
* Structural load distribution differences

Applications
-----------
Edge weight distance finds applications in various domains:

1. Social Network Analysis
   * Comparing interaction strengths between different time periods
   * Analyzing changes in community structures

2. Transportation Networks
   * Evaluating capacity differences between network designs
   * Comparing traffic flow patterns

3. Biological Networks
   * Analyzing protein interaction networks
   * Comparing neural pathway strengths

Usage Example
------------
```python
from distancia import EdgeWeightDistance

# Create two weighted graphs
G1 = nx.Graph()
G1.add_weighted_edges_from([(0, 1, 1.0), (1, 2, 2.0), (2, 0, 3.0)])

G2 = nx.Graph()
G2.add_weighted_edges_from([(0, 1, 1.5), (1, 2, 1.8), (2, 0, 2.7)])

# Calculate distance
distance_calculator = EdgeWeightDistance()
distance = distance_calculator.compute(G1, G2)
print(f"Edge Weight Distance: {distance}")
```

Computational Complexity
----------------------
The computational complexity is O(|E|), where |E| is the number of edges in the graphs.
* Time complexity: Linear with respect to the number of edges
* Space complexity: O(1) as it requires constant extra space

Academic References
-----------------
1. Newman, M. E. J. (2004). "Analysis of weighted networks." Physical Review E, 70(5), 056131.
2. Barrat, A., Barthélemy, M., & Vespignani, A. (2004). "Weighted evolving networks: Coupling topology and weight dynamics." Physical Review Letters, 92(22), 228701.
3. Opsahl, T., Agneessens, F., & Skvoretz, J. (2010). "Node centrality in weighted networks: Generalizing degree and shortest paths." Social Networks, 32(3), 245-251.

Conclusion
---------
Edge Weight Distance provides a straightforward yet powerful way to compare weighted graphs by focusing on the strength of connections. While simple to compute, it offers valuable insights into how interaction patterns differ between networks. The metric is particularly useful when the magnitude of connections is as important as their existence.

For most accurate results, this distance measure should be used in conjunction with other metrics that capture different aspects of graph similarity, especially when analyzing complex network structures.
