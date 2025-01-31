=====================================
Closeness Centrality in Distancia
=====================================

Introduction
-----------
The ``ClosenessCentrality`` class implements a fundamental network measure that quantifies how efficiently a node can reach all other nodes in a network. This metric is crucial for understanding information flow, accessibility, and node importance in networks ranging from social networks to transportation systems.

Conceptual Framework
------------------
Closeness centrality measures the reciprocal of the sum of shortest path distances to all other nodes. Higher values indicate nodes that can efficiently spread information or influence through the network. The metric is particularly useful for:

- Identifying optimal locations in physical networks
- Finding influential spreaders in social networks
- Analyzing accessibility in transportation networks
- Understanding information dissemination patterns

Formal Definition
---------------
For a graph G = (V,E), the closeness centrality C(v) of a vertex v is defined as:

.. math::

    C(v) = \frac{n - 1}{\sum_{u \in V\setminus\{v\}} d(v,u)}

where:
- n is the number of nodes in the graph
- d(v,u) is the shortest path distance between nodes v and u

For weighted graphs:

.. math::

    C_w(v) = \frac{n - 1}{\sum_{u \in V\setminus\{v\}} d_w(v,u)}

where d_w(v,u) represents the weighted shortest path distance.

For disconnected graphs, the harmonic centrality version is used:

.. math::

    C_H(v) = \frac{1}{n-1}\sum_{u \in V\setminus\{v\}} \frac{1}{d(v,u)}

Implementation
-------------
.. code-block:: python

    from distancia import ClosenessCentrality

    # Initialize calculator
    calculator = ClosenessCentrality()

    # Example graph
    graph = {
        'A': {'B': 1.0, 'C': 2.0},
        'B': {'C': 1.5, 'D': 1.0},
        'C': {'D': 2.0},
        'D': {}
    }

    # Calculate closeness centrality
    centrality = calculator.calculate(graph, harmonic=False)
    harmonic_centrality = calculator.calculate(graph, harmonic=True)

Complexity Analysis
-----------------
The implementation uses Dijkstra's algorithm for each node with the following complexities:

* Unweighted graphs: O(|V|(|E| + |V| log|V|))
* Weighted graphs: O(|V|(|E| + |V| log|V|))

Space complexity: O(|V|)

Academic References
-----------------
1. Sabidussi, G. (1966). "The centrality index of a graph."
   Psychometrika, 31(4), 581-603.
   *Original formulation of closeness centrality.*

2. Freeman, L. C. (1979). "Centrality in social networks: Conceptual clarification."
   Social Networks, 1(3), 215-239.
   *Foundational work on centrality measures.*

3. Rochat, Y. (2009). "Closeness centrality extended to unconnected graphs: The harmonic centrality index."
   Applications of Social Network Analysis.
   *Introduction of harmonic centrality.*

4. Opsahl, T., Agneessens, F., & Skvoretz, J. (2010).
   "Node centrality in weighted networks: Generalizing degree and shortest paths."
   Social Networks, 32(3), 245-251.
   *Extension to weighted networks.*

Special Cases and Considerations
-----------------------------
1. **Disconnected Graphs**:
   - Harmonic centrality handles disconnected components
   - Traditional closeness undefined for disconnected graphs
   - Infinity values handled appropriately

2. **Edge Cases**:
   - Single node: centrality = 0
   - Star network: center has maximum centrality
   - Complete graph: all nodes have equal centrality

3. **Numerical Considerations**:
   - Normalization by (n-1) for comparability
   - Handling of zero distances
   - Precision issues in large networks

Conclusion
---------
The ``ClosenessCentrality`` implementation in Distancia provides:

* Efficient calculation using optimized shortest path algorithms
* Support for both weighted and unweighted graphs
* Harmonic centrality for disconnected graphs
* Robust handling of special cases
* Numerically stable computations

Future enhancements could include:
* Parallel computation for large networks
* Approximate algorithms for massive graphs
* Dynamic updates for evolving networks
* Specialized versions for directed networks

Use cases:
* Network topology analysis
* Identifying optimal facility locations
* Social influence analysis
* Transportation network planning

The implementation strikes a balance between computational efficiency and mathematical rigor, making it suitable for both research and practical applications in network analysis.
