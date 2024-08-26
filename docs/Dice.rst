Dice Distance
=============

The **Dice Distance** (also known as the Dice Coefficient or Sorensen-Dice Index) is a measure of similarity between two sets, typically used to compare the similarity between two strings or sequences. It is particularly useful in cases where the data is binary or categorical.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Dice Distance between two sets  :math:`A` and  :math:`B` is defined as:

.. math::

   D(A, B) = 1 - \frac{2 \cdot |A \cap B|}{|A| + |B|}

Where:

-  :math:`|A \cap B|` is the size of the intersection of sets  :math:`A` and  :math:`B`.
    
-  :math:`|A|` and  :math:`|B|` are the sizes of the sets  :math:`A` and  :math:`B`, respectively.

The Dice Distance ranges from 0 to 1, where 0 indicates that the two sets are identical, and 1 indicates that they are completely different.

History
-------

The Dice Coefficient was introduced by Lee Raymond Dice in 1945 as a statistical tool for comparing the similarity between two samples. Initially, it was used in ecology for comparing the similarity between two different habitats or populations. Over time, the Dice Coefficient has been adopted in various fields, including natural language processing, computer vision, and information retrieval, where it is used to compare the similarity of text, images, or other data types.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the Dice Distance between two binary strings using the `Distancia` package:

.. code-block:: python

    from distancia import Dice

    # Define two binary sets
    set1 = {1, 0, 1, 1}
    set2 = {1, 1, 0, 1}

    # Calculate Dice Distance
    distance = dice().calculate(set1, set2)

    print(f"Dice Distance: {distance}")

In this example, the sets `set1` and `set2` are compared. The Dice Distance between these sets is calculated and printed, showing the similarity between the two sets.

Applications
------------

Dice Distance is used in various applications, including:

- **Natural Language Processing**: To compare the similarity between text documents or strings.
- **Image Analysis**: To measure the similarity between binary images or segmentations.
- **Information Retrieval**: To rank the relevance of search results based on similarity to the query.
- **Genetics**: To compare the similarity between DNA sequences or genetic profiles.

Reference
---------

For an academic reference, you can refer to the following paper:
This paper introduces the Dice Coefficient and discusses its application in ecology for comparing species.


:footcite:t:``

.. footbibliography::

   dice

Conclusion
----------

The Dice Distance is a robust measure for comparing the similarity between two sets, particularly in binary or categorical data. Its widespread use across various fields demonstrates its versatility and utility in different contexts.

