===================================
Modularity Score Distance
===================================

Introduction
-----------
Modularity Score Distance is a graph similarity metric that compares networks based on their achieved community division quality. Unlike modularity optimization which focuses on finding optimal divisions, this metric compares the actual quality scores of given community structures. It is particularly useful for analyzing real-world networks where communities are already defined or when comparing the effectiveness of different community detection results.

Formal Definition
---------------
For two graphs G1 and G2 with given community assignments C1 and C2, the modularity score distance uses their achieved modularity scores Q(G,C):

Let Q(G,C) be the modularity score for graph G with community assignment C:
Q(G,C) = (1/2m) ∑_ij [A_ij - (k_i k_j)/(2m)] δ(c_i,c_j)

where:
* m is the number of edges
* A_ij is the adjacency matrix
* k_i, k_j are the degrees of nodes i and j
* c_i, c_j are the assigned communities of nodes i and j
* δ is the Kronecker delta function

The distance is then defined as:
D(G1,G2) = |Q(G1,C1) - Q(G2,C2)|

Intuition and Significance
------------------------
This metric captures:
* Differences in community quality
* Variations in structural organization
* Community definition effectiveness
* Relative clustering strength

Applications
-----------
Modularity Score Distance finds applications in various domains:

1. Social Network Analysis
   * Comparing community detection results
   * Evaluating group structures
   * Analyzing organizational divisions

2. Biological Networks
   * Comparing functional modules
   * Analyzing protein complexes
   * Studying cellular organization

3. Information Networks
   * Evaluating document clustering
   * Analyzing web communities
   * Comparing network partitions

Usage Example
------------
```python
from distancia import ModularityScoreDistance

# Create example graphs with community assignments
G1 = nx.Graph()
G1.add_edges_from([
    (0,1), (1,2), (0,2),  # Community 1
    (3,4), (4,5), (3,5)   # Community 2
])
communities1 = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1}

G2 = nx.Graph()
G2.add_edges_from([
    (0,1), (1,2), (0,2),  # Community 1
    (3,4), (4,5), (3,5),  # Community 2
    (2,3)                 # Inter-community edge
])
communities2 = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1}

# Calculate modularity score distance
score_calculator = ModularityScoreDistance()
distance = score_calculator.compute(G1, G2, communities1, communities2)
print(f"Modularity Score Distance: {distance}")
```

Computational Complexity
----------------------
The computational complexity for comparing two graphs:
* Time complexity: O(|E|) for modularity score calculation
* Space complexity: O(|V|) for community assignments
* Overall comparison complexity: O(|E|)

where |V| is the number of vertices and |E| is the number of edges.

Academic References
-----------------
1. Newman, M. E. J. (2004). "Analysis of weighted networks." Physical Review E, 70(5), 056131.
2. Fortunato, S. (2010). "Community detection in graphs." Physics Reports, 486(3-5), 75-174.
3. Guimera, R., & Amaral, L. A. N. (2005). "Functional cartography of complex metabolic networks." Nature, 433(7028), 895-900.
4. Danon, L., et al. (2005). "Comparing community structure identification." Journal of Statistical Mechanics: Theory and Experiment, 2005(09), P09008.

Conclusion
---------
Modularity Score Distance provides a practical way to compare networks based on their achieved community structure quality. This metric is particularly effective for:
* Evaluating community detection results
* Comparing network partitioning
* Analyzing structural organization
* Studying community evolution

Key considerations:
* Requires predefined community assignments
* Sensitive to network size and density
* Affected by resolution limits
* Depends on community definition quality

Best practices include:
* Using consistent community detection methods
* Normalizing for network size when appropriate
* Comparing similar-sized networks
* Combining with other structural metrics

The metric is most effective when used alongside other distance measures, as it specifically captures community quality while potentially missing other structural properties.
