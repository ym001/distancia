Correlation Distance
==================

Introduction
-----------
The Correlation Distance is a metric that transforms the Pearson correlation coefficient into a distance measure, making it particularly useful for analyzing similarities between time series data. This distance metric focuses on capturing the relationship between the patterns and trends of two sequences, rather than their absolute values.

While correlation coefficients measure similarity (with values ranging from -1 to 1), the Correlation Distance converts this into a proper distance metric (with values ranging from 0 to 1), where:
- A distance of 0 indicates perfectly correlated sequences
- A distance of 1 indicates perfectly anti-correlated sequences
- A distance of 0.5 indicates uncorrelated sequences

Mathematical Definition
---------------------
For two time series X and Y, the Correlation Distance is defined as:

.. math::

   d_{corr}(X,Y) = \frac{1 - \rho(X,Y)}{2}

where:
- :math:`d_{corr}(X,Y)` is the correlation distance between sequences X and Y
- :math:`\rho(X,Y)` is the Pearson correlation coefficient between X and Y

Properties
---------
The Correlation Distance exhibits several important properties:

1. **Non-negativity**: The distance is always greater than or equal to 0
2. **Symmetry**: The distance from X to Y is the same as Y to X
3. **Scale-invariance**: The distance is independent of the scale of the input sequences
4. **Bounded**: Values are always in the range [0, 1]

Academic References
-----------------
The correlation distance has been widely used in various fields, particularly in time series analysis and clustering:

1. Golay, X., et al. (1998). "A new correlation-based fuzzy logic clustering algorithm for FMRI." Magnetic Resonance in Medicine, 40(2), 249-260.

2. Mantegna, R. N. (1999). "Hierarchical structure in financial markets." The European Physical Journal B, 11(1), 193-197.

Use Cases
--------
The Correlation Distance is particularly useful in:

- Financial time series analysis
- Gene expression studies
- Climate data analysis
- Pattern recognition in temporal data
- Signal processing applications

Conclusion
---------
The Correlation Distance provides a robust and intuitive way to measure the similarity between time series based on their patterns rather than absolute values. Its scale-invariance and bounded nature make it particularly suitable for comparing sequences of different magnitudes and for use in clustering algorithms. The transformation from correlation coefficient to distance metric allows for easier integration with distance-based machine learning algorithms.

.. note::
   This distance metric is particularly useful when the relationship between patterns is more important than the absolute differences between values.
