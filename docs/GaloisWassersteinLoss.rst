GaloisWassersteinLoss
======================

Introduction
------------

The **Galois-Wasserstein Loss** is an innovative loss function designed to capture complex relationships between classes in classification tasks, particularly in text classification. It combines advanced concepts from probability theory and discrete mathematics, including the Wasserstein distance, cross-entropy, and Galois lattices. This loss function models not only the accuracy of predictions but also the underlying hierarchical relationships between classes.

Formula
-------

The **Galois-Wasserstein Loss** function is defined by the following equation:

.. math::

    \text{Galois-Wasserstein Loss} = \alpha \cdot W(P, Q) + \beta \cdot \text{CrossEntropy}(P, Q) + \gamma \cdot G(P, Q)

where:

- :math:`W(P, Q)` represents the Wasserstein distance between the true and predicted class probability distributions.

- :math:`\text{CrossEntropy}(P, Q)` is the cross-entropy between the true and predicted distributions.

- :math:`G(P, Q)` measures the distance between class concepts within a Galois lattice.

- :math:`\alpha`, :math:`\beta`, and :math:`\gamma` are adjustable hyperparameters that weight the influence of each term.

Concept and Purpose
-------------------

The **Galois-Wasserstein Loss** was developed to better account for structural relationships between classes in classification models. Galois lattices are used to represent hierarchical relationships and set inclusions among class groups, which is crucial in many contexts, such as hierarchical text or object classification.

This loss function is particularly useful for tasks where classification errors have different implications depending on the conceptual proximity of the classes. By combining this approach with the Wasserstein distance and cross-entropy, the **Galois-Wasserstein Loss** offers a more comprehensive and robust assessment of model performance.


History
-------

The concept of **Galois-Wasserstein Loss** was introduced by [Your Name], founder of the `distancia` package, as a response to the limitations of traditional loss functions in text classification, especially when classes have complex and hierarchical relationships. This loss function is based on deep mathematical notions from Galois theory, introduced by Évariste Galois in the 19th century, and the Wasserstein distance, a metric derived from optimal transport theory.

Academic Reference
------------------

For a deeper understanding of the underlying concepts of the **Galois-Wasserstein Loss**, you can refer to the following paper:

- Villani, C. (2003). *Topics in Optimal Transportation*. Graduate Studies in Mathematics, Vol. 58. American Mathematical Society.

Conclusion
----------

The **Galois-Wasserstein Loss** is an innovative contribution to the array of loss functions for classification tasks, especially in areas where hierarchy and class relationships are critical. By combining several advanced mathematical concepts, this function better captures the complexity of data and provides a more nuanced evaluation of model performance. This approach, developed by [Your Name], reflects a commitment to pushing the boundaries of data science and providing tools tailored to the modern challenges of classification.
