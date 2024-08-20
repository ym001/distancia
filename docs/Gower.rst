Gower
=====

Introduction
------------

The **Gower similarity coefficient** is a versatile metric used to measure the similarity between two entities with mixed data types. It is particularly useful in situations where the data includes both categorical and numerical variables, as it can handle these different types seamlessly. Unlike many other distance or similarity measures, the Gower coefficient can combine various types of data into a single, unified measure of similarity, making it ideal for datasets with diverse attributes.

Formula
-------

The **Gower similarity coefficient** for two entities :math:`i` and :math:`j` is calculated as:

.. math::

    S_{ij} = \frac{1}{p} \sum_{k=1}^{p} s_{ijk}

Where:

- :math:`p` is the number of variables.
- :math:`s_{ijk}` is the contribution of the k-th variable to the overall similarity between entities :math:`i` and :math:`j`.

For numerical variables:

.. math::

    s_{ijk} = 1 - \frac{|x_{ik} - x_{jk}|}{R_k}

Where:

- :math:`x_{ik}` and :math:`x_{jk}` are the values of the k-th variable for entities :math:`i` and :math:`j`, respectively.
- :math:`R_k` is the range of the k-th variable across all entities.

For categorical variables:

.. math::

    s_{ijk} = 
    \begin{cases}
    1 & \text{if } x_{ik} = x_{jk}\\
    0 & \text{if } x_{ik} \neq x_{jk}
    \end{cases}

The overall Gower similarity is the average of the individual similarities across all variables.

Concept and Purpose
-------------------

The **Gower similarity coefficient** is designed to address the challenge of calculating similarity between entities described by both numerical and categorical variables. Traditional measures, such as Euclidean distance, are limited to numerical data, whereas other metrics are better suited to categorical data. Gower's coefficient uniquely combines these capabilities, allowing for the analysis of complex, real-world datasets that contain a mix of data types.

This coefficient is particularly useful in fields like ecology, social science, and marketing, where datasets often include diverse variables such as measurements, counts, and categorical labels. By standardizing the contribution of each variable to the overall similarity, the Gower coefficient provides a balanced and interpretable measure of similarity.

.. code-block:: python

        # Create an instance of the Gower class
        gower = Gower()

        # Test cases: pairs of data points with mixed types (numerical and categorical)
        test_cases = [
            (["Red", 3.2, 5], ["Blue", 4.1, 3], [None, 5.0, 10]),
            ([5.5, "M", 200], [6.1, "F", 180], [10, None, 50]),
            ([0, "High", 10], [1, "Low", 10], [1, None, 10]),
            ([100, "Yes", 3.5], [150, "No", 2.8], [50, None, 5]),
            ([1.5, "Green", 2], [1.5, "Green", 2], [None, None, None])
        ]

        # Compute and print the Gower similarity for each pair
        for vec1, vec2, ranges in test_cases:
            similarity = gower.distance(vec1, vec2, ranges)
            print(f"Gower similarity between {vec1} and {vec2}: {similarity:.4f}")

.. code-block:: python

    >>>Gower similarity between ['Red', 3.2, 5] and ['Blue', 4.1, 3]: 0.5400
    >>>Gower similarity between [5.5, 'M', 200] and [6.1, 'F', 180]: 0.5133
    >>>Gower similarity between [0, 'High', 10] and [1, 'Low', 10]: 0.3333
    >>>Gower similarity between [100, 'Yes', 3.5] and [150, 'No', 2.8]: 0.2867
    >>>Gower similarity between [1.5, 'Green', 2] and [1.5, 'Green', 2]: 1.0000

History
-------

The **Gower similarity coefficient** was introduced by J. C. Gower in 1971 in his seminal paper titled *"A General Coefficient of Similarity and Some of Its Properties"*. This work was groundbreaking in that it provided a method for combining different types of data into a single measure of similarity, which was previously a significant challenge in statistical analysis.

Gower's work has since become foundational in many fields, including ecology, biology, and data science, where researchers and analysts often work with mixed-type data. The Gower coefficient remains a widely used tool for clustering, classification, and other forms of multivariate analysis.

Academic Reference
------------------

For a detailed explanation of the Gower similarity coefficient, refer to the original publication:

- Gower, J. C. (1971). *A general coefficient of similarity and some of its properties*. Biometrics, 27(4), 857-871. DOI: 10.2307/2528823

This paper lays out the theoretical foundations of the coefficient and discusses its properties and applications in depth.

Conclusion
----------

The **Gower similarity coefficient** is a powerful and flexible tool for measuring similarity between entities in datasets with mixed data types. Its ability to handle both numerical and categorical variables in a unified manner makes it an essential method for modern data analysis, particularly in fields dealing with diverse and complex data. As part of the `distancia` package, the Gower coefficient enables users to perform sophisticated similarity analyses with ease, contributing to more accurate and meaningful insights in data science and beyond.

