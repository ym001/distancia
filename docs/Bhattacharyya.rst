Bhattacharyya Distance
======================

The **Bhattacharyya Distance** is a measure of similarity between two probability distributions. It is used to quantify the amount of overlap between these distributions, often employed in statistics, pattern recognition, and information theory.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Bhattacharyya Distance between two probability distributions :math:`P` and :math:`Q` is given by:

.. math::

   D_B(P, Q) = -\ln \left( \sum_{x} \sqrt{P(x) \cdot Q(x)} \right)

Where:

- :math:`P(x)` and :math:`Q(x)` represent the probabilities of event :math:`x` in distributions :math:`P` and :math:`Q`, respectively.

- The summation is over all possible values of :math:`x`.

- The natural logarithm (:math:`\ln`) is used to transform the result into a distance measure.

The Bhattacharyya Distance ranges from 0 (when the distributions are identical) to positive infinity (when there is no overlap between the distributions).

History
--------

The Bhattacharyya Distance was introduced by Anil Bhattacharyya in 1943. It emerged from his work on statistical discrimination and has been influential in various fields such as machine learning, pattern recognition, and computer vision. The distance provides a way to measure how one distribution diverges from another, which is crucial in tasks involving classification and clustering.

Usage Example
--------------

Here is an example of how to calculate the Bhattacharyya Distance using the `Distancia` package:

.. code-block:: python

    from distancia import Bhattacharyya

    # Define two probability distributions
    p = [0.1, 0.4, 0.5]
    q = [0.2, 0.2, 0.6]

    # Calculate Bhattacharyya Distance
    distance = bhattacharyya().distance(p, q)

    print(f"Bhattacharyya Distance: {distance}")

In this example, two probability distributions `p` and `q` are compared using the Bhattacharyya Distance, which quantifies their similarity or dissimilarity.

Applications
------------

The Bhattacharyya Distance is widely used in various applications, including:

- **Pattern Recognition**: To measure the similarity between different classes or clusters.
- **Image Retrieval**: To assess the similarity between query images and database images.
- **Speech Recognition**: To compare different acoustic models and features.

Reference
---------

For an academic reference, you can consult the following paper:

Bhattacharyya, A. (1943). *On a Measure of Divergence Between Two Multinomial Populations*. Sankhyā: The Indian Journal of Statistics, Series A, 4(4), 99-110. DOI:10.2307/2332386.

This paper provides the original definition and context of the Bhattacharyya Distance, offering insights into its theoretical foundations and applications.

Conclusion
----------

The Bhattacharyya Distance is a powerful metric for comparing probability distributions, providing valuable information about the overlap and divergence between them. Its applications span a range of fields, highlighting its importance in both theoretical and practical contexts.
