Sokal-Michener Distance
========================

Introduction
------------

The Sokal-Michener distance, also known as the Sokal-Michener similarity coefficient, is a metric used to measure the similarity or dissimilarity between two binary data vectors. It is particularly useful in the fields of cluster analysis, taxonomy, and other domains where the comparison of binary vectors is necessary. This metric is a variant of the simple matching coefficient, with an emphasis on equal importance of both presence and absence of attributes.

Formula
-------

The Sokal-Michener distance between two binary vectors \( A \) and \( B \) is calculated using the following formula:

.. math::

    D(A, B) = 1 - \frac{(a + d)}{n}

where:

- \( a \) = Number of attributes where both \( A \) and \( B \) have a value of 1 (presence).
- \( d \) = Number of attributes where both \( A \) and \( B \) have a value of 0 (absence).
- \( n \) = Total number of attributes.

In essence, the Sokal-Michener distance is derived by subtracting the proportion of matching attributes (both present and absent) from 1.

Interpretation
--------------

The Sokal-Michener distance measures how dissimilar two binary vectors are by considering both matches where attributes are present and matches where attributes are absent. The value of the distance ranges from 0 to 1, where:

- **0** indicates that the vectors are identical (all attributes match).
- **1** indicates that the vectors are completely dissimilar (no attributes match).

This metric gives equal weight to the presence and absence of attributes, making it a balanced choice for various applications in binary data comparison.

.. code-block:: python

    from distancia import SokalMichener  # Import the SokalMichener class from the distancia package

    def main():
        # Define two binary vectors for comparison
        vector1 = [1, 0, 1, 1, 0, 0, 1]
        vector2 = [1, 1, 0, 1, 0, 0, 1]

        # Create an instance of the SokalMichener class
        sokal_michener = SokalMichener(vector1, vector2)

        # Calculate the Sokal-Michener distance
        distance = sokal_michener.calculate()

        # Print the result
        print(f"Sokal-Michener distance between {vector1} and {vector2} is: {distance:.4f}")

    if __name__ == "__main__":
        main()

.. code-block:: bash

    >>>Sokal-Michener distance between [1, 0, 1, 1, 0, 0, 1] and [1, 1, 0, 1, 0, 0, 1] is: 0.2857

History
-------

The Sokal-Michener distance was introduced by Robert R. Sokal and Charles D. Michener in their 1958 paper. It was developed as a method for numerical taxonomy, where the aim was to classify organisms based on a large number of binary attributes. The method has since been widely adopted in various disciplines requiring the comparison of binary vectors.

**Reference**:


:footcite:t:`sokalmichener`

.. footbibliography::


Conclusion
----------

The Sokal-Michener distance is a robust and balanced metric for comparing binary vectors, giving equal consideration to both the presence and absence of attributes. Its inclusion in the `distancia` package provides users with a versatile tool for analyzing binary data across a wide range of applications.

This documentation aims to provide a comprehensive understanding of the Sokal-Michener distance, its calculation, and its practical uses in binary data analysis.

