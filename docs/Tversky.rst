Tversky Index
=============

The **Tversky Index** is a generalization of the Tanimoto coefficient and Jaccard index, commonly used in the fields of information retrieval, machine learning, and bioinformatics. It is designed to account for asymmetrical relationships between sets, allowing for flexible comparison depending on the importance of certain elements.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Tversky Index between two sets :math:`A` and :math:`B` is defined as:

.. math::

   S(A, B) = \frac{|A \cap B|}{|A \cap B| + \alpha \cdot |A - B| + \beta \cdot |B - A|}

Where:
                               
- :math:`|A \cap B|` represents the intersection of sets :math:`A` and :math:`B`.
    
- :math:`|A - B|` is the difference between set :math:`A` and set :math:`B` (elements in :math:`A` but not in :math:`B`).
    
- :math:`|B - A|` is the difference between set :math:`B` and set :math:`A`.
    
- :math:`\alpha` and :math:`\beta` are parameters that determine the weight of the differences. Typically, :math:`\alpha = \beta = 1` reduces the Tversky Index to the Jaccard Index.

The Tversky Index can range from 0 to 1, where 1 indicates identical sets, and lower values indicate greater dissimilarity.

History
-------

The Tversky Index was introduced by Amos Tversky in 1977 as part of his work on cognitive psychology and similarity judgments. Tversky's work aimed to understand how humans perceive similarity and how this perception could be mathematically modeled, especially in cases where the asymmetry of features plays a crucial role.

Usage Example
-------------

Here is an example of how to calculate the Tversky Index between two sets using the `Distancia` package:

.. code-block:: python

    from distancia import Tversky

    # Define two sets
    set1 = {1, 2, 3, 4}
    set2 = {2, 3, 5, 6}

    # Parameters for the Tversky Index
    alpha = 0.5
    beta = 0.5

    # Calculate Tversky Index
    similarity = Tversky().calculate(set1, set2, alpha, beta)

    print(f"Tversky Index: {similarity}")

In this example, the sets `set1` and `set2` are compared using the Tversky Index, with \( \alpha \) and \( \beta \) set to 0.5, allowing for a balanced contribution of differences between the sets.

Applications
------------

The Tversky Index is widely used in various applications, including:

- **Information Retrieval**: To evaluate the similarity between query results and documents, particularly when some features are more relevant than others.
- **Machine Learning**: As a similarity measure in clustering and classification algorithms, where asymmetric importance of features is present.
- **Bioinformatics**: To compare biological sequences or molecular structures, where certain features (e.g., functional groups) may be more critical than others.

Reference
---------

For an academic reference, you can refer to the following paper:

.. footbibliography::


Tversky, A. (1977). *Features of Similarity*. Psychological Review, 84(4), 327-352. DOI:10.1037/0033-295X.84.4.327.

This paper outlines the theoretical foundation of the Tversky Index and explores its applications in cognitive psychology and similarity measures.

Conclusion
----------

The Tversky Index is a versatile and powerful similarity measure that accounts for asymmetry in feature importance. Its broad applicability across different fields, from psychology to bioinformatics, underscores its relevance and utility in both theoretical research and practical applications.
