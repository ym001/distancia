.. _negative-log-likelihood-probability:

===========================================================
Negative Log-Likelihood for Probabilistic Analysis
===========================================================

Introduction
------------

Negative Log-Likelihood (NLL) represents a fundamental probabilistic metric that plays a critical role in statistical inference and machine learning. This sophisticated measure provides a robust mechanism for evaluating the goodness of fit of probabilistic models by quantifying the likelihood of observed data under a given statistical distribution.

Theoretical Foundations
----------------------

Formula Interpretation
~~~~~~~~~~~~~~~~~~~~~

The Negative Log-Likelihood methodology is characterized by:

- Transforming probability likelihood into a minimizable loss function
- Providing a precise measure of model performance
- Enabling maximum likelihood estimation across diverse probabilistic models
- Facilitating model parameter optimization

Formal Mathematical Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a set of observations X and a parametric probability distribution with parameters :math:`\theta`, Negative Log-Likelihood is mathematically defined as:

.. math::

   NLL(\theta; X) = -\log\left(L(\theta; X)\right) = -\sum_{i=1}^{n} \log\left(P(x_i|\theta)\right)

Where:

- :math:`L(\theta; X)` represents the likelihood function
- :math:`P(x_i|\theta)` denotes the probability of observation :math:`x_i` under parameters :math:`\theta`
- :math:`\log()` represents the natural logarithm
- :math:`n` is the total number of observations

Key Mathematical Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Converts multiplicative likelihood to additive log-space
- Provides a convex optimization objective
- Enables gradient-based parameter estimation
- Maintains numerical stability for small probability values

Computational Complexity
-----------------------

Time Complexity
~~~~~~~~~~~~~~

- **O(n)**: Linear computational complexity
- Efficient processing of probabilistic time series
- Scalable across diverse dataset dimensions

Space Complexity
~~~~~~~~~~~~~~~

- **O(1)**: Constant memory requirements
- Minimal additional memory allocation
- Optimal memory utilization during computation

Academic References
------------------

1. Casella, G., & Berger, R. L. (2002). *Statistical Inference*. Duxbury Press.

2. Murphy, K. P. (2012). *Machine Learning: A Probabilistic Perspective*. MIT Press.

Implementation Considerations
----------------------------

Key Advantages
~~~~~~~~~~~~~~

- Fundamental approach to statistical model evaluation
- Provides a principled method for parameter estimation
- Enables maximum likelihood estimation
- Applicable across diverse probabilistic models
- Supports gradient-based optimization techniques

Practical Applications
~~~~~~~~~~~~~~~~~~~~~

- Statistical model selection
- Machine learning parameter estimation
- Time series analysis
- Probabilistic prediction
- Maximum likelihood estimation
- Model comparison and validation

Conclusion
----------

Negative Log-Likelihood emerges as a sophisticated probabilistic distance measure, offering a fundamental approach to quantifying the performance of statistical models. By transforming likelihood into a minimizable objective function, this metric provides researchers and data scientists with a powerful tool for understanding and optimizing probabilistic representations of time series data.

.. note::
   This implementation is part of the Distancia package and designed for advanced statistical analysis.

.. warning::
   Careful interpretation of NLL requires understanding the underlying probabilistic model and data characteristics.
