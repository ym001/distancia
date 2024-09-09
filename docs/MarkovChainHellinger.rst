MarkovChainTotalVariation
==========================

Introduction
------------

The ``MarkovChainTotalVariation`` class calculates the total variation distance between two Markov chains by comparing their transition matrices. The total variation distance is a classical and intuitive metric in probability theory, measuring the maximum difference between two probability distributions.

In the context of Markov chains, it evaluates how different the behavior of two chains is based on their transition probabilities.

Meaning of the Distance
-----------------------

The **total variation distance** represents the largest possible discrepancy between the transition probabilities of two Markov chains for any given state. It quantifies how much probability mass needs to be moved or altered to transform the transition matrix of one chain into that of another.

A small total variation distance indicates that the two Markov chains behave similarly, while a large distance suggests significant differences in their transitions.

Formal Definition
-----------------

The total variation distance between two Markov chains :math:`P` and :math:`Q`, with transition matrices :math:`P_{ij}` and :math:`Q_{ij}`, is defined as:

.. math::

    d_{TV}(P, Q) = \frac{1}{2} \sum_{i,j} \left| P_{ij} - Q_{ij} \right|

Where:

- :math:`P_{ij}` is the probability of transitioning from state :math:`i` to state :math:`j` in the first Markov chain,
- :math:`Q_{ij}` is the corresponding transition probability in the second Markov chain,
- The absolute difference :math:`\left| P_{ij} - Q_{ij} \right|` represents the local discrepancy between the two chains for each pair of states.

Usage Example
-------------


.. code-block:: python

    from distancia import MarkovChainHellinger

    # Example usage
    P = [[0.9, 0.1], [0.2, 0.8]]  # Transition matrix for Markov chain 1
    Q = [[0.85, 0.15], [0.25, 0.75]]  # Transition matrix for Markov chain 2

    markov_hellinger = MarkovChainHellinger(P, Q)

    # Compute the Hellinger distance between stationary distributions
    print("Hellinger Distance:", markov_hellinger.compute_hellinger_distance())


.. code-block:: bash

   >>>Hellinger Distance: 0.0308120923491926


Academic Reference
------------------

The total variation distance is widely used in probability theory and Markov chain analysis. One foundational reference is:

:footcite:t:`MarkovChainHellinger`

.. footbibliography::

This manuscript covers the use of total variation distance in the analysis of Markov chains and random walks.

Conclusion
----------

The ``MarkovChainTotalVariation`` class in the ``distancia`` package implements the total variation distance for comparing the transition matrices of two Markov chains. This distance is particularly useful in applications where it is important to understand the maximum deviation between probabilistic behaviors.

By using this class, practitioners can easily quantify the dissimilarity between two Markov chains and gain insights into the differences in their underlying stochastic processes.
