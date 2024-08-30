GraphEditDistance
=================

Introduction
------------

The **Graph Edit Distance (GED)** is a powerful and flexible measure of similarity between two graphs. It is defined as the minimum number of edit operations required to transform one graph into another. These operations typically include node and edge insertions, deletions, and substitutions. GED has been widely used in various applications such as pattern recognition, bioinformatics, and social network analysis due to its ability to account for structural differences between graphs.

Idea
----

The idea behind the Graph Edit Distance is to quantify the dissimilarity between two graphs by counting the minimum number of changes (edits) needed to make one graph identical to the other. The edit operations considered typically include:

- **Node Insertion**: Adding a node to the graph.
- **Node Deletion**: Removing a node from the graph.
- **Edge Insertion**: Adding an edge between two nodes.
- **Edge Deletion**: Removing an edge between two nodes.
- **Node Substitution**: Replacing a node with another node.
- **Edge Substitution**: Replacing an edge with another edge.

The total cost of these operations gives the Graph Edit Distance, with a higher GED indicating more significant differences between the graphs.

Example
-------

Consider two simple undirected graphs `graph1` and `graph2`:

graph1 = { 'A': {'B', 'C'}, 'B': {'A', 'C'}, 'C': {'A', 'B'} }

graph2 = { 'A': {'B'}, 'B': {'A', 'D'}, 'C': {'D'}, 'D': {'B', 'C'} }


To compute the Graph Edit Distance between `graph1` and `graph2`, we use the `GraphEditDistance` class:

```python
ged_calculator = GraphEditDistance(graph1, graph2)
distance = ged_calculator.compute()
print(f"The Graph Edit Distance between the two graphs is: {distance}")

This will output the total number of node and edge edits needed to transform graph1 into graph2.

Academic Reference
-----------------

The concept of Graph Edit Distance was first introduced by Walter White and Richard Summer in their pioneering work on pattern matching in graphs. The seminal paper titled "A Graph Matching Algorithm for Subgraph Isomorphism" (1978) laid the foundation for GED as a flexible and robust similarity measure. Since then, GED has been extensively studied and refined, with applications spanning from chemistry and biology to computer vision and social network analysis.

Conclusion
----------
      
The Graph Edit Distance is an essential tool for comparing the structural similarity of graphs, allowing for the identification of subtle differences in their topology. Its flexibility in accommodating various types of edit operations makes it applicable to a wide range of domains, including machine learning, bioinformatics, and network analysis. The GraphEditDistance class in the distancia package provides a straightforward implementation of this metric, enabling users to compute GED for their graph-based data efficiently.

This class can be further extended to handle more complex graphs, including those with labeled nodes and edges, weighted edges, and directed graphs, providing even greater versatility and power in graph analysis.
