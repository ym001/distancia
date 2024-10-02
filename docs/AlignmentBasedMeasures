AlignmentBasedMeasures
=======================

Introduction
------------
The **AlignmentBasedMeasures** class is used to compute the similarity between two text documents by aligning them word by word or phrase by phrase. This method is particularly useful in comparing translations, paraphrases, or similar text pairs where the goal is to find an optimal correspondence between the elements of the two documents.

Distance Meaning
----------------
The **AlignmentBasedMeasures** approach focuses on finding the best alignment between the elements (words, phrases, or sentences) of two texts. By minimizing the number of operations (insertions, deletions, and substitutions) required to align the two texts, this method provides a robust measure of their similarity, capturing both lexical and syntactic correspondences.

Formal Definition
-----------------
Let :math:`A` and :math:`B` be two sequences of text, where each sequence consists of elements (words or phrases). The goal is to find an alignment between :math:`A` and :math:`B` that minimizes a predefined cost function. The alignment-based distance is calculated as follows:

.. math::
   D(A, B) = \min \sum_{i,j} c(A_i, B_j)

where:
- :math:`c(A_i, B_j)` is the cost of aligning element :math:`A_i` from sequence :math:`A` with element :math:`B_j` from sequence :math:`B`,
- The cost function can be based on operations such as insertions, deletions, and substitutions, or more complex measures like semantic or syntactic similarity.

.. code-block:: python

   # Example usage:
   text1: str = "The quick brown fox jumps over the lazy dog"
   text2: str = "The quick fox jumps over a lazy dog"

   # Initialize AlignmentBasedMeasures class
   alignment_measure = AlignmentBasedMeasures()

   # Align the texts and compute the alignment score
   aligned_texts: List[Tuple[str, str]] = alignment_measure.align_texts(text1, text2)
   score: float = alignment_measure.alignment_score(text1, text2)

   # Output the results
   print("Aligned Texts:")
   for word1, word2 in aligned_texts:
       print(f"{word1:15} {word2:15}")

   print(f"\nAlignment Score: {score}")

Academic Reference
------------------
The **AlignmentBasedMeasures** technique is often associated with methods used in computational linguistics and bioinformatics, such as sequence alignment algorithms:


Conclusion
----------
The **AlignmentBasedMeasures** class offers a powerful way to compare two text documents by focusing on the optimal alignment of their elements. This method is particularly valuable in tasks such as translation evaluation, paraphrase detection, and text matching, where preserving the order and relationships between elements is crucial.
