================================================
Global Alignment Kernel (GAK) Distance
================================================

Introduction
------------
The Global Alignment Kernel (GAK) is a sophisticated similarity measure that combines the flexibility of Dynamic Time Warping (DTW) with the mathematical properties of kernel methods. It provides a positive definite kernel that captures the similarity between time series while considering all possible alignments between sequences. This approach offers both the ability to handle temporal distortions and the mathematical guarantees required for kernel-based learning methods.

Intuition Behind the Formula
---------------------------
The GAK builds upon the concept of sequence alignment by:

1. Considering all possible alignments between sequences, not just the optimal one
2. Weighting each alignment based on its quality
3. Incorporating a local similarity measure between sequence elements
4. Ensuring positive definiteness, making it suitable for kernel-based methods

The resulting measure provides a more robust similarity assessment than traditional DTW while maintaining the mathematical properties required for kernel methods.

Formal Definition
----------------
For two time series :math:`x = (x_1, ..., x_n)` and :math:`y = (y_1, ..., y_m)`, the GAK is defined as:

.. math::

    k_{GA}(x, y) = \sum_{π ∈ A(n,m)} e^{-\frac{1}{ν}D_π(x,y)}

where:
- :math:`A(n,m)` is the set of all possible alignments
- :math:`D_π(x,y)` is the cost of alignment π
- :math:`ν` is a smoothing parameter
- The local kernel between elements is defined as:

.. math::

    k(x_i, y_j) = e^{-\frac{\|x_i - y_j\|^2}{2σ^2}}

Academic References
-----------------
1. Cuturi, M. (2011). "Fast Global Alignment Kernels." International Conference on Machine Learning (ICML).

2. Cuturi, M., Vert, J. P., Birkenes, Ø., & Matsui, T. (2007). "A Kernel for Time Series Based on Global Alignments." IEEE International Conference on Acoustics, Speech and Signal Processing.

3. Lebarbier, É., Mary-Huard, T., & Robin, S. (2013). "Classification and Regression Trees on Time Series." Journal de la Société Française de Statistique.

Conclusion
---------
The Global Alignment Kernel represents a significant advancement in time series analysis by providing:

* A theoretically sound kernel for time series data
* Robust handling of temporal distortions
* Compatibility with kernel-based machine learning methods
* Efficient computation through dynamic programming

These properties make GAK particularly valuable in applications such as:

* Time series classification
* Sequence clustering
* Pattern recognition in temporal data
* Anomaly detection

Installation
-----------
The GAK metric is available as part of the ``distancia`` package and can be installed via pip:

.. code-block:: bash

   pip install distancia

Usage
-----
.. code-block:: python

   from distancia import GAK
   
   # Initialize with desired parameters
   gak = GAK(sigma=1.0, nu=0.1)
   
   # Calculate kernel value between two time series
   similarity = gak.calculate(series1, series2)
   
   # For use with kernel methods
   kernel_matrix = gak.compute_kernel_matrix(series_list)
