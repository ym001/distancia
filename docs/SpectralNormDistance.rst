Spectral Norm Distance
=====================

A Distance Measure Based on Matrix Spectral Properties
---------------------------------------------------

Introduction
-----------
The Spectral Norm Distance provides a sophisticated approach to comparing Markov chains by examining the spectral properties of their transition matrices. This measure is particularly effective in capturing structural differences between stochastic processes, as it considers the eigenvalue and eigenvector characteristics that define the chains' long-term behavior.

Mathematical Foundation
--------------------
The Spectral Norm Distance leverages the spectral decomposition of transition matrices to quantify the difference between two Markov chains. This approach is rooted in linear algebra theory and provides insights into both the immediate transitions and the asymptotic behavior of the processes.

Formal Definition
---------------
For two n×n transition matrices P and Q, the Spectral Norm Distance is defined as:

.. math::

    d_{spec}(P, Q) = ||P - Q||_2 = \sigma_{max}(P - Q)

where:
- ||·||₂ denotes the spectral norm (also known as 2-norm or operator norm)
- σ_max represents the largest singular value of the difference matrix
- P and Q are the transition matrices of the respective Markov chains

Properties
---------
1. Symmetry: d_spec(P,Q) = d_spec(Q,P)
2. Non-negativity: d_spec(P,Q) ≥ 0
3. Identity of indiscernibles: d_spec(P,Q) = 0 if and only if P = Q
4. Triangle inequality: d_spec(P,R) ≤ d_spec(P,Q) + d_spec(Q,R)
5. Bounded: d_spec(P,Q) ≤ 2 for stochastic matrices

Implementation
------------
The measure is implemented in the `distancia` package:

.. code-block:: python

    from distancia.metrics import SpectralNormDistance
    
    # Initialize the measure
    spec_dist = SpectralNormDistance()
    
    # Calculate distance between two Markov chains
    distance = spec_dist.compute(matrix_p, matrix_q)

Usage Example
-----------
Here's a practical example comparing two Markov chains:

.. code-block:: python

    import numpy as np
    from distancia.metrics import SpectralNormDistance
    
    # Define two transition matrices
    P = np.array([[0.8, 0.2, 0.0],
                  [0.1, 0.7, 0.2],
                  [0.0, 0.3, 0.7]])
    
    Q = np.array([[0.7, 0.2, 0.1],
                  [0.2, 0.6, 0.2],
                  [0.1, 0.2, 0.7]])
    
    # Calculate spectral norm distance
    spec_dist = SpectralNormDistance()
    result = spec_dist.compute(P, Q)
    print(f"Spectral Norm Distance: {result:.4f}")

Computational Complexity
---------------------
- Time Complexity: O(n³) where n is the number of states, due to singular value decomposition
- Space Complexity: O(n²) for storing intermediate matrices during computation

The implementation uses optimized linear algebra routines from NumPy/SciPy for efficient computation of singular values.

Academic References
----------------
1. Stewart, G. W. (1990). "Matrix Algorithms: Basic Decompositions." SIAM.
2. Golub, G. H., & Van Loan, C. F. (2013). "Matrix Computations." JHU Press.
3. Seneta, E. (2006). "Non-negative Matrices and Markov Chains." Springer Science & Business Media.
4. Cho, G. E., & Meyer, C. D. (2001). "Comparison of perturbation bounds for the stationary distribution of a Markov chain." Linear Algebra and its Applications, 335(1-3), 137-150.

Conclusion
---------
The Spectral Norm Distance provides a mathematically rigorous approach to comparing Markov chains through their spectral properties. Its implementation in the `distancia` package offers a reliable tool for analyzing stochastic processes in various applications, from network analysis to time series comparison. The measure is particularly valuable when the long-term behavior and structural properties of the processes are of primary interest.

See Also
--------
- Matrix Divergence
- Operator Norm Distance
- Frobenius Norm Distance
- Total Variation Distance
