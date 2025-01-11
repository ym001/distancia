RadialBasisFunction
==================

Introduction
------------
The RadialBasisFunction (RBF) class implements a kernel-based measure specifically designed for comparing matrix-valued data. This kernel function provides a way to measure similarity between matrices by mapping them into a high-dimensional feature space, making it particularly useful for matrix-valued pattern recognition and machine learning tasks. The RBF kernel is known for its flexibility and effectiveness in capturing non-linear relationships in matrix data.

Description
-----------
The RBF kernel for matrix-valued data extends the traditional scalar RBF kernel to handle matrices while preserving their structural properties. It computes the similarity between two matrices by considering their element-wise differences within a non-linear exponential function, weighted by a scaling parameter (bandwidth).

Mathematical Formulation
-----------------------
For two matrices A and B ∈ ℝ^(m×n), the matrix-valued RBF kernel is defined as:

.. math::

   k(A,B) = \exp\left(-\frac{||A - B||_F^2}{2\sigma^2}\right)

where:
- ||·||_F denotes the Frobenius norm
- σ > 0 is the bandwidth parameter
- exp(·) is the exponential function

For collections of matrices {Aᵢ} and {Bⱼ}, the kernel matrix K is computed as:

.. math::

   K_{ij} = k(A_i, B_j)

Properties
---------
The matrix-valued RBF kernel exhibits several important properties:

1. Symmetry: k(A,B) = k(B,A)
2. Positive definiteness
3. Boundedness: 0 < k(A,B) ≤ 1
4. k(A,A) = 1 for any matrix A
5. Scale sensitivity controlled by σ
6. Invariance to orthogonal transformations when using Frobenius norm

Implementation Features
---------------------
The class provides:
1. Automatic bandwidth selection methods
   - Median heuristic
   - Cross-validation
   - Maximum likelihood estimation
2. Efficient computation for large matrix collections
3. Sparse matrix support
4. GPU acceleration options
5. Numerical stability safeguards

Academic References
-----------------
1. Scholkopf, B., & Smola, A. J. (2002). Learning with Kernels: Support Vector Machines, Regularization, Optimization, and Beyond. MIT Press.

2. Genton, M. G. (2001). Classes of Kernels for Machine Learning: A Statistics Perspective. Journal of Machine Learning Research, 2, 299-312.

3. Wolf, L., & Shashua, A. (2003). Learning over Sets using Kernel Principal Angles. Journal of Machine Learning Research, 4, 913-931.

4. Jayasumana, S., Hartley, R., Salzmann, M., Li, H., & Harandi, M. (2013). Kernel Methods on Riemannian Manifolds with Gaussian RBF Kernels. IEEE Transactions on Pattern Analysis and Machine Intelligence, 37(12), 2464-2477.

Applications
-----------
The matrix-valued RBF kernel is particularly useful in:
- Image analysis (covariance descriptors)
- Signal processing (spectral matrices)
- Computer vision (region covariance matrices)
- Bioinformatics (connectivity matrices)
- Machine learning (kernel methods for matrix data)
- Pattern recognition (similarity-based classification)

Computational Considerations
--------------------------
1. Bandwidth Selection:
   - Critical for performance
   - Trade-off between over- and under-smoothing
   - Multiple scales possible for different features

2. Numerical Stability:
   - Handling of very large/small matrix differences
   - Prevention of numerical overflow/underflow
   - Efficient computation for large datasets

Conclusion
----------
The RadialBasisFunction class provides a robust and efficient implementation of the matrix-valued RBF kernel within the distancia package. Its flexible design accommodates various types of matrix data while maintaining computational efficiency. The implementation includes automatic parameter selection and optimization features, making it suitable for both research and practical applications. The class serves as a fundamental tool for kernel-based learning methods when working with matrix-valued data.

Usage Notes
----------
- Proper matrix normalization is recommended before kernel computation
- Bandwidth parameter should be tuned according to the specific application
- Memory requirements scale quadratically with the number of matrices
- Consider using approximate methods for very large datasets
