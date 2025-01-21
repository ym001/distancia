Derivative Dynamic Time Warping (DDTW)
===================================

Introduction
-----------
Derivative Dynamic Time Warping (DDTW) is an extension of the traditional Dynamic Time Warping (DTW) algorithm that operates on the first derivatives of time series rather than their raw values. By considering the rate of change between consecutive points, DDTW emphasizes the shape similarity between sequences and is less sensitive to baseline shifts and amplitude variations. This approach makes it particularly effective for applications where the trend and shape patterns are more important than absolute values.

Mathematical Definition
---------------------
For two time series X = (x₁, ..., xₙ) and Y = (y₁, ..., yₘ), DDTW first computes their derivatives:

.. math::

   D(x_i) = \frac{(x_{i+1} - x_{i-1}) + (x_i - x_{i-1})/2}{2}, \quad 1 < i < n

   D(y_j) = \frac{(y_{j+1} - y_{j-1}) + (y_j - y_{j-1})/2}{2}, \quad 1 < j < m

The DDTW distance is then defined recursively as:

.. math::

   DDTW(i,j) = d(D(x_i), D(y_j)) + min\begin{cases}
   DDTW(i-1,j) \\
   DDTW(i-1,j-1) \\
   DDTW(i,j-1)
   \end{cases}

where:
- :math:`d(D(x_i), D(y_j))` is typically the squared difference between derivatives
- :math:`D(x_i)` and :math:`D(y_j)` are the estimated derivatives
- Boundary conditions are handled specially for i=1 and i=n

Properties
---------
DDTW exhibits several important characteristics:

1. **Key Properties**:
   - Shape-based similarity measure
   - Invariant to shifts in baseline
   - Less sensitive to amplitude variations
   - Preserves monotonicity
   - Satisfies continuity

2. **Advantages**:
   - Better handling of shape patterns
   - Robust to signal shifts
   - Improved alignment in many cases
   - Captures local trends effectively
   - Reduces singularities

3. **Considerations**:
   - Higher computational cost
   - Sensitive to noise
   - Requires careful derivative estimation
   - May need preprocessing

Academic References
-----------------
1. Keogh, E. J., & Pazzani, M. J. (2001). "Derivative Dynamic Time Warping." First SIAM International Conference on Data Mining.

2. Górecki, T., & Łuczak, M. (2013). "Using Derivatives in Time Series Classification." Data Mining and Knowledge Discovery, 26(2), 310-331.

3. Salvador, S., & Chan, P. (2007). "Toward Accurate Dynamic Time Warping in Linear Time and Space." Intelligent Data Analysis, 11(5), 561-580.

Use Cases
--------
DDTW is particularly effective in:

- Shape pattern recognition
- Trend analysis
- Gesture recognition
- Speech processing
- ECG signal comparison
- Financial time series analysis
- Sensor data pattern matching

Implementation Details
--------------------
In the distancia package, DDTW is implemented with the following features:

- Multiple derivative estimation methods
- Customizable warping window
- Various local cost measures
- Optional normalization steps

Example Usage
------------
.. code-block:: python

    from distancia import DDTW
    
    # Initialize DDTW with parameters
    ddtw = DDTW(window=None)
    
    # Calculate distance between two time series
    distance = ddtw.calculate(series1, series2)
    
    # With specific window size
    ddtw_constrained = DDTW(window=10)
    distance_constrained = ddtw_constrained.calculate(series1, series2)

Complexity Analysis
-----------------
- Time Complexity: O(nm)
- Space Complexity: O(nm)

where n and m are the lengths of the input sequences.

Parameter Selection
-----------------
1. **Derivative Estimation**:
   - Central difference
   - Higher-order methods
   - Smoothed derivatives
   - Robust estimation techniques

2. **Window Constraints**:
   - Sakoe-Chiba band
   - Itakura parallelogram
   - Custom constraints

3. **Preprocessing Options**:
   - Smoothing
   - Normalization
   - Outlier removal
   - Noise reduction

Conclusion
---------
Derivative Dynamic Time Warping represents a significant enhancement to traditional DTW by focusing on shape similarity through the comparison of derivatives. Its ability to handle baseline shifts and amplitude variations while maintaining sensitivity to local patterns makes it particularly valuable for applications where shape matching is crucial.

The method's robustness to certain types of variations, combined with its shape-preserving properties, makes it an excellent choice for many real-world applications. However, users should carefully consider the trade-offs between computational cost, noise sensitivity, and the need for accurate derivative estimation when applying this method.

.. note::
   Proper preprocessing and derivative estimation are crucial for optimal performance. Consider the noise characteristics of your data and the importance of local shape features when configuring these parameters.

See Also
--------
- :class:`DTW`
- :class:`WeightedDTW`
- :class:`ShapeDTW`
