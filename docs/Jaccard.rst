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

   from distancia import Jaccard, CustomObject

   def main():
       jaccard_dist = JaccardDistance()

       print("Example with strings:")
       s1 = ["apple", "banana", "cherry", "date"]
       s2 = ["banana", "cherry", "date", "elderberry"]
    
       distance_s = jaccard_dist.distance(s1, s2)
       similarity_s = jaccard_dist.similarity(s1, s2)

       print(f"Jaccard distance between {s1} and {s2}: {distance_s:.4f}")
       print(f"Jaccard similarity between {s1} and {s2}: {similarity_s:.4f}")

       print("\nExample with integers:")
       i1 = [1, 2, 3, 4, 5]
       i2 = [4, 5, 6, 7, 8]

       distance_i = jaccard_dist.distance(i1, i2)
       similarity_i = jaccard_dist.similarity(i1, i2)

       print(f"Jaccard distance between {i1} and {i2}: {distance_i:.4f}")
       print(f"Jaccard similarity between {i1} and {i2}: {similarity_i:.4f}")

       print("\nExample with custom objects:")
       c1 = [CustomObject("a"), CustomObject("b"), CustomObject("c"), CustomObject(1)]
       c2 = [CustomObject("b"), CustomObject("c"), CustomObject(1), CustomObject(2)]

       distance_c = jaccard_dist.distance(c1, c2)
       similarity_c = jaccard_dist.similarity(c1, c2)

       print(f"Jaccard distance between {c1} and {c2}: {distance_c:.4f}")
       print(f"Jaccard similarity between {c1} and {c2}: {similarity_c:.4f}")

       print("\nEdge case - empty lists:")
       empty1: List[int] = []
       empty2: List[int] = []

       distance_empty = jaccard_dist.distance(empty1, empty2)
       similarity_empty = jaccard_dist.similarity(empty1, empty2)

       print(f"Jaccard distance between {empty1} and {empty2}: {distance_empty:.4f}")
       print(f"Jaccard similarity between {empty1} and {empty2}: {similarity_empty:.4f}")

   if __name__ == "__main__":
       main()

.. code-block:: bash

   >>>Example with strings:
   >>>Jaccard distance between ['apple', 'banana', 'cherry', 'date'] and ['banana', 'cherry', 'date', 'elderberry']: 0.4000
   >>>Jaccard similarity between ['apple', 'banana', 'cherry', 'date'] and ['banana', 'cherry', 'date', 'elderberry']: 0.6000

   >>>Example with integers:
   >>>Jaccard distance between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]: 0.7500
   >>>Jaccard similarity between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]: 0.2500

   >>>Example with custom objects:
   >>>Jaccard distance between [CustomObject(a), CustomObject(b), CustomObject(c), CustomObject(1)] and [CustomObject(b),  CustomObject(c), CustomObject(1), CustomObject(2)]: 0.4000
   >>>Jaccard similarity between [CustomObject(a), CustomObject(b), CustomObject(c), CustomObject(1)] and [CustomObject(b),    >>>CustomObject(c), CustomObject(1), CustomObject(2)]: 0.6000

   >>>Edge case - empty lists:
   >>>Jaccard distance between [] and []: 0.0000
   >>>Jaccard similarity between [] and []: 1.0000

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

