=======================
KullbackLeibler Divergence
=======================

Introduction
============

The `KullbackLeibler Divergence` (KL divergence), also known as relative entropy, is a measure of how one probability distribution diverges from a second, reference probability distribution. In the context of machine learning, KL divergence is often used to compare a predicted probability distribution with the true distribution.

Mathematical Formula
====================

The KL divergence between two probability distributions `P` and `Q` is mathematically defined as:

.. math::

    D_{KL}(P || Q) = \sum_{i=1}^{N} P(i) \log\left(\frac{P(i)}{Q(i)}\right)

where:

- :math:`P(i)` is the true probability of event `i`.
  
- :math:`Q(i)` is the predicted probability of event `i`.
  
- :math:`N` is the number of possible events or classes.

Meaning and Concept Behind Kullback-Leibler Divergence
======================================================

KL divergence quantifies the amount of information lost when `Q` is used to approximate `P`. In essence, it measures how much one distribution diverges from a baseline distribution. A KL divergence of 0 indicates that the two distributions are identical, while a higher value indicates a greater difference between them.

**Interpretation:** KL divergence is asymmetric, meaning that :math:`D_{KL}(P || Q) \neq D_{KL}(Q || P)`. This characteristic is crucial when using KL divergence in contexts such as variational inference and regularization in machine learning.

.. code-block:: python

    from distancia import KullbackLeibler
    # Example probability distributions
    p = [0.1, 0.4, 0.5]  # True distribution
    q = [0.2, 0.3, 0.5]  # Predicted distribution

    # Create an instance of KullbackLeiblerLoss
    kl_loss = KullbackLeibler()

    # Calculate the KL divergence
    kl_value = kl_loss(p, q)
    print(f'Kullback-Leibler Divergence: {kl_value}')

.. code-block:: bash

    >>>Kullback-Leibler Divergence: 0.04575811092471789


History and Context
===================

The concept of KL divergence was introduced by Solomon Kullback and Richard Leibler in their 1951 paper titled "On Information and Sufficiency". It has since become a fundamental concept in information theory, statistics, and machine learning, particularly in the fields of Bayesian inference and information-theoretic approaches to machine learning.

KL divergence is also closely related to the concept of entropy, which was introduced earlier by Claude Shannon. While entropy measures the uncertainty within a single probability distribution, KL divergence measures the difference between two distributions.

Academic Reference
==================

For a deeper understanding, refer to the foundational paper by Kullback and Leibler: :footcite:t:`kullbackleibler`

.. footbibliography::


Conclusion
==========

The `Kullback-Leibler Divergence` is a critical measure for comparing probability distributions in machine learning and information theory. Its ability to quantify the difference between a predicted distribution and a true distribution makes it invaluable in various applications, including model evaluation, regularization, and probabilistic inference.
