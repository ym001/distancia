===================================
Modularity Distance
===================================

Introduction
-----------
Modularity Distance is a graph similarity metric that compares networks based on their community structure strength. Modularity quantifies how well a network divides into communities or modules, measuring the density of links inside communities compared to links between communities. This distance metric is particularly valuable for analyzing social networks, biological systems, and other networks where community structure is significant.

Formal Definition
---------------
For two graphs G1 and G2, the modularity distance uses the modularity Q(G):

Let Q(G) be the modularity:
Q = (1/2m) ∑_ij [A_ij - (k_i k_j)/(2m)] δ(c_i,c_j)

where:
* m is the number of edges
* A_ij is the adjacency matrix
* k_i, k_j are the degrees of nodes i and j
* c_i, c_j are the communities of nodes i and j
* δ is the Kronecker delta function

The distance is then defined as:
D(G1, G2) = |Q(G1) - Q(G2)|

Intuition and Significance
------------------------
This metric captures:
* Differences in community structure strength
* Variations in network partitioning
* Community isolation patterns
* Internal vs external connectivity patterns

Applications
-----------
Modularity Distance finds applications in various domains:

1. Social Networks
   * Comparing community structures
   * Analyzing group formation
   * Studying social organization

2. Biological Networks
   * Analyzing protein complexes
   * Studying metabolic modules
   * Comparing brain regions

3. Information Networks
   * Analyzing topic clusters
   * Studying document organizations
   * Comparing web communities

Usage Example
------------
```python
from distancia import ModularityDistance

# Create example graphs
G1 = nx.Graph()
# Two clear communities
G1.add_edges_from([
    (0,1), (1,2), (0,2),  # Community 1
    (3,4), (4,5), (3,5),  # Community 2
    (2,3)                 # Inter-community edge
])

G2 = nx.Graph()
# Less defined communities
G2.add_edges_from([
    (0,1), (1,2), (2,3),
    (3,4), (4,5), (5,0)
])

# Calculate modularity distance
modularity_calculator = ModularityDistance()
distance = modularity_calculator.compute(G1, G2)
print(f"Modularity Distance: {distance}")
```

Computational Complexity
----------------------
The computational complexity for comparing two graphs:
* Time complexity for modularity calculation: O(|E|)
* Time complexity for community detection: O(|V||E|) using fast greedy algorithms
* Space complexity: O(|V| + |E|)
* Overall comparison complexity: O(|V||E|)

where |V| is the number of vertices and |E| is the number of edges.

Academic References
-----------------
1. Newman, M. E. J., & Girvan, M. (2004). "Finding and evaluating community structure in networks." Physical Review E, 69(2), 026113.
2. Fortunato, S. (2010). "Community detection in graphs." Physics Reports, 486(3-5), 75-174.
3. Blondel, V. D., et al. (2008). "Fast unfolding of communities in large networks." Journal of Statistical Mechanics: Theory and Experiment, 2008(10), P10008.
4. Newman, M. E. J. (2006). "Modularity and community structure in networks." Proceedings of the National Academy of Sciences, 103(23), 8577-8582.

Conclusion
---------
Modularity Distance provides a sophisticated way to compare networks based on their community structure. This metric is particularly effective for:
* Comparing organizational structures
* Analyzing network evolution
* Studying community formation
* Evaluating network partitioning

Key considerations:
* Resolution limit in community detection
* Multiple possible community partitions
* Size effects on modularity values
* Sensitivity to network density

Best practices include:
* Using consistent community detection algorithms
* Considering resolution parameters
* Combining with other structural metrics
* Accounting for network size effects

The metric is most effective when used alongside other distance measures, as it specifically captures community-related properties while potentially missing other structural differences.
