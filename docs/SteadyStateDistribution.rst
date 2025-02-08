Steady-State Distribution Distance
================================

A Distance Measure for Long-term Markov Chain Behavior
---------------------------------------------------

Introduction
-----------
The Steady-State Distribution Distance quantifies the difference between two Markov chains by comparing their equilibrium distributions. This measure is particularly valuable when the long-term behavior of the processes is of primary interest, as it captures fundamental differences in the asymptotic properties of the chains, regardless of their initial states.

Mathematical Foundation
--------------------
The measure is based on the principle that every irreducible and aperiodic Markov chain converges to a unique steady-state (or stationary) distribution. By comparing these limiting distributions, we can assess how different two Markov processes are in their long-term behavior.

Formal Definition
---------------
For two Markov chains with transition matrices P and Q, let π_P and π_Q be their respective steady-state distributions. The distance is defined as:

.. math::

    d_{ss}(P, Q) = ||\pi_P - \pi_Q||_1 = \sum_{i=1}^n |\pi_P(i) - \pi_Q(i)|

where:
- π_P and π_Q are the steady-state probability vectors
- ||·||₁ denotes the L1-norm (Manhattan distance)
- n is the number of states in the Markov chains

Properties
---------
1. Non-negativity: d_ss(P,Q) ≥ 0
2. Symmetry: d_ss(P,Q) = d_ss(Q,P)
3. Identity of indiscernibles: d_ss(P,Q) = 0 if and only if π_P = π_Q
4. Triangle inequality: d_ss(P,R) ≤ d_ss(P,Q) + d_ss(Q,R)
5. Bounded: d_ss(P,Q) ≤ 2 for probability distributions

Implementation
------------
The measure is implemented in the `distancia` package:

.. code-block:: python

    from distancia.metrics import SteadyStateDistance
    
    # Initialize the measure
    ss_dist = SteadyStateDistance()
    
    # Calculate distance between two Markov chains
    distance = ss_dist.compute(matrix_p, matrix_q)

Usage Example
-----------
Here's a practical example comparing two Markov chains:

.. code-block:: python

    import numpy as np
    from distancia.metrics import SteadyStateDistance
    
    # Define two transition matrices
    P = np.array([[0.9, 0.1],
                  [0.3, 0.7]])
    
    Q = np.array([[0.7, 0.3],
                  [0.4, 0.6]])
    
    # Calculate steady-state distance
    ss_dist = SteadyStateDistance()
    result = ss_dist.compute(P, Q)
    print(f"Steady-State Distance: {result:.4f}")
    
    # Access the computed steady-state distributions
    pi_p = ss_dist.get_steady_state(P)
    pi_q = ss_dist.get_steady_state(Q)

Computational Complexity
---------------------
- Time Complexity: O(n³) where n is the number of states, due to eigenvalue computation
- Space Complexity: O(n²) for storing matrices and intermediate calculations

The implementation uses efficient numerical methods for computing steady-state distributions:
1. Eigenvalue decomposition method for smaller matrices
2. Power iteration method for larger, sparse matrices
3. Linear system solving for specific cases

Academic References
----------------
1. Norris, J. R. (1998). "Markov Chains." Cambridge University Press.
2. Meyer, C. D. (2000). "Matrix Analysis and Applied Linear Algebra." SIAM.
3. Levin, D. A., & Peres, Y. (2017). "Markov Chains and Mixing Times." American Mathematical Society.
4. Kemeny, J. G., & Snell, J. L. (1976). "Finite Markov Chains." Springer-Verlag.

Conclusion
---------
The Steady-State Distribution Distance provides a meaningful way to compare Markov chains based on their long-term behavior. Its implementation in the `distancia` package offers researchers and practitioners a reliable tool for analyzing asymptotic properties of stochastic processes. This measure is particularly useful in applications where the transient behavior is less important than the eventual equilibrium state, such as in:
- Social network analysis
- Economic modeling
- Population dynamics
- Queuing systems

See Also
--------
- Matrix Divergence
- Spectral Norm Distance
- Total Variation Distance
- Equilibrium Analysis
