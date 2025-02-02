===================================
Conductance Distance
===================================

Introduction
-----------
Conductance Distance is a graph similarity metric that compares networks based on their community separation quality. Conductance measures how well-connected a community is internally versus how connected it is to the rest of the network. This distance metric is particularly valuable for analyzing network partitions and evaluating community boundaries in complex networks.

Formal Definition
---------------
For two graphs G1 and G2, the conductance distance uses the conductance measure φ(S):

Let φ(S) be the conductance of a community S:
φ(S) = c(S) / min(vol(S), vol(V-S))

where:
* c(S) is the number of edges leaving the set S
* vol(S) is the sum of degrees of nodes in S
* V-S represents the complement of set S

For graphs with multiple communities, the overall conductance Φ(G) is:
Φ(G) = average(φ(Si)) for all communities Si

The distance is then defined as:
D(G1, G2) = |Φ(G1) - Φ(G2)|

Intuition and Significance
------------------------
This metric captures:
* Community isolation quality
* Boundary definition strength
* Internal vs external connectivity
* Community separation effectiveness

Applications
-----------
Conductance Distance finds applications in various domains:

1. Social Networks
   * Evaluating community boundaries
   * Analyzing group isolation
   * Studying social segregation

2. Communication Networks
   * Analyzing network partitions
   * Evaluating network bottlenecks
   * Studying information flow barriers

3. Biological Networks
   * Analyzing protein modules
   * Studying metabolic pathways
   * Evaluating neural communities

Usage Example
------------
```python
from distancia import ConductanceDistance

# Create example graphs with communities
G1 = nx.Graph()
G1.add_edges_from([
    (0,1), (1,2), (0,2),  # Community 1
    (3,4), (4,5), (3,5),  # Community 2
    (2,3)                 # Single bridge
])
communities1 = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1}

G2 = nx.Graph()
G2.add_edges_from([
    (0,1), (1,2), (0,2),  # Community 1
    (3,4), (4,5), (3,5),  # Community 2
    (0,3), (1,4)          # Multiple bridges
])
communities2 = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1}

# Calculate conductance distance
conductance_calculator = ConductanceDistance()
distance = conductance_calculator.compute(G1, G2, communities1, communities2)
print(f"Conductance Distance: {distance}")
```

Computational Complexity
----------------------
The computational complexity for comparing two graphs:
* Time complexity: O(|E|) for conductance calculation
* Space complexity: O(|V|) for community storage
* Overall comparison complexity: O(|E|)

where |V| is the number of vertices and |E| is the number of edges.

Academic References
-----------------
1. Kannan, R., Vempala, S., & Vetta, A. (2004). "On clusterings: Good, bad and spectral." Journal of the ACM, 51(3), 497-515.
2. Leskovec, J., Lang, K. J., & Mahoney, M. (2010). "Empirical comparison of algorithms for network community detection." WWW '10.
3. Andersen, R., Chung, F., & Lang, K. (2006). "Local graph partitioning using PageRank vectors." FOCS '06.
4. Schaeffer, S. E. (2007). "Graph clustering." Computer Science Review, 1(1), 27-64.

Conclusion
---------
Conductance Distance provides an effective way to compare networks based on their community boundary quality. This metric is particularly useful for:
* Evaluating community detection results
* Comparing network partitioning quality
* Analyzing boundary definitions
* Studying community isolation

Key considerations:
* Sensitive to community size variations
* Affected by network density
* Requires predefined communities
* Balance between internal and external connections

Best practices include:
* Using consistent community definitions
* Considering multiple scales of analysis
* Normalizing for network size
* Combining with other structural metrics

The metric is most effective when used as part of a comprehensive suite of distance measures, as it specifically captures boundary quality while potentially missing other important network properties.
