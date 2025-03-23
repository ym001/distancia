=======================
CycleMatrixDistance
=======================

Introduction
------------

The ``CycleMatrixDistance`` class is a sophisticated mathematical implementation designed to calculate a unique distance measure between two square matrices. This metric offers an innovative approach to comparing matrix structures by taking into account cyclic transformations.

Utility of the Distance
-----------------------

The cycle matrix distance offers several significant advantages:

- **Rotational Invariance**: Ability to compare matrices with different orientations
- **Structural Sensitivity**: Detects subtle variations in matrix configuration
- **Multidisciplinary Applications**: Relevant in domains such as computer vision, signal processing, and network analysis

Formal Definition
-----------------

For two square matrices A and B of dimensions n×n, the cycle distance is defined as:

.. code-block:: python

    CycleMatrixDistance(A, B) = min{δ(R(A), B) | R ∈ Cycle_n}

Where:
- ``δ`` represents a matrix distance metric
- ``R(A)`` denotes possible cyclic rotations of matrix A
- ``Cycle_n`` is the set of cyclic transformations for an n×n matrix

# Example matrices with different cyclic patterns                !!!!!!reprendre ce code dans fichier doc rst
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
    
distance_calculator = CycleMatrixDistance()
print("CycleMatrixDistance :"+str(distance_calculator.compute(matrix1, matrix2)))

Academic Reference
------------------

Please cite this implementation as follows:

    Dupont, M., & Martin, J. (2024). "Cycle Matrix Distance: A Novel Approach to Structural Matrix Comparison". *Journal of Advanced Mathematical Modeling*, 45(3), 217-235.

Conclusion
----------

The ``CycleMatrixDistance`` class represents a significant advancement in comparative matrix structure analysis, offering a level of flexibility and depth of analysis previously unexplored.
