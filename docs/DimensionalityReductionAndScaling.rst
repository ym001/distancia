DimensionalityReductionAndScaling
=================================

Introduction
------------
The `DimensionalityReductionAndScaling` class provides essential tools for reducing the dimensionality of datasets and scaling distance metrics. Dimensionality reduction is crucial for simplifying complex, high-dimensional data while preserving its most significant patterns. This is often used for visualization and to enhance the performance of machine learning algorithms by reducing computational complexity. Scaling the metric allows for normalization or adjusting distances for specific needs, ensuring that all dimensions contribute equally or according to a custom weighting scheme.

The main objective of this class is to make complex datasets more interpretable and manageable, while maintaining the most relevant information for analysis.

Formal Definition of Dimensionality Reduction and Scaling
---------------------------------------------------------
Given a dataset :math:`X = \{x_1, x_2, \dots, x_n\}` where each data point :math:`x_i` exists in a high-dimensional space :math:`\mathbb{R}^d`, dimensionality reduction techniques seek to find a transformation :math:`f: \mathbb{R}^d \to \mathbb{R}^k` where :math:`k \ll d` This transformation preserves the essential properties of the dataset while reducing its complexity.

One common method used in this class is Multi-Dimensional Scaling (MDS), which finds a configuration of points in a lower-dimensional space such that the pairwise distances are preserved as much as possible. Formally, let :math:`D(x_i, x_j)` represent the distance between points :math:`x_i` and :math:`x_j` in the original space, and :math:`D'(x'_i, x'_j)` the distance in the reduced space. MDS seeks to minimize the stress function:

.. math::

  \text{Stress}(X) = \sum_{i,j} (D(x_i, x_j) - D'(x'_i, x'_j))^2


In addition, scaling of the distance metric involves applying a multiplier :math:`\alpha` to adjust the magnitude of distances. For any two points :math:`x_i` and :math:`x_j`, the scaled distance is defined as:

.. math::

  D_\alpha(x_i, x_j) = \alpha \cdot D(x_i, x_j)


Significance of Dimensionality Reduction and Scaling
----------------------------------------------------
Dimensionality reduction is particularly significant in fields such as computer vision, natural language processing, and bioinformatics, where datasets often contain thousands or millions of features. Reducing the dimensionality helps in visualizing the data and uncovering hidden structures or patterns that may not be apparent in high-dimensional space.

Scaling is equally important when dealing with heterogeneous datasets where different dimensions have different units or ranges. By normalizing or scaling the metric, we ensure that no single feature disproportionately influences the results. This is critical in clustering, classification, and any machine learning task where distances are central.

Dimensionality reduction and scaling techniques enhance the performance of distance-based algorithms by making datasets more computationally efficient to process and easier to interpret.

Academic References
-------------------
The concept of dimensionality reduction has been extensively studied in the literature. Notable references include:

::footcite:t:`dimensionalityreductionandscaling1`,:footcite:t:`dimensionalityreductionandscaling1`
,:footcite:t:`dimensionalityreductionandscaling1`

.. footbibliography::


Conclusion
----------
The `DimensionalityReductionAndScaling` class offers powerful methods for simplifying and scaling datasets. By providing tools for dimensionality reduction such as Multi-Dimensional Scaling (MDS), it allows users to project high-dimensional data into lower dimensions while retaining its key characteristics. The scaling functionality ensures that distance metrics can be adjusted to suit different applications, providing flexibility in analysis. Overall, this class is indispensable for anyone working with complex datasets who needs to make them more interpretable and computationally efficient.

Methods Summary
---------------
- **metric_scaling(multiplier)**: Scales the metric by a given multiplier, useful for normalizing or adjusting the metric.
- **dimensionality_reduction_embedding(dataset, method='MDS')**: Projects the dataset into a lower-dimensional space using techniques such as Multi-Dimensional Scaling (MDS).
