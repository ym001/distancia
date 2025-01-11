Non-negative Matrix Factorization Comparator
==========================================

Introduction
------------
The Non-negative Matrix Factorization (NMF) Comparator is a method for comparing matrices based on their decomposition into non-negative components. NMF is particularly useful when dealing with data that has natural non-negativity constraints, such as image intensities, text document frequencies, or spectral data.

Mathematical Foundation
---------------------
NMF decomposes a non-negative matrix V into the product of two non-negative matrices W and H, where W represents the basis vectors and H represents the encodings or weights. The comparison between matrices is then performed in this factorized space.

Formal Definition
----------------
Given a non-negative matrix V ∈ ℝᵐˣⁿ₊, NMF finds matrices W ∈ ℝᵐˣᵏ₊ and H ∈ ℝᵏˣⁿ₊ such that:

.. math::

    V ≈ WH

where k is the number of components, and ℝ₊ denotes the non-negative real numbers.

The optimization problem is formulated as:

.. math::

    \min_{W,H} ||V - WH||_F^2
    \text{ subject to } W, H \geq 0

For comparing two matrices V₁ and V₂, we compute their respective factorizations:

.. math::

    V_1 ≈ W_1H_1
    V_2 ≈ W_2H_2

The distance measure D(V₁,V₂) is then defined as:

.. math::

    D(V_1,V_2) = \alpha \cdot d(W_1,W_2) + (1-\alpha) \cdot d(H_1,H_2)

where:
- d(·,·) is a suitable distance metric (e.g., Frobenius norm)
- α is a weighting parameter (default: 0.5)

Implementation Details
--------------------
The NMFComparator class implements this comparison through several key components:

1. **Initialization**:
   - Random initialization of W and H matrices
   - Option for different initialization strategies
   
2. **Optimization**:
   - Multiplicative update rules for W and H
   - Convergence monitoring
   - Numerical stability safeguards
   
3. **Comparison Metrics**:
   - Reconstruction error computation
   - Feature similarity assessment
   - Combined distance measure

Usage Example
------------
.. code-block:: python

    # Initialize comparator
    nmf_comp = NMFComparator(n_components=2)
    
    # Example matrices
    matrix1 = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ]
    
    matrix2 = [
        [2.0, 3.0, 4.0],
        [5.0, 6.0, 7.0],
        [8.0, 9.0, 10.0]
    ]
    
    # Compare matrices
    comparison = nmf_comp.compare(matrix1, matrix2)

Academic References
-----------------
1. Lee, D. D., & Seung, H. S. (1999). Learning the parts of objects by non-negative matrix factorization. Nature, 401(6755), 788-791.

2. Berry, M. W., Browne, M., Langville, A. N., Pauca, V. P., & Plemmons, R. J. (2007). Algorithms and applications for approximate nonnegative matrix factorization. Computational Statistics & Data Analysis, 52(1), 155-173.

3. Kim, J., He, Y., & Park, H. (2014). Algorithms for nonnegative matrix and tensor factorizations: A unified view based on block coordinate descent framework. Journal of Global Optimization, 58(2), 285-319.

Advantages and Limitations
------------------------
**Advantages**:
- Preserves non-negativity constraints
- Provides interpretable components
- Suitable for part-based decomposition
- Handles sparse data effectively

**Limitations**:
- Non-unique factorization
- Sensitive to initialization
- Local minima in optimization
- Computational complexity

Conclusion
----------
The NMF Comparator provides a powerful method for comparing non-negative matrices by leveraging their factorized representations. It is particularly valuable when dealing with naturally non-negative data and when interpretability of the components is important. The implementation in the distancia package offers a flexible framework for performing these comparisons while maintaining numerical stability and providing various options for customization.

.. note::

   The choice of the number of components and initialization strategy can significantly impact the results. It is recommended to run multiple comparisons with different initializations to ensure robust results.

See Also
--------
- ``PCAComparator``: For general matrix comparisons
- ``EnergyDistance``: For probability distribution-based comparisons
- ``LogDetDivergence``: For positive definite matrix comparisons
