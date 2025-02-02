Spectral Radius Distance
=====================

Introduction
-----------
The Spectral Radius Distance is a graph similarity measure based on the comparison of the largest eigenvalues (spectral radii) of the adjacency matrices of two graphs. This metric provides a scalar value that captures global structural properties of the graphs, making it particularly useful for comparing network topologies.

Mathematical Foundation
--------------------
The spectral radius of a graph is defined as the largest eigenvalue (λ₁) of its adjacency matrix. For two graphs G₁ and G₂, the spectral radius distance is calculated as:

    d(G₁, G₂) = |λ₁(G₁) - λ₁(G₂)|

where:
- λ₁(G₁) is the largest eigenvalue of graph G₁'s adjacency matrix
- λ₁(G₂) is the largest eigenvalue of graph G₂'s adjacency matrix

This measure is based on the Perron-Frobenius theorem, which guarantees that the largest eigenvalue of an adjacency matrix is real and positive for connected graphs.

Application
----------
The Spectral Radius Distance is particularly effective in:
- Comparing the overall connectivity patterns of networks
- Detecting structural similarities between graphs of different sizes
- Analyzing dynamic changes in evolving networks
- Identifying graphs with similar global properties

Usage Example
------------
Here's how to use the Spectral Radius Distance measure in the distancia package:

```python
from distancia import SpectralRadiusDistance
import networkx as nx

# Create two example graphs
G1 = nx.erdos_renyi_graph(10, 0.3, seed=42)
G2 = nx.erdos_renyi_graph(10, 0.4, seed=42)

# Initialize the distance measure
sr_distance = SpectralRadiusDistance()

# Calculate the distance between the two graphs
distance = sr_distance.compute(G1, G2)
print(f"Spectral Radius Distance: {distance}")
```

Computational Complexity
----------------------
The computational complexity of calculating the spectral radius distance is dominated by the eigenvalue computation:
- Time complexity: O(n³) for dense matrices, where n is the number of vertices
- Space complexity: O(n²) for storing the adjacency matrix

For sparse graphs, iterative methods like the power iteration can be used to compute the spectral radius more efficiently, with complexity O(m), where m is the number of edges.

Academic References
-----------------
1. Cvetković, D., Rowlinson, P., & Simić, S. (2010). An Introduction to the Theory of Graph Spectra. Cambridge University Press.

2. Van Dam, E. R., & Haemers, W. H. (2003). Which graphs are determined by their spectrum?. Linear Algebra and its Applications, 373, 241-272.

3. Wilson, R. C., & Zhu, P. (2008). A study of graph spectra for comparing graphs and trees. Pattern Recognition, 41(9), 2833-2841.

Conclusion
---------
The Spectral Radius Distance provides a mathematically sound and computationally feasible approach to comparing graphs based on their spectral properties. While it may not capture all aspects of graph similarity, it offers a robust global measure that is particularly useful when analyzing network structures and their evolution over time. Its main advantages include invariance to graph isomorphism and the ability to compare graphs of different sizes, making it a valuable tool in network analysis applications.
