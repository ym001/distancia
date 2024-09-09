MarkovChainJensenShannon
==========================

Introduction
------------

The ``MarkovChainJensenShannon`` class computes the Jensen-Shannon divergence between two Markov chains based on their transition matrices. The Jensen-Shannon divergence is a symmetric and smoothed version of the Kullback-Leibler divergence, making it a true metric in many contexts. It is widely used to compare probability distributions because it is always finite and symmetric.

In the context of Markov chains, it provides a way to measure how different the transition dynamics of two chains are.

Meaning of the Distance
-----------------------

The **Jensen-Shannon divergence** measures the similarity between two probability distributions by calculating the Kullback-Leibler divergence of each distribution from the average of the two. Unlike the Kullback-Leibler divergence, the Jensen-Shannon divergence is symmetric and bounded between 0 and 1, making it more interpretable as a distance measure.

A lower Jensen-Shannon divergence between two Markov chains indicates similar transition dynamics, while a higher value signifies more significant differences.

Formal Definition
-----------------

The Jensen-Shannon divergence between two Markov chains :math:`P` and :math:`Q`, with transition matrices :math:`P_{ij}` and :math:`Q_{ij}`, is defined as:

.. math::

    D_{JS}(P \parallel Q) = \frac{1}{2} D_{KL}(P \parallel M) + \frac{1}{2} D_{KL}(Q \parallel M)

Where:

- :math:`M` is the average of the two transition matrices: :math:`M = \frac{1}{2}(P + Q)`,
- :math:`D_{KL}` is the Kullback-Leibler divergence,
- :math:`P_{ij} \) and \( Q_{ij}` represent the transition probabilities of the two Markov chains.

The Jensen-Shannon divergence is symmetric and always defined, even when the Kullback-Leibler divergence is not.

Usage Example
-------------


.. code-block:: python

    from distancia import MarkovChainJensenShannon

    # Example usage
    P = [[0.9, 0.1], [0.2, 0.8]]  # Transition matrix for Markov chain 1
    Q = [[0.85, 0.15], [0.25, 0.75]]  # Transition matrix for Markov chain 2

    markov_js = MarkovChainJensenShannon(P, Q)

    # Compute the Jensen-Shannon distance between stationary distributions
    print("Jensen-Shannon Distance:", markov_js.compute_js_distance())



.. code-block:: bash

   >>>Jensen-Shannon Distance: 0.030808744879339073



Academic Reference
------------------

The Jensen-Shannon divergence was introduced in:
:footcite:t:`MarkovChainJensenShannon`

.. footbibliography::

This paper provides a comprehensive treatment of the Jensen-Shannon divergence and its theoretical properties.

Conclusion
----------

The ``MarkovChainJensenShannon`` class in the ``distancia`` package implements the Jensen-Shannon divergence for comparing the transition matrices of two Markov chains. This distance is especially useful for comparing stochastic processes, as it provides a symmetric, bounded, and interpretable measure of dissimilarity.

By utilizing this class, users can gain insights into the differences between the probabilistic dynamics of two Markov chains and apply it in various fields such as machine learning, statistical modeling, and information theory.
