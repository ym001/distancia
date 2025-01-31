=======================================
Betweenness Centrality in Distancia
=======================================

Introduction
-----------
The ``BetweennessCentrality`` class implements a fundamental network analysis metric that quantifies the importance of nodes in a graph based on their role in connecting other nodes. This implementation supports both weighted and unweighted graphs, making it versatile for various network analysis applications.

Conceptual Framework
------------------
Betweenness centrality measures the extent to which a node lies on paths between other nodes. Nodes with high betweenness centrality act as bridges or gatekeepers in the network, often representing critical points of control over information flow or resource distribution.

Key aspects measured:
- Path intermediacy
- Network flow control
- Information bottlenecks
- Structural bridges

Formal Definition
---------------
For a graph G = (V,E), the betweenness centrality BC(v) of a vertex v is defined as:

.. math::

    BC(v) = \sum_{s \neq v \neq t \in V} \frac{\sigma_{st}(v)}{\sigma_{st}}

where:
- σₛₜ is the total number of shortest paths between nodes s and t
- σₛₜ(v) is the number of shortest paths between s and t that pass through v

For weighted graphs, the formula incorporates edge weights:

.. math::

    BC_w(v) = \sum_{s \neq v \neq t \in V} \frac{\sigma_{st}(v)}{w_{st}}

where w_{st} represents the weight of the shortest path between s and t.

Normalized betweenness centrality is scaled by:

.. math::

    BC_{norm}(v) = \frac{2}{(n-1)(n-2)} BC(v)

where n is the number of nodes in the graph.

Implementation
-------------
.. code-block:: python

    from distancia import BetweennessCentrality

    # Initialize calculator
    calculator = BetweennessCentrality()

    # Example graph
    graph = {
        'A': {'B': 1.0, 'C': 2.0},
        'B': {'C': 1.5, 'D': 1.0},
        'C': {'D': 2.0},
        'D': {}
    }

    # Calculate betweenness centrality
    centrality = calculator.calculate(graph, normalized=True)

Complexity Analysis
-----------------
The implementation uses Brandes' algorithm with the following complexities:

* Unweighted graphs: O(|V||E|)
* Weighted graphs: O(|V||E| + |V|² log|V|)

Space complexity: O(|V| + |E|)

where |V| is the number of vertices and |E| is the number of edges.

Academic References
-----------------
1. Brandes, U. (2001). "A faster algorithm for betweenness centrality."
   Journal of Mathematical Sociology, 25(2), 163-177.
   *Presents the efficient algorithm used in this implementation.*

2. Freeman, L. C. (1977). "A set of measures of centrality based on betweenness."
   Sociometry, 40(1), 35-41.
   *Introduces the concept of betweenness centrality.*

3. Newman, M. E. J. (2010). "Networks: An Introduction."
   Oxford University Press.
   *Comprehensive overview of network centrality measures.*

4. Opsahl, T., Agneessens, F., & Skvoretz, J. (2010).
   "Node centrality in weighted networks: Generalizing degree and shortest paths."
   Social Networks, 32(3), 245-251.
   *Extends betweenness centrality to weighted networks.*

Special Cases and Considerations
-----------------------------
1. **Disconnected Graphs**:
   - Handled by treating disconnected components separately
   - Infinity values avoided in path calculations

2. **Edge Cases**:
   - Single-node graphs: BC = 0
   - Star networks: Center node has maximum BC
   - Complete graphs: All nodes have BC = 0

3. **Numerical Stability**:
   - Large networks handled with appropriate scaling
   - Accumulation of floating-point errors minimized

Conclusion
---------
The ``BetweennessCentrality`` implementation in Distancia provides:

* Efficient calculation using Brandes' algorithm
* Support for both weighted and unweighted graphs
* Optional normalization
* Robust handling of special cases
* Numerically stable computations

Future enhancements could include:
* Parallel computation for large networks
* Approximation algorithms for massive graphs
* Specialized versions for specific network types
* Dynamic updates for evolving networks

The implementation balances computational efficiency with mathematical rigor, making it suitable for both research and practical applications in network analysis.
