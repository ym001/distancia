Temporal Reachability Distance
==========================

Introduction
-----------
The Temporal Reachability Distance is a sophisticated measure for comparing dynamic graphs by analyzing how nodes can reach each other through time-varying edges. This measure is particularly important for temporal networks where connections appear and disappear over time, such as communication networks, transportation systems, or social interactions.

Mathematical Foundation
--------------------
The temporal reachability distance between two temporal graphs G₁(V₁, E₁, T₁) and G₂(V₂, E₂, T₂) is based on comparing their reachability matrices over time. For a temporal graph G, the reachability matrix R(t) at time t is defined as:

    R(t)[i,j] = 1 if node i can reach node j through a time-respecting path up to time t
                0 otherwise

The temporal reachability distance can be computed as:

    d(G₁, G₂) = ∑_t |R₁(t) - R₂(t)|_F / |T|

where:
- R₁(t) and R₂(t) are the reachability matrices at time t
- |·|_F denotes the Frobenius norm
- |T| is the number of time steps considered
- A time-respecting path must follow the temporal ordering of edges

Application
----------
The Temporal Reachability Distance is particularly useful for:
- Analyzing information flow in communication networks
- Studying disease spread patterns
- Evaluating transportation network efficiency
- Comparing social network evolution
- Assessing network vulnerability over time
- Analyzing temporal network resilience

Usage Example
------------
Here's how to use the Temporal Reachability Distance measure in the distancia package:

```python
from distancia import TemporalReachabilityDistance
import networkx as nx

# Create two temporal graphs using lists of (node1, node2, timestamp) edges
edges1 = [
    (0, 1, 1), (1, 2, 2), (2, 3, 3),  # Graph 1 temporal edges
    (0, 2, 2), (1, 3, 4)
]
edges2 = [
    (0, 1, 1), (1, 2, 3), (2, 3, 4),  # Graph 2 temporal edges
    (0, 2, 2), (1, 3, 5)
]

# Initialize the distance measure
tr_distance = TemporalReachabilityDistance()

# Calculate the distance between the two temporal graphs
distance = tr_distance.compute(edges1, edges2)
print(f"Temporal Reachability Distance: {distance}")

# Optional: Get reachability matrices for specific timestamps
t = 3
reach_matrix1 = tr_distance.get_reachability_matrix(edges1, t)
reach_matrix2 = tr_distance.get_reachability_matrix(edges2, t)
```

Computational Complexity
----------------------
The computational complexity involves several components:
- Building temporal adjacency matrices: O(|E|), where |E| is the number of temporal edges
- Computing reachability for each timestamp: O(|V|³) using standard algorithms
- Total complexity: O(|T| × |V|³), where |T| is the number of timestamps

Optimizations:
- Incremental updates for streaming data
- Parallel computation for different time windows
- Sparse matrix representations for large, sparse networks
- Approximate algorithms for large-scale temporal networks

Academic References
-----------------
1. Holme, P., & Saramäki, J. (2012). Temporal networks. Physics Reports, 519(3), 97-125.

2. Kostakos, V. (2009). Temporal graphs. Physica A: Statistical Mechanics and its Applications, 388(6), 1007-1023.

3. Pan, R. K., & Saramäki, J. (2011). Path lengths, correlations, and centrality in temporal networks. Physical Review E, 84(1), 016105.

4. Wu, H., et al. (2016). Path problems in temporal graphs. Proceedings of the VLDB Endowment, 9(7), 672-683.

Conclusion
---------
The Temporal Reachability Distance provides a robust framework for comparing dynamic networks by considering the evolution of node reachability over time. This measure is particularly valuable for applications where the timing of interactions is crucial, such as epidemiology, information diffusion, and transportation networks. While computationally intensive for large networks, various optimizations and approximations make it practical for real-world applications. The measure's ability to capture both temporal and topological aspects of network evolution makes it an essential tool for analyzing dynamic systems.
