LongestCommonSubsequence
=========================

Introduction
------------

The Longest Common Subsequence (LCSS) is a well-known measure used in computer science and bioinformatics to find the longest subsequence that two sequences have in common. Unlike the longest common substring, the elements of the LCSS do not need to occupy consecutive positions in the original sequences, making it a robust tool for sequence comparison in various domains.

The LCSS distance is particularly useful in identifying similarities between strings, DNA sequences, or time series data, where exact matches are less common, and slight variations between sequences are allowed.

Idea
----

The LCSS distance between two sequences measures the difference between the sequences based on the length of their longest common subsequence. The concept relies on dynamic programming to compute the LCSS, where a matrix is used to store the lengths of LCSSs of prefixes of the sequences.

Given two sequences `A` and `B`, the LCSS length is computed by filling out a matrix where each cell `(i, j)` contains the LCSS length of `A[0..i-1]` and `B[0..j-1]`. The value of each cell depends on the values of the neighboring cells and whether the current elements of `A` and `B` match. This method efficiently computes the LCSS and, consequently, the LCSS distance.

Example
-------

Here is a simple example of how to use the `LongestCommonSubsequence` class:

.. code-block:: python

  from distancia import LongestCommonSubsequence

  # Sample sequences
  sequence_a = "AGGTAB"
  sequence_b = "GXTXAYB"

  # Create an instance of the LongestCommonSubsequence class
  lcss = LongestCommonSubsequence()

  # Compute the LCSS distance
  distance = lcss.calculate(sequence_a, sequence_b)
  print(f"LCSS Distance: {distance}")

  # Get the Longest Common Subsequence
  lcs = lcss.get_lcs()
  print(f"Longest Common Subsequence: {lcs}")

.. code-block:: python

  LCSS Distance: 4
  Longest Common Subsequence: GTAB

In this example, the sequences `"AGGTAB"` and `"GXTXAYB"` are compared. The LCSS distance is computed, along with the longest common subsequence itself.

Academic Reference
------------------

The LCSS problem and its applications have been widely studied in the field of computational biology and computer science. A classic reference is: :footcite:t:`longestcommonsubsequence`

.. footbibliography::

   

- **Gusfield, D. (1997).** *Algorithms on Strings, Trees, and Sequences: Computer Science and Computational Biology*. Cambridge University Press.

This book provides an in-depth discussion of algorithms related to sequence comparison, including LCSS.

Conclusion
----------

The Longest Common Subsequence (LCSS) is a fundamental tool for measuring the similarity between sequences. It is particularly valuable in scenarios where the sequences may not align perfectly, but still share common patterns. The `LongestCommonSubsequence` class in the `distancia` package offers an efficient and easy-to-use implementation for computing the LCSS distance, making it a valuable addition for any sequence analysis toolkit.
