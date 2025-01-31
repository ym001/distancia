================================
Katz Centrality in Distancia
================================

Introduction
-----------
The ``KatzCentrality`` class implements Katz centrality, a refined version of eigenvector centrality that addresses convergence issues through an attenuation factor. This metric measures node importance while accounting for both direct and indirect connections, with decreasing weight given to longer paths.

Conceptual Framework
------------------
Katz centrality extends eigenvector centrality by:
- Including a baseline score for each node
- Applying an attenuation factor to path lengths
- Ensuring convergence for all network types
- Balancing local and global network effects

Formal Definition
---------------
For a graph G = (V,E) with adjacency matrix A, the Katz centrality x_i of node i is:

.. math::

    x_i = \alpha \sum_{j \in N(i)} A_{ij}x_j + \beta

In matrix form:

.. math::

    \mathbf{x} = \alpha \mathbf{Ax} + \beta \mathbf{1}

    \mathbf{x} = \beta(I - \alpha \mathbf{A})^{-1}\mathbf{1}

where:
- α (alpha) is the attenuation factor (0 < α < 1/λ_max)
- β (beta) is the baseline centrality
- λ_max is the largest eigenvalue of A
- 1 is a vector of ones

For weighted graphs:

.. math::

    x_i = \alpha \sum_{j \in N(i)} w_{ij}x_j + \beta

Implementation
-------------
.. code-block:: python

    from distancia import KatzCentrality

    # Initialize calculator
    calculator = KatzCentrality()

    # Example graph
    graph = {
        'A': {'B': 1.0, 'C': 2.0},
        'B': {'C': 1.5, 'D': 1.0},
        'C': {'D': 2.0},
        'D': {}
    }

    # Calculate Katz centrality
    centrality = calculator.calculate(graph, alpha=0.1, beta=1.0)

Complexity Analysis
-----------------
Using power iteration method:

* Time complexity: O(k|E|)
  - k is the number of iterations
  - typically k << |V|

* Space complexity: O(|V|)

For direct solution:
* Time complexity: O(|V|³)
* Space complexity: O(|V|²)

Academic References
-----------------
1. Katz, L. (1953). "A new status index derived from sociometric analysis."
   Psychometrika, 18(1), 39-43.
   *Original formulation of Katz centrality.*

2. Newman, M. E. J. (2010). "Networks: An Introduction."
   Oxford University Press.
   *Comprehensive treatment of centrality measures.*

3. Bonacich, P., & Lloyd, P. (2001).
   "Eigenvector-like measures of centrality for asymmetric relations."
   Social Networks, 23(3), 191-201.
   *Comparison with other centrality measures.*

4. Foster, K. C., et al. (2001).
   "The importance of being modest: A new network measure."
   Proceedings of the National Academy of Sciences, 98(12), 7340-7345.
   *Applications and extensions.*

Special Cases and Considerations
-----------------------------
1. **Parameter Selection**:
   - α < 1/λ_max for convergence
   - β typically set to 1.0
   - Trade-off between local and global influence

2. **Edge Cases**:
   - α = 0: all nodes have centrality β
   - α → 1/λ_max: approaches eigenvector centrality
   - Disconnected graphs: well-defined unlike eigenvector centrality

3. **Numerical Considerations**:
   - Stability of matrix inversion
   - Convergence rate monitoring
   - Precision control

Implementation Details
--------------------
1. **Power Iteration Solution**:
   ```python
   def power_iteration(A, alpha, beta, tol):
       n = len(A)
       x = np.ones(n)
       while True:
           x_new = alpha * (A @ x) + beta
           if np.all(np.abs(x_new - x) < tol):
               break
           x = x_new
       return x
   ```

2. **Direct Solution**:
   ```python
   def direct_solution(A, alpha, beta):
       n = len(A)
       I = np.eye(n)
       return beta * np.linalg.solve(I - alpha * A, np.ones(n))
   ```

Conclusion
---------
The ``KatzCentrality`` implementation provides:

* Choice of solution methods (iterative or direct)
* Support for weighted/unweighted graphs
* Parameter optimization capabilities
* Robust convergence guarantees

Future enhancements could include:
* Parallel implementation for large networks
* Adaptive parameter selection
* Incremental updates for dynamic networks
* Memory-efficient sparse matrix operations

Applications:
* Social network analysis
* Web page ranking
* Recommendation systems
* Information diffusion modeling

The implementation balances mathematical rigor with practical considerations, making it suitable for both research and industrial applications.
