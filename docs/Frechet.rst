Frechet Distance
================

Introduction
------------

The Fréchet Distance is a measure of similarity between two curves that takes into account the location and ordering of the points along the curves. Unlike simpler distance metrics such as Euclidean distance, the Fréchet Distance is particularly well-suited for comparing paths or trajectories in space, as it considers the direction and shape of the curves. This makes it an important tool in fields like computational geometry, computer graphics, and geographic information systems (GIS).

Idea
----

The concept behind the Fréchet Distance is to imagine a man walking his dog, where the man follows one curve and the dog follows another. Both the man and the dog can vary their speed but cannot backtrack. The Fréchet Distance between the two curves is the minimum length of a leash required to connect the man and the dog as they traverse their respective paths. This leash length represents the "effort" needed to keep the two curves connected, making it a robust metric for comparing the shapes of the curves.

In mathematical terms, the Fréchet Distance is computed using a dynamic programming approach that recursively compares the distances between pairs of points on the two curves, taking into account the paths traversed so far.

Example
-------

Consider two curves represented by the following sets of points:

- Curve A: [(0, 0), (1, 1), (2, 2)]
- Curve B: [(0, 0), (1, 2), (2, 3)]

To compute the Fréchet Distance between these curves using the `FrechetDistance` class in the `distancia` package:

.. code-block:: python

  from distancia import FrechetDistance

  curve1 = [(0, 0), (1, 1), (2, 2)]
  curve2 = [(0, 0), (1, 2), (2, 3)]

  frechet_distance = Frechet()
  distance = frechet_distance.calculate(curve1, curve2)
  print(f"Fréchet Distance: {distance}")

.. code-block:: bash

  >>>Fréchet Distance: 1.0



This example demonstrates the calculation of the Fréchet Distance between two simple 2D curves. The resulting distance provides a measure of how similar these two curves are in terms of shape and trajectory.

Academic Reference
------------------

The Fréchet Distance was first introduced by Maurice Fréchet in 1906 in the context of functional analysis. It was later applied to computational geometry to compare curves and paths. The foundational paper in this field is:

.. bibliography::

  frechet

- Alt, Helmut, and Michael Godau. "Computing the Fréchet distance between two polygonal curves." *International Journal of Computational Geometry & Applications* 5.01n02 (1995): 75-91.

Conclusion
----------

The Fréchet Distance is a powerful tool for comparing the similarity between two curves or trajectories, considering both their shape and direction. It is particularly useful in applications where the order of points along the curves is important, such as in path comparison, movement analysis, and shape matching. The `FrechetDistance` class in the `distancia` package offers an easy-to-use implementation of this complex distance metric, enabling its application in a wide range of computational geometry tasks.
