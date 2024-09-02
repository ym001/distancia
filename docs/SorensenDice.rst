Sørensen Dice Distance
=======================

The **Sørensen-Dice Distance** (also known simply as the Dice Coefficient or Sørensen Index) is a statistical tool used to measure the similarity between two samples or sets. It is particularly useful in cases where the data is binary or categorical and is often used in fields such as ecology, information retrieval, and natural language processing.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Sørensen-Dice Distance between two sets :math:`A` and :math:`B` is defined as:

.. math::

   D(A, B) = 1 - \frac{2 \cdot |A \cap B|}{|A| + |B|}

Where:

- :math:`|A \cap B|` is the size of the intersection of sets :math:`A` and :math:`B`.

- :math:`|A| \) and :math:`|B|` are the sizes of the sets :math:`A` and :math:`B`, respectively.

The SørensenDice Distance ranges from 0 to 1, where 0 indicates that the two sets are identical, and 1 indicates that they are completely different.

History
-------

The SørensenDice Coefficient was independently introduced by two researchers: the Danish botanist Thorvald Sørensen in 1948 and the American biologist Lee Raymond Dice in 1945. Sørensen introduced the index as a measure of the similarity between plant communities, while Dice applied it to biological samples. Over time, the coefficient became widely used in various scientific fields beyond ecology, including text mining, image processing, and data clustering.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the SørensenDice distance between two binary strings using the `Distancia` package:

.. code-block:: python

   from distancia import SorensenDice

   # Define two binary sets
   str1 = "night"
   str2 = "nacht"

   # Calculate SørensenDice Distance
   distance = SorensenDice().calculate(str1, str2)
   print(f"Sørensen Dice Distance: {distance}")

.. code-block:: bash

   >>>Sørensen Dice Distance: 0.75

In this example, the sets `str1` and `str2` are compared. The Sørensen-Dice Distance between these str is calculated and printed, showing the similarity between the two str.

Applications
------------

The Sørensen Dice distance is used in various applications, including:

- **Natural Language Processing**: To compare the similarity between text documents, especially in information retrieval and text classification tasks.
- **Image Analysis**: To measure the similarity between binary images or segmentations.
- **Genetics**: To compare the similarity between DNA sequences or genetic profiles.
- **Ecology**: To compare species composition between different ecological communities.

Reference
---------

For an academic reference, you can refer to the following paper: :footcite:t:`sorensendice`

.. footbibliography::


This paper introduces the Sørensen Index and discusses its application in the study of plant communities.

Conclusion
----------

The Sørensen-Dice Distance is a robust and widely-used measure for comparing the similarity between two sets, especially in the context of binary or categorical data. Its dual origin and extensive application across multiple fields demonstrate its versatility and significance in both theoretical and applied research.

