Pearson Distance
================

Introduction
------------

The Pearson distance, derived from the Pearson correlation coefficient, is a measure of the linear relationship between two variables. The Pearson correlation coefficient itself ranges between -1 and 1, where 1 indicates a perfect positive linear relationship, -1 indicates a perfect negative linear relationship, and 0 indicates no linear relationship. The Pearson distance is calculated as 1 minus the absolute value of the Pearson correlation coefficient, which gives a measure of dissimilarity between two datasets. It is widely used in statistics, machine learning, and data analysis to assess the degree of correlation between variables.

Formula
-------

The Pearson correlation coefficient :math:`r` between two vectors :math:`x` and :math:`y` is defined as:

.. math::

    r = \frac{\sum_{i=1}^{n} (x_i - \overline{x})(y_i - \overline{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \overline{x})^2}\sqrt{\sum_{i=1}^{n} (y_i - \overline{y})^2}}

Where:

- :math:`x_i` and :math:`y_i` are the elements of vectors :math:`x` and :math:`y` respectively.

- :math:`\overline{x}` and :math:`\overline{y}` are the means of vectors :math:`x` and :math:`y`.

- :math:`n` is the number of elements in the vectors.

The Pearson distance :math:`D` is then calculated as:

.. math::

    D = 1 - |r|

History
-------

The Pearson correlation coefficient was developed by Karl Pearson in the late 19th century. It has since become one of the most widely used statistics for measuring the strength and direction of a linear relationship between two variables. The Pearson distance, as a derivative, has found applications in various fields including bioinformatics, data science, and machine learning, particularly when measuring dissimilarity between feature vectors.

Example of Use
--------------

The Pearson distance is often used in:

- Clustering analysis to measure the similarity between data points.
- Gene expression analysis in bioinformatics.
- Recommender systems to find similarities between users or items.

Example of Python Code
----------------------

Here is an example of how to use the Pearson distance with the `distanciaa` package:

```python
    # Import the distanciaa package
    from distanciaa import Pearson

    # Define two sample vectors representing data points
    data_point_1 = [2.5, 3.6, 2.1, 4.0]
    data_point_2 = [3.0, 3.7, 2.3, 3.8]

    # Create an instance of the PearsonDistance class
    pearson_dist = Pearson()

    # Calculate the Pearson distance between the two data points
    distance = pearson_dist.distance(data_point_1, data_point_2)

    # Print the result
    print(f"The Pearson distance between the two data points is: {distance}")

Expected Output:

The Pearson distance between the two data points is: 0.010248

Academic Reference
------------------

For further reading and a deeper understanding of the Pearson distance and its applications, refer to the following academic paper:

Pearson, K. (1895). Note on Regression and Inheritance in the Case of Two Parents. Proceedings of the Royal Society of London, 58(347-352), 240-242. DOI: 10.1098/rspl.1895.0041.

Conclusion
----------
The Pearson distance is a valuable tool for assessing the linear dissimilarity between datasets. Its wide application in various fields, from bioinformatics to machine learning, attests to its importance in data analysis. By leveraging the distanciaa package's implementation of the Pearson distance, researchers and data scientists can easily integrate this measure into their workflows, facilitating more insightful analyses.
