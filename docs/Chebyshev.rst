Chebyshev Distance
===================

The Chebyshev distance, also known as the maximum metric or L∞ metric, is a measure of the distance between two points in a space. It is defined as the maximum absolute difference between the coordinates of the points. This metric is particularly useful in situations where movement is allowed only in discrete steps.

.. contents::
   :local:
   :depth: 2

Formula
--------

The formula for calculating the Chebyshev distance between two points :math:`\mathbf{p}` and :math:`\mathbf{q}` in an n-dimensional space is given by:

.. math::

    d(\mathbf{p}, \mathbf{q}) = \max_{i} \left| p_i - q_i \right|

Where:

- :math:`\mathbf{p}` and :math:`\mathbf{q}` are two points in n-dimensional space.

- :math:`p_i` and :math:`q_i` are the coordinates of the points in the i-th dimension.

- :math:`\left| p_i - q_i \right|` is the absolute difference between the coordinates.

History
--------

The Chebyshev distance is named after the Russian mathematician Pafnuty Chebyshev, who contributed significantly to the field of mathematical analysis and approximation theory. The metric itself was introduced in the mid-19th century as part of Chebyshev's work on polynomial approximation.

Unlike Euclidean distance, which measures the straight-line distance between two points, the Chebyshev distance measures the maximum difference along any coordinate dimension. This metric is particularly useful in grid-based environments such as chessboards, where the distance between two points is determined by the maximum number of steps required along any axis.

Example Usage
-------------

Here is a Python example demonstrating how to calculate the Chebyshev distance between two points using the `distancia` package:

.. code-block:: python

    from distancia import Chebyshev

    # Define the coordinates of the two points
    point1 = (1, 3, 4)
    point2 = (4, 7, 1)

    # Create an instance of ChebyshevDistance
    chebyshev = Chebyshev()

    # Calculate the Chebyshev distance
    distance = chebyshev.calculate(point1, point2)

    print(f"Chebyshev Distance: {distance}")

Reference
---------

For further reading on the Chebyshev distance and its applications, refer to the following academic article:

:footcite:t:``

.. footbibliography::

   chebyshev

This paper provides an in-depth discussion of Chebyshev's contributions to approximation theory and metrics.

Conclusion
----------

The Chebyshev distance is a valuable metric for various applications where movement is restricted to grid-like steps or where the maximum deviation in any coordinate dimension is of interest. Its simplicity and practicality make it useful in computational problems and analysis involving discrete steps. By implementing the Chebyshev distance in the distancia package, users can efficiently calculate this metric in Python for diverse applications, including grid-based and discrete space analyses. This metric complements other distance measures by providing a different perspective on spatial relationships.
