=======================
Cross Entropy Loss
=======================

Introduction
============

The `Cross Entropy Loss` is a widely used measure to evaluate the difference between two probability distributions. In the context of neural networks, it is primarily used to assess the performance of classification models, particularly in multi-class classification tasks.

Mathematical Formula
====================

The cross entropy loss function is mathematically defined as follows:

.. math::

    L(y, \hat{y}) = -\sum_{i=1}^{N} y_i \log(\hat{y}_i)

where:

- :math:`y` represents the vector of true labels (a probability distribution where only one class is assigned a value of 1, and the others are 0).
  
- :math:`\hat{y}` represents the vector of model predictions (the predicted probabilities for each class).
  
- :math:`N` is the number of classes.

Meaning and Concept Behind Cross Entropy
========================================

The central idea behind Cross Entropy is to quantify the "disagreement" between the true and predicted probability distributions. If the probabilities predicted by the model are close to the true probabilities (the labels), the loss will be low. Conversely, if the predictions are far from the true labels, the loss will be high. This measure encourages the model to refine its predictions to better match the observed truths.

**Interpretation:** A cross entropy loss of zero means the model has perfectly predicted the correct class for all examples, while a high loss indicates that the model often assigned low probabilities to the correct classes.

History and Context
===================

Cross entropy has its roots in information theory, introduced by Claude Shannon in 1948. In this context, entropy measures the uncertainty of an information source. Cross entropy, on the other hand, measures the divergence between two probability distributions, thus linking concepts from information theory to modern machine learning.

The use of cross entropy as a loss function gained popularity with the development of artificial neural networks and is now one of the standard loss functions for classification tasks.



Academic Reference
==================

For a deeper understanding, you can refer to the foundational work by Claude Shannon on information theory:

- Shannon, C. E. (1948). "A Mathematical Theory of Communication." *The Bell System Technical Journal*, 27(3), 379-423. [doi:10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x)

Conclusion
==========

The `Cross Entropy Loss` is an essential loss function for classification models in machine learning. It guides the model by providing an error signal based on the divergence between the true and predicted distributions. Understanding and using this loss function is fundamental to developing effective and accurate classification models.
