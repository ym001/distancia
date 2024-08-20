Manhattan Distance
==================

**Manhattan Distance**, also known as **L1 Distance** or **Taxicab Distance**, is a measure of distance in a grid-based path. It calculates the sum of the absolute differences between the coordinates of two points.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Manhattan Distance between two points :math:`\mathbf{A} = (A_1, A_2, \dots, A_n)` and :math:`\mathbf{B} = (B_1, B_2, \dots, B_n)` in an n-dimensional space is defined as:

.. math::

   \text{Manhattan Distance} = \sum_{i=1}^{n} |A_i - B_i|

Where:

- :math:`\mathbf{A} = (A_1, A_2, \dots, A_n)` is the first point.

- :math:`\mathbf{B} = (B_1, B_2, \dots, B_n)` is the second point.

- :math:`n` is the number of dimensions.

The result is the sum of the absolute differences of their corresponding coordinates.

History
-------

The Manhattan Distance is named after the grid-like street geography of the borough of Manhattan in New York City, where the shortest path between two points is along the grid rather than a straight line. This concept became widely used in various fields, particularly in mathematics, computer science, and operations research.

Manhattan Distance is particularly useful in settings where movement is restricted to horizontal and vertical paths, making it ideal for grid-based algorithms and spatial analysis.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the Manhattan Distance between two points using the `distancia` package:

.. code-block:: python

    from distancia import Manhattan

    # Define two points
    point1 = [1, 2, 3]
    point2 = [4, 6, 3]

    # Calculate Manhattan Distance
    distance = Manhattan().calculate(point1, point2)

    print(f"Manhattan Distance: {distance}")

In this example, the points :math:`\mathbf{A} = (1, 2, 3)` and :math:`\mathbf{B} = (4, 6, 3)` are compared. The Manhattan Distance between these points is calculated and printed.

Applications
------------

Manhattan Distance is widely used in various domains, including:

- **Computer Vision**: For measuring differences between pixel values.
- **Clustering Algorithms**: Such as k-medians clustering, where L1 distance is often more robust to outliers.
- **Robotics and Pathfinding**: For determining the shortest path in grid-based maps.
- **Operations Research**: For solving optimization problems where movement is restricted to a grid.

Reference
---------

For an academic reference, you can refer to the following article that discusses the application of Manhattan Distance in clustering algorithms:

Aggarwal, C. C., Hinneburg, A., & Keim, D. A. (2001). *On the Surprising Behavior of Distance Metrics in High Dimensional Space*. In International Conference on Database Theory (pp. 420-434). Springer.

This article explores the behavior of various distance metrics, including Manhattan Distance, in the context of high-dimensional data analysis.

Conclusion
----------

Manhattan Distance is a versatile and intuitive measure of distance, particularly useful in grid-based environments where movement is constrained to horizontal and vertical directions. Its simplicity and robustness make it a valuable tool in many applications, from computer vision to clustering and pathfinding.

