Ratcliff Obershelp Distance
===========================

Introduction
------------

The Ratcliff/Obershelp distance is a string similarity measure used to quantify the similarity between two sequences of characters. It is particularly effective for comparing strings where substrings or common segments are important for evaluating similarity. Developed by John Ratcliff and David Obershelp, this distance measure is widely utilized in fields such as text processing, plagiarism detection, and record linkage.

The Ratcliff/Obershelp algorithm operates by identifying the longest common contiguous substrings between two sequences and using them to compute a similarity score. The measure is known for its ability to handle mismatches and partial matches effectively.

Formula
-------

The Ratcliff/Obershelp distance between two strings :math:`s1` and :math:`s2` is computed using the following recursive approach:

1. **Find the Longest Common Substring (LCS)** between :math:`s1` and :math:`s2`.
2. **Divide** the strings into segments before and after the LCS.
3. **Recursively calculate** the similarity score for these segments.
4. Combine the scores from the LCS and the recursive calls to obtain the final similarity score.

The distance :math:`D(s1, s2)` is given by:

.. math::

    D(s1, s2) = \frac{1 - \text{Ratcliff/Obershelp Similarity}(s1, s2)}{2}

where the Ratcliff/Obershelp Similarity is a measure of how similar :math:`s1` and :math:`s2` are, based on the recursive matching of their substrings.

Interpretation
--------------

The Ratcliff/Obershelp distance provides a measure of dissimilarity between two strings. The value ranges from 0 to 1, where 0 indicates that the two strings are identical and 1 indicates that they are completely dissimilar.

- **Long Common Substrings**: The algorithm focuses on finding and aligning the longest common substrings, which helps in recognizing significant similarities even in the presence of small differences.
- **Recursive Calculation**: By recursively applying the algorithm to the segments of the strings, it accounts for multiple overlapping matches, making it robust against minor variations.

.. code-block:: python

    from distancia import RatcliffObershelp  # Import the RatcliffObershelp class from the distancia package

    def run_tests() -> None:
        """
        Run test cases to demonstrate usage and verify functionality.
        """
        ro = RatcliffObershelp(case_sensitive=False)
    
        # Test cases
        test_pairs = [
        ("hello", "hello world"),
        ("PYTHON", "python"),
        ("distance", "difference"),
        ("", "test"),  # Should raise ValueError
        ("The quick brown fox", "The quick brown dog"),
        ("Ratcliff", "Obershelp"),
        ("algorithm", "logarithm"),
    ]
    
        for seq1, seq2 in test_pairs:
            try:
                distance = ro.compute(seq1, seq2)
                quick_ratio = ro.quick_ratio(seq1, seq2)
            
                print(f"\nTest: '{seq1}' vs '{seq2}'")
                print(f"Distance: {distance:.4f}")
                print(f"Quick ratio: {quick_ratio:.4f}")
            
            except ValueError as e:
                print(f"\nError with '{seq1}' vs '{seq2}': {str(e)}")

    if __name__ == "__main__":
        run_tests()

.. code-block:: bash

   Test: 'hello' vs 'hello world'
    Distance: 0.3750
    Quick ratio: 0.6250

    Test: 'PYTHON' vs 'python'
    Distance: 0.0000
    Quick ratio: 1.0000

    Test: 'distance' vs 'difference'
    Distance: 0.4444
    Quick ratio: 0.5556

    Error with '' vs 'test': Input sequences cannot be empty

    Test: 'The quick brown fox' vs 'The quick brown dog'
    Distance: 0.1053
    Quick ratio: 0.8947

    Test: 'Ratcliff' vs 'Obershelp'
    Distance: 0.7647
    Quick ratio: 0.2353

    Test: 'algorithm' vs 'logarithm'
    Distance: 0.3333
    Quick ratio: 0.6667
 

History
--------

The Ratcliff/Obershelp distance was introduced by John Ratcliff and David Obershelp in their 1983 paper. The algorithm was developed as part of their work on string matching and similarity measures, addressing the need for a metric that could effectively handle variations in text and data. Their approach improved the accuracy of similarity assessments by focusing on contiguous substrings and their alignments.

**Reference**:

:footcite:t:`ratcliffobershelp`

.. footbibliography::

    

This paper details the development of the Ratcliff/Obershelp algorithm and its applications in pattern recognition and string matching.

Conclusion
----------

The Ratcliff/Obershelp distance is a valuable metric for comparing sequences based on their longest common substrings. Its recursive approach and focus on contiguous matches make it well-suited for applications where string similarity needs to be assessed despite minor differences or variations. Incorporating the Ratcliff/Obershelp distance into the `distancia` package provides users with a robust tool for handling text similarity and record linkage tasks.

This documentation aims to facilitate understanding and implementation of the Ratcliff/Obershelp distance, ensuring effective application in various domains of text analysis and processing.

