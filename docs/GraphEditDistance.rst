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

.. code-block:: python

      from distancia import GraphEditDistance

      g1 = Graph(directed=False, weighted=True)
    
        # Add some edges
        g1.add_edge("A", "B", 4)
        g1.add_edge("B", "C", 3)
        g1.add_edge("C", "D", 2)
        g1.add_edge("D", "A", 5)
        
        g2 = Graph(directed=False, weighted=True)
    
        # Add some edges
        g2.add_edge("A", "B", 4)
        g2.add_edge("C", "D", 2)
        g2.add_edge("D", "A", 5)
        
        #graph=Graph(Graph.nodes_1,Graph.edges_1)
        distance=self.compute(g1,g2)
        print(f"{self.__class__.__name__} distance between {g2} in {g1} is {distance:.2f}")

This will output the total number of node and edge edits needed to transform graph1 into graph2.

.. code-block:: bash

      GraphEditDistance distance between <distancia.tools.Graph object at 0x7f78d3640090> in <distancia.tools.Graph object at 0x7f78d3275790> is 7.00


Academic Reference
-----------------

:footcite:t:`GraphEditDistance`

.. footbibliography::


Conclusion
----------
      
The Graph Edit Distance is an essential tool for comparing the structural similarity of graphs, allowing for the identification of subtle differences in their topology. Its flexibility in accommodating various types of edit operations makes it applicable to a wide range of domains, including machine learning, bioinformatics, and network analysis. The GraphEditDistance class in the distancia package provides a straightforward implementation of this metric, enabling users to compute GED for their graph-based data efficiently.

This class can be further extended to handle more complex graphs, including those with labeled nodes and edges, weighted edges, and directed graphs, providing even greater versatility and power in graph analysis.
