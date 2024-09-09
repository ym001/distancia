MarkovChainSpectral
====================

Introduction
------------

The ``MarkovChainSpectral`` class computes the spectral distance between two Markov chains by comparing their transition matrices. The spectral distance focuses on the eigenvalues of the transition matrices and measures how different the chains are in terms of their long-term behavior. It is particularly relevant in the study of the stability and convergence properties of Markov chains.

In the context of Markov chains, the spectral distance provides insights into the differences between the dynamics of the two systems.

Meaning of the Distance
-----------------------

The **spectral distance** measures the discrepancy between the eigenvalues of the transition matrices of two Markov chains. The eigenvalues of a transition matrix govern the long-term behavior of a Markov chain, including how quickly it converges to its steady-state distribution. By comparing the eigenvalues of two chains, we can assess how their long-term behaviors differ.

A smaller spectral distance indicates that the two chains exhibit similar long-term dynamics, while a larger distance suggests significant differences in their stability and convergence properties.

Formal Definition
-----------------

The spectral distance between two Markov chains :math:`P` and :math:`Q`, with transition matrices :math:`P_{ij} \) and :math:`Q_{ij}`, is defined based on the difference between their eigenvalues:

.. math::

    d_{spec}(P, Q) = \| \lambda(P) - \lambda(Q) \|

Where:

- :math:`\lambda(P)` represents the vector of eigenvalues of the transition matrix :math:`P`,
- :math:`\lambda(Q)` represents the vector of eigenvalues of the transition matrix :math:`Q`,
- :math:`\| \cdot \|` denotes a suitable norm (e.g., Euclidean norm) to measure the difference between the eigenvalue vectors of the two matrices.

Usage Example
-------------


.. code-block:: python

    from distancia import MarkovChainSpectral

    # Example usage
    P = [[0.9, 0.1], [0.2, 0.8]]  # Transition matrix for Markov chain 1
    Q = [[0.85, 0.15], [0.25, 0.75]]  # Transition matrix for Markov chain 2

    markov_spectral = MarkovChainSpectral(P, Q)

    # Compute the spectral distance between the transition matrices
    print("Spectral Distance:", markov_spectral.spectral_distance())

.. code-block:: bash

   >>>Spectral Distance: 0.1000000000000002


Academic Reference
------------------

The spectral properties of Markov chains have been extensively studied. A key reference for understanding the spectral distance and its applications is:


This book offers a detailed discussion of Markov chain eigenvalue analysis and spectral distances.

Conclusion
----------

The ``MarkovChainSpectral`` class in the ``distancia`` package provides a method for calculating the spectral distance between two Markov chains. This distance is particularly useful for analyzing the long-term behavior of stochastic systems and understanding how their transition dynamics differ in terms of stability and convergence.

By applying this class, users can assess the differences between two Markov chains based on their spectral characteristics, which is important in fields such as dynamic systems, probabilistic modeling, and machine learning.
