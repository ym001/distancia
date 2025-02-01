==================================
PageRank Centrality in Distancia
==================================

Introduction
-----------
The ``PageRank`` class implements a sophisticated probabilistic algorithm for measuring node importance in networks. Originally developed by Google to rank web pages, this method has become a fundamental technique for understanding node significance across various network types, from social networks to citation graphs.

Conceptual Framework
------------------
PageRank operates on the fundamental principle that a node's importance is determined by both its direct connections and the importance of nodes linking to it. The algorithm models a random walk through the network, where:

- Nodes represent network entities
- Edges represent connections or influence paths
- Importance is recursively defined through network structure
- A damping factor prevents infinite accumulation of importance

Formal Definition
---------------
The PageRank score π(v) for a node v is defined mathematically as:

.. math::

    \pi(v) = (1-d) + d \sum_{u \in N^{in}(v)} \frac{\pi(u)}{|N^{out}(u)|}

where:
- d is the damping factor (typically 0.85)
- N^{in}(v) represents nodes linking to v
- N^{out}(u) represents nodes linked from u
- (1-d) ensures a baseline importance for all nodes

Matrix formulation:

.. math::

    \pi = (1-d)\mathbf{1} + d\mathbf{P}^T\pi

where P is the column-stochastic transition probability matrix.

Implementation
-------------
.. code-block:: python

    from distancia import PageRank

    # Initialize calculator
    pr_calculator = PageRank()

    # Example directed graph
    graph = {
        'A': {'B', 'C'},
        'B': {'C'},
        'C': {'A'},
        'D': {'C'}
    }

    # Calculate PageRank
    scores = pr_calculator.calculate(
        graph, 
        damping_factor=0.85, 
        max_iterations=100, 
        convergence_threshold=1e-8
    )

Complexity Analysis
-----------------
Computational characteristics:

* Time Complexity: O(|E| * k)
  - |E|: Number of edges
  - k: Number of iterations to convergence
  - Typically k << |V|

* Space Complexity: O(|V|)
  - Linear with number of nodes
  - Efficient memory utilization

* Iterative Method: Power iteration
* Convergence: Guaranteed for strongly connected graphs

Academic References
-----------------
1. Page, L., et al. (1999). "The PageRank Citation Ranking: Bringing Order to the Web."
   Stanford InfoLab Technical Report.
   *Original PageRank formulation by Google founders.*

2. Brin, S., & Page, L. (1998). "The Anatomy of a Large-Scale Hypertextual Web Search Engine."
   Computer Networks, 30(1-7), 107-117.
   *Seminal paper introducing web ranking methodology.*

3. Langville, A. N., & Meyer, C. D. (2011). 
   "Google's PageRank and Beyond: The Science of Search Engine Rankings."
   Princeton University Press.
   *Comprehensive mathematical treatment.*

4. Gleich, D. F. (2015). "PageRank Beyond the Web."
   SIAM Review, 57(3), 321-363.
   *Extensions and applications in various domains.*

Special Considerations
---------------------
1. **Parameter Sensitivity**:
   - Damping factor (d) typically 0.85
   - Small variations can significantly impact results
   - Requires careful calibration

2. **Network Properties**:
   - Works best in strongly connected graphs
   - Handles directed and weighted networks
   - Adaptive to different network topologies

3. **Numerical Stability**:
   - Handles small graphs and massive networks
   - Convergence monitoring
   - Precision control mechanisms

Conclusion
-----------
The ``PageRank`` implementation in Distancia offers:

* Robust probabilistic node importance measurement
* Support for directed and weighted graphs
* Efficient iterative computation
* Flexible configuration options

Potential Future Enhancements:
* Parallel processing for large networks
* Adaptive damping factor selection
* Integration with community detection
* Dynamic network support

Practical Applications:
* Web page ranking
* Social network analysis
* Academic citation networks
* Recommendation systems
* Influence propagation modeling

The implementation balances computational efficiency with mathematical rigor, making it suitable for both academic research and industrial applications.
