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

    def main():
        # Define two strings for comparison
        string1 = "example string for comparison"
        string2 = "example string for comparision"

        # Create an instance of the RatcliffObershelp class
        ratcliff_obershelp_distance = RatcliffObershelp()

        # Calculate the Ratcliff/Obershelp distance
        distance = ratcliff_obershelp_distance.calculate(string1, string2)

        # Print the result
        print(f"Ratcliff/Obershelp distance between '{string1}' and '{string2}' is: {distance:.4f}")

    if __name__ == "__main__":
        main()

.. code-block:: bash

    >>>Ratcliff/Obershelp distance between 'example string for comparison' and 'example string for comparision' is: -0.8983

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

