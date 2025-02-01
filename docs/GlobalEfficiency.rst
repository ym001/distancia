===================================
Global Efficiency Distance
===================================

Introduction
-----------
Global Efficiency Distance is a graph similarity metric that compares networks based on their information exchange capacity. Global efficiency quantifies how efficiently information can be transmitted across a network by measuring the average inverse shortest path length between all pairs of nodes. This distance metric is particularly valuable for analyzing communication networks, transportation systems, and information flow in complex networks.

Formal Definition
---------------
For two graphs G1 and G2, the global efficiency distance uses the global efficiency E(G):

Let E(G) be the global efficiency:
E(G) = (1 / (n(n-1))) ∑(i≠j) (1 / d_ij)

where:
* n is the number of nodes
* d_ij is the shortest path length between nodes i and j
* The sum is taken over all pairs of nodes

The distance is then defined as:
D(G1, G2) = |E(G1) - E(G2)|

For disconnected pairs, 1/d_ij is defined as 0.

Intuition and Significance
------------------------
This metric captures:
* Information exchange efficiency differences
* Network accessibility variations
* Communication capacity disparities
* Structural robustness differences

Applications
-----------
Global Efficiency Distance finds applications in various domains:

1. Communication Networks
   * Comparing network architectures
   * Analyzing routing efficiency
   * Evaluating network designs

2. Transportation Systems
   * Analyzing traffic flow patterns
   * Comparing infrastructure designs
   * Evaluating accessibility

3. Biological Networks
   * Studying brain connectivity
   * Analyzing metabolic networks
   * Comparing protein interaction networks

Usage Example
------------
```python
from distancia import GlobalEfficiencyDistance

# Create example graphs
G1 = nx.Graph()
G1.add_edges_from([
    (0,1), (1,2), (2,3), (3,0)  # Cycle graph
])

G2 = nx.Graph()
G2.add_edges_from([
    (0,1), (1,2), (2,3), (0,2), (1,3)  # More connected graph
])

# Calculate global efficiency distance
efficiency_calculator = GlobalEfficiencyDistance()
distance = efficiency_calculator.compute(G1, G2)
print(f"Global Efficiency Distance: {distance}")
```

Computational Complexity
----------------------
The computational complexity for comparing two graphs:
* Time complexity: O(|V|(|E| + |V|log|V|)) using Dijkstra's algorithm
* Space complexity: O(|V|²) for storing distance matrix
* For unweighted graphs using BFS: O(|V|(|V| + |E|))

where |V| is the number of vertices and |E| is the number of edges.

Academic References
-----------------
1. Latora, V., & Marchiori, M. (2001). "Efficient behavior of small-world networks." Physical Review Letters, 87(19), 198701.
2. Crucitti, P., et al. (2003). "Efficiency of scale-free networks: error and attack tolerance." Physica A, 320, 622-642.
3. Achard, S., & Bullmore, E. (2007). "Efficiency and cost of economical brain functional networks." PLoS Computational Biology, 3(2), e17.
4. Wang, X., et al. (2014). "Efficiency measurement in complex networks." EPL (Europhysics Letters), 106(2), 28003.

Conclusion
---------
Global Efficiency Distance provides a sophisticated way to compare networks based on their information exchange capabilities. This metric is particularly effective for:
* Evaluating network performance differences
* Comparing communication capabilities
* Analyzing structural robustness
* Studying network optimization

Key considerations:
* Handles disconnected components naturally
* Sensitive to both local and global structure
* Reflects practical communication capacity
* Accounts for parallel paths

Best practices include:
* Normalizing for network size when appropriate
* Considering weighted versions for weighted networks
* Combining with other metrics for comprehensive comparison
* Accounting for the specific context of the network

The metric is most useful when combined with other distance measures, as it specifically captures efficiency-related properties while potentially missing other structural aspects.
