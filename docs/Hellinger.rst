Hellinger Distance
==================

Introduction
------------

The Hellinger distance is a measure of the dissimilarity between two probability distributions. It is derived from the Hellinger integral and is closely related to the Bhattacharyya distance. The Hellinger distance is widely used in various fields such as statistics, machine learning, and information theory due to its ability to measure the similarity between two distributions in a robust manner. It is particularly effective when dealing with probability distributions and is often preferred in cases where the distributions have varying scales.

Formula
-------

The Hellinger distance :math:`H(P, Q)` between two probability distributions :math:`P` and :math:`Q` is defined as:

.. math::

    H(P, Q) = \frac{1}{\sqrt{2}} \sqrt{\sum_{i=1}^{n} \left( \sqrt{P(i)} - \sqrt{Q(i)} \right)^2}

Where:

- :math:`P(i)` and :math:`Q(i)` are the probabilities of the :math:`i`

- the event in distributions :math:`P` and :math:`Q` respectively.

- The distance ranges from 0 (if :math:`P = Q`) to 1 (if :math:`P` and :math:`Q` are completely disjoint).

History
-------

The Hellinger distance is named after Ernst Hellinger, a German mathematician who introduced the Hellinger integral in 1909 as part of his work on integral equations. Over the years, the Hellinger distance has been adapted and used in various applications beyond its original mathematical context, becoming an essential tool in statistical analysis, pattern recognition, and machine learning.

Example of Use
--------------

The Hellinger distance is commonly used in:

- Comparing probability distributions in statistical analysis.
- Measuring the dissimilarity between distributions in machine learning models, particularly in clustering and classification tasks.
- Information retrieval, where it quantifies the divergence between document distributions.

Example of Python Code
----------------------

Here is an example of how to use the Hellinger distance with the `distanciaa` package:

.. code-block:: python
  
  # Import the distanciaa package
  from distanciaa import Hellinger

  # Define two probability distributions
  distribution_1 = [0.2, 0.3, 0.1, 0.4]
  distribution_2 = [0.1, 0.4, 0.2, 0.3]

  # Create an instance of the Hellinger class
  hellinger_dist = Hellinger()

  # Calculate the Hellinger distance between the two distributions
  distance = hellinger_dist.calculate(distribution_1, distribution_2)

  # Print the result
  print(f"The Hellinger distance between the two distributions is: {distance}")

Expected Output:

The Hellinger distance between the two distributions is: 0.14832397

Academic Reference
------------------

For further reading and a deeper understanding of the Hellinger distance and its applications, refer to the following academic paper:

.. bibliography::

    Hellinger

Conclusion
----------

The Hellinger distance is a powerful tool for comparing probability distributions, providing a clear and interpretable measure of dissimilarity. Its mathematical foundations and applicability across various domains, from statistics to machine learning, make it an indispensable component in the toolkit of any data scientist or researcher. The distanciaa package simplifies the computation of the Hellinger distance, enabling easy integration into analysis workflows.
