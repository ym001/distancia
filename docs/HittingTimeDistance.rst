Hitting Time Distance
===================

A First-Passage Time Based Distance Measure for Markov Chains
---------------------------------------------------------

Introduction
-----------
The Hitting Time Distance quantifies the difference between Markov chains by comparing the expected time it takes for a random walk to first reach specific states. This measure provides valuable insights into the accessibility of states and the overall structure of the transition dynamics, making it particularly useful for analyzing state reachability and chain efficiency.

Mathematical Foundation
--------------------
The hitting time (also known as first-passage time) measures the expected number of steps needed for a Markov chain to first reach a target state when starting from any other state. This fundamental concept captures the temporal accessibility structure of the chain.

Formal Definition
---------------
For a Markov chain with transition matrix P, the hitting time h(i,j) from state i to state j is defined as:

.. math::

    h(i,j) = E[\min\{t \geq 0 : X_t = j | X_0 = i\}]

The Hitting Time Distance between two Markov chains P and Q is then defined as:

.. math::

    d_h(P,Q) = \left(\sum_{i=1}^n \sum_{j=1}^n (h_P(i,j) - h_Q(i,j))^2\right)^{1/2}

where:
- h_P(i,j) is the hitting time from state i to j in chain P
- h_Q(i,j) is the hitting time from state i to j in chain Q
- n is the number of states

Properties
---------
1. Non-negativity: d_h(P,Q) ≥ 0
2. Symmetry: d_h(P,Q) = d_h(Q,P)
3. Identity of indiscernibles: d_h(P,Q) = 0 if and only if P = Q
4. Sensitive to path structure
5. Captures directional accessibility

Implementation
------------
The measure is implemented in the `distancia` package:

.. code-block:: python

    from distancia.metrics import HittingTimeDistance
    
    # Initialize the measure
    ht_dist = HittingTimeDistance()
    
    # Calculate distance between two Markov chains
    distance = ht_dist.compute(matrix_p, matrix_q)

Usage Example
-----------
Here's a practical example comparing two Markov chains:

.. code-block:: python

    import numpy as np
    from distancia.metrics import HittingTimeDistance
    
    # Define two transition matrices
    P = np.array([[0.7, 0.2, 0.1],
                  [0.3, 0.4, 0.3],
                  [0.2, 0.3, 0.5]])
    
    Q = np.array([[0.6, 0.3, 0.1],
                  [0.2, 0.5, 0.3],
                  [0.1, 0.4, 0.5]])
    
    # Calculate hitting time distance
    ht_dist = HittingTimeDistance()
    result = ht_dist.compute(P, Q)
    print(f"Hitting Time Distance: {result:.4f}")
    
    # Access individual hitting times
    hitting_times_p = ht_dist.get_hitting_times(P)
    hitting_times_q = ht_dist.get_hitting_times(Q)

Computational Complexity
---------------------
- Time Complexity: O(n³) where n is the number of states, due to matrix inversion
- Space Complexity: O(n²) for storing hitting time matrices

The implementation includes:
1. Efficient computation using fundamental matrix method
2. Handling of absorbing states
3. Detection of unreachable states
4. Numerical stability safeguards

Academic References
----------------
1. Kemeny, J. G., & Snell, J. L. (1976). "Finite Markov Chains." Springer-Verlag.
2. Norris, J. R. (1998). "Markov Chains." Cambridge University Press.
3. Hunter, J. J. (1983). "Mathematical Techniques of Applied Probability." Academic Press.
4. Grinstead, C. M., & Snell, J. L. (2012). "Introduction to Probability." American Mathematical Society.

Conclusion
---------
The Hitting Time Distance provides a sophisticated way to compare Markov chains based on their first-passage properties. Its implementation in the `distancia` package offers researchers and practitioners a powerful tool for analyzing:
- State accessibility patterns
- Process efficiency
- Path optimization
- System bottlenecks

The measure is particularly valuable in applications where the time to reach specific states is critical, such as:
- Network routing
- Service systems
- Resource allocation
- Process optimization

See Also
--------
- Commute Time Distance
- First Passage Time Analysis
- Mean Recurrence Time
- Absorption Time Distance
