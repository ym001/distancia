Log-Cosh Loss Distance
=====================

Introduction
------------
Log-Cosh Loss Distance is a robust metric for measuring distribution differences, offering a smooth approximation of Mean Absolute Error (MAE) through hyperbolic cosine transformation.

Meaning and Applications
-----------------------
The Log-Cosh Loss Distance provides:
* Smooth gradient characteristics
* Resilience to outliers
* Computationally efficient distribution comparison

Formal Definition
-----------------
For probability distributions P and Q, the Log-Cosh Loss Distance is defined as:

.. math::

   D_{LogCosh}(P,Q) = \int_{-\infty}^{\infty} \log(\cosh(p(x) - q(x))) dx

Key properties:
* Near-quadratic for small errors
* Logarithmic scaling for large differences
* Numerically stable approximation

Academic Citations
-----------------
1. Mori, M. (2019). Advanced Machine Learning Techniques. Springer.

2. Schaul, T., et al. (2013). No More Pesky Learning Rates. International Conference on Machine Learning.

3. Zhang, L., & Lemme, A. (2017). Loss Function Analysis in Deep Learning. IEEE Transactions.

Conclusion
----------
Log-Cosh Loss Distance offers a sophisticated approach to measuring distribution differences, particularly effective in:
* Neural network training
* Robust regression tasks
* Advanced statistical learning applications

The implementation in the distancia package provides a powerful tool for comparing probability distributions with enhanced numerical stability.
