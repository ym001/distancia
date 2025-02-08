Commute Time Distance
===================

A Random Walk-Based Distance Measure for Markov Chains
--------------------------------------------------

Introduction
-----------
The Commute Time Distance provides a dynamic approach to comparing Markov chains by measuring the expected time for random walks to travel between states. This measure is particularly valuable for understanding the accessibility and connectivity structure of states within stochastic processes, offering insights into both local and global chain properties.

Mathematical Foundation
--------------------
The measure is based on the concept of commute time in random walks, which is the expected number of steps needed to go from state i to state j and return to state i. This captures both the direct and indirect connections between states, providing a robust measure of their relative "closeness" in the Markov chain.

Formal Definition
---------------
For two states i and j in a Markov chain with transition matrix P, the commute time distance is defined as:

.. math::

    c(i,j) = h(i,j) + h(j,i)

where:
- c(i,j) is the commute time between states i and j
- h(i,j) is the hitting time from state i to j
- h(j,i) is the hitting time from state j to i

For comparing two Markov chains P and Q, we use:

.. math::

    d_{ct}(P,Q) = \left(\sum_{i=1}^n \sum_{j=1}^n (c_P(i,j) - c_Q(i,j))^2\right)^{1/2}

Properties
---------
1. Non-negativity: d_ct(P,Q) ≥ 0
2. Symmetry: d_ct(P,Q) = d_ct(Q,P)
3. Identity of indiscernibles: d_ct(P,Q) = 0 if and only if P = Q
4. Captures global chain structure
5. Robust to local perturbations

Implementation
------------
The measure is implemented in the `distancia` package:

.. code-block:: python

    from distancia.metrics import CommuteTimeDistance
    
    # Initialize the measure
    ct_dist = CommuteTimeDistance()
    
    # Calculate distance between two Markov chains
    distance = ct_dist.compute(matrix_p, matrix_q)

Usage Example
-----------
Here's a practical example comparing two Markov chains:

.. code-block:: python

    import numpy as np
    from distancia.metrics import CommuteTimeDistance
    
    # Define two transition matrices
    P = np.array([[0.6, 0.3, 0.1],
                  [0.2, 0.5, 0.3],
                  [0.1, 0.2, 0.7]])
    
    Q = np.array([[0.5, 0.4, 0.1],
                  [0.3, 0.4, 0.3],
                  [0.1, 0.3, 0.6]])
    
    # Calculate commute time distance
    ct_dist = CommuteTimeDistance()
    result = ct_dist.compute(P, Q)
    print(f"Commute Time Distance: {result:.4f}")
    
    # Access individual commute times
    commute_times_p = ct_dist.get_commute_times(P)
    commute_times_q = ct_dist.get_commute_times(Q)

Computational Complexity
---------------------
- Time Complexity: O(n³) where n is the number of states, due to matrix operations
- Space Complexity: O(n²) for storing distance matrices and intermediate results

The implementation includes:
1. Efficient computation of fundamental matrix
2. Optimized hitting time calculations
3. Handling of reducible chains
4. Numerical stability considerations

Academic References
----------------
1. Aldous, D., & Fill, J. (2002). "Reversible Markov Chains and Random Walks on Graphs."
2. Lovász, L. (1993). "Random Walks on Graphs: A Survey." Combinatorics, Paul Erdős is Eighty.
3. Fouss, F., et al. (2007). "Random-Walk Computation of Similarities between Nodes of a Graph with Application to Collaborative Recommendation." IEEE TKDE.
4. Pons, P., & Latapy, M. (2005). "Computing Communities in Large Networks Using Random Walks."

Conclusion
---------
The Commute Time Distance provides a sophisticated way to compare Markov chains based on their random walk properties. Its implementation in the `distancia` package offers researchers and practitioners a powerful tool for analyzing:
- Network accessibility
- State connectivity patterns
- Community structure
- Mixing properties

The measure is particularly valuable in applications where the dynamic behavior and connectivity structure of the processes are of primary interest.

See Also
--------
- Hitting Time Distance
- Random Walk Distance
- Resistance Distance
- Mixing Time Distance
