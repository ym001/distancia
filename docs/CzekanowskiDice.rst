Czekanowski Dice
===============

Introduction
------------

The **Czekanowski-Dice** similarity coefficient, also known as the **Sørensen-Dice index** or simply the **Dice coefficient**, is a statistical measure used to gauge the similarity between two sets. It is widely applied in various fields, including ecology, information retrieval, and text classification. This measure emphasizes the overlap between the two sets and is particularly effective when dealing with binary attributes or presence/absence data.

Formula
-------

The **Czekanowski Dice** similarity coefficient is defined by the following formula:

.. math::

    S(X, Y) = \frac{2 |X \cap Y|}{|X| + |Y|}

where:

- :math:`X` and :math:`Y` are two sets.
- :math:`|X \cap Y|` represents the cardinality of the intersection of sets :math:`X` and :math:`Y`, i.e., the number of elements common to both sets.
- :math:`|X|` and :math:`|Y|` denote the cardinality of sets :math:`X` and :math:`Y`, respectively.

Concept and Purpose
-------------------

The **Czekanowski Dice** coefficient provides a measure of similarity that ranges from 0 (no similarity) to 1 (perfect similarity). The formula focuses on the overlap between two sets, making it particularly useful for tasks where the relative size of the intersection is more significant than the overall size of the sets. This is especially relevant in scenarios such as text classification, where the presence of certain keywords or attributes is more informative than the absence of others.

The measure is symmetrical, meaning that the similarity between set :math:`X` and set :math:`Y` is the same as that between :math:`Y` and :math:`X`. This property makes it suitable for comparing datasets where directionality is not a concern.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the Dice Distance between two vector using the `Distancia` package:

.. code-block:: python

    from distancia import CzekanowskiDice

    # Define two vector
    set1 = [1.3, 0, 1, 1]
    set2 = [1, 1, 0, 1]

    # Calculate Dice Distance
    similarity = CzekanowskiDice().calculate(set1, set2)

    print(f"Czekanowski Dice similarity: {similarity}")

.. code-block:: python

    >>>Czekanowski Dice similarity: 0.3650793650793651

History
-------

The **Czekanowski-Dice** coefficient has its roots in the early 20th century. It was independently introduced by the Polish statistician J. Czekanowski in 1913 and the Danish botanist Thorvald Sørensen in 1948. Czekanowski’s work initially focused on anthropological studies, while Sørensen applied a similar concept in ecological studies, particularly in plant community analysis. Over time, the Dice coefficient became a fundamental tool in various scientific disciplines.

Academic Reference
------------------


For a more in-depth understanding of the **Czekanowski-Dice** similarity coefficient and its applications, refer to the following publication :footcite:t:`czekanowskiDice`:

.. footbibliography::

    

Conclusion
----------

The **Czekanowski-Dice** similarity coefficient is a simple yet powerful tool for quantifying the similarity between two sets. Its focus on the intersection relative to the size of the sets makes it particularly effective in situations where the presence of shared attributes is critical. This coefficient has stood the test of time, finding applications in a wide range of fields from ecology to data science. As part of the `distancia` package, it provides a reliable and interpretable measure of similarity for your classification tasks.

