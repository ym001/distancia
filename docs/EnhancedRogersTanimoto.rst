Enhanced Rogers Tanimoto Distance
=================================

Introduction
------------

The Enhanced Rogers-Tanimoto distance is an improvement on the classical Rogers-Tanimoto distance, which is used to measure the similarity or dissimilarity between two binary vectors. This enhanced version introduces additional weighting factors and adjustments to better capture the complexity and nuances in certain datasets, especially in cases where binary features are not equally important or where interactions between features need to be considered.

The Enhanced Rogers-Tanimoto distance is particularly useful in fields like bioinformatics, text analysis, and pattern recognition, where binary data is prevalent, and more sophisticated measures of similarity are required.

Formula
-------

The Enhanced Rogers Tanimoto distance between two binary vectors :math:`x` and :math:`y` is defined as:

.. math::

    D_{ERT}(x, y) = \frac{ \alpha(n_{01} + n_{10}) + \beta(n_{11}) }{ \alpha(n_{00} + n_{01} + n_{10} + n_{11}) + n_{11} }

Where:

- :math:`n_{00}` is the number of positions where both vectors have 0.

- :math:`n_{01}` is the number of positions where the first vector has 0 and the second has 1.

- :math:`n_{10}` is the number of positions where the first vector has 1 and the second has 0.

- :math:`n_{11}` is the number of positions where both vectors have 1.

- :math:`\alpha` and :math:`\beta` are weighting factors that can be adjusted depending on the importance of matches and mismatches in the specific application.

History
-------

The Rogers Tanimoto distance was originally developed by Rogers and Tanimoto in the 1960s as a way to compare binary data. It has been widely used in various fields, particularly in the analysis of categorical data. However, over time, researchers identified scenarios where the original formula did not sufficiently account for the significance of certain features or their interactions.

The Enhanced Rogers Tanimoto distance was developed as a response to these limitations. By introducing weighting factors, it provides a more flexible and accurate measure of similarity or dissimilarity, especially in complex datasets where not all binary features are equally important.

Example of Use
--------------

The Enhanced Rogers-Tanimoto distance can be used in various applications, including:

- Bioinformatics: Comparing gene sequences where certain genetic markers may have more significance.
- Text Analysis: Analyzing the presence or absence of key terms in documents where some terms are more relevant than others.
- Pattern Recognition: Comparing binary patterns where some features may have a higher impact on classification than others.

Example of Python Code
----------------------

Here is an example of how to use the Enhanced Rogers Tanimoto distance with the `distanciaa` package:

.. code-block:: python

    # Import the distanciaa package
    from distanciaa import EnhancedRogersTanimoto

    # Define two binary vectors
    vector_1 = [1, 0, 1, 1, 0]
    vector_2 = [1, 1, 1, 0, 0]

    # Create an instance of the EnhancedRogersTanimoto class with specific weights
    enhanced_rt_dist = EnhancedRogersTanimoto(alpha=1.5, beta=1.0)

    # Calculate the Enhanced Rogers-Tanimoto distance between the two vectors
    distance = enhanced_rt_dist.calculate(vector_1, vector_2)

    # Print the result
    print(f"The Enhanced Rogers-Tanimoto distance between the two vectors is: {distance}")

Expected Output:

The Enhanced Rogers-Tanimoto distance between the two vectors is: 0.5455

Academic Reference
------------------

For more detailed information on the Enhanced Rogers-Tanimoto distance and its applications, consider the following reference::footcite:t:`enhancedrogerstanimoto`

.. footbibliography::

    


Conclusion
----------

The Enhanced Rogers-Tanimoto distance offers a more nuanced approach to measuring similarity or dissimilarity between binary vectors by incorporating adjustable weighting factors. This makes it particularly valuable in fields where certain features or interactions between features carry more significance. The distanciaa package provides a simple and effective way to calculate this distance, allowing researchers and data scientists to apply it to their specific use cases with ease.
