=================================================
Permutation Entropy Distance
=================================================

Introduction
------------
The Permutation Entropy Distance is a complexity-based measure for comparing time series that leverages the concept of ordinal patterns and information theory. This approach transforms time series into sequences of permutations representing local ordinal patterns, then compares their entropy profiles. By focusing on the ordinal relationships between values rather than the values themselves, this metric is particularly robust to noise and scaling variations while capturing the underlying dynamics of the systems.

Intuition Behind the Formula
---------------------------
The method works by:

1. Converting segments of the time series into ordinal patterns (permutations)
2. Computing the probability distribution of these patterns
3. Calculating the entropy of the distribution
4. Comparing the entropy profiles of different time series

This approach is based on the principle that similar dynamical systems will produce similar distributions of ordinal patterns, regardless of their absolute values or scales.

Formal Definition
----------------
For a time series :math:`X = (x_1, ..., x_N)`, the permutation entropy is defined using:

.. math::

    PE(X) = -\sum_{π ∈ Π_n} p(π) \log p(π)

where:
- :math:`Π_n` is the set of all possible permutations of order n
- :math:`p(π)` is the probability of permutation π occurring in the time series
- The distance between two time series X and Y is then:

.. math::

    D_{PE}(X,Y) = |PE(X) - PE(Y)| + λ KL(P_X || P_Y)

where:
- :math:`KL(P_X || P_Y)` is the Kullback-Leibler divergence between permutation distributions
- :math:`λ` is a weighting parameter
- :math:`P_X` and :math:`P_Y` are the probability distributions of permutations

Academic References
-----------------
1. Bandt, C., & Pompe, B. (2002). "Permutation Entropy: A Natural Complexity Measure for Time Series." Physical Review Letters, 88(17).

2. Zanin, M., Zunino, L., Rosso, O. A., & Papo, D. (2012). "Permutation Entropy and Its Main Biomedical and Econophysics Applications: A Review." Entropy, 14(8).

3. Cao, Y., Tung, W. W., Gao, J. B., Protopopescu, V. A., & Hively, L. M. (2004). "Detecting Dynamical Changes in Time Series Using the Permutation Entropy." Physical Review E, 70(4).

Conclusion
---------
The Permutation Entropy Distance provides several advantages for time series analysis:

* Robustness to noise and scaling variations
* Capture of dynamical system properties
* Computational efficiency
* Model-free approach
* Invariance to monotonic transformations

These characteristics make it particularly valuable for:

* Complexity analysis of time series
* Change point detection
* System state monitoring
* Classification of dynamical systems
* Anomaly detection in temporal data

Installation
-----------
The Permutation Entropy Distance metric is available as part of the ``distancia`` package and can be installed via pip:

.. code-block:: bash

   pip install distancia

Usage
-----
.. code-block:: python

   from distancia import PermutationEntropyDistance
   
   # Initialize with desired parameters
   pe_dist = PermutationEntropyDistance(order=3, delay=1, lambda_weight=0.5)
   
   # Calculate distance between two time series
   distance = pe_dist.calculate(series1, series2)
   
   # Get individual entropy values
   entropy1 = pe_dist.get_entropy(series1)
   entropy2 = pe_dist.get_entropy(series2)
