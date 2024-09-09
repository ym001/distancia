MarkovChainKullbackLeibler
===========================

Introduction
------------

The ``MarkovChainKullbackLeibler`` class calculates the Kullback-Leibler divergence between two Markov chains based on their transition matrices. The Kullback-Leibler divergence, also known as **KL-divergence**, is an asymmetric measure that quantifies the difference between two probability distributions. It is widely used in information theory to compare probabilistic models.

This class is specifically designed to measure the dissimilarity between two Markov chains by comparing their transition probabilities.

Meaning of the Distance
------------------------

The **Kullback-Leibler divergence** measures how much one Markov chain diverges from another. Although often referred to as a "distance," it is not a true distance in the mathematical sense because it is not symmetric and does not satisfy the triangle inequality. However, it provides a useful measure of information loss when one chain is used to approximate another.

A low Kullback-Leibler divergence between two chains indicates they are close in probabilistic behavior, while a high value suggests a greater dissimilarity.

Formal Definition
-----------------

The Kullback-Leibler divergence between two Markov chains ` P \) and \( Q \), with transition matrices \( P_{ij} \) and \( Q_{ij} \) respectively, is given by:

.. math::

    D_{KL}(P \parallel Q) = \sum_{i,j} P_{ij} \log \left( \frac{P_{ij}}{Q_{ij}} \right)

Where:

- \( P_{ij} \) is the transition probability from state \( i \) to state \( j \) in Markov chain \( P \),
- \( Q_{ij} \) is the corresponding probability for Markov chain \( Q \),
- The sum is over all states \( i \) and \( j \).

This divergence is defined only when all \( Q_{ij} \) are non-zero for those \( i, j \) where \( P_{ij} \neq 0 \).

Academic Reference
------------------

The Kullback-Leibler divergence was introduced by Solomon Kullback and Richard Leibler in their foundational 1951 paper:

- Kullback, S., & Leibler, R. A. (1951). On Information and Sufficiency. *The Annals of Mathematical Statistics*, 22(1), 79-86. doi:10.1214/aoms/1177729694.

Since then, it has become an essential tool in information theory, statistics, and machine learning, especially for comparing probabilistic models.

Conclusion
----------

The ``MarkovChainKullbackLeibler`` class in the ``distancia`` package provides an implementation of the Kullback-Leibler divergence for Markov chains. While not a true distance metric, it offers a powerful and useful measure for evaluating the difference between two probabilistic models. It is an important tool in fields like stochastic processes, dynamic systems analysis, and complex system behavior comparison.

This class can be used in various contexts, including probabilistic modeling, process analysis, and model comparison in machine learning.
