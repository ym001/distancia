Outlier Detection
================

Introduction
------------

The `OutlierDetection` class in the `distancia` package provides a sophisticated method for identifying outliers in datasets through the application of various distance metrics. Outliers, or anomalies, are data points that differ significantly from the rest of the dataset. Detecting these anomalies is crucial in numerous applications, from fraud detection to ensuring data quality in scientific research.

Idea and Utility
----------------

Outliers are more than just statistical anomalies; they often carry significant real-world implications. For instance, in financial datasets, an outlier might indicate fraudulent activity, while in manufacturing data, it might highlight a defect in a product. The ability to accurately detect outliers is therefore vital across various fields.

The `OutlierDetection` class allows users to identify these outliers by measuring the distance of each data point from a central reference point, typically the centroid of the dataset. If a point lies far from this centroid, it is likely an outlier.

One of the key strengths of this class is its flexibility. Different datasets may require different distance metrics to accurately identify outliers. For instance, while Euclidean distance is straightforward and intuitive, it may not account for correlations between variables in the data, which can be critical in high-dimensional datasets. On the other hand, Mahalanobis distance takes these correlations into account, providing a more nuanced detection mechanism in such cases.

Furthermore, the `OutlierDetection` class can be particularly effective when combined with domain knowledge. By understanding the context in which data is collected, users can fine-tune the threshold for what constitutes an outlier, making the detection process more robust and relevant to specific applications.

Example
-------

.. code-block:: python
    from distancia import OutlierDetection
    from distancia import Euclidean

    # Sample data points (2D)
    data_points = [
        [1.0, 2.0],
        [2.1, 3.0],
        [0.9, 1.8],
        [10.0, 10.0],  # Potential outlier
        [2.2, 3.1],
        [1.9, 2.8]
    ]

    # Create an instance of OutlierDetection with Euclidean distance
    outlier_detector = OutlierDetection(data_points, metric=Euclidean(), threshold=1.5)

    # Detect outliers
    outliers = outlier_detector.detect_outliers()

    print("Detected outliers:")
    for outlier, distance in outliers:
        print(f"Point: {outlier}, Distance from centroid: {distance}")

.. code-block:: bash

    >>>Detected outliers:
    >>>Point: [10.0, 10.0], Distance from centroid: 9.349539501434757

Academic Reference
------------------

Outlier detection is a well-explored domain in both statistics and machine learning. A comprehensive resource on the topic is: :footcite:t:`outlier`

.. footbibliography::

    


Conclusion
----------

The `OutlierDetection` class is a powerful tool within the `distancia` package, providing essential functionality for identifying anomalies in datasets. By supporting a variety of distance metrics, it offers flexibility and precision in detecting outliers across different types of data. This makes it an invaluable resource for data scientists, researchers, and analysts who need to ensure the integrity of their datasets while uncovering meaningful insights. The inclusion of this class in `distancia` underscores the package's commitment to providing comprehensive, customizable tools for advanced data analysis.

