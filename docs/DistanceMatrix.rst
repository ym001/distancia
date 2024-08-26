DistanceMatrix
==============

Introduction
------------
The `DistanceMatrix` class in the `distancia` package is designed to automatically generate distance matrices for a set of data points using any of the implemented distance metrics. This class allows users to quickly and efficiently calculate pairwise distances across a dataset, making it particularly useful for tasks that require an understanding of the similarity or dissimilarity between data points.

Utility and Concept
-------------------
In data science and machine learning, distance metrics are foundational for various algorithms, particularly those involving clustering, classification, and anomaly detection. A distance matrix provides a structured representation of the pairwise distances between data points, which can be used in algorithms like K-means clustering, hierarchical clustering, and in visualizations such as heatmaps.

For example, in clustering, a distance matrix helps in understanding the proximity of different data points to one another, aiding in the grouping of similar points. In visualizations, heatmaps generated from distance matrices can reveal patterns of similarity or dissimilarity in the data, which can be critical for exploratory data analysis.

Mathematically, if we have a dataset of `n` data points, a distance matrix `D` is an `n x n` matrix where the element `D[i][j]` represents the distance between the `i-th` and `j-th` data points. The distance metric used can vary, including popular choices like Euclidean, Cosine, or Manhattan distances.


exemple:
--------

.. code-block:: python

    # Example Usage
    data_points = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]


    distance_matrix = DistanceMatrix(data_points, metric=Euclidean())
    print(distance_matrix.get_matrix())

.. code-block:: bash


    >>>[[0.0, 2.8284271247461903, 5.656854249492381, 8.48528137423857], [2.8284271247461903, 0.0, 2.8284271247461903, 5.656854249492381], [5.656854249492381, 2.8284271247461903, 0.0, 2.8284271247461903], [8.48528137423857, 5.656854249492381, 2.8284271247461903, 0.0]]

Academic Reference
------------------
The concept of distance matrices is well-established in various fields, including statistics, machine learning, and computational biology. A relevant academic reference is::footcite:t:`distancematrix`



This book extensively discusses the use of distance matrices in clustering algorithms, providing both theoretical foundations and practical applications.


.. footbibliography::

Conclusion
----------
The `DistanceMatrix` class in the `distancia` package provides a powerful tool for researchers and practitioners who need to compute and utilize distance matrices in their work. By supporting multiple distance metrics and offering a simple interface, this class enhances the flexibility and usability of the `distancia` package, making it an essential component for tasks involving similarity or dissimilarity analysis in datasets.
