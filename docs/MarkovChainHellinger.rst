Markov Chain Hellinger Distance
==============================

A Probabilistic Distance Measure for Markov Chain Comparison
---------------------------------------------------------

Introduction
-----------
The Markov Chain Hellinger Distance provides a probabilistic approach to measuring the similarity between two Markov chains through their stationary distributions. This measure is particularly valuable for comparing probability distributions while maintaining scale-invariance and satisfying probability metric properties. It offers a more nuanced comparison than traditional L1 or L2 norms when dealing with probability distributions.

Mathematical Foundation
--------------------
The Hellinger distance is based on measuring the similarity between probability distributions using the geometric properties of their probability densities. When applied to Markov chains, it compares their stationary distributions, making it particularly useful for analyzing long-term behavioral differences.

Formal Definition
---------------
For two Markov chains with stationary distributions π_P and π_Q, the Hellinger distance is defined as:

.. math::

    H(P, Q) = \frac{1}{\sqrt{2}} \sqrt{\sum_{i=1}^n (\sqrt{\pi_P(i)} - \sqrt{\pi_Q(i)})^2}

where:
- π_P and π_Q are the stationary distributions of the respective Markov chains
- n is the number of states in the state space
- The factor 1/√2 ensures the distance is normalized between 0 and 1

Properties
---------
1. Boundedness: 0 ≤ H(P,Q) ≤ 1
2. Symmetry: H(P,Q) = H(Q,P)
3. Identity of indiscernibles: H(P,Q) = 0 if and only if P = Q
4. Triangle inequality: H(P,R) ≤ H(P,Q) + H(Q,R)
5. Scale-invariance: preserved under coordinate transformations

Implementation
------------
The measure is implemented in the `distancia` package:

.. code-block:: python

    from distancia.metrics import MarkovChainHellinger
    
    # Initialize the measure
    hellinger_dist = MarkovChainHellinger()
    
    # Calculate distance between two Markov chains
    distance = hellinger_dist.compute(matrix_p, matrix_q)

Usage Example
-----------
Here's a practical example comparing two Markov chains:

.. code-block:: python

    import numpy as np
    from distancia.metrics import MarkovChainHellinger
    
    # Define two transition matrices
    P = np.array([[0.7, 0.2, 0.1],
                  [0.3, 0.5, 0.2],
                  [0.2, 0.3, 0.5]])
    
    Q = np.array([[0.6, 0.3, 0.1],
                  [0.2, 0.6, 0.2],
                  [0.1, 0.2, 0.7]])
    
    # Calculate Hellinger distance
    hellinger_dist = MarkovChainHellinger()
    result = hellinger_dist.compute(P, Q)
    print(f"Hellinger Distance: {result:.4f}")
    
    # Access the computed stationary distributions
    pi_p = hellinger_dist.get_stationary_distribution(P)
    pi_q = hellinger_dist.get_stationary_distribution(Q)

Computational Complexity
---------------------
- Time Complexity: O(n³) where n is the number of states, due to stationary distribution computation
- Space Complexity: O(n²) for matrix storage and intermediate calculations

The implementation includes:
1. Efficient computation of stationary distributions
2. Numerical stability safeguards for small probability values
3. Validation of input probability constraints

Academic References
----------------
1. Hellinger, E. (1909). "Neue Begründung der Theorie quadratischer Formen von unendlichvielen Veränderlichen." Journal für die reine und angewandte Mathematik.
2. Beran, R. (1977). "Minimum Hellinger Distance Estimates for Parametric Models." The Annals of Statistics.
3. Deza, M. M., & Deza, E. (2009). "Encyclopedia of Distances." Springer Berlin Heidelberg.
4. Le Cam, L., & Yang, G. L. (2000). "Asymptotics in Statistics: Some Basic Concepts." Springer Science & Business Media.

Conclusion
---------
The Markov Chain Hellinger Distance provides a sophisticated yet interpretable way to compare Markov chains through their stationary distributions. Its implementation in the `distancia` package offers a robust tool for analyzing stochastic processes across various applications, including:
- Pattern recognition
- Information theory
- Statistical inference
- Machine learning model comparison

The measure's probabilistic interpretation and desirable mathematical properties make it particularly suitable for applications where scale-invariance and bounded distances are important.

See Also
--------
- Kullback-Leibler Divergence
- Total Variation Distance
- Steady-State Distribution Distance
- Wasserstein Distance
