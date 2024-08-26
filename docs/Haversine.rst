Haversine Distance
====================

The Haversine distance is a measure of the distance between two points on the surface of a sphere. It is commonly used in navigation and geographic information systems (GIS) to calculate the great-circle distance between two points specified by their latitude and longitude.

.. contents::
   :local:
   :depth: 2

Formula
--------

The Haversine formula calculates the distance between two points on the Earth given their longitude and latitude. The formula is as follows:

.. math::

    d = 2 \cdot R \cdot \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1) \cdot \cos(\phi_2) \cdot \sin^2\left(\frac{\Delta \lambda}{2}\right)}\right)

Where:

- :math:`d` is the distance between the two points.

- :math:`R` is the Earth's radius (mean radius = 6,371 km).

- :math:`\phi_1` and :math:`\phi_2` are the latitudes of the two points (in radians).

- :math:`\Delta \phi` is the difference in latitudes.

- :math:`\Delta \lambda` is the difference in longitudes.

History
--------

The Haversine formula was first introduced by the French mathematician and astronomer Jean Baptiste Joseph Delambre in the early 19th century. It was later popularized by the work of the British mathematician and geographer, G. W. Haversine, who adapted it for practical navigation and geographic calculations.

The formula is particularly useful for calculating distances over the Earth's surface, as it accounts for the spherical shape of the Earth. This makes it more accurate for large distances compared to simple planar distance calculations.

Example Usage
-------------

Here is a Python example demonstrating how to calculate the Haversine distance between two geographical points using the `distancia` package:

.. code-block:: python

    from distancia import Haversine

    # Define the coordinates of the two points (latitude, longitude)
    point1 = (52.2296756, 21.0122287)  # Warsaw, Poland
    point2 = (41.8919300, 12.5113300)  # Rome, Italy

    # Create an instance of HaversineDistance
    haversine = Haversine()

    # Calculate the Haversine distance
    distance = haversine.calculate(point1, point2)

    print(f"Haversine Distance: {distance} km")


Reference
---------

For further details on the Haversine formula and its applications, refer to the following academic article:


:footcite:t:``

.. footbibliography::

   haversine

This paper provides an in-depth discussion of the Haversine formula and its use in calculating spherical distances.


Conclusion
----------

The Haversine distance is a crucial tool for various applications in geolocation and navigation. By providing an accurate measurement of the distance between two points on the Earth's surface, it facilitates numerous practical tasks ranging from flight planning to geographic analysis. Its spherical model accounts for the curvature of the Earth, making it a preferred choice over planar distance measures for large-scale calculations. The implementation of the Haversine formula in the distancia package allows for straightforward and efficient distance calculations in Python, making it a valuable addition to any geospatial analysis toolkit.
