===================================
Graph Assortativity Distance
===================================

Introduction
-----------
Graph Assortativity Distance measures the difference in mixing patterns between networks by comparing their assortativity coefficients. Assortativity quantifies the tendency of nodes to connect to other nodes with similar properties (e.g., degree, attributes). This distance metric is particularly valuable for comparing social, biological, and technological networks where node similarity plays a crucial role in connection patterns.

Formal Definition
---------------
For two graphs G1 and G2, the assortativity distance uses the assortativity coefficient r(G):

Let r(G) be the degree assortativity coefficient:
r(G) = (∑xy xy(e_xy - a_x b_y)) / (σ_a σ_b)

where:
* e_xy is the fraction of edges connecting nodes of degree x and y
* a_x and b_y are the fraction of edges starting and ending at nodes of degree x and y
* σ_a and σ_b are the standard deviations of distributions a and b

The distance is then defined as:
D(G1, G2) = |r(G1) - r(G2)|

Intuition and Significance
------------------------
This metric captures:
* Differences in node mixing patterns
* Variations in network homophily
* Structural hierarchy differences
* Social stratification patterns

Applications
-----------
Graph Assortativity Distance finds applications in various domains:

1. Social Networks
   * Analyzing friendship patterns
   * Studying social stratification
   * Comparing community structures

2. Biological Networks
   * Analyzing protein-protein interactions
   * Studying ecological networks
   * Comparing gene regulatory networks

3. Technological Networks
   * Analyzing Internet topology
   * Studying power grid structures
   * Comparing communication networks

Usage Example
------------
```python
from distancia import AssortativeDistance

# Create example graphs
G1 = nx.Graph()
G1.add_edges_from([
    (0,1), (1,2), (2,3),  # High-degree nodes connected
    (3,4), (4,5), (5,0)
])  # Assortative network

G2 = nx.Graph()
G2.add_edges_from([
    (0,1), (1,2), (2,3),  # Star-like pattern
    (1,4), (1,5)
])  # Disassortative network

# Calculate assortativity distance
assortativity_calculator = AssortativeDistance()
distance = assortativity_calculator.compute(G1, G2)
print(f"Assortativity Distance: {distance}")
```

Computational Complexity
----------------------
The computational complexity for comparing two graphs:
* Time complexity: O(|E|) for degree assortativity
* Space complexity: O(|V|) for degree sequence storage
* For attribute assortativity: O(|E| + |V|)

where |V| is the number of vertices and |E| is the number of edges.

Academic References
-----------------
1. Newman, M. E. J. (2002). "Assortative mixing in networks." Physical Review Letters, 89(20), 208701.
2. Foster, J. G., et al. (2010). "Edge direction and the structure of networks." Proceedings of the National Academy of Sciences, 107(24), 10815-10820.
3. Piraveenan, M., et al. (2012). "Measuring assortativity in complex networks." EPL (Europhysics Letters), 100(2), 28006.
4. Newman, M. E. J. (2003). "Mixing patterns in networks." Physical Review E, 67(2), 026126.

Conclusion
---------
Graph Assortativity Distance provides a sophisticated way to compare networks based on their mixing patterns. This metric is particularly effective for:
* Understanding differences in social stratification
* Comparing hierarchical structures
* Analyzing network resilience patterns
* Studying evolutionary patterns in networks

Key considerations:
* Different types of assortativity (degree, attribute)
* Network size effects on measurements
* Direction of mixing patterns
* Local vs. global patterns

Best practices include:
* Considering both degree and attribute assortativity
* Normalizing for network size when appropriate
* Combining with other structural metrics
* Accounting for network density effects

The metric is most effective when used alongside other distance measures, as it specifically captures mixing patterns while potentially missing other structural differences.
