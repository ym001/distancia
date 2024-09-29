SmithWaterman
=============

Introduction
------------
The **SmithWaterman** algorithm is a dynamic programming algorithm used to calculate the optimal local alignment between two sequences, such as strings of text. It identifies similar regions between the sequences by allowing for insertions, deletions, and substitutions, making it ideal for comparing texts with variations, like partially matching documents.

Distance Meaning
----------------
The **SmithWaterman** distance measures the dissimilarity between two sequences based on how well they align locally. Unlike global alignment methods, this algorithm focuses on finding the best matching subsequences within the texts, which can be particularly useful when comparing texts with segments that differ significantly or when only parts of the texts are similar.

Formal Definition
-----------------
Let :math:`S_1` and :math:`S_2` be two sequences of characters. The **SmithWaterman** algorithm computes a score matrix :math:`H` where each element :math:`H(i, j)` is the highest score achievable for aligning a subsequence ending at position :math:`i` in :math:`S_1` and position :math:`j` in :math:`S_2`. The recurrence relation is given by:

.. math::
   H(i, j) = \max\left( \begin{array}{ll}
   0, & \\
   H(i-1, j-1) + \text{match/mismatch score}, & \text{if } S_1[i] = S_2[j] \text{ or mismatch},\\
   H(i-1, j) + \text{gap penalty}, & \\
   H(i, j-1) + \text{gap penalty} &
   \end{array}\right)

The final score of the local alignment is the maximum value found in the matrix :math:`H`.

Academic Reference
------------------
For more details on the **SmithWaterman** algorithm, refer to the original work:

**Smith, T.F., & Waterman, M.S.** (1981). "Identification of Common Molecular Subsequences." *Journal of Molecular Biology*, 147(1), 195-197.

Conclusion
----------
The **SmithWaterman** algorithm is a powerful tool for comparing two text sequences, especially when the goal is to find the most similar local regions. Its flexibility in allowing gaps and mismatches makes it well-suited for applications in natural language processing, bioinformatics, and text comparison tasks where partial matches are relevant.
