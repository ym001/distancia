Euclidean Distance
==================

**Euclidean Distance** is one of the most commonly used metrics in mathematics, computer science, and machine learning. It measures the "straight line" distance between two points in Euclidean space.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Euclidean distance between two points \\( \mathbf{p} \\) and \\( \mathbf{q} \\) in \\( n \\)-dimensional space is defined as:

.. math::

   d(\mathbf{p}, \mathbf{q}) = \sqrt{ \sum_{i=1}^{n} (p_i - q_i)^2 }

Where:

* $$ \\mathbf{p} = (p_1, p_2, \\dots, p_n) $$ is the first point.

* \( \mathbf{q} = (q_1, q_2, \dots, q_n) \) is the second point.

* \( n \) is the number of dimensions.

History
-------

The concept of Euclidean distance originates from the work of the ancient Greek mathematician **Euclid** in his seminal work "Elements" around 300 BC. Euclid's work laid the foundation for geometry as we know it today, and the distance formula is derived from the Pythagorean theorem, which Euclid described in one of the propositions in his work.

Over centuries, Euclidean distance has become a cornerstone in various fields such as geometry, physics, and data science. It serves as the most straightforward distance measure in Euclidean space and is used in numerous applications including clustering, nearest neighbor algorithms, and many other machine learning techniques.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the Euclidean distance between two points using the `Distancer` package:

.. code-block:: python

    from distancer import euclidean_distance

    # Define two points in 3D space
    point1 = [2, 3, 5]
    point2 = [7, 1, 9]

    # Calculate Euclidean Distance
    distance = euclidean_distance(point1, point2)

    print(f"Euclidean Distance: {distance}")

In this example, the points \( \mathbf{p} = (2, 3, 5) \) and \( \mathbf{q} = (7, 1, 9) \) are defined in a 3-dimensional space. The Euclidean distance between these points is calculated and printed.

Applications
------------

Euclidean distance is widely used in various applications, including but not limited to:

- **K-Nearest Neighbors (KNN)**: In machine learning, Euclidean distance is often used to find the nearest neighbors of a data point.
- **Clustering**: Algorithms like K-Means use Euclidean distance to minimize the distance between points and the cluster centers.
- **Computer Vision**: Euclidean distance can be used to compare feature vectors extracted from images.
- **Physics**: It represents the shortest path between two points in physical space.

Reference
---------

For an academic reference, you can refer to the following article that discusses the Euclidean distance and its applications in depth:

Beyer, K., Goldstein, J., Ramakrishnan, R., & Shaft, U. (1999). When is "nearest neighbor" meaningful?. In *International Conference on Database Theory* (pp. 217-235). Springer, Berlin, Heidelberg.

This paper discusses the use of Euclidean distance in the context of high-dimensional data and its relevance in database theory.

Conclusion
----------

The Euclidean distance is a fundamental measure in various disciplines, and its simplicity and effectiveness make it a go-to metric in many scenarios. Whether you're working on machine learning algorithms, analyzing data points, or dealing with geometric problems, understanding and utilizing Euclidean distance is crucial.

