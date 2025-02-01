===================================
Edge Betweenness Distance
===================================

Introduction
-----------
Edge betweenness distance is a graph similarity metric that quantifies the structural difference between two graphs by comparing the edge betweenness centrality distributions. Edge betweenness centrality measures the importance of edges in a network by counting the number of shortest paths passing through each edge. This distance metric is particularly useful in analyzing how information flows differently between two network structures.

Formal Definition
---------------
For two graphs G1 and G2, the edge betweenness distance is computed by:

Let eb(e) be the edge betweenness centrality of edge e
Let EB(G) be the normalized distribution of edge betweenness values for graph G

The distance is defined as:

D(G1, G2) = ||EB(G1) - EB(G2)||

where ||·|| represents a suitable norm (typically L1 or L2) between the distributions.

Intuition and Significance
------------------------
The edge betweenness distance captures differences in:
* Network flow patterns
* Critical communication pathways
* Load distribution across network edges
* Structural bottlenecks

This makes it particularly valuable for:
* Comparing information flow in social networks
* Analyzing changes in transportation networks
* Detecting structural similarities in biological networks

Computational Complexity
----------------------
The computational complexity is dominated by the edge betweenness calculation:
* O(|V||E|) for unweighted graphs
* O(|V||E| + |V|^2 log|V|) for weighted graphs

where |V| is the number of vertices and |E| is the number of edges.

Academic References
-----------------
1. Freeman, L.C. (1977). "A set of measures of centrality based on betweenness." Sociometry, 40(1), 35-41.
2. Girvan, M., & Newman, M. E. J. (2002). "Community structure in social and biological networks." Proceedings of the National Academy of Sciences, 99(12), 7821-7826.
3. Brandes, U. (2001). "A faster algorithm for betweenness centrality." Journal of Mathematical Sociology, 25(2), 163-177.

Conclusion
---------
Edge betweenness distance provides a sophisticated way to compare graph structures by focusing on the role of edges in facilitating network flow. While computationally intensive, it offers valuable insights into structural similarities and differences between networks, particularly in cases where the pattern of information flow is of primary interest.

The metric is especially powerful when combined with other graph distance measures to provide a comprehensive view of network similarity.
