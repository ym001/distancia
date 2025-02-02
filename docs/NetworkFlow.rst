Network Flow Distance
================

Introduction
-----------
The Network Flow Distance is a sophisticated measure that compares graphs based on their capacity to transport flow between nodes. This measure is inspired by the maximum flow problem and considers the network's ability to handle flow across multiple paths. It is particularly valuable for analyzing transportation networks, communication systems, and resource distribution networks where capacity and bottlenecks are crucial considerations.

Mathematical Foundation
--------------------
The network flow distance between two graphs G₁(V₁, E₁) and G₂(V₂, E₂) is based on comparing their flow capacities. For a graph G, the maximum flow capacity between any two nodes s and t is defined as:

    f(s,t) = max ∑_v f_sv

subject to:
1. Flow conservation: ∑_v f_uv = ∑_v f_vu for all u ≠ s,t
2. Capacity constraints: f_uv ≤ c_uv for all edges (u,v)
3. Non-negativity: f_uv ≥ 0 for all edges (u,v)

The network flow distance is then computed as:

    d(G₁, G₂) = ||F₁ - F₂||_F

where:
- F₁ and F₂ are matrices of maximum flow values between all pairs of nodes
- ||·||_F denotes the Frobenius norm
- F_ij represents the maximum flow between nodes i and j

Application
----------
The Network Flow Distance is particularly useful for:
- Analyzing transportation network capacity
- Evaluating communication network bandwidth
- Studying supply chain networks
- Identifying network bottlenecks
- Comparing infrastructure resilience
- Optimizing resource distribution networks
- Analyzing social network information flow

Usage Example
------------
Here's how to use the Network Flow Distance measure in the distancia package:

```python
from distancia import NetworkFlowDistance
import networkx as nx

# Create two example graphs with capacities
G1 = nx.DiGraph()
G1.add_weighted_edges_from([
    (0, 1, 10), (1, 2, 8), (2, 3, 12),
    (0, 2, 5),  (1, 3, 6)
])

G2 = nx.DiGraph()
G2.add_weighted_edges_from([
    (0, 1, 8),  (1, 2, 10), (2, 3, 10),
    (0, 2, 6),  (1, 3, 8)
])

# Initialize the distance measure
nf_distance = NetworkFlowDistance()

# Calculate the distance between the two graphs
distance = nf_distance.compute(G1, G2)
print(f"Network Flow Distance: {distance}")

# Optional: Get maximum flow between specific nodes
source, target = 0, 3
flow1 = nf_distance.get_max_flow(G1, source, target)
flow2 = nf_distance.get_max_flow(G2, source, target)
```

Computational Complexity
----------------------
The computational complexity involves:
- Max-flow computation for each pair: O(|V|²|E|) using Ford-Fulkerson
- Total complexity for all pairs: O(|V|⁴|E|)

Alternative algorithms:
- Push-relabel algorithm: O(|V|²|E|) for single source-target
- Edmonds-Karp algorithm: O(|V||E|²) for single source-target

Optimizations:
- Caching flow computations
- Parallel computation for different source-target pairs
- Approximation algorithms for large networks
- Incremental updates for dynamic networks

Academic References
-----------------
1. Ford, L. R., & Fulkerson, D. R. (1956). Maximal flow through a network. Canadian Journal of Mathematics, 8, 399-404.

2. Goldberg, A. V., & Tarjan, R. E. (1988). A new approach to the maximum-flow problem. Journal of the ACM, 35(4), 921-940.

3. Ahuja, R. K., Magnanti, T. L., & Orlin, J. B. (1993). Network Flows: Theory, Algorithms, and Applications. Prentice Hall.

4. Newman, M. E. J. (2010). Networks: An Introduction. Oxford University Press.

Conclusion
---------
The Network Flow Distance provides a sophisticated approach to comparing graphs based on their flow capacities and bottleneck characteristics. This measure is particularly valuable for applications where the ability to transport resources, information, or traffic through a network is crucial. While computationally intensive for large networks, various algorithms and optimizations make it practical for real-world applications. The measure's strong theoretical foundation in network flow theory, combined with its practical relevance to infrastructure and communication networks, makes it an essential tool for analyzing and comparing complex networks where capacity and flow are key considerations.
