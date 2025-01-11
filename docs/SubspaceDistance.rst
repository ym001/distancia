SubspaceDistance
===============

Introduction
------------
The SubspaceDistance class implements methods for measuring distances between linear subspaces spanned by matrices using Singular Value Decomposition (SVD). This measure is fundamental in various fields, including computer vision, signal processing, and data analysis, where comparing subspaces is essential for understanding data relationships and geometric structures.

Description
-----------
The subspace distance quantifies the geometric difference between two linear subspaces by analyzing their principal angles. These angles are computed efficiently using SVD, providing a robust and numerically stable way to measure how "far apart" two subspaces are from each other in terms of their spanning directions.

Mathematical Formulation
-----------------------
For two matrices A ∈ ℝ^(m×p) and B ∈ ℝ^(m×q), the subspace distance is computed using their orthonormal bases obtained through SVD:

.. math::

   A = U_A \Sigma_A V_A^T
   B = U_B \Sigma_B V_B^T

The principal angles θᵢ between the subspaces are computed as:

.. math::

   \cos(\theta_i) = \sigma_i(U_A^T U_B)

where σᵢ are the singular values of U_A^T U_B.

The subspace distance can then be defined in several ways:

1. Geodesic distance:
   .. math::
      d_{geo}(A,B) = \sqrt{\sum_{i=1}^{\min(p,q)} \theta_i^2}

2. Projection distance:
   .. math::
      d_{proj}(A,B) = \sqrt{1 - \sigma_{min}^2(U_A^T U_B)}

3. Chordal distance:
   .. math::
      d_{chord}(A,B) = \sqrt{\sum_{i=1}^{\min(p,q)} \sin^2(\theta_i)}

Properties
---------
1. Non-negativity: d(A,B) ≥ 0
2. Identity of indiscernibles: d(A,B) = 0 iff span(A) = span(B)
3. Symmetry: d(A,B) = d(B,A)
4. Triangle inequality (for certain metrics)
5. Invariance under orthogonal transformations
6. Scale invariance

Implementation Features
---------------------
The class provides:
1. Multiple distance metrics (geodesic, projection, chordal)
2. Efficient SVD computation
3. Handling of numerical instabilities
4. Support for sparse matrices
5. Dimension mismatch handling
6. Principal angles computation

Academic References
-----------------
1. Golub, G. H., & Van Loan, C. F. (2013). Matrix Computations (4th ed.). Johns Hopkins University Press.

2. Björck, Å., & Golub, G. H. (1973). Numerical methods for computing angles between linear subspaces. Mathematics of Computation, 27(123), 579-594.

3. Absil, P.-A., Mahony, R., & Sepulchre, R. (2008). Optimization Algorithms on Matrix Manifolds. Princeton University Press.

4. Stewart, G. W., & Sun, J. G. (1990). Matrix Perturbation Theory. Academic Press.

Applications
-----------
Subspace distances are particularly useful in:
- Computer vision (image set classification)
- Signal processing (subspace tracking)
- Pattern recognition (face recognition)
- Data mining (subspace clustering)
- Machine learning (domain adaptation)
- Dimensionality reduction (manifold alignment)

Computational Considerations
--------------------------
1. SVD Computation:
   - Choice of SVD algorithm based on matrix size
   - Handling of rank-deficient matrices
   - Numerical stability in presence of small singular values

2. Efficiency:
   - Optimizations for high-dimensional data
   - Memory-efficient implementations
   - Parallel computation options

Conclusion
----------
The SubspaceDistance class provides a comprehensive implementation of subspace distance metrics within the distancia package. Its robust implementation, based on SVD, ensures numerical stability and accuracy in comparing linear subspaces. The class supports multiple distance metrics and includes optimizations for various practical scenarios, making it suitable for both theoretical research and real-world applications.

Usage Notes
----------
- Input matrices should be preprocessed to handle numerical issues
- Consider dimensionality and rank when choosing metrics
- Be aware of computational complexity for large matrices
- Use appropriate tolerance levels for numerical comparisons
