=================================================
Soft Dynamic Time Warping (Soft-DTW) Distance
=================================================

Introduction
------------
Soft Dynamic Time Warping (Soft-DTW) is a differentiable variant of the classical Dynamic Time Warping (DTW) algorithm. It provides a smooth measure of similarity between temporal sequences, making it particularly suitable for gradient-based optimization problems and deep learning applications. Unlike traditional DTW, Soft-DTW replaces the min operator with a differentiable soft-minimum, enabling backpropagation through the distance computation.

Intuition Behind the Formula
---------------------------
The key insight behind Soft-DTW is the replacement of the hard minimum operation in classical DTW with a smoothed version. This modification:

1. Creates a continuous and differentiable loss surface
2. Allows for more flexible alignments between sequences
3. Provides better gradient flow in optimization problems
4. Maintains the essential time-warping properties of DTW

The smoothing parameter γ (gamma) controls the degree of smoothing: as γ approaches 0, Soft-DTW converges to classical DTW, while larger values create a more smooth approximation.

Formal Definition
----------------
For two time series :math:`x = (x_1, ..., x_n)` and :math:`y = (y_1, ..., y_m)`, Soft-DTW is defined as:

.. math::

    DTW_γ(x, y) = min^γ_{π ∈ A(n,m)} ⟨A_π, Δ(x, y)⟩

where:
- :math:`min^γ` is the soft-minimum operator with smoothing parameter γ
- :math:`A(n,m)` is the set of all possible alignment paths
- :math:`A_π` is the alignment matrix
- :math:`Δ(x, y)` is the pairwise distance matrix
- The soft-min operator is defined as:

.. math::

    min^γ(a_1, ..., a_n) = -γ \log(\sum_{i=1}^n e^{-a_i/γ})

Academic References
-----------------
1. Cuturi, M., & Blondel, M. (2017). "Soft-DTW: A Differentiable Loss Function for Time-Series." International Conference on Machine Learning (ICML).

2. Saigo, H., Jean-Philippe, V., & Vert, J. P. (2006). "Optimizing amino acid substitution matrices with a local alignment kernel." BMC Bioinformatics, 7(1), 246.

3. Blondel, M., Mensch, A., & Vert, J. P. (2018). "Differentiable Dynamic Programming for Structured Prediction and Attention." International Conference on Machine Learning (ICML).

Conclusion
---------
Soft-DTW represents a significant advancement in time series analysis by providing a differentiable alternative to classical DTW. Its key advantages include:

* Seamless integration with gradient-based optimization methods
* Improved stability in learning tasks
* Flexible control over the degree of smoothing
* Preservation of DTW's ability to handle temporal distortions

These properties make Soft-DTW particularly valuable in modern machine learning applications, especially those involving neural networks and deep learning architectures.

Installation
-----------
The Soft-DTW metric is available as part of the ``distancia`` package and can be installed via pip:

.. code-block:: bash

   pip install distancia

Usage
-----
.. code-block:: python

   from distancia import SoftDTW
   
   # Initialize with desired gamma parameter
   soft_dtw = SoftDTW(gamma=1.0)
   
   # Calculate distance between two time series
   distance = soft_dtw.calculate(series1, series2)
   
   # For gradient-based optimization
   gradient = soft_dtw.gradient(series1, series2)
