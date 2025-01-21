FastDTW Distance
===============

Introduction
-----------
FastDTW (Fast Dynamic Time Warping) is an approximation algorithm that provides a linear time complexity solution to compute the similarity between two time series. While maintaining a high degree of accuracy comparable to the traditional DTW algorithm, FastDTW significantly reduces the computational overhead, making it particularly suitable for analyzing large-scale time series datasets.

The algorithm addresses the quadratic time and space complexity limitations of traditional DTW through a multilevel approach that combines coarsening, refinement, and radius calculations to find an approximate optimal warping path.

Algorithm Overview
----------------
FastDTW operates through three main steps:

1. **Coarsening**: Recursively creating a lower-resolution version of the time series by averaging adjacent points
2. **Low-Resolution Path Finding**: Computing the warping path at the lowest resolution
3. **Refinement**: Projecting and refining the path to higher resolutions while constraining the search to a narrow corridor around the projected path

Mathematical Definition
---------------------
For two time series X and Y, FastDTW uses a radius parameter r and operates recursively:

.. math::

   FastDTW(X, Y, radius) = \begin{cases}
   DTW(X, Y) & \text{if } length(X) \leq radius \\
   refinement(FastDTW(coarsen(X), coarsen(Y), radius)) & \text{otherwise}
   \end{cases}

where:
- :math:`coarsen(X)` reduces the resolution of time series X
- :math:`refinement(path)` projects the warping path to a higher resolution
- :math:`radius` defines the width of the search corridor

Complexity Analysis
-----------------
- Time Complexity: O(N)
- Space Complexity: O(N)

where N is the length of the input sequences.

Properties
---------
1. **Approximate Solution**: Provides a near-optimal warping path
2. **Linear Complexity**: Achieves O(N) time complexity versus O(N²) for traditional DTW
3. **Radius Parameter**: Controls the trade-off between accuracy and speed
4. **Multilevel Approach**: Uses multiple resolutions to find the optimal path efficiently

Academic References
-----------------
1. Salvador, S., & Chan, P. (2007). "Toward accurate dynamic time warping in linear time and space." Intelligent Data Analysis, 11(5), 561-580.

2. Müller, M., et al. (2016). "Dynamic Time Warping." In Information Retrieval for Music and Motion (pp. 69-84). Springer.

Use Cases
--------
FastDTW is particularly valuable in:

- Real-time sequence matching
- Large-scale time series mining
- Gesture recognition
- Speech recognition
- Financial data analysis
- IoT sensor data processing

Implementation Details
--------------------
In the distancia package, FastDTW is implemented with the following key parameters:

- `radius`: Controls the accuracy vs. speed trade-off
- `min_window_size`: Minimum size of the coarsened time series
- `dist_method`: Distance measure used for point-to-point comparisons

Example Usage
------------
.. code-block:: python

    from distancia import FastDTW
    
    # Initialize FastDTW with radius parameter
    fastdtw = FastDTW(radius=30)
    
    # Calculate distance between two time series
    distance = fastdtw.calculate(series1, series2)

Conclusion
---------
FastDTW represents a significant advancement in time series analysis by providing a highly efficient approximation of Dynamic Time Warping. Its linear time complexity makes it practical for large-scale applications while maintaining accuracy comparable to traditional DTW. The algorithm's adaptability through its radius parameter allows users to fine-tune the trade-off between computational efficiency and accuracy based on their specific needs.

.. note::
   While FastDTW provides an approximate solution, its accuracy is generally sufficient for most practical applications, and its efficiency makes it the preferred choice for large-scale time series analysis.

See Also
--------
- :class:`DTW`
- :class:`MDTW`
