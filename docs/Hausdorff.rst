Hausdorff Distance
==================

Introduction
------------

The Hausdorff Distance is a measure of the similarity between two sets of points. It is widely used in various domains such as image analysis, pattern recognition, and computer vision. The distance quantifies how far two sets are from each other by finding the greatest of all distances from a point in one set to the closest point in the other set.

Meaning of the Distance
-----------------------

The Hausdorff Distance captures the largest minimal distance between two sets of points. This makes it sensitive to the "worst-case" point-to-set distances, which is useful when a global measure of similarity is required.

Formal Definition
-----------------

Let A and B be two non-empty sets of points in a metric space. The Hausdorff Distance `d_H` is defined as:

.. math::

    d_H(A, B) = \max \{ \sup_{a \in A} \inf_{b \in B} d(a, b), \sup_{b \in B} \inf_{a \in A} d(b, a) \}

Where:
- `d(a, b)` is the distance between points `a` and `b` in the metric space.
- `A` and `B` are the two sets being compared.

Academic Reference
------------------

Rote, G. (1991). Computing the Hausdorff Distance between Sets of Points. *Proceedings of the International Conference on Computational Geometry*, 324-330.

Conclusion
----------

The Hausdorff Distance is a robust method to compare two sets of points, particularly useful in domains where the worst-case scenario matters. It finds applications in image comparison, shape analysis, and trajectory matching.
