Matrix Divergence
================

A Comprehensive Distance Measure for Markov Chain Comparison
---------------------------------------------------------

Introduction
-----------
Matrix Divergence provides a robust approach to quantify the dissimilarity between two Markov chains by analyzing their transition matrices. This measure is particularly useful in comparing stochastic processes, evaluating model convergence, and analyzing time-series data through their underlying Markov representations.

Mathematical Foundation
--------------------
The Matrix Divergence measure captures the fundamental differences between two Markov chains by examining their transition probabilities. Given two Markov chains with transition matrices P and Q, the divergence is calculated based on the element-wise differences while accounting for the stochastic nature of the matrices.

Formal Definition
---------------
For two n×n transition matrices P = (p_ij) and Q = (q_ij), the Matrix Divergence is defined as:

.. math::

    D(P||Q) = \sum_{i=1}^n \sum_{j=1}^n p_{ij} \log\left(\frac{p_{ij}}{q_{ij}}\right)

where:
- p_ij represents the transition probability from state i to state j in the first Markov chain
- q_ij represents the transition probability from state i to state j in the second Markov chain
- The logarithm is typically taken with base 2 or e

Properties
---------
1. Non-negativity: D(P||Q) ≥ 0
2. Identity of indiscernibles: D(P||Q) = 0 if and only if P = Q
3. Asymmetry: Generally, D(P||Q) ≠ D(Q||P)
4. Sensitivity to zero probabilities: Requires special handling when q_ij = 0

Implementation
------------
The measure is implemented in the `distancia` package as part of the distance metrics collection:

.. code-block:: python

    from distancia.metrics import MatrixDivergence
    
    # Initialize the measure
    div_measure = MatrixDivergence()
    
    # Calculate distance between two Markov chains
    distance = div_measure.compute(matrix_p, matrix_q)

Usage Example
-----------
Here's a practical example comparing two simple Markov chains:

.. code-block:: python

    import numpy as np
    from distancia.metrics import MatrixDivergence
    
    # Define two transition matrices
    P = np.array([[0.7, 0.3],
                  [0.4, 0.6]])
    
    Q = np.array([[0.8, 0.2],
                  [0.3, 0.7]])
    
    # Calculate divergence
    div_measure = MatrixDivergence()
    result = div_measure.compute(P, Q)
    print(f"Matrix Divergence: {result:.4f}")

Computational Complexity
---------------------
- Time Complexity: O(n²) where n is the number of states in the Markov chains
- Space Complexity: O(1) additional space beyond input storage

The implementation optimizes for both speed and memory efficiency while maintaining numerical stability through appropriate handling of edge cases.

Academic References
----------------
1. Kullback, S., & Leibler, R. A. (1951). "On information and sufficiency." The Annals of Mathematical Statistics, 22(1), 79-86.
2. Cover, T. M., & Thomas, J. A. (2006). "Elements of Information Theory." Wiley-Interscience.
3. Deza, M. M., & Deza, E. (2009). "Encyclopedia of Distances." Springer Berlin Heidelberg.

Conclusion
---------
Matrix Divergence provides a theoretically sound and practically useful measure for comparing Markov chains. Its implementation in the `distancia` package offers researchers and practitioners a reliable tool for analyzing stochastic processes across various domains, from natural language processing to biological sequence analysis.

See Also
--------
- Kullback-Leibler Divergence
- Jensen-Shannon Divergence
- Wasserstein Distance
