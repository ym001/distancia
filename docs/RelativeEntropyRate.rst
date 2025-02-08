Relative Entropy Rate
===================

An Information-Theoretic Distance Measure for Markov Chains
-------------------------------------------------------

Introduction
-----------
The Relative Entropy Rate provides an information-theoretic approach to comparing Markov chains by measuring the divergence between their entropy rates. This measure captures the fundamental differences in the information content and predictability of the processes, making it particularly valuable for analyzing the complexity and predictability differences between stochastic processes.

Mathematical Foundation
--------------------
The measure is based on the concept of entropy rate, which quantifies the average amount of information produced by a stochastic process per unit time. The relative entropy rate extends this to measure how different two processes are in terms of their information generation.

Formal Definition
---------------
For two Markov chains P and Q with stationary distributions π_P and π_Q, the relative entropy rate is defined as:

.. math::

    h(P||Q) = \sum_{i=1}^n \sum_{j=1}^n \pi_P(i)p_{ij}\log\left(\frac{p_{ij}}{q_{ij}}\right)

where:
- p_ij and q_ij are transition probabilities
- π_P(i) is the stationary probability of state i in chain P
- n is the number of states
- The logarithm is typically taken with base 2 (for bits) or e (for nats)

Properties
---------
1. Non-negativity: h(P||Q) ≥ 0
2. Asymmetry: Generally h(P||Q) ≠ h(Q||P)
3. h(P||Q) = 0 if and only if P = Q
4. Chain rule decomposition
5. Convexity in probability space

Implementation
------------
The measure is implemented in the `distancia` package:

.. code-block:: python

    from distancia.metrics import RelativeEntropyRate
    
    # Initialize the measure
    rer_dist = RelativeEntropyRate()
    
    # Calculate distance between two Markov chains
    distance = rer_dist.compute(matrix_p, matrix_q)

Usage Example
-----------
Here's a practical example comparing two Markov chains:

.. code-block:: python

    import numpy as np
    from distancia.metrics import RelativeEntropyRate
    
    # Define two transition matrices
    P = np.array([[0.7, 0.2, 0.1],
                  [0.1, 0.8, 0.1],
                  [0.2, 0.1, 0.7]])
    
    Q = np.array([[0.6, 0.3, 0.1],
                  [0.2, 0.7, 0.1],
                  [0.1, 0.2, 0.7]])
    
    # Calculate relative entropy rate
    rer_dist = RelativeEntropyRate()
    result = rer_dist.compute(P, Q)
    print(f"Relative Entropy Rate: {result:.4f}")
    
    # Access individual entropy rates
    h_p = rer_dist.get_entropy_rate(P)
    h_q = rer_dist.get_entropy_rate(Q)

Computational Complexity
---------------------
- Time Complexity: O(n³) where n is the number of states
- Space Complexity: O(n²) for storing matrices and intermediate calculations

The implementation includes:
1. Efficient computation of stationary distributions
2. Handling of zero transition probabilities
3. Numerical stability for small probabilities
4. Optional base selection for logarithm

Academic References
----------------
1. Cover, T. M., & Thomas, J. A. (2006). "Elements of Information Theory." Wiley-Interscience.
2. Rached, Z., et al. (2004). "The Relative Entropy Rate of Markov Sources." IEEE Transactions on Information Theory.
3. Gray, R. M. (2011). "Entropy and Information Theory." Springer.
4. Khudanpur, S. P., & Narayan, P. (2002). "Order estimation for Markov chains and hidden Markov models." IEEE Transactions on Information Theory.

Conclusion
---------
The Relative Entropy Rate provides a sophisticated way to compare Markov chains based on their information-theoretic properties. Its implementation in the `distancia` package offers researchers and practitioners a powerful tool for analyzing:
- Process complexity
- Predictability differences
- Information generation rates
- Model selection

The measure is particularly valuable in applications such as:
- Natural language processing
- Data compression
- Pattern recognition
- Time series analysis

See Also
--------
- Kullback-Leibler Divergence
- Cross Entropy
- Shannon Entropy
- Jensen-Shannon Divergence
