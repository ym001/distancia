Matrix Distances
================

Introduction
============
Matrices are widely used in fields such as machine learning, data science, image processing, and network analysis. Comparing two matrices can help reveal similarities or differences in patterns, structures, or data distributions. The **Distancia** package offers a variety of distance measures tailored for matrix comparison, ranging from simple element-wise comparisons to more complex spectral and structural comparisons.

Categories
==========

1. **Element-Wise Distances**
2. **Norm-Based Distances**
3. **Spectral-Based Distances**

List  of Matrix Distances
=========================

**Element-Wise Distances**
--------------------------

These distances compare two matrices by evaluating differences between corresponding elements. They are useful when the exact values or differences between matrix entries are important, such as in image comparisons or heatmap analysis.

    Euclidean Distance: Measures the straight-line distance between two matrices by treating them as flattened vectors.

    Manhattan Distance (L1 Distance): Sum of the absolute differences between corresponding elements of two matrices.

    Chebyshev Distance: Maximum absolute difference between corresponding elements of two matrices.

    Minkowski Distance: Generalization of Euclidean and Manhattan distances, parameterized by a power p.

    Hamming Distance: Measures the number of positions where corresponding elements are different (binary matrices or categorical values).

2. Norm-Based Distance

These distances are based on matrix norms, which are generalizations of vector norms.

    Frobenius Norm: Sum of the squares of the matrix elements, often used to compare the overall magnitude of two matrices.
    Nuclear Norm: Sum of the singular values of the matrix, often used for comparing low-rank matrices.
    Operator Norm: Based on the largest singular value (spectral norm) of the difference between two matrices.

3. Kernel-Based Distance

These methods compute distances between matrices using kernels, which map matrices to higher-dimensional spaces.

    Gaussian Kernel Distance: Measures similarity based on the Gaussian kernel applied to matrix entries.
    Polynomial Kernel Distance: Computes distances using a polynomial kernel applied to matrix entries.
    RBF (Radial Basis Function) Distance: Another kernel-based measure, widely used for comparing matrix-valued data.

4. Geometric Distance

These distances treat matrices as geometric objects and compute distances based on their structure.

    Procrustes Distance: Measures the similarity between two matrices by finding the best alignment through rotation, scaling, and translation.
    Hausdorff Distance: Measures the maximum distance of a point in one matrix to the closest point in the other matrix.
    Earth Mover’s Distance (Wasserstein Distance): Measures the minimum "cost" to transform one matrix into another, useful in distributions or spatial data.

5. Decomposition-Based Distance

These methods rely on matrix decompositions like SVD or eigenvalue decompositions.

    Subspace Distance: Measures the distance between the subspaces spanned by two matrices, using singular value decomposition (SVD).
    Canonical Correlation Distance: Compares matrices by measuring the correlation between their canonical variables.
    Eigenvalue-Based Distance: Compares matrices based on the differences between their eigenvalues (often for symmetric matrices).

6. Information-Theoretic Distance

These methods compare matrices using concepts from information theory, often treating matrices as probabilistic models.

    Kullback-Leibler (KL) Divergence: Measures the divergence between two matrices viewed as probability distributions.
    Jensen-Shannon Divergence: A symmetrized and smoothed version of KL divergence for matrix comparison.
    Log-Determinant Divergence: Measures the divergence between two positive semi-definite matrices using their determinants.

7. Graph-Based Distance

If matrices are adjacency matrices of graphs, specialized graph distances are used.

    Spectral Graph Distance: Compares matrices based on their eigenvalue spectra, often used for graph adjacency matrices.
    Graph Edit Distance: Measures the number of edits (insertion, deletion, modification of edges/nodes) needed to transform one graph into another.
    Resistance Distance: Based on electrical network theory, comparing the resistance of nodes between two graph adjacency matrices.

8. Statistical Distance

These distances focus on comparing matrices that represent statistical properties or distributions.

    Mahalanobis Distance: Takes into account the correlations between variables in the matrices, useful for covariance matrices.
    Bhattacharyya Distance: Measures the overlap between statistical distributions represented by two matrices.
    Energy Distance: Measures the statistical distance between two matrices in terms of their probability distributions.

9. Compression-Based Distance

These methods compress the matrices and then compare their compressed versions.

    Normalized Compression Distance (NCD): Uses compression algorithms (like zlib) to measure the complexity difference between two matrices.
    Kolmogorov Complexity: Measures the difference between the compressibility of two matrices by estimating their algorithmic complexity.

10. Matrix Factorization-Based Distance

These methods are based on matrix factorizations like NMF (Non-negative Matrix Factorization) or PCA (Principal Component Analysis).

    Non-negative Matrix Factorization (NMF) Distance: Compares matrices based on their factorizations into non-negative components.
    Principal Component Distance: Measures the distance between two matrices by comparing their principal components (from PCA).

**Norm-Based Distances**
------------------------

Norm-based distances focus on comparing matrices using mathematical norms, which summarize the overall difference between two matrices in terms of magnitude or geometric properties.

1. :doc:`L1`

   - Measures the sum of the absolute differences between corresponding elements in two matrices, highlighting overall deviation.

2. :doc:`L2`

   - Computes the Euclidean distance between two matrices, summing the squared differences between elements and taking the square root.

3. :doc:`MaxNorm`

   - Compares two matrices by finding the largest absolute difference between corresponding elements, focusing on the most significant deviation.

**Spectral-Based Distances**
----------------------------

Spectral-based distances compare matrices by analyzing their spectral properties, such as eigenvalues or singular values. These distances are particularly effective for comparing matrices in fields such as graph theory or signal processing, where the structure and flow captured in matrix transformations are of interest.

1. :doc:`SpectralNorm`

   - Compares matrices by calculating the largest singular value difference, capturing differences in matrix transformations.

2. :doc:`Eigenvalue`

   - Measures the distance between the eigenvalue spectra of two matrices, often used in structural or network matrix comparisons.

3. :doc:`NuclearNorm`

   - Uses the sum of the singular values of the matrix difference to capture differences in the overall structure and rank of the matrices.

Conclusion
==========
The diverse set of matrix distance measures provided by **Distancia** allows for comprehensive analysis across various domains, from numerical accuracy in computations to structural comparisons in matrices representing networks or systems. Each distance captures unique aspects of the matrices, whether focusing on element-wise precision, overall magnitude, or spectral properties. The flexibility of these distances makes **Distancia** an invaluable tool for applications in machine learning, image processing, and network analysis.
