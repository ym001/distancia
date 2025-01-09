OperatorNormCalculator
=====================

The `OperatorNormCalculator` class computes the **operator norm** (also known as the spectral norm) of a matrix. This norm is defined as the largest singular value of the matrix. It is commonly used in applications requiring stability analysis, spectral properties, and numerical approximations.

Introduction
------------

The operator norm is a fundamental matrix norm, closely related to the spectral properties of matrices. It represents the maximum stretching effect a matrix has on any vector. This norm is particularly useful in numerical analysis, control theory, and optimization. 

When comparing two matrices, the operator norm of their difference highlights the maximum deviation in their linear transformations.

Meaning of the Measure
-----------------------

The operator norm captures the largest singular value of a matrix, which corresponds to its maximum eigenvalue magnitude in cases of symmetric matrices. This makes it an excellent measure of the "largest impact" or "worst-case" scenario when applying the matrix transformation. 

For two matrices \( A \) and \( B \), the operator norm distance is defined as:

.. math::

   \|A - B\|_2 = \max_i \sigma_i(A - B)

where:
- \( \sigma_i \) are the singular values of \( A - B \),
- \( \| \cdot \|_2 \) denotes the spectral norm.

Smaller values of the operator norm indicate that the matrices \( A \) and \( B \) are more similar in their linear transformations, while larger values suggest greater differences.

Formal Calculation of the Distance
-----------------------------------

Given two matrices \( A \) and \( B \), the operator norm distance is computed as follows:

1. Compute the difference matrix \( D = A - B \).
2. Perform singular value decomposition (SVD) on \( D \), obtaining singular values \( \sigma_1, \sigma_2, \dots \).
3. Select the largest singular value:

.. math::

   \|D\|_2 = \max_i \sigma_i

This maximum singular value represents the spectral norm of \( A - B \).

Academic Citation
-----------------

The operator norm is extensively used in matrix theory and has significant implications in various scientific disciplines. For further mathematical insights and applications, refer to:

- Horn, R. A., & Johnson, C. R. (1985). *Matrix Analysis*. Cambridge University Press. https://doi.org/10.1017/CBO9780511810817

Conclusion
----------

The `OperatorNormCalculator` class provides an essential tool for assessing the spectral properties of matrices and their differences. Its reliance on the largest singular value makes it particularly suitable for stability analysis, error estimation, and assessing maximum deviations in matrix transformations. This norm is a cornerstone in both theoretical and applied mathematics.
