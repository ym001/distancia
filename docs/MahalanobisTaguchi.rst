Mahalanobis-Taguchi System (MTS) Distance
=========================================

Introduction
------------

The Mahalanobis-Taguchi System (MTS) is a multivariate statistical method used for pattern recognition and diagnosis based on the Mahalanobis distance. The method was developed by Genichi Taguchi and is particularly effective in situations where the dataset is highly dimensional and correlations between variables need to be considered. MTS is a robust tool in quality engineering, particularly for dimensionality reduction and anomaly detection.

The Mahalanobis distance itself is a measure that accounts for the correlations between variables, making it ideal for identifying outliers in multivariate datasets. MTS enhances this by creating a diagnostic system that helps in identifying and quantifying factors contributing to deviations.

Formula
-------

The Mahalanobis distance between a point `\mathbf{x}` and a distribution with mean `\mathbf{\mu}` and covariance matrix `\mathbf{\Sigma}` is given by:

.. math::

    D_M(\mathbf{x}, \mathbf{\mu}) = \sqrt{(\mathbf{x} - \mathbf{\mu})^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{\mu})}

In the context of the Mahalanobis-Taguchi System, the Mahalanobis distance is applied to determine the degree of abnormality in a dataset when compared to a normal (reference) group.

- `\mathbf{x}`: The vector of observed data.
- `\mathbf{\mu}`: The mean vector of the reference group.
- `\mathbf{\Sigma}`: The covariance matrix of the reference group.

Interpretation
--------------

The Mahalanobis-Taguchi System uses the Mahalanobis distance as a foundation for diagnosing and predicting the performance of systems based on multivariate data. The distance itself is a measure of how far a point is from the center of a distribution, considering the shape of the distribution.

In practical terms, a smaller Mahalanobis distance indicates that the observation is similar to the reference group, while a larger distance indicates that the observation is an outlier or abnormal in comparison. The MTS method provides a structured way to use this information for decision-making, particularly in quality control and diagnostics.

.. code-block:: python

    from distancia import MahalanobisTaguchi  # Assuming the MahalanobisTaguchi class is in the distancia package

    def main():
        # Example reference group data (2D array where each row is a data point)
        reference_group = [
            [1.0, 2.0, 3.0],
            [1.1, 2.1, 2.9],
            [0.9, 1.8, 3.1],
            [1.2, 2.2, 3.2]
        ]

        # Example test data (data point to be evaluated against the reference group)
        test_data = [1.3, 2.3, 3.3]

        # Create an instance of the MahalanobisTaguchi class
        m_taguchi = MahalanobisTaguchi(reference_group)

        # Calculate the Mahalanobis-Taguchi distance for the test data
        distance = m_taguchi.calculate(test_data)

        # Print the result
        print(f"Mahalanobis-Taguchi distance for the test data {test_data} is: {distance}")

    if __name__ == "__main__":
        main()


.. code-block:: bash

    >>>Mahalanobis-Taguchi distance for the test data [1.3, 2.3, 3.3] is: 2.59807621135332

History
-------

The Mahalanobis distance was introduced by Indian statistician P.C. Mahalanobis in 1936 as a way to measure the distance between a point and a distribution, considering correlations between variables. The Mahalanobis-Taguchi System (MTS) was later developed by Genichi Taguchi in the 1990s as part of his broader work in quality engineering.

Taguchi’s methodology integrates the Mahalanobis distance into a diagnostic framework, enhancing its applicability in industrial contexts. The MTS method has since been adopted in various fields, including healthcare, manufacturing, and environmental studies, for its effectiveness in handling high-dimensional data and improving decision-making processes.

Academic Reference
------------------

A key reference for understanding the Mahalanobis-Taguchi System is:

.. bibliography::


Taguchi, G., Jugulum, R. (2002). *The Mahalanobis-Taguchi Strategy: A Pattern Technology System*. Wiley.

This work outlines the principles of the MTS and provides practical examples of its application in quality engineering.

Conclusion
----------

The Mahalanobis-Taguchi System (MTS) distance is a powerful tool for analyzing multivariate data, particularly in contexts where correlations between variables are significant. By combining the Mahalanobis distance with a structured diagnostic system, MTS allows for effective pattern recognition, anomaly detection, and dimensionality reduction.

Incorporating the Mahalanobis-Taguchi distance into the `distancia` package provides users with a robust method for assessing and diagnosing multivariate data, making it a valuable addition for those working in fields such as quality engineering, data science, and beyond.

This documentation was prepared to help users of the `distancia` package understand and effectively apply the Mahalanobis-Taguchi distance in their analytical work.

