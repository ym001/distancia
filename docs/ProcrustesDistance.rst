ProcrustesDistance
=================

Introduction
------------
The ProcrustesDistance class implements the Procrustes analysis method, a powerful technique for comparing the shapes of matrices by finding optimal geometric transformations between them. Named after the Greek mythological figure Procrustes, this method determines the optimal rotation, scaling, and translation needed to best align one matrix with another, providing a measure of their similarity that is invariant to these transformations.

Description
-----------
Procrustes analysis minimizes the sum of squared distances between corresponding points in two matrices by applying a series of geometric transformations. This approach is particularly valuable when the absolute positions of points are less important than their relative configurations, making it ideal for shape analysis, pattern matching, and data alignment problems.

Mathematical Formulation
-----------------------
For two matrices X, Y ∈ ℝ^(n×p), the Procrustes distance is computed by solving:

.. math::

   d^2(X,Y) = \min_{R,t,s} ||Y - sXR - t||_F^2

subject to:
   R^TR = I (orthogonality constraint)

where:
- R is a p×p rotation matrix
- s is a scaling factor
- t is a translation vector
- ||·||_F denotes the Frobenius norm

The solution involves these steps:
1. Center the matrices:
   .. math::
      X_c = X - \bar{X}, Y_c = Y - \bar{Y}

2. Compute SVD:
   .. math::
      X_c^T Y_c = U\Sigma V^T

3. Find optimal rotation:
   .. math::
      R = VU^T

4. Compute scaling (if allowed):
   .. math::
      s = \frac{tr(Y_c^T X_c R)}{tr(X_c^T X_c)}

Properties
---------
1. Non-negativity: d(X,Y) ≥ 0
2. Identity of indiscernibles: d(X,Y) = 0 iff X and Y are identical up to allowed transformations
3. Symmetry: d(X,Y) = d(Y,X)
4. Invariance to:
   - Rotations
   - Translations
   - Scaling (if enabled)
   - Choice of reference point

Implementation Features
---------------------
The class provides:
1. Multiple Procrustes variants:
   - Ordinary (rotation and translation)
   - Generalized (rotation, translation, and scaling)
   - Partial (subset matching)
2. Efficient SVD computation
3. Handling of reflection options
4. Automatic dimensionality matching
5. Weighted Procrustes analysis
6. Iterative refinement options

Academic References
-----------------
1. Gower, J. C., & Dijksterhuis, G. B. (2004). Procrustes Problems. Oxford University Press.

2. Dryden, I. L., & Mardia, K. V. (2016). Statistical Shape Analysis: With Applications in R. John Wiley & Sons.

3. Schönemann, P. H. (1966). A generalized solution of the orthogonal Procrustes problem. Psychometrika, 31(1), 1-10.

4. Ten Berge, J. M. (1977). Orthogonal Procrustes rotation for two or more matrices. Psychometrika, 42(2), 267-276.

Applications
-----------
Procrustes analysis is particularly useful in:
- Shape analysis and morphometrics
- Protein structure alignment
- Image registration
- Motion capture data analysis
- Psychometrics
- Sensory profiling
- Geographic data matching
- Pattern recognition

Computational Considerations
--------------------------
1. SVD Computation:
   - Choice of algorithm based on matrix size
   - Handling of numerical stability
   - Efficient updates for iterative procedures

2. Optimization:
   - Efficient handling of large datasets
   - Parallel computation options
   - Memory-efficient implementations

Conclusion
----------
The ProcrustesDistance class provides a comprehensive implementation of Procrustes analysis within the distancia package. Its robust implementation supports various types of geometric transformations and includes optimizations for different use cases. The class serves as a fundamental tool for shape analysis and pattern matching problems where geometric alignment is crucial.

Usage Notes
----------
- Consider which transformations should be allowed (rotation, scaling, translation)
- Pre-process data to handle scale differences if necessary
- Be aware of computational complexity for large matrices
- Handle missing data appropriately
- Consider using weighted variants for non-uniform reliability
