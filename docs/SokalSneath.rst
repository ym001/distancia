Sokal Sneath Distance
======================

Introduction
------------

The Sokal-Sneath distance, also known as the Sokal-Sneath dissimilarity index, is a metric used to measure the dissimilarity between two binary data vectors. It is particularly useful in cluster analysis, biological taxonomy, and other fields where binary data comparison is crucial. The Sokal-Sneath distance is part of a family of similarity and dissimilarity coefficients introduced by Sokal and Sneath, aimed at quantifying the differences between binary vectors with an emphasis on the presence of shared attributes.

Formula
-------

The Sokal-Sneath distance between two binary vectors \( A \) and \( B \) is calculated using the following formula:

.. math::

    D(A, B) = \frac{c + 2b}{a + b + c}

where:

- \( a \) = Number of attributes where both \( A \) and \( B \) have a value of 1 (presence).
- \( b \) = Number of attributes where \( A \) has a value of 1 and \( B \) has a value of 0.
- \( c \) = Number of attributes where \( A \) has a value of 0 and \( B \) has a value of 1.

The Sokal-Sneath distance gives more weight to mismatches (attributes where one vector has a value of 1 and the other has 0) than to matches, making it particularly sensitive to the presence of differences between vectors.

Interpretation
--------------

The Sokal-Sneath distance measures the dissimilarity between two binary vectors, with a focus on the differences between them. The value of the distance ranges from 0 to 1, where:

- **0** indicates that the vectors are identical (all attributes match).
- **1** indicates that the vectors are completely dissimilar (no attributes match).

This metric is useful in situations where the presence of differences between binary vectors is more important than their similarities.

.. code-block:: python

    from distancia import SokalSneath  # Import the SokalSneath class from the distancia package

    def main():
        # Define two binary vectors for comparison
        vector1 = [1, 0, 1, 1, 0, 0, 1]
        vector2 = [1, 1, 0, 1, 0, 0, 1]

        # Create an instance of the SokalSneath class
        sokal_sneath = SokalSneath(vector1, vector2)

        # Calculate the Sokal-Sneath distance
        distance = sokal_sneath.calculate()

        # Print the result
        print(f"Sokal-Sneath distance between {vector1} and {vector2} is: {distance:.4f}")

    if __name__ == "__main__":
        main()

.. code-block:: bash

    >>>Sokal-Sneath distance between [1, 0, 1, 1, 0, 0, 1] and [1, 1, 0, 1, 0, 0, 1] is: 0.6000

History
-------

The Sokal-Sneath distance was introduced by Robert R. Sokal and Peter H. A. Sneath in their 1963 book "Principles of Numerical Taxonomy." The metric was developed as part of a broader framework for numerical taxonomy, which aimed to classify organisms based on their phenotypic characteristics. The Sokal-Sneath family of similarity and dissimilarity measures has since become a staple in various fields, particularly in the analysis of binary data.

**Reference**:
.. bibliography::


Sokal, R. R., & Sneath, P. H. A. (1963). *Principles of Numerical Taxonomy*. W. H. Freeman and Company.

This book provides a comprehensive overview of numerical taxonomy and the development of the Sokal-Sneath coefficients.

Conclusion
----------

The Sokal-Sneath distance is a valuable metric for comparing binary vectors, particularly in cases where the emphasis is on the presence of differences. Its inclusion in the `distancia` package offers users a robust tool for analyzing binary data in various applications, from cluster analysis to biological taxonomy.

This documentation aims to provide a thorough understanding of the Sokal-Sneath distance, its calculation, and its practical uses in binary data analysis.

