Dynamic Centrality Distance
=======================

Introduction
-----------
The Dynamic Centrality Distance is a sophisticated measure for comparing evolving networks based on the temporal evolution of node centralities. This measure extends traditional static centrality concepts to dynamic networks, capturing how the importance of nodes changes over time. It provides insights into the evolutionary patterns of node roles and network structure in temporal networks.

Mathematical Foundation
--------------------
The Dynamic Centrality Distance between two temporal graphs G₁(V₁, E₁, T₁) and G₂(V₂, E₂, T₂) is computed by comparing their centrality evolution vectors. For a temporal graph G, the dynamic centrality vector C(t) at time t is defined as:

    C(t) = [c₁(t), c₂(t), ..., cₙ(t)]

where cᵢ(t) is the centrality of node i at time t.

The distance measure is then defined as:

    d(G₁, G₂) = ∑_t w(t) × ||C₁(t) - C₂(t)||₂ / |T|

where:
- C₁(t) and C₂(t) are the centrality vectors at time t
- w(t) is a time-dependent weight function
- ||·||₂ denotes the L2 norm
- |T| is the number of time steps

Supported centrality measures include:
- Dynamic degree centrality
- Dynamic betweenness centrality
- Dynamic closeness centrality
- Dynamic eigenvector centrality

Application
----------
The Dynamic Centrality Distance is particularly useful for:
- Tracking influence evolution in social networks
- Analyzing leadership dynamics in organizational networks
- Monitoring network infrastructure importance over time
- Studying information flow patterns in communication networks
- Identifying key actors in temporal interaction networks
- Analyzing the evolution of community structures

Usage Example
------------
Here's how to use the Dynamic Centrality Distance measure in the distancia package:

```python
from distancia import DynamicCentralityDistance
import networkx as nx

# Create two temporal graphs using lists of (node1, node2, timestamp) edges
edges1 = [
    (0, 1, 1), (1, 2, 2), (2, 3, 3),
    (0, 2, 2), (1, 3, 4)
]
edges2 = [
    (0, 1, 1), (1, 2, 3), (2, 3, 4),
    (0, 2, 2), (1, 3, 5)
]

# Initialize the distance measure with specific centrality type
dc_distance = DynamicCentralityDistance(centrality_type='degree')

# Calculate the distance between the two temporal graphs
distance = dc_distance.compute(edges1, edges2)
print(f"Dynamic Centrality Distance: {distance}")

# Optional: Get centrality evolution for specific nodes
node_id = 1
centrality_evolution = dc_distance.get_node_centrality_evolution(edges1, node_id)
```

Computational Complexity
----------------------
The computational complexity varies based on the chosen centrality measure:
- Dynamic degree centrality: O(|E|)
- Dynamic betweenness centrality: O(|T| × |V| × |E|)
- Dynamic closeness centrality: O(|T| × |V| × (|V| + |E|))
- Dynamic eigenvector centrality: O(|T| × k × |E|), where k is the number of iterations

Additional costs:
- Temporal graph construction: O(|E|)
- Distance computation between centrality vectors: O(|T| × |V|)

Optimizations:
- Incremental centrality updates
- Parallel computation across time windows
- Approximation algorithms for large networks

Academic References
-----------------
1. Kim, H., & Anderson, R. (2012). Temporal node centrality in complex networks. Physical Review E, 85(2), 026107.

2. Tang, J., et al. (2010). Analysing Information Flows and Key Mediators through Temporal Centrality Metrics. In Proceedings of the 3rd Workshop on Social Network Systems.

3. Nicosia, V., et al. (2013). Graph Metrics for Temporal Networks. In Temporal Networks (pp. 15-40). Springer.

4. Taylor, D., et al. (2017). Eigenvector-based centrality measures for temporal networks. Multiscale Modeling & Simulation, 15(1), 537-574.

Conclusion
---------
The Dynamic Centrality Distance provides a comprehensive framework for comparing temporal networks through the lens of evolving node importance. By extending traditional centrality concepts to the temporal domain, this measure captures both structural and temporal aspects of network evolution. While different centrality types offer various perspectives on network dynamics, the measure's flexible framework allows for adaptation to specific application needs. This makes it a valuable tool for analyzing complex dynamic systems, from social networks to infrastructure networks, where the temporal evolution of node roles is crucial for understanding system behavior.
