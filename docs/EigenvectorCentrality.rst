======================================
Eigenvector Centrality in Distancia
======================================

Introduction
-----------
The ``EigenvectorCentrality`` class implements a sophisticated measure of node importance that considers both direct and indirect connections in a network. Unlike simpler centrality measures, eigenvector centrality recursively defines a node's importance based on the importance of its neighbors, making it particularly valuable for understanding influence and prestige in networks.

Conceptual Framework
------------------
Eigenvector centrality extends the concept of degree centrality by incorporating the quality of connections. A node's centrality is proportional to the sum of the centralities of its neighbors. This recursive definition leads to:
- High scores for nodes connected to other important nodes
- Recognition of influential network positions
- Identification of prestige in social networks
- Understanding of cascading effects in networks

Formal Definition
---------------
For a graph G = (V,E) with adjacency matrix A, the eigenvector centrality x_i of node i is given by:

.. math::

    x_i = \frac{1}{\lambda} \sum_{j \in N(i)} A_{ij}x_j

In matrix form:

.. math::

    \mathbf{Ax} = \lambda\mathbf{x}

where:
- λ is the largest eigenvalue of A
- x is the corresponding eigenvector
- A_{ij} is the (i,j)th entry of the adjacency matrix

For weighted graphs:

.. math::

    x_i = \frac{1}{\lambda} \sum_{j \in N(i)} w_{ij}x_j

Implementation
-------------
.. code-block:: python

    from distancia import EigenvectorCentrality

    # Initialize calculator
    calculator = EigenvectorCentrality()

    # Example graph
    graph = {
        'A': {'B': 1.0, 'C': 2.0},
        'B': {'C': 1.5, 'D': 1.0},
        'C': {'D': 2.0},
        'D': {}
    }

    # Calculate eigenvector centrality
    centrality = calculator.calculate(graph, max_iter=100, tol=1e-6)

Complexity Analysis
-----------------
Using power iteration method:

* Time complexity: O(k|E|)
  - k is the number of iterations
  - typically k << |V|

* Space complexity: O(|V|)

For dense graphs:
* Time complexity: O(k|V|²)

Academic References
-----------------
1. Bonacich, P. (1972). "Factoring and weighting approaches to status scores and clique identification."
   Journal of Mathematical Sociology, 2(1), 113-120.
   *Original formulation of eigenvector centrality.*

2. Newman, M. E. J. (2008). "The mathematics of networks."
   The New Palgrave Encyclopedia of Economics, 2, 1-12.
   *Comprehensive mathematical treatment.*

3. Langville, A. N., & Meyer, C. D. (2005).
   "A survey of eigenvector methods for web information retrieval."
   SIAM Review, 47(1), 135-161.
   *Applications and computational aspects.*

4. Perra, N., & Fortunato, S. (2008).
   "Spectral centrality measures in complex networks."
   Physical Review E, 78(3), 036107.
   *Theoretical analysis and comparisons.*

Special Cases and Considerations
-----------------------------
1. **Convergence Issues**:
   - Guaranteed for connected, non-bipartite graphs
   - May require damping for disconnected graphs
   - Special handling for directed graphs

2. **Edge Cases**:
   - Single node: centrality = 1
   - Symmetric star: center has maximum centrality
   - Regular graph: all nodes have equal centrality

3. **Numerical Stability**:
   - Normalization after each iteration
   - Handling of floating-point arithmetic
   - Convergence criteria selection

Algorithm Implementation Details
-----------------------------
1. **Power Iteration Method**:
   ```python
   def power_iteration(A, max_iter, tol):
       n = len(A)
       x = np.ones(n) / np.sqrt(n)
       for _ in range(max_iter):
           x_new = A @ x
           x_new /= np.linalg.norm(x_new)
           if np.all(np.abs(x_new - x) < tol):
               break
           x = x_new
       return x
   ```

2. **Key Features**:
   - Sparse matrix operations
   - Convergence monitoring
   - Numerical stability checks
   - Error handling

Conclusion
---------
The ``EigenvectorCentrality`` implementation provides:

* Efficient computation using power iteration
* Support for weighted and unweighted graphs
* Robust convergence handling
* Numerical stability safeguards

Future enhancements could include:
* Parallel implementation for large networks
* Alternative eigenvalue computation methods
* Dynamic updates for evolving networks
* Specialized versions for directed networks

Applications:
* Ranking algorithms
* Influence analysis
* Resource allocation
* Network vulnerability assessment

The implementation balances computational efficiency with numerical stability, making it suitable for both research and practical applications in network analysis.
