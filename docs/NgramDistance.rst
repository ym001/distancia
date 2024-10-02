NgramDistance
=============

Introduction
------------
**NgramDistance** is a technique used to compare two text documents by breaking them down into contiguous sequences of *n* characters or words, known as n-grams. This method is effective in capturing both local and global similarities between texts, as it considers overlapping subsequences within the documents. It is widely used in tasks such as plagiarism detection, text classification, and information retrieval.

Distance Meaning
----------------
The **NgramDistance** measures the similarity between two documents by comparing the sets of n-grams generated from each document. The more n-grams that the two documents have in common, the more similar they are considered to be. The distance is typically calculated by determining how many n-grams are shared between the two documents and normalizing this value based on the total number of n-grams in both texts.

Formal Definition
-----------------
Given two documents :math:`D_1` and :math:`D_2`, each of which is decomposed into n-grams of length :math:`n`, let :math:`G(D_1)` and :math:`G(D_2)` represent the sets of n-grams extracted from :math:`D_1` and :math:`D_2` respectively. The **NgramDistance** is often defined as the complement of the Jaccard similarity, which measures the ratio of the intersection to the union of the two n-gram sets:

.. math::
   \text{Jaccard}(D_1, D_2) = \frac{|G(D_1) \cap G(D_2)|}{|G(D_1) \cup G(D_2)|}

The Ngram distance can then be expressed as:

.. math::
   \text{NgramDistance}(D_1, D_2) = 1 - \text{Jaccard}(D_1, D_2)

.. code-block:: python

   # Exemple d'utilisation
   ngram_distance = NgramDistance(n=3)  # Tri-grammes (n=3)

   text1: str = "The quick brown fox"
   text2: str = "The quick brown dog"

   distance: float = ngram_distance.compute(text1, text2)
   print(f"N-gram Distance: {distance}")

Academic Reference
------------------
A thorough exploration of n-grams and their applications in text comparison can be found in: :footcite:t:`NgramDistance`

.. footbibliography::

Conclusion
----------
**NgramDistance** offers a flexible and effective way to compare the similarity of two text documents by leveraging the power of n-gram analysis. Its ability to capture overlapping subsequences makes it a useful tool in various applications like text matching, document similarity analysis, and content duplication detection.
