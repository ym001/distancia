NuclearNorm
===========

The `NuclearNorm` class computes the **nuclear norm** of a matrix, which is defined as the sum of the singular values of the matrix. This metric is particularly useful in various fields such as low-rank matrix approximation, optimization, and machine learning.

Introduction
------------

The nuclear norm is a widely used matrix norm that measures the sum of the singular values of a matrix. It is equivalent to the Schatten 1-norm and is often used as a convex surrogate for the rank function in optimization problems. 

The nuclear norm has applications in areas such as compressed sensing, collaborative filtering, and image processing, where low-rank matrix approximations are important.

Meaning of the Measure
-----------------------

The nuclear norm captures the "complexity" or "rank-structure" of a matrix. In the context of comparing two matrices, it provides a scalar measure of their similarity by evaluating the nuclear norm of their difference. Smaller nuclear norms of the difference matrix indicate higher similarity, whereas larger norms suggest greater dissimilarity.

For two matrices \( A \) and \( B \), the nuclear norm is computed as:

.. math::

   \|A - B\|_* = \sum_{i=1}^{\min(m, n)} \sigma_i(A - B)

where:
- \( \sigma_i \) are the singular values of \( A - B \),
- \( m \) and \( n \) are the dimensions of the matrices.

Formal Calculation of the Distance
-----------------------------------

Given two matrices \( A \) and \( B \), the nuclear norm distance is calculated as follows:

1. Compute the difference matrix \( D = A - B \).
2. Perform singular value decomposition (SVD) on \( D \), yielding the singular values \( \sigma_1, \sigma_2, \dots \).
3. Sum all singular values:

.. math::

   \|D\|_* = \sum_{i} \sigma_i

This provides the nuclear norm of \( A - B \).

Academic Citation
-----------------

The nuclear norm is grounded in matrix theory and has been explored extensively in the literature. For a detailed mathematical treatment, refer to:

- Candès, E. J., & Recht, B. (2009). "Exact Matrix Completion via Convex Optimization." *Foundations of Computational Mathematics*, 9(6), 717–772. https://doi.org/10.1007/s10208-009-9045-5

Conclusion
----------

The `NuclearNorm` class provides a robust and interpretable measure for comparing matrices. Its basis in singular value decomposition makes it particularly useful for tasks involving low-rank approximations or regularization in optimization problems. By leveraging this measure, users can effectively analyze and quantify the differences between matrices in various applications.
