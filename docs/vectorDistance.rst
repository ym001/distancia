Vector-Based Distances in Distancia
===================================

Introduction
============
When comparing vectors, it is crucial to understand the different mathematical principles and methods that can be applied depending on the type of data and the context. The **Distancia** package provides a comprehensive suite of vector-based distance measures that allow for the evaluation of similarity or dissimilarity between vectors. These methods can be applied in domains such as machine learning, signal processing, and data clustering, among others.

Categories of Vector-Based Distances
====================================

1. **Metric Distances**
2. **Non-Metric Distances**
3. **Probabilistic Distances**
4. **Information-Theoretic Distances**


List of Vector-Based Distances
==============================

**Metric Distances**
--------------------

Metric distances follow mathematical properties such as symmetry, non-negativity, and the triangle inequality. These distances are often used when a precise, geometrically consistent measurement is required between vectors.

1. :doc:`Euclidean`

   - Calculates the straight-line (L2 norm) distance between two vectors in n-dimensional space, often used as the default distance measure.

2. :doc:`Manhattan`

   - Measures the distance between two vectors by summing the absolute differences of their coordinates, simulating a grid-like path between points.

3. :doc:`Minkowski`

   - Generalizes both Euclidean and Manhattan distances by using an adjustable parameter p to define the Lp norm, providing flexibility in the distance calculation.

4. :doc:`Chebyshev`

   - Measures the greatest difference between any corresponding components of two vectors, often used in chessboard-like grid layouts.

5. :doc:`Cosine`

   - Measures the cosine of the angle between two vectors, evaluating how closely aligned they are in space, regardless of their magnitude.

6. :doc:`Mahalanobis`

   - A distance metric that accounts for the correlations between features, giving greater weight to highly correlated dimensions.

**Non-Metric Distances**
------------------------

  Non-metric distances do not strictly adhere to all the properties of metric distances but are often more flexible or tailored for specific data types. These distances are useful when traditional metrics fail to capture the nuances in vector comparison.

1. :doc:`Hamming`

   - Counts the number of positions where corresponding elements of two vectors differ, commonly used for comparing binary or categorical data.

2. :doc:`Jaccard`

   - Measures the dissimilarity between two vectors by comparing the size of their intersection relative to their union, often used for sparse or binary data.

3. :doc:`Bray-Curtis`

   - Quantifies the dissimilarity between two vectors based on their magnitudes, commonly used in ecological and biological studies.

**Probabilistic Distances**
---------------------------

  Probabilistic distances treat the vectors as representations of probability distributions. These measures are useful in contexts such as statistical modeling, where vectors represent frequencies, likelihoods, or distributions.

1. :doc:`Kullback-LeiblerDivergence`

   - Measures the divergence between two probability distributions by comparing how one distribution diverges from a reference distribution.

2. :doc:`Jensen-ShannonDivergence`

   - A symmetrized and smoother version of Kullback-Leibler divergence that measures the similarity between two probability distributions.

3. :doc:`Bhattacharyya Distance`

   - Estimates the amount of overlap between two statistical distributions, useful in classification and pattern recognition.

**Information-Theoretic Distances**
-----------------------------------

  Information-theoretic distances are derived from concepts in information theory, such as entropy and divergence. These distances quantify the difference in information content between vectors, making them ideal for applications involving data compression or communication theory.

1. :doc:`Entropy-Based Distance`

   - Measures the difference in information content between two vectors by comparing their entropy values, capturing the unpredictability in their distributions.

2. :doc:`Normalized Compression Distance`

   - Measures the distance between two data points by comparing how much their combined representation can be compressed, making it ideal for detecting shared structure between data.
   
Conclusion
==========
The **Distancia** package provides a versatile and robust collection of vector-based distance measures, allowing users to compare vectors in various ways depending on their specific needs. By categorizing distances into metric, non-metric, probabilistic, and information-theoretic types, **Distancia** enables flexible and accurate vector comparisons. Whether you need to compute exact geometric distances or probabilistic differences, **Distancia** offers a comprehensive toolkit for analyzing the relationships between vectors in your data.
