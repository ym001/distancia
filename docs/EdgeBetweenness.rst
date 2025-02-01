Edge Betweenness Distance
=========================

Introduction
------------

The **Edge Betweenness Distance** is a graph similarity measure that evaluates the structural difference between two graphs based on **edge betweenness centrality**. Edge betweenness measures the number of shortest paths that traverse a given edge. This metric provides insight into how edges contribute to information flow and connectivity within a network. Comparing graphs using this measure allows for a nuanced understanding of their topological differences.

Definition and Formalism
------------------------

Given a graph \( G = (V, E) \), the **edge betweenness centrality** of an edge \( e \in E \) is defined as:

\[
EB(e) = \sum_{s \neq t} \frac{\sigma_{s,t}(e)}{\sigma_{s,t}}
\]

where:
- \( \sigma_{s,t} \) is the total number of shortest paths between nodes \( s \) and \( t \),
- \( \sigma_{s,t}(e) \) is the number of those shortest paths that pass through edge \( e \).

To compare two graphs \( G_1 \) and \( G_2 \), the **Edge Betweenness Distance** is computed as:

\[
D_{EB}(G_1, G_2) = \sum_{e \in E} |EB_{G_1}(e) - EB_{G_2}(e)|
\]

where \( EB_{G_1}(e) \) and \( EB_{G_2}(e) \) are the edge betweenness values of edge \( e \) in graphs \( G_1 \) and \( G_2 \), respectively.

Computational Complexity
-------------------------

Computing **edge betweenness centrality** for a single edge requires computing shortest paths between all pairs of nodes. Using **Brandes' algorithm**, the complexity for a graph with \( n \) nodes and \( m \) edges is:

\[
O(nm)
\]

Thus, computing the **Edge Betweenness Distance** for two graphs requires **O(nm)** operations per graph, making it feasible for moderate-sized networks but expensive for large-scale applications.

Academic Reference
-------------------

This measure is inspired by the **Edge Betweenness Centrality** introduced by:

L. C. Freeman, "A Set of Measures of Centrality Based on Betweenness," *Sociometry*, vol. 40, no. 1, pp. 35–41, 1977.

For an application of edge betweenness in graph comparison, see:

M. Girvan and M. E. J. Newman, "Community structure in social and biological networks," *PNAS*, vol. 99, no. 12, pp. 7821–7826, 2002.

Conclusion
----------

The **Edge Betweenness Distance** provides a powerful way to compare graph structures by leveraging the importance of edges in shortest-path routing. While computationally intensive, it is particularly useful in network analysis, bioinformatics, and social network studies. Future optimizations, such as approximating shortest paths, could improve its scalability.

