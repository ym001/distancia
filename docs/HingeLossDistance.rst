Hinge Loss Distance
==================

Introduction
------------
Hinge Loss Distance is a pivotal metric primarily used in Support Vector Machines (SVMs) for measuring distance between probability distributions during neural network training.

Meaning and Applications
-----------------------
Hinge Loss Distance characterizes:
* Separability between probability distributions
* Margin optimization in classification tasks
* Robust handling of linear and non-linear separations

Formal Definition
-----------------
For probability distributions P and Q, the Hinge Loss Distance is defined as:

.. math::

   D_{Hinge}(P,Q) = \max(0, 1 - \hat{y}(p(x) - q(x)))

where:
* :math:`\hat{y}` is the true label (+1 or -1)
* Penalizes misclassified samples
* Ensures maximal margin between distributions

Academic Citations
-----------------
1. Cortes, C., & Vapnik, V. (1995). Support-vector networks. Machine Learning, 20(3), 273-297.

2. Scholkopf, B., & Smola, A. J. (2001). Learning with Kernels. MIT Press.

3. Cristianini, N., & Shawe-Taylor, J. (2000). An Introduction to Support Vector Machines. Cambridge University Press.

Conclusion
----------
Hinge Loss Distance provides a powerful approach for:
* Measuring distribution separation
* Optimizing classification margins
* Supporting complex machine learning algorithms

Implemented in the distancia package for advanced statistical learning tasks.
