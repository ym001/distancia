MarkovChainFrobenius
=====================

Introduction
------------

The ``MarkovChainFrobenius`` class calculates the Frobenius distance between two Markov chains by comparing their transition matrices. The Frobenius distance is a matrix norm that measures the difference between two matrices by summing the squared differences of their corresponding elements. It is widely used in linear algebra to quantify the difference between matrices.

In the context of Markov chains, the Frobenius distance provides a way to measure how different the transition matrices of two chains are.

Meaning of the Distance
-----------------------

The **Frobenius distance** measures the element-wise difference between the transition matrices of two Markov chains. It treats the matrix as a collection of individual probabilities and calculates how far apart the matrices are in terms of those probabilities.

A smaller Frobenius distance indicates that the two Markov chains have similar transition probabilities, while a larger distance reflects more significant differences in their transitions.

Formal Definition
-----------------

The Frobenius distance between two Markov chains :math:` P` and :math:` Q`, with transition matrices :math:` P_{ij}` and :math:` Q_{ij}`, is defined as:

.. math::

    d_{F}(P, Q) = \sqrt{ \sum_{i,j} (P_{ij} - Q_{ij})^2 }

Where:

- :math:`P_{ij} is the transition probability from state :math:`i` to state :math:`j` in the first Markov chain,
- :math:`Q_{ij}` is the corresponding transition probability in the second Markov chain,
- The sum is taken over all pairs of states :math:`i` and :math:`j`.

The Frobenius distance can be interpreted as the Euclidean norm of the difference between the two transition matrices.

Usage Example
-------------


.. code-block:: python

    from distancia import MarkovChainFrobenius
    # Example usage
    P = [[0.9, 0.1], [0.2, 0.8]]  # Transition matrix for Markov chain 1
    Q = [[0.85, 0.15], [0.25, 0.75]]  # Transition matrix for Markov chain 2

    markov_frobenius = MarkovChainFrobenius(P, Q)

    # Compute the Frobenius distance between the transition matrices
    print("Frobenius Distance:", markov_frobenius.frobenius_distance())



.. code-block:: bash

   >>>Frobenius Distance: 0.10000000000000003


Academic Reference
------------------

The Frobenius distance is commonly used in matrix analysis. A key reference for matrix norms, including the Frobenius norm, is:

- Golub, G. H., & Van Loan, C. F. (2013). *Matrix Computations* (4th ed.). Johns Hopkins University Press.

This book provides a thorough explanation of matrix norms and their applications.

Conclusion
----------

The ``MarkovChainFrobenius`` class in the ``distancia`` package implements the Frobenius distance for comparing the transition matrices of two Markov chains. This distance is useful in various fields, such as stochastic modeling, statistical analysis, and machine learning, where understanding the differences between probabilistic systems is important.

By using this class, users can quantify the difference between the transition dynamics of two Markov chains in a straightforward and mathematically robust way.
