Tanimoto Distance
=================

The **Tanimoto Distance**, also known as the **Tanimoto Coefficient** or **Jaccard-Tanimoto Coefficient**, is a measure of similarity between two sets or vectors. It is closely related to the Jaccard index but is typically applied in the context of binary vectors or in cheminformatics to compare molecular fingerprints.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Tanimoto Distance between two sets :math:`A` and :math:`B` is defined as:

.. math::

   D(A, B) = 1 - \frac{|A \cap B|}{|A| + |B| - |A \cap B|}

Where:

- :math:`|A \cap B|` is the size of the intersection of sets :math:`A` and :math:`B`.
    
- :math:`|A|` and :math:`|B|` are the sizes of the sets :math:`A` and :math:`B`, respectively.

The Tanimoto Distance ranges from 0 to 1, where 0 indicates that the two sets are identical, and 1 indicates that they are completely different.

History
-------

The Tanimoto Coefficient was introduced by T.T. Tanimoto in 1957 while working at IBM. It was initially developed as a metric for comparing binary data, particularly in the context of pattern matching and machine learning. Over time, it has become a widely used metric in various fields, including chemistry, bioinformatics, and machine learning.

Usage Example
-------------

Here is an example of how to calculate the Tanimoto Distance between two binary vectors using the `Distancia` package:

.. code-block:: python

    from distancia import Tanimoto

    # Define two binary sets or vectors
    set1 = {1, 0, 1, 1}
    set2 = {1, 1, 0, 1}

    # Calculate Tanimoto Distance
    distance = Tanimoto().calculate(set1, set2)

    print(f"Tanimoto Distance: {distance}")

In this example, the sets `set1` and `set2` are compared, and the Tanimoto Distance between these sets is calculated and printed, demonstrating how similar or dissimilar the two sets are.

Applications
------------

The Tanimoto Distance is widely used in various applications, including:

- **Cheminformatics**: To compare molecular fingerprints and assess chemical similarity.
- **Information Retrieval**: For comparing binary vectors in search engines and document retrieval systems.
- **Machine Learning**: As a distance metric in clustering algorithms, particularly for binary data.
- **Pattern Recognition**: Used in various pattern recognition tasks, especially when dealing with binary data.

Reference
---------

For an academic reference, you can refer to the following paper:

.. bibliography::

   tanimoto

Tanimoto, T.T. (1957). *IBM Internal Report: An Elementary Mathematical Theory of Classification and Prediction*. IBM.

This paper outlines the introduction and use of the Tanimoto Coefficient, particularly in the context of binary data comparison.

Conclusion
----------

The Tanimoto Distance is a robust and widely-used measure for comparing the similarity between two sets, particularly in the context of binary or categorical data. Its origins in pattern matching and its application in various scientific fields highlight its versatility and continued relevance in research and industry.
