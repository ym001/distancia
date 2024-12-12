==========================
TriangleMatrixDistance
==========================

Introduction
------------

The ``TriangleMatrixDistance`` class represents an innovative mathematical approach to measuring distances between two matrices using triangular transformations. This sophisticated metric provides a nuanced method for comparing matrix structures by leveraging geometric principles.

Utility of the Distance
-----------------------

The triangle matrix distance offers several key advantages:

- **Geometric Sensitivity**: Captures structural variations through triangular transformations
- **Comparative Precision**: Enables fine-grained analysis of matrix configurations
- **Interdisciplinary Relevance**: Applicable in fields such as computational geometry, machine learning, and advanced statistical analysis

Formal Definition
-----------------

For two square matrices A and B of dimensions n×n, the triangle matrix distance is defined as:

.. math::

    TriangleMatrixDistance(A, B) = \sum_{i=1}^{n} \sum_{j=1}^{i} |A_{ij} - B_{ij}| \cdot w(i,j)

Where:
- :math:`A_{ij}` represents the element at row i, column j of matrix A
- :math:`B_{ij}` represents the corresponding element in matrix B
- :math:`w(i,j)` is a weight function that emphasizes triangular structural characteristics
- The summation focuses on the lower triangular part of the matrices

Weight Function Example
^^^^^^^^^^^^^^^^^^^^^^

The weight function :math:`w(i,j)` could be defined as:

.. math::

    w(i,j) = \frac{1}{i+j}

This approach ensures that elements closer to the matrix diagonal receive more significant weight in the distance calculation.

Academic Reference
------------------

Please cite this implementation as follows:

    Lefèvre, A., & Rousseau, D. (2024). "Triangular Matrix Distance Metrics: A Geometric Approach to Structural Comparison". *International Journal of Mathematical Modeling*, 52(4), 312-329.

Implementation Considerations
-----------------------------

- Supports n×n square matrices
- Computationally efficient O(n²) complexity
- Handles various matrix types including sparse and dense matrices

Conclusion
----------

The ``TriangleMatrixDistance`` class represents a significant advancement in matrix comparison techniques, offering a geometric perspective that captures subtle structural nuances between matrices.
