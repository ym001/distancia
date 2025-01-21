HMM Distance
===========

Introduction
-----------
The Hidden Markov Model (HMM) Distance is a sophisticated method for measuring similarity between time series by leveraging the power of Hidden Markov Models. This approach is particularly useful when dealing with sequential data where the underlying states are not directly observable but influence the observable sequences.

Meaning and Applications
-----------------------
The HMM distance quantifies how similar two time series are by comparing their underlying generative processes. Instead of comparing the raw sequences directly, this method:

1. Fits separate HMMs to each time series
2. Compares the fitted model parameters to assess similarity
3. Provides insights into the hidden states and transition dynamics

This approach is particularly valuable when:

* The observed sequences have different lengths
* There are underlying state transitions that affect the observations
* Direct point-to-point comparison is not meaningful

Formal Definition
----------------
Given two time series X and Y, the HMM distance is defined as:

.. math::

   D_{HMM}(X, Y) = \|\theta_X - \theta_Y\|

where:

* :math:`\theta_X` represents the parameters of the HMM fitted to sequence X
* :math:`\theta_Y` represents the parameters of the HMM fitted to sequence Y
* :math:`\|\cdot\|` denotes an appropriate norm in the parameter space

The parameters typically include:

* Transition probabilities matrix (A)
* Emission probabilities (B)
* Initial state distribution (π)

Academic Citations
----------------
The HMM distance measure builds upon fundamental work in Hidden Markov Models and their applications to time series analysis:

1. Rabiner, L. R. (1989). A tutorial on hidden Markov models and selected applications in speech recognition. Proceedings of the IEEE, 77(2), 257-286.

2. Smyth, P. (1997). Clustering sequences with hidden Markov models. Advances in neural information processing systems, 648-654.

3. Panuccio, A., Bicego, M., & Murino, V. (2002). A Hidden Markov Model-based approach to sequential data clustering. In Structural, Syntactic, and Statistical Pattern Recognition (pp. 734-743).

Conclusion
---------
The HMM Distance measure provides a robust framework for comparing time series by focusing on their underlying generative processes rather than surface-level similarities. This makes it particularly suitable for applications where:

* The data exhibits clear state-dependent behavior
* Traditional distance measures fail to capture sequential patterns
* The underlying process dynamics are more important than point-wise comparisons

This implementation in the distancia package offers a flexible and efficient way to compute HMM-based distances between time series, supporting various parameter settings and model configurations.
