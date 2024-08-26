Jaccard Similarity
==================

**Jaccard Similarity** is a statistical measure used for comparing the similarity and diversity of sample sets. It is defined as the size of the intersection divided by the size of the union of the sample sets.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Jaccard Similarity between two sets :math:`A` and :math:`B` is defined as:

.. math::

   J(A, B) = \frac{|A \cap B|}{|A \cup B|}

Where:

- :math:`|A \cap B|` is the cardinality of the intersection of sets :math:`A` and :math:`B`, i.e., the number of elements common to both sets.

- :math:`|A \cup B|` is the cardinality of the union of sets :math:`A` and :math:`B`, i.e., the number of elements present in either one or both sets.

The Jaccard Similarity coefficient ranges from 0 to 1, where:

- 0 indicates that there are no common elements between the sets.

- 1 indicates that the sets are identical.

History
-------

The Jaccard Similarity was first introduced by the Swiss botanist Paul Jaccard in 1901. Jaccard developed this coefficient to quantify the similarity between sample sets of plants based on their shared characteristics. His work was part of an effort to develop quantitative methods in the study of biological diversity.

Since its introduction, the Jaccard Similarity has become a widely-used measure in various fields, including information retrieval, machine learning, and ecology, due to its simplicity and effectiveness in comparing binary and categorical data.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the Jaccard Similarity between two sets using the `distancia` package:

.. code-block:: python

    from distancia import Jaccard

    # Define two sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # Calculate Jaccard Similarity
    similarity = jaccard().calculate(set1, set2)

    print(f"Jaccard Similarity: {similarity}")

In this example, two sets `{1, 2, 3, 4, 5}` and `{4, 5, 6, 7, 8}` are compared. The Jaccard Similarity between these sets is calculated and printed, showing the proportion of shared elements relative to the total number of unique elements.

Applications
------------

Jaccard Similarity is used in various applications, including:

- **Information Retrieval**: To measure the similarity between documents based on the overlap of keywords or features.
- **Machine Learning**: For clustering and classification tasks, especially when dealing with binary or categorical data.
- **Biology and Ecology**: To compare the similarity of species composition between different habitats or ecological communities.
- **Recommender Systems**: To find users with similar preferences based on the intersection of liked items.

Reference
---------

For an academic reference, you can refer to the following seminal paper: :footcite:t:`jaccard`

.. footbibliography::

   

This paper introduces the Jaccard coefficient and its application to biological studies.

Conclusion
----------

Jaccard Similarity is a fundamental metric for comparing the similarity between two sets. Its versatility and straightforwardness make it a valuable tool across a broad range of disciplines, from computer science to biology.

