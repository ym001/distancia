Generalized Jaccard
==================

Introduction
------------

The **Generalized Jaccard** similarity coefficient is an extension of the classic Jaccard index, designed to measure the similarity between two sets or multi-dimensional vectors that can contain weighted or fuzzy elements. Unlike the traditional Jaccard index, which only considers binary (presence/absence) data, the Generalized Jaccard coefficient can handle more complex data structures where elements can have varying degrees of presence.

This makes the Generalized Jaccard coefficient particularly useful in applications such as text similarity, image comparison, and any domain where elements are not strictly binary but have associated weights or frequencies.

Formula
-------

The **Generalized Jaccard** similarity coefficient is defined as:

.. math::

    S(X, Y) = \frac{\sum_{i} \min(x_i, y_i)}{\sum_{i} \max(x_i, y_i)}

where:

- :math:`x_i` and :math:`y_i` represent the values of the i-th element in sets or vectors :math:`X` and :math:`Y`, respectively.
- The summation is performed over all elements :math:`i` in the universal set.

The Generalized Jaccard coefficient returns a value between 0 and 1, where 1 indicates identical sets or vectors and 0 indicates no similarity.

Concept and Purpose
-------------------

The **Generalized Jaccard** coefficient extends the classical Jaccard index to handle cases where data is not simply binary. For instance, in text mining, words in two documents can have varying frequencies, and the Generalized Jaccard index can take these frequencies into account to provide a more nuanced measure of similarity.

This coefficient is particularly valuable in scenarios where the similarity of objects is not binary but is instead graded or fuzzy, such as in comparing weighted networks, multi-dimensional data points, or probabilistic models.

.. code-block:: python

    # Importing the GeneralizedJaccard class from the distancia package
    from distancia import GeneralizedJaccard

    # Define a function to test the Generalized Jaccard similarity
    def test_generalized_jaccard():
        # Create an instance of the GeneralizedJaccard class
        similarity_calculator = GeneralizedJaccard()

        # Test cases: pairs of vectors to compare
        test_cases = [
            ([1, 2, 3], [3, 2, 1]),
            ([0, 1, 2], [2, 0, 1]),
            ([5, 10, 15], [10, 15, 5]),
            ([0.5, 0.7, 0.9], [0.9, 0.7, 0.5]),
            ([1, 1, 1], [1, 1, 1]),
            ([0, 0, 0], [1, 2, 3]),
        ]

        # Iterate through the test cases and compute the similarity
        for vec1, vec2 in test_cases:
            similarity = similarity_calculator.calculate(vec1, vec2)
            print(f"Generalized Jaccard similarity between {vec1} and {vec2}: {similarity:.4f}")

    if __name__ == "__main__":
        # Run the test function
        test_generalized_jaccard()

.. code-block:: bash

    >>>Generalized Jaccard similarity between [1, 2, 3] and [3, 2, 1]: 0.5000
    >>>Generalized Jaccard similarity between [0, 1, 2] and [2, 0, 1]: 0.8000
    >>>Generalized Jaccard similarity between [5, 10, 15] and [10, 15, 5]: 0.5000
    >>>Generalized Jaccard similarity between [0.5, 0.7, 0.9] and [0.9, 0.7, 0.5]: 0.3200
    >>>Generalized Jaccard similarity between [1, 1, 1] and [1, 1, 1]: 0.0000
    >>>Generalized Jaccard similarity between [0, 0, 0] and [1, 2, 3]: 1.0000

History
-------

The **Generalized Jaccard** coefficient evolved from the classic Jaccard index, which was introduced by the Swiss botanist Paul Jaccard in 1901. The original Jaccard index was developed to measure the similarity between two sets of binary attributes. As the need for more sophisticated measures grew, especially in the fields of information retrieval, machine learning, and data mining, the Jaccard index was generalized to accommodate non-binary data.

The Generalized Jaccard coefficient is now widely used in various applications, including image processing, text analysis, and bioinformatics, where the classic Jaccard index would be insufficient to capture the complexity of the data.

Academic Reference
------------------

For further reading on the **Generalized Jaccard** similarity coefficient, consider the following academic reference:

- Tanimoto, T. T. (1958). *An elementary mathematical theory of classification and prediction*. IBM Internal Report.

Although this reference discusses a related metric known as the Tanimoto coefficient, it is closely related to the Generalized Jaccard index and offers insight into its theoretical underpinnings.

Conclusion
----------

The **Generalized Jaccard** similarity coefficient is a powerful and flexible tool for measuring the similarity between non-binary or weighted data sets. By extending the classic Jaccard index, it allows for more sophisticated analyses in a wide range of fields, from text and image processing to biological data analysis. As part of the `distancia` package, the Generalized Jaccard coefficient enables users to compare complex data structures with precision, making it an essential tool for modern data science and machine learning tasks.

