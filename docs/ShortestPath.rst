ShortestPath
============

Introduction
------------

The `ShortestPath` class is designed to compute the shortest path between two nodes in a graph. This is an essential task in many domains, such as network routing, urban planning, and game development. By leveraging Dijkstra's algorithm, the `ShortestPath` class provides an efficient way to find the minimum distance between two points in a weighted graph.

Idea
----

The shortest path problem is a fundamental problem in graph theory and computer science. Given a graph where nodes represent points and edges represent connections between these points with associated weights, the goal is to find the path between two nodes that minimizes the total weight. Dijkstra's algorithm is one of the most popular solutions to this problem. It systematically explores paths from the starting node, expanding the least costly paths first, ensuring that once a node's shortest path is found, it is optimal.

This approach is particularly useful in scenarios where real-time decision-making is crucial, such as in GPS navigation systems or network traffic optimization.

Example
-------

Here is a simple example of how to use the `ShortestPath` class:

.. code-block:: python

    # Define a graph using a dictionary
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # Initialize the ShortestPath class with the graph
    shortest_path_calculator = ShortestPath(graph)

    # Compute the shortest path distance between nodes 'A' and 'D'
    distance = shortest_path_calculator.get_shortest_path('A', 'D')
    print(f"The shortest path distance between A and D is: {distance}")

.. code-block:: python

    La distance du plus court chemin entre A et D est : 4

In this example, the graph is defined with nodes 'A', 'B', 'C', and 'D'. The ShortestPath class calculates the shortest distance from node 'A' to node 'D', which in this case would be 4.

Academic Reference
The shortest path problem and Dijkstra's algorithm are well-established concepts in the field of computer science. For further reading, refer to:

Dijkstra, E. W. (1959). A Note on Two Problems in Connexion with Graphs. Numerische Mathematik, 1, 269-271.

This paper introduces the algorithm that efficiently solves the single-source shortest path problem, which is fundamental in various applications such as network routing, geographical mapping, and more.

Conclusion
The ShortestPath class provides a robust and efficient solution to finding the shortest path in weighted graphs. By incorporating Dijkstra's algorithm, it guarantees optimal results for non-negative weights, making it a valuable tool in many practical applications. This class is a crucial component for users who need to solve routing and navigation problems, ensuring that they can compute the shortest distances accurately and efficiently.

Whether used in transportation systems, network design, or any other field requiring optimal pathfinding, the ShortestPath class offers a dependable solution for your shortest path computation needs.
