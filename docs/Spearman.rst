Spearman Distance
=================

Introduction
------------

The Spearman distance is derived from the Spearman rank correlation coefficient, which is a measure of the monotonic relationship between two variables. Unlike the Pearson correlation coefficient, which assesses linear relationships, the Spearman rank correlation coefficient measures the strength and direction of association between two ranked variables. The Spearman distance is calculated as one minus the absolute value of the Spearman correlation coefficient, providing a dissimilarity measure between ranked data. It is widely used in cases where data do not necessarily follow a linear relationship but have a monotonic association.

Formula
-------

The Spearman rank correlation coefficient :math:`\rho` between two vectors :math:`x` and :math:`y` is defined as:

.. math::

    \rho = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}

Where:

- :math:`d_i` is the difference between the ranks of corresponding elements :math:`x_i` and :math:`y_i`.

- :math:`n` is the number of elements in the vectors.

The Spearman distance :math:`D` is then calculated as:

.. math::

    D = 1 - |\rho|

History
-------

The Spearman rank correlation coefficient was developed by Charles Spearman in 1904 as an alternative to the Pearson correlation coefficient, particularly for data that do not meet the assumptions of linearity and homoscedasticity. The Spearman distance, derived from this coefficient, has become a standard tool in non-parametric statistics, often used in fields such as psychology, biology, and economics where data can be ranked but may not follow a normal distribution.

Example of Use
--------------

The Spearman distance is often used in:

- Analyzing the relationship between ordinal variables.
- Non-parametric statistical tests.
- Measuring the association between two ranked variables in psychological and social sciences.

Example of Python Code
----------------------

Here is an example of how to use the Spearman distance with the `distanciaa` package:

.. code-block:: python

    # Import the distanciaa package
    from distanciaa import Spearman

    # Define two sample vectors representing data points
    data_point_1 = [12, 15, 10, 9, 16]
    data_point_2 = [11, 14, 10, 8, 18]

    # Create an instance of the Spearman class
    spearman_dist = Spearman()

    # Calculate the Spearman distance between the two data points
    distance = spearman_dist.calculate(data_point_1, data_point_2)

    # Print the result
    print(f"The Spearman distance between the two data points is: {distance}")

Expected Output:
    The Spearman distance between the two data points is: 0.05

Academic Reference
------------------

For further reading and a deeper understanding of the Spearman distance and its applications, refer to the following academic paper:

.. bibliography::


Spearman, C. (1904). The Proof and Measurement of Association Between Two Things. American Journal of Psychology, 15(1), 72-101. DOI: 10.2307/1412159.

Conclusion
----------

The Spearman distance is a valuable tool for assessing the monotonic dissimilarity between ranked datasets. Its wide application in various fields, from social sciences to biology, attests to its importance in non-parametric statistics. By leveraging the distanciaa package's implementation of the Spearman distance, researchers and data scientists can easily integrate this measure into their
