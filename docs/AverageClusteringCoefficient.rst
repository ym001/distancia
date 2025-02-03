Average Clustering Coefficient Distance
================================

Introduction
-----------
The Average Clustering Coefficient Distance is a measure that compares networks based on their tendency to form tightly connected groups. This measure quantifies the difference in how nodes in different networks cluster together, providing insights into the local cohesiveness and triadic closure patterns. It is particularly useful for analyzing social networks, biological networks, and other systems where clustering behavior is significant.

Mathematical Foundation
--------------------
The average clustering coefficient distance between two graphs G₁(V₁, E₁) and G₂(V₂, E₂) is based on comparing their average clustering coefficients. For a graph G, the clustering coefficient C_i of node i is defined as:

    C_i = 2L_i / (k_i(k_i-1))

where:
- k_i is the degree of node i
- L_i is the number of edges between neighbors of node i

The average clustering coefficient C is then:

    C(G) = (1/n) ∑_i C_i

The distance between two graphs is computed as:

    d(G₁, G₂) = |C(G₁) - C(G₂)|

Properties:
- Symmetric: d(G₁, G₂) = d(G₂, G₁)
- Non-negative: d(G₁, G₂) ≥ 0
- Bounded: 0 ≤ d(G₁, G₂) ≤ 1

Application
----------
The Average Clustering Coefficient Distance is particularly useful for:
- Analyzing social network structures
- Studying protein interaction networks
- Identifying community formation patterns
- Comparing real networks to random models
- Evaluating network organization
- Detecting hierarchical structure
- Understanding network formation processes

Usage Example
------------
Here's how to use the Average Clustering Coefficient Distance measure in the distancia package:

```python
from distancia import AvgClusteringDistance
import networkx as nx

# Create two example graphs
G1 = nx.Graph()
G1.add_edges_from([
    (0, 1), (1, 2), (2, 0),  # Triangle
    (2, 3), (3, 4), (4, 2)   # Additional triangle
])

G2 = nx.Graph()
G2.add_edges_from([
    (0, 1), (1, 2), (2, 3), (3, 0),  # Square
    (0, 2)  # Diagonal
])

# Initialize the distance measure
acc_distance = AvgClusteringDistance()

# Calculate the distance between the two graphs
distance = acc_distance.compute(G1, G2)
print(f"Average Clustering Coefficient Distance: {distance}")

# Optional: Get individual clustering coefficients
clustering1 = acc_distance.get_avg_clustering(G1)
clustering2 = acc_distance.get_avg_clustering(G2)
```

Computational Complexity
----------------------
The computational complexity includes:
- For each node i:
  * Finding neighbors: O(k_i)
  * Counting edges between neighbors: O(k_i²)
- Total complexity: O(∑_i k_i²) ≈ O(n⟨k²⟩)

where:
- n is the number of nodes
- ⟨k²⟩ is the second moment of the degree distribution

Optimizations:
- Parallel computation for large networks
- Efficient neighbor list implementations
- Caching of intermediate results

Academic References
-----------------
1. Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. Nature, 393(6684), 440-442.

2. Newman, M. E. J. (2003). The Structure and Function of Complex Networks. SIAM Review, 45(2), 167-256.

3. Barrat, A., & Weigt, M. (2000). On the properties of small-world network models. The European Physical Journal B, 13(3), 547-560.

4. Saramäki, J., et al. (2007). Generalizations of the clustering coefficient to weighted complex networks. Physical Review E, 75(2), 027105.

Conclusion
---------
The Average Clustering Coefficient Distance provides a powerful way to compare networks based on their local clustering patterns. This measure is particularly valuable for understanding how networks differ in their tendency to form tightly connected groups. While simple to understand, it captures important aspects of network organization that are relevant across many domains. The measure's clear mathematical properties and interpretability make it especially useful for applications where local network structure and community formation are key considerations.
