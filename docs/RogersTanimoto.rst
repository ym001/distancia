Rogers-Tanimoto Distance
========================

Introduction
------------

The Rogers-Tanimoto distance is a measure used to quantify the similarity or dissimilarity between two binary or categorical vectors. It is an extension of the Tanimoto coefficient, designed to handle both presence and absence of features in the comparison. The Rogers-Tanimoto distance is particularly useful in cases where the features are binary or categorical, and it captures both the similarity and dissimilarity in a balanced manner.

The Rogers-Tanimoto distance is widely used in fields such as information retrieval, pattern recognition, and genetic research, where comparing categorical data is crucial.

Formula
-------

The Rogers-Tanimoto distance between two vectors \( A \) and \( B \) is calculated using the following formula:

.. math::

    D(A, B) = \frac{a + b + c}{a + b + c + d}

where:

- \( a \) = Number of matching features that are present in both vectors.
- \( b \) = Number of features present in vector \( A \) but not in vector \( B \).
- \( c \) = Number of features present in vector \( B \) but not in vector \( A \).
- \( d \) = Number of matching features that are absent in both vectors.

The Rogers-Tanimoto distance is a measure of dissimilarity, where a lower value indicates higher similarity and a higher value indicates more dissimilarity.

Interpretation
--------------

The Rogers-Tanimoto distance provides a measure of dissimilarity between two categorical or binary vectors. The value ranges from 0 to 1, where:

- **0** indicates that the vectors are identical.
- **1** indicates that the vectors are completely dissimilar.

The distance takes into account both the presence and absence of features, making it well-suited for comparing binary and categorical data where both types of information are important.

Rogers-Tanimoto distance between [1, 0, 1, 1, 0] and [1, 1, 0, 1, 1] is: 1.0000

.. code-block:: python

    from distancia import RogersTanimoto  # Import the RogersTanimoto class from the distancia package

    def main():
        # Define two binary vectors for comparison
        vector1 = [1, 0, 1, 1, 0]
        vector2 = [1, 1, 0, 1, 1]

        # Create an instance of the RogersTanimoto class
        rogers_tanimoto_distance = RogersTanimoto(vector1, vector2)

        # Calculate the Rogers-Tanimoto distance
        distance = rogers_tanimoto_distance.calculate()

        # Print the result
        print(f"Rogers-Tanimoto distance between {vector1} and {vector2} is: {distance:.4f}")

    if __name__ == "__main__":
        main()

.. code-block:: python

    >>>Rogers-Tanimoto distance between [1, 0, 1, 1, 0] and [1, 1, 0, 1, 1] is: 1.0000

History
--------

The Rogers-Tanimoto distance was introduced by David W. Rogers and K. J. Tanimoto in their 1960 paper. It was developed as part of their work on similarity measures for categorical data and pattern recognition. The metric provides a way to compare binary vectors while accounting for both matching and non-matching features.

**Reference**:

Rogers, D. W., & Tanimoto, K. J. (1960). *A Computer Oriented Classificatory System*. IEEE Transactions on Electronic Computers, EC-9(3), 304-309.

This paper describes the Rogers-Tanimoto distance and its applications in pattern recognition and classification tasks.

Conclusion
----------

The Rogers-Tanimoto distance is a valuable metric for comparing binary and categorical vectors. It effectively captures both the similarity and dissimilarity between vectors by considering the presence and absence of features. Including the Rogers-Tanimoto distance in the `distancia` package provides users with a robust tool for analyzing categorical data and assessing the similarity between binary vectors.

This documentation aims to provide a comprehensive understanding of the Rogers-Tanimoto distance and its practical applications in various domains of data analysis.

