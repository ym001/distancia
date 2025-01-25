.. _log-cosh-loss-probability:

===========================================================
Log-Cosh Loss for Probabilistic Distance Measurement
===========================================================

Introduction
------------

Log-Cosh Loss represents an innovative probabilistic distance measure that provides a smooth, differentiable approximation of Mean Absolute Error (MAE). This sophisticated metric offers enhanced computational efficiency and numerical stability when comparing time series probability distributions.

Theoretical Foundations
----------------------

Formula Interpretation
~~~~~~~~~~~~~~~~~~~~~

The Log-Cosh Loss methodology creates a unique loss function that:

- Delivers a smooth approximation of absolute error
- Provides robust handling of probabilistic variations
- Maintains computational efficiency through hyperbolic cosine transformation

Formal Mathematical Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For probability distributions P and Q, the Log-Cosh Loss is defined as:

.. math::

   L_{log-cosh}(P, Q) = \sum_{i} \log(\cosh(p_i - q_i))

Where:

- :math:`p_i` represents individual probability values in distribution P
- :math:`q_i` represents individual probability values in distribution Q
- :math:`\cosh()` denotes the hyperbolic cosine function
- :math:`\log()` represents the natural logarithm

Mathematical Properties
~~~~~~~~~~~~~~~~~~~~~~

- Exhibits quadratic behavior for small errors
- Provides smoother gradient compared to traditional loss functions
- Maintains differentiability across the entire error range

Computational Complexity
-----------------------

Time Complexity
~~~~~~~~~~~~~~

- **O(n)**: Linear computational complexity
- Efficient processing of probabilistic time series
- Minimal computational overhead

Space Complexity
~~~~~~~~~~~~~~~

- **O(1)**: Constant memory requirements
- Minimal additional memory allocation during computation
- Scalable across varying dataset sizes

Academic References
------------------

1. Pohlen, T., Pecka, M., & Derner, E. (2018). *Learning Robust Motion Representations through Temporal Smoothing*. International Conference on Machine Learning.

2. Cheng, X., et al. (2019). *Robust Loss Functions for Deep Learning in Computer Vision*. IEEE Transactions on Pattern Analysis and Machine Intelligence.

Implementation Considerations
----------------------------

Key Advantages
~~~~~~~~~~~~~~

- Superior numerical stability
- Smooth gradient characteristics
- Robust handling of probabilistic distribution variations
- Reduced sensitivity to extreme observations
- Computationally efficient implementation

Practical Applications
~~~~~~~~~~~~~~~~~~~~~

- Time series analysis
- Probabilistic machine learning
- Financial risk modeling
- Signal processing and pattern recognition

Conclusion
----------

Log-Cosh Loss emerges as a sophisticated probabilistic distance measure, offering a nuanced approach to comparing time series distributions. By leveraging the hyperbolic cosine transformation, this metric provides a robust, computationally efficient alternative to traditional loss functions.

.. note::
   This implementation is part of the Distancia package and designed for advanced statistical analysis.

.. warning::
   Appropriate parameter selection remains critical for optimal performance.
