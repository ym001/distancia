MarkovChainWasserstein
=======================

Introduction
------------

The ``MarkovChainWasserstein`` class computes the Wasserstein distance (also known as the Earth Mover's Distance) between two Markov chains based on their transition matrices. The Wasserstein distance is a measure of the minimum amount of "work" required to transform one probability distribution into another, considering the underlying geometry of the space.

In the context of Markov chains, the Wasserstein distance captures how different the transition dynamics of two chains are.

Meaning of the Distance
-----------------------

The **Wasserstein distance** measures the cost of optimally transporting the mass of one probability distribution (in this case, one Markov chain’s transition matrix) to match another. It takes into account both the amount of probability that needs to be transported and the distance over which it must be moved.

A smaller Wasserstein distance indicates that the two Markov chains have similar transition behaviors, while a larger distance suggests more substantial differences in their probabilistic dynamics.

Formal Definition
-----------------

The Wasserstein distance between two Markov chains :math:`P` and :math:`Q`, with transition matrices :math:`P_{ij}` and \( Q_{ij} `, is formally given as:

.. math::

    W(P, Q) = \inf_{\gamma \in \Gamma(P, Q)} \sum_{i,j} \gamma(i,j) d(i, j)

Where:

- :math:`P_{ij}` and :math:`Q_{ij}` represent the transition probabilities of the two Markov chains,
- :math:`d(i, j)` is a distance metric on the state space,
- :math:`\Gamma(P, Q)` is the set of all joint distributions with marginals :math:`P` and :math:`Q`,
- The infimum represents the minimum transportation cost.

Usage Example
-------------


.. code-block:: python

    from distancia import MarkovChainWasserstein


    # Example usage
    P = [[0.9, 0.1], [0.2, 0.8]]  # Transition matrix for Markov chain 1
    Q = [[0.85, 0.15], [0.25, 0.75]]  # Transition matrix for Markov chain 2
    cost_matrix = [[0, 1], [1, 0]]  # Cost matrix (Euclidean distance between states)

    markov_wasserstein = MarkovChainWasserstein(P, Q, cost_matrix)

    # Compute the Wasserstein distance between stationary distributions
    print("Wasserstein Distance:", markov_wasserstein.wasserstein_distance())


.. code-block:: bash

   >>>Wasserstein Distance: 0.041666666586909984


Academic Reference
------------------

The Wasserstein distance has its origins in optimal transport theory and has been extensively studied in various fields, including probability theory and machine learning. One of the key references for the Wasserstein distance is:


This book provides a comprehensive treatment of the theory behind the Wasserstein distance and its applications.

Conclusion
----------

The ``MarkovChainWasserstein`` class in the ``distancia`` package offers an efficient method to compute the Wasserstein distance between two Markov chains. This distance metric is useful in various applications, including dynamic systems comparison, probabilistic modeling, and machine learning. By understanding how the transition dynamics of two chains differ, researchers can gain valuable insights into the behavior of complex stochastic systems.

This class is particularly valuable when one needs to quantify differences between Markov processes in a principled and geometrically meaningful way.
