Otsuka Distance
===============

Introduction
------------

The Otsuka distance is a metric used primarily for comparing categorical or nominal data. It is named after the Japanese statistician K. Otsuka, who developed it as part of his work on statistical methods for analyzing categorical data. This distance measure is particularly useful when dealing with datasets where the attributes are categorical and the traditional distance metrics (such as Euclidean or Manhattan distances) are not applicable.

The Otsuka distance is designed to measure the dissimilarity between two categorical objects by comparing their attribute values. It takes into account the frequency of attribute values and provides a way to quantify how different two categorical objects are based on their attribute distributions.

Formula
-------

The Otsuka distance between two categorical vectors \(\mathbf{x}\) and \(\mathbf{y}\) is given by:

.. math::

    D_O(\mathbf{x}, \mathbf{y}) = \frac{1}{2} \left[ \frac{a + d}{a + b + c + d} + \frac{b + c}{a + b + c + d} \right]

Where:
- \(a\): The number of attributes where both \(\mathbf{x}\) and \(\mathbf{y}\) have the same value.
- \(b\): The number of attributes where \(\mathbf{x}\) has the value but \(\mathbf{y}\) does not.
- \(c\): The number of attributes where \(\mathbf{y}\) has the value but \(\mathbf{x}\) does not.
- \(d\): The number of attributes where both \(\mathbf{x}\) and \(\mathbf{y}\) have different values.

Interpretation
--------------

The Otsuka distance provides a measure of dissimilarity between two categorical objects. The formula takes into account both matching and non-matching attributes. 

- The term \(\frac{a + d}{a + b + c + d}\) represents the proportion of attributes where the two objects either both match or both differ.
- The term \(\frac{b + c}{a + b + c + d}\) accounts for the proportion of attributes where one object has a value while the other does not.

The distance ranges from 0 to 1, where 0 indicates perfect similarity (all attributes match) and 1 indicates maximum dissimilarity (no attributes match). 

.. code-block:: python

    from distancia import Otsuka  # Import the Otsuka class from the distancia package

    def main():
        # Define two categorical vectors for comparison
        vector1 = ['A', 'B', 'C', 'D', 'E']
        vector2 = ['A', 'X', 'C', 'Y', 'E']

        # Create an instance of the Otsuka class
        otsuka_distance = Otsuka(vector1, vector2)

        # Calculate the Otsuka distance
        distance = otsuka_distance.calculate()

        # Print the result
        print(f"Otsuka distance between {vector1} and {vector2} is: {distance:.4f}")

    if __name__ == "__main__":
        main()

.. code-block:: bash

    >>>Otsuka distance between ['A', 'B', 'C', 'D', 'E'] and ['A', 'X', 'C', 'Y', 'E'] is: 0.5000

History
-------

The Otsuka distance was introduced by K. Otsuka as part of his research on statistical methods for analyzing categorical data. It was designed to address the need for a distance measure that could effectively handle nominal data where traditional numerical distances are not suitable. Otsuka's work has influenced the field of categorical data analysis and has been applied in various domains, including market research, social sciences, and bioinformatics.

Academic Reference
------------------

Otsuka, K. (1976). *Statistical Methods for Categorical Data*. Academic Press.

This reference provides an overview of the development and application of the Otsuka distance and other statistical methods for analyzing categorical data.

Conclusion
----------

The Otsuka distance is a valuable metric for measuring dissimilarity between categorical objects, offering a way to quantify differences in attribute distributions. Its development has provided a useful tool for analyzing categorical data where traditional distance measures are not applicable. By incorporating the Otsuka distance into the `distancia` package, users can effectively handle and analyze categorical data, making it a useful addition for various applications in data analysis.

This documentation aims to help users understand and apply the Otsuka distance in their analytical tasks, ensuring that categorical data can be compared and analyzed with appropriate metrics.

