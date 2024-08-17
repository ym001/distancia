Bray-Curtis Distance
====================

Introduction
------------

The Bray-Curtis distance, also known as the Bray-Curtis dissimilarity, is a measure used to quantify the dissimilarity between two different samples. It is particularly popular in the field of ecology to compare species abundance or diversity between different environments. The distance ranges from 0 (completely similar) to 1 (completely dissimilar).

Formula
-------

The Bray-Curtis distance between two vectors **x** and **y** of size **n** is defined as:

.. math::
    D_{BC} = \frac{\sum_{i=1}^{n} |x_i - y_i|}{\sum_{i=1}^{n} |x_i + y_i|}

Where:

- :math:`x_i` and :math:`y_i` are the elements of vectors **x** and **y** respectively.

- The numerator is the sum of absolute differences.

- The denominator is the sum of the sums of corresponding elements.

History
-------

The Bray-Curtis distance was first introduced by J.R. Bray and J.T. Curtis in 1957 in their work on ordination of plant communities. This measure was designed to assess the compositional dissimilarity between different sites based on counts of species or other ecological data. Over the years, it has become a standard tool in ecological and environmental sciences.

Example of Use
--------------

The Bray-Curtis distance is often used in:

- Ecology to measure the dissimilarity between species abundance profiles in different samples.
- Environmental science to compare pollutant concentration profiles.
- Social sciences to analyze behavioral differences between groups.

Example of Python Code
----------------------

Here is an example of how to use the Bray-Curtis distance with the `distanciaa` package:

.. code-block:: python

    # Import the distanciaa package
    from distanciaa import BrayCurtisDistance

    # Define two sample vectors representing species abundance in two different samples
    sample_1 = [2, 0, 3, 1]
    sample_2 = [1, 1, 2, 0]

    # Create an instance of the BrayCurtisDistance class
    bray_curtis_dist = BrayCurtisDistance()

    # Calculate the Bray-Curtis distance between the two samples
    distance = bray_curtis_dist.calculate(sample_1, sample_2)

    # Print the result
    print(f"The Bray-Curtis distance between the two samples is: {distance}")

Expected Output:

The Bray-Curtis distance between the two samples is: 0.3333333333333333

Academic Reference
------------------

For further reading and a deeper understanding of the Bray-Curtis distance, refer to the original paper:

Bray, J. R., & Curtis, J. T. (1957). An Ordination of the Upland Forest Communities of Southern Wisconsin. Ecological Monographs, 27(4), 325-349. DOI: 10.2307/1942268.

Conclusion
----------
The Bray-Curtis distance is a widely used measure of dissimilarity in ecological and environmental studies. It is a useful metric when comparing the relative abundances of species or other entities in different samples. By understanding and applying the Bray-Curtis distance, researchers can gain valuable insights into the compositional differences between various ecosystems or populations. The distanciaa package offers a straightforward implementation of this distance, making it easy to incorporate into your analyses.

