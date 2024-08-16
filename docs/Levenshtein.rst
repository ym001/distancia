Levenshtein Distance
====================

**Levenshtein Distance**, also known as **edit distance**, is a measure of the difference between two sequences. The distance is defined as the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one sequence into another.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Levenshtein Distance between two strings :math:`s_1` and :math:`s_2` is defined as:

.. math::

   d(s_1, s_2) = \text{min}(
       d(s_1 - \text{last char}, s_2) + 1,  \\
       d(s_1, s_2 - \text{last char}) + 1,  \\
       d(s_1 - \text{last char}, s_2 - \text{last char}) + cost
   )

Where:

- The cost is 0 if the last characters of :math:`s_1` and :math:`s_2` are the same, and 1 if they are different.

- :math:`d(s_1, s_2)` is the Levenshtein Distance between :math:`s_1` and :math:`s_2`.

- The distance is computed using dynamic programming, where a matrix is used to keep track of the distances between substrings.

The distance ranges from 0 (when the sequences are identical) to the length of the longer string (when the sequences have no characters in common).

History
-------

The concept of edit distance was introduced by the Russian scientist Vladimir Levenshtein in 1965. Originally, it was used in the context of error correction for noisy communication channels, where it helped determine how many errors could be corrected by analyzing the differences between received and expected strings.

Over time, the Levenshtein Distance has found widespread application in various fields, including computational linguistics, bioinformatics, and natural language processing, due to its ability to quantify differences between sequences.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the Levenshtein Distance between two strings using the `distancia` package:

.. code-block:: python

    from distancia import Levenshtein

    # Define two strings
    str1 = "kitten"
    str2 = "sitting"

    # Calculate Levenshtein Distance
    distance = Levenshtein().distance(str1, str2)

    print(f"Levenshtein Distance: {distance}")

In this example, the strings `"kitten"` and `"sitting"` are compared. The Levenshtein Distance between these strings is calculated and printed, showing the minimum number of edits required to change one string into the other.

Applications
------------

Levenshtein Distance is used in various applications, including:

- **Spell Checking**: To find the closest word to a misspelled word by comparing the edit distance between the misspelled word and words in a dictionary.
- **Natural Language Processing**: For text similarity, approximate string matching, and machine translation.
- **Bioinformatics**: To compare DNA, RNA, or protein sequences.
- **Plagiarism Detection**: To measure the similarity between documents and detect potential plagiarism by computing the edit distance between different parts of texts.

Reference
---------

For an academic reference, you can refer to the following seminal paper:

Levenshtein, V. I. (1966). *Binary Codes Capable of Correcting Deletions, Insertions, and Reversals*. Soviet Physics Doklady, 10(8), 707–710.

This paper introduces the Levenshtein Distance and its application in error correction.

Conclusion
----------

Levenshtein Distance is a fundamental metric for comparing sequences, particularly in contexts where understanding small changes or errors is crucial. Its utility across a variety of disciplines makes it an essential tool in the study of sequence similarity.

