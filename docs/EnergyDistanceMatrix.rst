EnergyDistanceMatrix
===================

Introduction
------------
The EnergyDistanceMatrix class implements the energy distance metric, a powerful statistical measure for comparing probability distributions. This metric belongs to the family of distance-based approaches in multivariate statistics and provides a robust method for measuring dissimilarity between distributions without requiring density estimation.

Description
-----------
The energy distance derives its name from Newton's gravitational potential energy, drawing an analogy between statistical distances and physical potential energies. For two distributions P and Q, the energy distance quantifies their dissimilarity by considering all pairwise Euclidean distances between samples.

Mathematical Formulation
-----------------------
For two samples X and Y with sizes n and m respectively, the energy distance is defined as:

.. math::

   \mathcal{E}(X,Y) = \left(\frac{2}{nm}\sum_{i=1}^n\sum_{j=1}^m ||x_i - y_j|| - \frac{1}{n^2}\sum_{i=1}^n\sum_{j=1}^n ||x_i - x_j|| - \frac{1}{m^2}\sum_{i=1}^m\sum_{j=1}^m ||y_i - y_j||\right)^{\frac{1}{2}}

where:
- ||·|| denotes the Euclidean norm
- x_i and y_j are sample points from distributions X and Y respectively
- n and m are the sample sizes for X and Y

Properties
---------
The energy distance has several important properties:

1. Non-negativity: E(X,Y) ≥ 0
2. Identity of indiscernibles: E(X,Y) = 0 if and only if X and Y are identically distributed
3. Symmetry: E(X,Y) = E(Y,X)
4. Triangle inequality: E(X,Z) ≤ E(X,Y) + E(Y,Z)

Academic References
-----------------
1. Székely, G. J., & Rizzo, M. L. (2013). Energy statistics: A class of statistics based on distances. Journal of Statistical Planning and Inference, 143(8), 1249-1272.

2. Szekely, G. J. (2003). E-statistics: The energy of statistical samples. Bowling Green State University, Department of Mathematics and Statistics Technical Report, 3(05), 1-18.

3. Rizzo, M. L., & Székely, G. J. (2016). Energy distance. Wiley Interdisciplinary Reviews: Computational Statistics, 8(1), 27-38.

Conclusion
----------
The EnergyDistanceMatrix class provides a robust implementation of the energy distance metric, making it particularly useful for:
- Testing multivariate goodness-of-fit
- Measuring statistical distance between samples
- Detecting differences in distributions without assuming a parametric form
- Cluster analysis and pattern recognition tasks

This implementation is optimized for efficiency while maintaining numerical stability, making it suitable for both small and large-scale statistical applications within the distancia package.
