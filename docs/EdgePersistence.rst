Edge Persistence Distance
====================

Introduction
-----------
The Edge Persistence Distance is a measure that compares temporal networks based on the stability of their edges over time. This measure quantifies how consistently connections are maintained in dynamic networks, providing insights into the temporal robustness of relationships. It is particularly valuable for analyzing long-term structural stability in evolving networks, such as social relationships, communication patterns, or infrastructure networks.

Mathematical Foundation
--------------------
The edge persistence distance between two temporal graphs G₁(V₁, E₁, T₁) and G₂(V₂, E₂, T₂) is based on comparing their edge persistence profiles. For a temporal graph G, the persistence of an edge e is defined as:

    P(e) = |T(e)| / |T|

where:
- |T(e)| is the number of time steps where edge e exists
- |T| is the total number of time steps

The edge persistence distance is then computed as:

    d(G₁, G₂) = ||P₁ - P₂||

where:
- P₁ and P₂ are the vectors of edge persistence values
- ||·|| denotes an appropriate vector norm (typically L1 or L2)

The persistence profile matrix M for a graph is defined as:

    M[i,j,t] = 1 if edge (i,j) exists at time t
              0 otherwise

Application
----------
The Edge Persistence Distance is particularly useful for:
- Analyzing stability of social relationships
- Evaluating network infrastructure reliability
- Studying communication pattern consistency
- Detecting anomalies in network evolution
- Understanding community stability
- Assessing temporal network resilience

Usage Example
------------
Here's how to use the Edge Persistence Distance measure in the distancia package:

```python
from distancia import EdgePersistenceDistance
import networkx as nx

# Create two temporal graphs using lists of (node1, node2, timestamp, duration) edges
edges1 = [
    (0, 1, 1, 3),  # Edge exists from t=1 to t=3
    (1, 2, 2, 4),  # Edge exists from t=2 to t=5
    (2, 3, 1, 5)   # Edge exists from t=1 to t=5
]
edges2 = [
    (0, 1, 1, 2),  # Edge exists from t=1 to t=2
    (1, 2, 3, 3),  # Edge exists from t=3 to t=5
    (2, 3, 2, 4)   # Edge exists from t=2 to t=5
]

# Initialize the distance measure
ep_distance = EdgePersistenceDistance()

# Calculate the distance between the two temporal graphs
distance = ep_distance.compute(edges1, edges2)
print(f"Edge Persistence Distance: {distance}")

# Optional: Get persistence values for specific edges
edge = (0, 1)
persistence1 = ep_distance.get_edge_persistence(edges1, edge)
persistence2 = ep_distance.get_edge_persistence(edges2, edge)
```

Computational Complexity
----------------------
The computational complexity includes:
- Building temporal adjacency matrices: O(|E| × |T|)
- Computing persistence values: O(|E| × |T|)
- Computing distance between persistence vectors: O(|E|)
- Total complexity: O(|E| × |T|)

Optimizations:
- Sparse matrix representations for temporal adjacency
- Incremental updates for streaming data
- Efficient data structures for temporal edge tracking
- Parallel computation across time windows

Academic References
-----------------
1. Nicosia, V., et al. (2013). Graph Metrics for Temporal Networks. In Temporal Networks (pp. 15-40). Springer.

2. Holme, P. (2015). Modern temporal network theory: A colloquium. The European Physical Journal B, 88(9), 234.

3. Santoro, N., et al. (2011). Time-Varying Graphs and Dynamic Networks. International Journal of Parallel, Emergent and Distributed Systems, 26(5), 395-408.

4. Tang, J., et al. (2013). Analysing temporal patterns of topic discussions in dynamic social networks. Social Network Analysis and Mining, 3(4), 1283-1295.

Conclusion
---------
The Edge Persistence Distance provides a robust framework for comparing temporal networks based on the stability of their connections over time. By quantifying how consistently edges are maintained, this measure offers unique insights into network dynamics that complement traditional static and temporal measures. Its ability to capture long-term structural stability makes it particularly valuable for applications where the durability of connections is crucial, such as social network analysis, infrastructure monitoring, and communication system evaluation. While the measure is computationally efficient for most practical applications, various optimizations are available for handling large-scale temporal networks.
