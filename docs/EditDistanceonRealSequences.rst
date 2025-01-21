Edit Distance on Real Sequences (EDR)
===================================

Introduction
-----------
Edit Distance on Real Sequences (EDR) is a robust distance metric designed specifically for comparing numerical time series. It extends the classical edit distance concept by introducing a matching threshold that determines whether two elements are considered similar. This approach makes EDR particularly effective for handling noisy data and numerical variations in time series analysis.

Unlike traditional edit distance which works with discrete values, EDR accommodates the continuous nature of real-valued sequences by considering two elements as matching if their absolute difference falls within a specified threshold.

Mathematical Definition
---------------------
For two time series X = (x₁, ..., xₙ) and Y = (y₁, ..., yₘ), and a matching threshold ε, EDR is defined recursively as:

.. math::

   EDR(X, Y) = EDR(i, j) = \begin{cases}
   i & \text{if } j = 0 \\
   j & \text{if } i = 0 \\
   min\begin{cases}
   EDR(i-1, j-1) + subcost(x_i, y_j) \\
   EDR(i-1, j) + 1 \\
   EDR(i, j-1) + 1
   \end{cases} & \text{otherwise}
   \end{cases}

where:
- :math:`subcost(x_i, y_j) = \begin{cases} 0 & \text{if } |x_i - y_j| \leq \epsilon \\ 1 & \text{otherwise} \end{cases}`
- :math:`\epsilon` is the matching threshold
- :math:`|x_i - y_j|` is the absolute difference between elements

Properties
---------
EDR exhibits several important characteristics:

1. **Metric Properties**:
   - Non-negativity
   - Symmetry
   - Triangle inequality
   - Identity of indiscernibles

2. **Advantages**:
   - Robust to noise
   - Handles local time shifts
   - Supports sequences of different lengths
   - Less sensitive to outliers than DTW
   - Provides intuitive distance values

3. **Key Features**:
   - Threshold-based matching
   - Gap penalties of 1
   - Integer-valued distances
   - Bounded output range [0, max(n,m)]

Academic References
-----------------
1. Chen, L., Özsu, M. T., & Oria, V. (2005). "Robust and Fast Similarity Search for Moving Object Trajectories." Proceedings of the 2005 ACM SIGMOD International Conference on Management of Data, 491-502.

2. Ding, H., Trajcevski, G., Scheuermann, P., Wang, X., & Keogh, E. (2008). "Querying and Mining of Time Series Data: Experimental Comparison of Representations and Distance Measures." Proceedings of the VLDB Endowment, 1(2), 1542-1552.

3. Wang, X., Mueen, A., Ding, H., Trajcevski, G., Scheuermann, P., & Keogh, E. (2013). "Experimental Comparison of Representation Methods and Distance Measures for Time Series Data." Data Mining and Knowledge Discovery, 26(2), 275-309.

Use Cases
--------
EDR is particularly effective in:

- Time series classification
- Pattern matching in noisy data
- Trajectory similarity analysis
- Sensor data comparison
- Financial time series analysis
- Gesture recognition
- Speech pattern matching

Implementation Details
--------------------
In the distancia package, EDR is implemented with the following key parameters:

- `epsilon`: The matching threshold
- `window`: Optional constraint on the matching window size
- `normalize`: Boolean flag for result normalization

Example Usage
------------
.. code-block:: python

    from distancia import EDR
    
    # Initialize EDR with matching threshold
    edr = EDR(epsilon=0.5)
    
    # Calculate distance between two time series
    distance = edr.calculate(series1, series2)

Complexity Analysis
-----------------
- Time Complexity: O(nm)
- Space Complexity: O(nm)

where n and m are the lengths of the input sequences.

Selecting the Epsilon Parameter
-----------------------------
The choice of ε (epsilon) is crucial for EDR's performance:

- Too small: Becomes too sensitive to noise
- Too large: May miss important pattern differences
- Typical values: 10-25% of the standard deviation of the series
- Can be determined through cross-validation for specific applications

Conclusion
---------
Edit Distance on Real Sequences (EDR) provides a robust and intuitive approach to measuring similarity between numerical time series. Its threshold-based matching mechanism makes it particularly suitable for handling noisy data and numerical variations while maintaining the desirable properties of a metric. The integer-valued output and intuitive gap penalties make it easier to interpret compared to other time series distance measures.

EDR's effectiveness in handling noise and outliers, combined with its metric properties, makes it a valuable tool for various time series analysis tasks, especially when dealing with real-world data that contains measurement errors or natural variations.

.. note::
   The selection of an appropriate epsilon value is crucial for optimal performance. It's recommended to experiment with different threshold values based on the characteristics of your data and application requirements.

See Also
--------
- :class:`ERP`
- :class:`DTW`
- :class:`LCSS`
