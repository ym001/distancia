Principal Component Comparator
============================

Introduction
------------
The Principal Component Comparator (PCA Comparator) is a method for measuring the similarity between two matrices by comparing their principal components. This approach provides a way to assess the structural similarities between datasets by examining their fundamental patterns of variation.

Mathematical Foundation
---------------------
Principal Component Analysis (PCA) is a dimensionality reduction technique that identifies the directions (principal components) along which the data varies the most. When comparing two matrices using PCA, we essentially compare how their underlying patterns of variation align.

Formal Definition
----------------
Given two matrices A and B, the PCA-based comparison involves:

1. **Centering**: For each matrix M, compute M' = M - μ_M, where μ_M is the column-wise mean
2. **Covariance**: Compute C = (M'ᵀM')/(n-1) for each centered matrix
3. **Eigendecomposition**: Find eigenvalues λᵢ and eigenvectors vᵢ for each covariance matrix
4. **Distance Computation**:

The distance measure D(A,B) between matrices A and B is defined as:

.. math::

    D(A,B) = \sum_{i=1}^{k} w_i \left(\frac{|\lambda_i^A - \lambda_i^B|}{\lambda_i^A + \lambda_i^B} \cdot (1 - |\langle v_i^A, v_i^B \rangle|)\right)

where:
- k is the number of components considered
- λᵢᴬ, λᵢᴮ are the i-th eigenvalues of A and B
- vᵢᴬ, vᵢᴮ are the i-th eigenvectors
- wᵢ are optional weights (default to 1)
- ⟨·,·⟩ denotes the inner product

Implementation Details
--------------------
The PCAComparator class implements this comparison through several key steps:

1. **Data Preprocessing**:
   - Matrix centering
   - Covariance matrix computation
   
2. **Principal Component Extraction**:
   - Power iteration method for eigenvalue/eigenvector computation
   - Matrix deflation for subsequent components
   
3. **Comparison Metrics**:
   - Eigenvalue distance calculation
   - Eigenvector similarity assessment
   - Weighted total distance computation

Usage Example
------------
.. code-block:: python

    # Initialize comparator
    pca_comp = PCAComparator(n_components=2)
    
    # Example matrices
    matrix1 = [
        [1.0, 0.0, 3.0],
        [2.0, 4.0, 1.0],
        [0.0, 2.0, 8.0],
        [4.0, 1.0, 2.0]
    ]
    
    matrix2 = [
        [5.0, 2.0, 1.0],
        [1.0, 7.0, 3.0],
        [3.0, 4.0, 2.0],
        [2.0, 3.0, 6.0]
    ]
    
    # Compare matrices
    result = pca_comp.compare(matrix1, matrix2)

Academic References
-----------------
1. Jolliffe, I. T. (2002). Principal Component Analysis, Second Edition. Springer Series in Statistics.

2. Van der Maaten, L., Postma, E., & Van den Herik, J. (2009). Dimensionality reduction: A comparative review. Journal of Machine Learning Research, 10, 66-71.

3. Wang, J. L., Chiou, J. M., & Müller, H. G. (2016). Functional data analysis. Annual Review of Statistics and Its Application, 3, 257-295.

Advantages and Limitations
------------------------
**Advantages**:
- Captures structural similarities between matrices
- Invariant to rotation and scaling
- Focuses on principal patterns of variation

**Limitations**:
- Assumes linear relationships in data
- Sensitive to outliers
- May lose information in highly non-linear data

Conclusion
----------
The PCA Comparator provides a robust method for comparing matrices based on their fundamental structure rather than element-wise differences. This makes it particularly useful for applications where the overall pattern of variation is more important than exact numerical matches. The implementation in the distancia package offers a flexible and efficient way to perform these comparisons while maintaining numerical stability and providing interpretable results.

.. note::

   The choice of the number of components (n_components) can significantly impact the comparison results. It is recommended to experiment with different values based on the specific characteristics of your data.

See Also
--------
- ``NMFComparator``: For non-negative matrix comparisons
- ``EnergyDistance``: For probability distribution-based comparisons
- ``LogDetDivergence``: For positive definite matrix comparisons
