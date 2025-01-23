Huber Loss Distance
==================

Introduction
------------
Huber Loss Distance is a robust metric for measuring distance between probability distributions, particularly valuable in neural network training. It combines characteristics of Mean Squared Error (MSE) and Mean Absolute Error (MAE), providing resilience to outliers while maintaining computational efficiency.

Meaning and Applications
-----------------------
The Huber Loss Distance offers a hybrid approach to measuring distribution differences by:

* Reducing the impact of extreme outliers
* Providing smooth gradient characteristics
* Balancing sensitivity and robustness

Formal Definition
-----------------
For probability distributions P and Q, the Huber Loss Distance is defined as:

.. math::

   D_{Huber}(P,Q) = \int_{-\infty}^{\infty} \rho\left(\frac{p(x) - q(x)}{\sigma}\right) dx

where:

* :math:`\rho(z) = \begin{cases} 
      \frac{1}{2}z^2 & \text{if } |z| \leq \delta \\
      \delta|z| - \frac{1}{2}\delta^2 & \text{otherwise}
   \end{cases}`
* :math:`\delta` is a hyperparameter controlling the transition point
* :math:`\sigma` is the scale parameter

Key characteristics:
* Quadratic for small errors
* Linear for large errors
* Reduces extreme outlier influence

Academic Citations
-----------------
1. Huber, P. J. (1964). Robust estimation of a location parameter. The Annals of Mathematical Statistics, 35(1), 73-101.

2. Vapnik, V. (1998). Statistical learning theory. Wiley.

3. Bishop, C. M. (2006). Pattern recognition and machine learning. Springer.

Conclusion
----------
Huber Loss Distance provides a robust, flexible approach to measuring distribution differences, particularly effective in:

* Neural network training
* Regression tasks with potential outliers
* Statistical learning applications

The implementation in the distancia package offers a sophisticated tool for comparing probability distributions with enhanced resilience to extreme values.==================

