Graph Density Distance
=================

Introduction
-----------
The Graph Density Distance is a fundamental measure that compares networks based on their edge density characteristics. This measure quantifies the difference in how densely connected two graphs are by comparing the proportion of actual edges to possible edges in each graph. While simple in concept, this measure provides valuable insights into the overall connectivity patterns and structural compactness of networks.

Mathematical Foundation
--------------------
The graph density distance between two graphs G₁(V₁, E₁) and G₂(V₂, E₂) is based on comparing their density values. For a simple undirected graph G with |V| vertices and |E| edges, the density is defined as:

    ρ(G) = 2|E| / (|V|(|V|-1))

For directed graphs:

    ρ(G) = |E| / (|V|(|V|-1))

The graph density distance is then computed as:

    d(G₁, G₂) = |ρ(G₁) - ρ(G₂)|

Properties:
- Symmetric: d(G₁, G₂) = d(G₂, G₁)
- Non-negative: d(G₁, G₂) ≥ 0
- Bounded: 0 ≤ d(G₁, G₂) ≤ 1
- Triangle inequality: d(G₁, G₃) ≤ d(G₁, G₂) + d(G₂, G₃)

Application
----------
The Graph Density Distance is particularly useful for:
- Comparing network sparseness/density patterns
- Analyzing social network cohesion
- Studying network evolution over time
- Identifying structural changes in dynamic networks
- Comparing different types of real-world networks
- Benchmarking network generation models
- Evaluating community structures

Usage Example
------------
Here's how to use the Graph Density Distance measure in the distancia package:

```python
from distancia import GraphDensityDistance
import networkx as nx

# Create two example graphs
G1 = nx.Graph()
G1.add_edges_from([
    (0, 1), (1, 2), (2, 3), (3, 0),
    (0, 2)  # Diamond with one diagonal
])

G2 = nx.Graph()
G2.add_edges_from([
    (0, 1), (1, 2), (2, 3), (3, 0)  # Simple diamond
])

# Initialize the distance measure
gd_distance = GraphDensityDistance()

# Calculate the distance between the two graphs
distance = gd_distance.compute(G1, G2)
print(f"Graph Density Distance: {distance}")

# Optional: Get individual densities
density1 = gd_distance.get_density(G1)
density2 = gd_distance.get_density(G2)
```

Computational Complexity
----------------------
The computational complexity is straightforward:
- Counting edges: O(|E|)
- Counting vertices: O(1)
- Computing density: O(1)
- Total complexity: O(|E|)

For weighted or directed graphs:
- Same complexity as unweighted graphs
- No additional overhead for direction consideration

Academic References
-----------------
1. Newman, M. E. J. (2010). Networks: An Introduction. Oxford University Press.

2. Wasserman, S., & Faust, K. (1994). Social Network Analysis: Methods and Applications. Cambridge University Press.

3. Barabási, A. L. (2016). Network Science. Cambridge University Press.

4. Costa, L. D. F., et al. (2007). Characterization of complex networks: A survey of measurements. Advances in Physics, 56(1), 167-242.

Conclusion
---------
The Graph Density Distance provides a simple yet powerful way to compare networks based on their connectivity patterns. While it may not capture fine-grained structural differences, its simplicity and computational efficiency make it an excellent first-order measure for network comparison. The measure is particularly valuable as a baseline metric and can be effectively combined with other more sophisticated measures for comprehensive network analysis. Its clear mathematical properties and interpretability make it an essential tool in the network analysis toolkit, especially for applications where the overall connectivity level is a key consideration.
