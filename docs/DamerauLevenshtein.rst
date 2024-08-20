Damerau Levenshtein
==================

Introduction
------------

The **Damerau Levenshtein** distance is a string metric used to measure the minimum number of operations required to transform one string into another. It is an extension of the Levenshtein distance, incorporating an additional operation: transposition of two adjacent characters. This metric is particularly useful in applications like spell checking, DNA sequencing, and natural language processing, where small changes in order or adjacent characters can significantly affect meaning.

Formula
-------

The **Damerau Levenshtein** distance between two strings is defined as the minimum number of operations needed to transform one string into another. These operations include:

- **Insertion**: Adding a character.
- **Deletion**: Removing a character.
- **Substitution**: Replacing one character with another.
- **Transposition**: Swapping two adjacent characters.

Formally, the distance :math:`d(i, j)` between two strings :math:`s` and :math:`t` of lengths :math:`m` and :math:`n` respectively, can be defined recursively as:

.. math::

    d(i, j) = \min \begin{cases} 
    d(i-1, j) + 1 & \text{(deletion)} \\
    d(i, j-1) + 1 & \text{(insertion)} \\
    d(i-1, j-1) + 1[s_i \neq t_j] & \text{(substitution)} \\
    d(i-2, j-2) + 1 & \text{(transposition, if } s_i = t_{j-1} \text{ and } s_{i-1} = t_j\text{)} 
    \end{cases}

where :math:`1[s_i \neq t_j]` is 0 when :math:`s_i = t_j` and 1 otherwise.

Concept and Purpose
-------------------

The **Damerau Levenshtein** distance is a powerful tool for quantifying the difference between two strings, particularly when the order of characters is important. By allowing transpositions, it provides a more accurate reflection of the types of errors commonly found in human typing and communication, such as mistyped or swapped adjacent characters. This makes it especially valuable in tasks such as spelling correction, where correcting such errors is crucial.

The metric is also valuable in comparing sequences beyond simple strings, such as genetic sequences in bioinformatics, where small changes in order can represent significant mutations.

# Importing the DamerauLevenshtein class from the distancia package
from distancia import DamerauLevenshtein

# Define a function to test the DamerauLevenshtein distance


def test_damerau_levenshtein():
    # Create an instance of the DamerauLevenshtein class
    distance_calculator = DamerauLevenshtein()

    # Test cases: Pairs of strings to compare
    test_cases = [
        ("kitten", "sitting"),
        ("flaw", "lawn"),
        ("saturday", "sundays"),
        ("gumbo", "gambol"),
        ("ca", "abc"),
    ]

    # Iterate through the test cases and compute the distance
    for str1, str2 in test_cases:
        distance = distance_calculator.calculate(str1, str2)
        print(f"Damerau-Levenshtein distance between '{str1}' and '{str2}': {distance}")

if __name__ == "__main__":
    # Run the test function
    test_damerau_levenshtein()

History
-------

The **Damerau Levenshtein** distance was first described by Fred J. Damerau in 1964 in the context of automatic spelling correction. Damerau observed that over 80% of human misspellings involved a single error, including transpositions. Later, in 1966, the mathematician Vladimir Levenshtein introduced a similar distance metric without the transposition operation. The combination of these two works led to the metric we know today as the Damerau-Levenshtein distance.

Academic Reference
------------------

For a deeper understanding of the **Damerau-Levenshtein** distance and its applications, consider the following reference:

- Damerau, F. J. (1964). *A technique for computer detection and correction of spelling errors*. Communications of the ACM, 7(3), 171-176.
- Levenshtein, V. I. (1966). *Binary codes capable of correcting deletions, insertions, and reversals*. Soviet Physics Doklady, 10(8), 707-710.

Conclusion
----------

The **Damerau-Levenshtein** distance remains a crucial metric for assessing the similarity between strings in a wide variety of fields. By considering common errors such as adjacent transpositions, it offers a more nuanced and practical measure of string similarity than the traditional Levenshtein distance. As part of the `distancia` package, it provides users with a robust tool for tasks ranging from text processing to bioinformatics, reflecting its enduring relevance and utility in computational contexts.

