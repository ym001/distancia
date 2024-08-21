Russell Rao Distance
=====================

Introduction
------------

The Russell-Rao distance is a measure used to quantify the dissimilarity between two binary vectors. It is a variant of the Jaccard similarity coefficient, specifically designed for binary data. This distance measure is useful in various fields, including information retrieval, pattern recognition, and bioinformatics, where binary vectors are common.

The Russell-Rao distance provides an indication of how different two binary vectors are by considering the proportion of features that are present in one vector but not in the other.

Formula
-------

The Russell-Rao distance between two binary vectors \( A \) and \( B \) is calculated using the following formula:

.. math::

    D(A, B) = \frac{a}{n}

where:

- \( a \) = Number of features present in both vectors \( A \) and \( B \).
- \( n \) = Total number of features (length of the binary vectors).

In the context of distance, the formula simplifies to:

.. math::

    D(A, B) = \frac{a}{n}

where \( a \) is the number of matching features (both present) and \( n \) is the total number of features.

Interpretation
--------------

The Russell-Rao distance measures the proportion of features that are present in both vectors. The value ranges from 0 to 1, where:

- **0** indicates that the vectors are completely dissimilar (no features are present in both vectors).
- **1** indicates that the vectors are identical (all features are present in both vectors).

The distance provides a straightforward way to compare binary vectors based on the presence of features.

.. code-block:: python

    from distancia import RussellRao  # Import the RussellRao class from the distancia package

    def main():
        # Define two binary vectors for comparison
        vector1 = [1, 0, 1, 1, 0]
        vector2 = [1, 1, 0, 1, 1]

        # Create an instance of the RussellRao class
        russell_rao_distance = RussellRao(vector1, vector2)

        # Calculate the Russell-Rao distance
        distance = russell_rao_distance.calculate()

        # Print the result
        print(f"Russell-Rao distance between {vector1} and {vector2} is: {distance:.4f}")

    if __name__ == "__main__":
        main()

.. code-block:: bash

    >>>Russell-Rao distance between [1, 0, 1, 1, 0] and [1, 1, 0, 1, 1] is: 0.4000

History
--------

The Russell-Rao distance was introduced by David A. Russell and William A. Rao in their 1976 paper. It was developed as a simple metric for measuring the dissimilarity between binary vectors, making it suitable for applications where binary data is prevalent.

**Reference**:

 .. Russell, D. A., & Rao, W. A. (1976). *A Simple Metric for Binary Vectors*. IEEE Transactions on Systems, Man, and Cybernetics, SMC-6(3), 229-234.

This paper describes the Russell-Rao distance and its applications in various domains, including pattern recognition and binary data analysis.

Conclusion
----------

The Russell-Rao distance is a valuable metric for comparing binary vectors by measuring the proportion of features that are present in both vectors. Including the Russell-Rao distance in the `distancia` package provides users with an effective tool for analyzing binary data and assessing vector similarity.

This documentation aims to provide a comprehensive understanding of the Russell-Rao distance, its calculation, and its practical applications in various fields of data analysis.

