Mahalanobis Distance
====================

The Mahalanobis distance is a measure of the distance between a point and a distribution, or between two points in a distribution that accounts for the correlation between the variables. It is particularly useful in identifying multivariate outliers and in classification problems.

Formula
--------
The Mahalanobis distance between a point :math:`\mathbf{x}` and a mean vector :math:`\mathbf{\mu}` with covariance matrix :math:`\mathbf{\Sigma}` is given by:

.. math::
    D_{M}(\mathbf{x}, \mathbf{\mu}) = \sqrt{(\mathbf{x} - \mathbf{\mu})^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{\mu})}

Here:

- :math:`\mathbf{x}` is the point of interest.

- :math:`\mathbf{\mu}` is the mean vector of the distribution.

- :math:`\mathbf{\Sigma}` is the covariance matrix of the distribution.

- :math:`\mathbf{\Sigma}^{-1}` is the inverse of the covariance matrix.

History
--------
The Mahalanobis distance was introduced by the Indian statistician Prasanta Chandra Mahalanobis in 1936. It is a generalized distance metric that accounts for correlations between variables, making it more effective in high-dimensional spaces compared to Euclidean distance.

Mahalanobis distance is commonly used in multivariate anomaly detection, clustering, and classification tasks where understanding the variance and covariance of the data is crucial.

Example Usage
-------------

Here is a Python example demonstrating how to calculate the Mahalanobis distance between a point and a distribution using the `distancia` package:

.. code-block:: python

    from distancia import MahalanobisDistance

    # Define the mean vector and covariance matrix of the distribution
    data = = [
        [2, 1, 0],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
    ]

    # Define the point of interest
    point = [3, 5]

    # Create an instance of MahalanobisDistance
    distance = Mahalanobis().calculate(point, data)

    print(f"Mahalanobis Distance: {distance}")

Reference
---------
For more detailed information on Mahalanobis distance and its applications, refer to the following academic article:

.. bibliography::


Mahalanobis, P. C. (1936). "On the generalized distance in statistics." Proceedings of the National Institute of Sciences of India, 2(1), 49-55.
This paper introduces the concept of Mahalanobis distance and discusses its properties and applications in statistical analysis.


Conclusion
----------


