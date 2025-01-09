Matrix Distances
================

Introduction
============
Matrices are widely used in fields such as machine learning, data science, image processing, and network analysis. Comparing two matrices can help reveal similarities or differences in patterns, structures, or data distributions. The **Distancia** package offers a variety of distance measures tailored for matrix comparison, ranging from simple element-wise comparisons to more complex spectral and structural comparisons.

List  of Matrix Distances
=========================

**Element-Wise Distances**
-----------------------------

These distances compare two matrices by evaluating differences between corresponding elements. They are useful when the exact values or differences between matrix entries are important, such as in image comparisons or heatmap analysis.

#. `Euclidean`_ : Measures the straight-line distance between two matrices by treating them as flattened vectors.
#. `Manhattan`_ (L1 Distance): Sum of the absolute differences between corresponding elements of two matrices.
#. `chebyshev`_  : Maximum absolute difference between corresponding elements of two matrices.
#. `Minkowski`_  : Generalization of Euclidean and Manhattan distances, parameterized by a power p.
#. `Hamming`_  : Measures the number of positions where corresponding elements are different (binary matrices or categorical values).

.. _Euclidean: https://distancia.readthedocs.io/en/latest/Euclidean.html
.. _Manhattan: https://distancia.readthedocs.io/en/latest/Manhattan.html
.. _Chebyshev: https://distancia.readthedocs.io/en/latest/Chebyshev.html
.. _Hamming: https://distancia.readthedocs.io/en/latest/Hamming.html
.. _Minkowski: https://distancia.readthedocs.io/en/latest/Minkowski.html

**Norm-Based Distances**
------------------------

Norm-based distances focus on comparing matrices using mathematical norms, which summarize the overall difference between two matrices in terms of magnitude or geometric properties.

6. `L1`_  : Measures the sum of the absolute differences between corresponding elements in two matrices, highlighting overall deviation.
#. `L2`_  : Computes the Euclidean distance between two matrices, summing the squared differences between elements and taking the square root.
#. `MaxNorm`_  : Compares two matrices by finding the largest absolute difference between corresponding elements, focusing on the most significant deviation.
#. `NormalizedSpectral`_
#. `Frobenius`_  : Sum of the squares of the matrix elements, often used to compare the overall magnitude of two matrices.
#. `Nuclear`_  : Sum of the singular values of the matrix, often used for comparing low-rank matrices.
#. `OperatorNormCalculator`_  : Based on the largest singular value (spectral norm) of the difference between two matrices.

**Kernel-Based Distance**
------------------------

These methods compute distances between matrices using kernels, which map matrices to higher-dimensional spaces.

13. `Gaussian Kernel`_  : Measures similarity based on the Gaussian kernel applied to matrix entries.
#. `Polynomial Kernel`_  : Computes distances using a polynomial kernel applied to matrix entries.
#. `RBF (Radial Basis Function)`_  : Another kernel-based measure, widely used for comparing matrix-valued data.
#. `HeatKernel`_

**Geometric Distance**
---------------------

These distances treat matrices as geometric objects and compute distances based on their structure.

17. `Procrustes`_  : Measures the similarity between two matrices by finding the best alignment through rotation, scaling, and translation.
#. `Hausdorff`_  : Measures the maximum distance of a point in one matrix to the closest point in the other matrix.
#. `Earth Mover’s Distance (Wasserstein Distance)`_  : Measures the minimum "cost" to transform one matrix into another, useful in distributions or spatial data.
#. `TriangleMatrixDistance`_

**Decomposition-Based Distance**
-------------------------------

These methods rely on matrix decompositions like SVD or eigenvalue decompositions.

21. `Subspace`_  : Measures the distance between the subspaces spanned by two matrices, using singular value decomposition (SVD).
#. `Canonical Correlation`_  : Compares matrices by measuring the correlation between their canonical variables.
#. `Eigenvalue-Based`_  : Compares matrices based on the differences between their eigenvalues (often for symmetric matrices).

**Information-Theoretic Distance**
---------------------------------

These methods compare matrices using concepts from information theory, often treating matrices as probabilistic models.

24. `Kullback-Leibler`_  : Measures the divergence between two matrices viewed as probability distributions.
#. `Jensen-Shannon`_  : A symmetrized and smoothed version of KL divergence for matrix comparison.
#. `Log-Determinant Divergence`_  : Measures the divergence between two positive semi-definite matrices using their determinants.

**Graph-Based Distance**
-----------------------

If matrices are adjacency matrices of graphs, specialized graph distances are used.

27. `MatrixSpectral`_ : Compares matrices based on their eigenvalue spectra, often used for graph adjacency matrices.
#. `Graph Edit`_  : Measures the number of edits (insertion, deletion, modification of edges/nodes) needed to transform one graph into another.
#. `Resistance`_  : Based on electrical network theory, comparing the resistance of nodes between two graph adjacency matrices.
#. `RandomWalk`_
#. `GraphEditMatrix`_
#. `PatternBased`_
#. `CliqueBasedGraph`_
#. `CycleMatrixDistance`_
#. `GraphletMatrixDistance`_
#. `MinimumCutDistanceCalculator`_
#. `Percolation`_
#. `NetSimile`_
#. `PureDiffusion`_

**Statistical Distance**
-----------------------

These distances focus on comparing matrices that represent statistical properties or distributions.

40. `Mahalanobis`_  : Takes into account the correlations between variables in the matrices, useful for covariance matrices.
#. `MahalanobisTaguchi`_
#. `Bhattacharyya`_  : Measures the overlap between statistical distributions represented by two matrices.
#. `Energy`_  : Measures the statistical distance between two matrices in terms of their probability distributions.
#. `WeisfeilerLehman`_

**Compression-Based Distance**
-----------------------------

These methods compress the matrices and then compare their compressed versions.

44. `Normalized Compression Distance (NCD)`_  : Uses compression algorithms (like zlib) to measure the complexity difference between two matrices.
#. `Kolmogorov`_  : Measures the difference between the compressibility of two matrices by estimating their algorithmic complexity.

**Matrix Factorization-Based Distance**
---------------------------------------

These methods are based on matrix factorizations like NMF (Non-negative Matrix Factorization) or PCA (Principal Component Analysis).

46. `Non-negative Matrix Factorization (NMF)`_  : Compares matrices based on their factorizations into non-negative components.
#. `Principal Component`_  : Measures the distance between two matrices by comparing their principal components (from PCA).



**Spectral-Based Distances**
----------------------------

Spectral-based distances compare matrices by analyzing their spectral properties, such as eigenvalues or singular values. These distances are particularly effective for comparing matrices in fields such as graph theory or signal processing, where the structure and flow captured in matrix transformations are of interest.

48. `SpectralNorm`_  : Compares matrices by calculating the largest singular value difference, capturing differences in matrix transformations.
#. `Eigenvalue`_  : Measures the distance between the eigenvalue spectra of two matrices, often used in structural or network matrix comparisons.
#. `NuclearNorm`_  : Uses the sum of the singular values of the matrix difference to capture differences in the overall structure and rank of the matrices.

Conclusion
==========
The diverse set of matrix distance measures provided by **Distancia** allows for comprehensive analysis across various domains, from numerical accuracy in computations to structural comparisons in matrices representing networks or systems. Each distance captures unique aspects of the matrices, whether focusing on element-wise precision, overall magnitude, or spectral properties. The flexibility of these distances makes **Distancia** an invaluable tool for applications in machine learning, image processing, and network analysis.

.. _Mahalanobis: https://distancia.readthedocs.io/en/latest/Mahalanobis.html
.. _MahalanobisTaguchi: https://distancia.readthedocs.io/en/latest/MahalanobisTaguchi.html
.. _MatrixSpectral: https://distancia.readthedocs.io/en/latest/MatrixSpectral.html
.. _NormalizedSpectral: https://distancia.readthedocs.io/en/latest/NormalizedSpectral.html
.. _PureDiffusion: https://distancia.readthedocs.io/en/latest/PureDiffusion.html
.. _RandomWalk: https://distancia.readthedocs.io/en/latest/RandomWalk.html
.. _HeatKernel: https://distancia.readthedocs.io/en/latest/HeatKernel.html
.. _GraphEditMatrix: https://distancia.readthedocs.io/en/latest/GraphEditMatrix.html
.. _WeisfeilerLehman: https://distancia.readthedocs.io/en/latest/WeisfeilerLehman.html
.. _NetSimile: https://distancia.readthedocs.io/en/latest/NetSimile.html
.. _TriangleMatrixDistance: https://distancia.readthedocs.io/en/latest/TriangleMatrixDistance.html
.. _PatternBased: https://distancia.readthedocs.io/en/latest/PatternBased.html
.. _CliqueBasedGraph: https://distancia.readthedocs.io/en/latest/CliqueBasedGraph.html
.. _CycleMatrixDistance: https://distancia.readthedocs.io/en/latest/CycleMatrixDistance.html
.. _GraphletMatrixDistance: https://distancia.readthedocs.io/en/latest/GraphletMatrixDistance.html
.. _MinimumCutDistanceCalculator: https://distancia.readthedocs.io/en/latest/MinimumCutDistanceCalculator.html
.. _Percolation: https://distancia.readthedocs.io/en/latest/Percolation.html
.. _OperatorNormCalculator: https://distancia.readthedocs.io/en/latest/OperatorNormCalculator.html
.. _Frobenius: https://distancia.readthedocs.io/en/latest/Frobenius.html
.. _Nuclear: https://distancia.readthedocs.io/en/latest/NuclearNorm.html

