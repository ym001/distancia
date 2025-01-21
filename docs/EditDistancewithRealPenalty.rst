Edit Distance with Real Penalty (ERP)
===================================

Introduction
-----------
Edit Distance with Real Penalty (ERP) is a distance metric designed for measuring similarity between numerical time series. It combines the robustness of edit distance with the ability to handle real-valued sequences. ERP addresses limitations of other metrics by using a constant reference value (gap) when computing the cost of element mismatches, making it particularly effective for sequences with different lengths and numerical values.

Mathematical Definition
---------------------
For two time series X = (x₁, ..., xₙ) and Y = (y₁, ..., yₘ), and a constant gap value g, ERP is defined recursively as:

.. math::

   ERP(X, Y) = ERP(i, j) = \begin{cases}
   \sum_{k=1}^{i} |x_k - g| & \text{if } j = 0 \\
   \sum_{k=1}^{j} |y_k - g| & \text{if } i = 0 \\
   min\begin{cases}
   ERP(i-1, j-1) + |x_i - y_j| \\
   ERP(i-1, j) + |x_i - g| \\
   ERP(i, j-1) + |y_j - g|
   \end{cases} & \text{otherwise}
   \end{cases}

where:
- :math:`|x_i - y_j|` is the distance between elements
- :math:`|x_i - g|` and :math:`|y_j - g|` are the penalties for gaps
- :math:`g` is the gap value (typically 0 or the mean of the series)

Properties
---------
ERP possesses several important properties:

1. **Metric Properties**:
   - Non-negativity
   - Symmetry
   - Triangle inequality
   - Identity of indiscernibles

2. **Advantages**:
   - Handles sequences of different lengths
   - Supports real-valued elements
   - Less sensitive to noise than Euclidean distance
   - More robust than DTW in some scenarios

3. **Characteristics**:
   - Parameter-dependent (gap value)
   - Translation-invariant when using appropriate gap value
   - Handles local time shifting

Academic References
-----------------
1. Chen, L., & Ng, R. (2004). "On the marriage of Lp-norms and edit distance." Proceedings of the 30th International Conference on Very Large Data Bases, 792-803.

2. Chen, L., Özsu, M. T., & Oria, V. (2005). "Robust and fast similarity search for moving object trajectories." Proceedings of the 2005 ACM SIGMOD International Conference on Management of Data, 491-502.

3. Wang, X., Mueen, A., Ding, H., Trajcevski, G., Scheuermann, P., & Keogh, E. (2013). "Experimental comparison of representation methods and distance measures for time series data." Data Mining and Knowledge Discovery, 26(2), 275-309.

Use Cases
--------
ERP is particularly effective in:

- Financial time series analysis
- Trajectory matching
- Sensor data comparison
- Pattern recognition in noisy environments
- Sequence alignment with numerical values
- Time series classification

Implementation Details
--------------------
In the distancia package, ERP is implemented with the following key parameters:

- `gap_value`: The reference value for computing penalties
- `window`: Optional constraint on the matching window size
- `normalize`: Boolean flag for result normalization

Example Usage
------------
.. code-block:: python

    from distancia import ERP
    
    # Initialize ERP with gap value
    erp = ERP(gap_value=0)
    
    # Calculate distance between two time series
    distance = erp.calculate(series1, series2)

Complexity Analysis
-----------------
- Time Complexity: O(nm)
- Space Complexity: O(nm)

where n and m are the lengths of the input sequences.

Conclusion
---------
Edit Distance with Real Penalty (ERP) represents a powerful metric for time series comparison that combines the benefits of edit distance with the ability to handle numerical values. Its metric properties and robustness make it particularly suitable for applications requiring accurate similarity measurement between sequences of different lengths or with noise. The gap parameter provides flexibility in adapting the metric to specific domain requirements, while maintaining the mathematical properties necessary for various data mining tasks.

.. note::
   The choice of gap value can significantly impact the results. It's recommended to experiment with different values (such as 0 or the mean of the series) to find the most appropriate for your specific use case.

See Also
--------
- :class:`EditDistance`
- :class:`DTW`
- :class:`LCSS`
