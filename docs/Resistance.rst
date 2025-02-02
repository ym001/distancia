Resistance Distance
===============

Introduction
-----------
The Resistance Distance is a sophisticated graph similarity measure based on the electrical network analogy of graphs. This measure views a graph as an electrical circuit where each edge represents a unit resistor. The resulting distance metric captures both direct and indirect connections between nodes, providing a nuanced view of network connectivity that considers all possible paths between vertices.

Mathematical Foundation
--------------------
The resistance distance between two nodes i and j in a graph G is defined as:

    Ω_ij = L⁺_ii + L⁺_jj - 2L⁺_ij

where:
- L⁺ is the Moore-Penrose pseudoinverse of the graph Laplacian matrix L
- L = D - A (D is the degree matrix, A is the adjacency matrix)

The resistance distance between two graphs G₁ and G₂ is then computed as:

    d(G₁, G₂) = ||Ω₁ - Ω₂||_F

where:
- Ω₁ and Ω₂ are the resistance distance matrices of G₁ and G₂
- ||·||_F denotes the Frobenius norm

Properties:
- Symmetric: d(G₁, G₂) = d(G₂, G₁)
- Non-negative: d(G₁, G₂) ≥ 0
- Identity of indiscernibles: d(G₁, G₂) = 0 iff G₁ and G₂ are isomorphic
- Captures both local and global connectivity patterns

Application
----------
The Resistance Distance is particularly useful for:
- Analyzing network robustness
- Studying network flow patterns
- Evaluating communication network efficiency
- Comparing molecular structures
- Analyzing transportation networks
- Identifying critical network components

Usage Example
------------
Here's how to use the Resistance Distance measure in the distancia package:

```python
from distancia import ResistanceDistance
import networkx as nx

# Create two example graphs
G1 = nx.Graph()
G1.add_edges_from([
    (0, 1), (1, 2), (2, 3), (3, 0),  # Square
    (0, 2)  # Diagonal
])

G2 = nx.Graph()
G2.add_edges_from([
    (0, 1), (1, 2), (2, 3), (3, 0),  # Square
    (1, 3)  # Different diagonal
])

# Initialize the distance measure
rd_distance = ResistanceDistance()

# Calculate the distance between the two graphs
distance = rd_distance.compute(G1, G2)
print(f"Resistance Distance: {distance}")

# Optional: Get resistance distance matrix for a single graph
resistance_matrix = rd_distance.get_resistance_matrix(G1)
```

Computational Complexity
----------------------
The main computational costs are:
- Laplacian matrix construction: O(|V| + |E|)
- Moore-Penrose pseudoinverse: O(|V|³)
- Resistance matrix computation: O(|V|²)
- Total complexity: O(|V|³)

Optimizations:
- Sparse matrix implementations for large networks
- Approximation methods for pseudoinverse computation
- Parallel computation for large graphs
- Incremental updates for dynamic networks

Academic References
-----------------
1. Klein, D. J., & Randić, M. (1993). Resistance distance. Journal of Mathematical Chemistry, 12(1), 81-95.

2. Xiao, W., & Gutman, I. (2003). Resistance distance and Laplacian spectrum. Theoretical Chemistry Accounts, 110(4), 284-289.

3. Babić, D., et al. (2002). On the resistance-distance matrix of a graph. Journal of Mathematical Chemistry, 31(1), 1-9.

4. Stephenson, K., & Zelen, M. (1989). Rethinking centrality: Methods and examples. Social Networks, 11(1), 1-37.

Conclusion
---------
The Resistance Distance provides a powerful framework for comparing graphs based on their electrical network properties. By incorporating both direct and indirect connections, it offers a more nuanced view of network similarity than simpler topological measures. While computationally intensive for large networks, various optimizations make it practical for real-world applications. The measure's foundation in electrical network theory provides it with strong mathematical properties and clear physical interpretation, making it particularly valuable for applications where the flow and distribution of resources through a network are important considerations.
