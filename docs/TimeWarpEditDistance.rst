Time Warp Edit Distance (TWED)
============================

Introduction
-----------
Time Warp Edit Distance (TWED) is an elastic distance metric that combines the advantages of Dynamic Time Warping (DTW) and edit distance while preserving temporal relationships between sequences. TWED introduces time stamps into the distance calculation, making it particularly suitable for time series data where the temporal aspect is crucial. Unlike traditional edit distances, TWED considers both the values and their temporal locations, providing a more accurate similarity measure for time-dependent sequences.

Mathematical Definition
---------------------
For two time series A = (A₁, ..., Aₙ) and B = (B₁, ..., Bₘ), with corresponding time stamps TA = (tA₁, ..., tAₙ) and TB = (tB₁, ..., tBₘ), TWED is defined as:

.. math::

   TWED_{\lambda,\nu}(A,B) = TWED(i,j) = \begin{cases}
   \sum_{k=1}^{i} (\Delta_A(k,0) + \nu|tA_k - tA_{k-1}|^p) & \text{if } j = 0 \\
   \sum_{k=1}^{j} (\Delta_B(k,0) + \nu|tB_k - tB_{k-1}|^p) & \text{if } i = 0 \\
   min\begin{cases}
   TWED(i-1,j-1) + d(A_i,B_j) + d(A_{i-1},B_{j-1}) + \\ 
   \nu(|tA_i - tB_j|^p + |tA_{i-1} - tB_{j-1}|^p) \\
   TWED(i-1,j) + \Delta_A(i,j) + \nu|tA_i - tA_{i-1}|^p \\
   TWED(i,j-1) + \Delta_B(i,j) + \nu|tB_j - tB_{j-1}|^p
   \end{cases} & \text{otherwise}
   \end{cases}

where:
- :math:`\lambda` is the stiffness parameter
- :math:`\nu` is the time penalty parameter
- :math:`p` is typically set to 2
- :math:`\Delta_A(i,j)` and :math:`\Delta_B(i,j)` are deletion costs
- :math:`d(A_i,B_j)` is the distance between elements

Properties
---------
TWED possesses several important properties:

1. **Metric Properties**:
   - Non-negativity
   - Symmetry
   - Triangle inequality
   - Identity of indiscernibles

2. **Advantages**:
   - Time-aware similarity measurement
   - Elastic matching capabilities
   - Robust to temporal distortions
   - Preserves temporal order

3. **Parameters Impact**:
   - λ controls the cost of deletions
   - ν adjusts the importance of temporal aspects
   - Higher ν values increase temporal penalties
   - Higher λ values make the distance more rigid

Academic References
-----------------
1. Marteau, P.-F. (2009). "Time Warp Edit Distance with Stiffness Adjustment for Time Series Matching." IEEE Transactions on Pattern Analysis and Machine Intelligence, 31(2), 306-318.

2. Marteau, P.-F. (2008). "Time Warp Edit Distance." In International Symposium on String Processing and Information Retrieval (pp. 164-175). Springer.

3. Vallance, E., Marteau, P.-F. (2016). "Fast Time Series Matching with TWED Distance: Batch and Streaming Algorithms." arXiv preprint arXiv:1606.08917.

Use Cases
--------
TWED is particularly effective in:

- Time series classification
- Pattern recognition with temporal constraints
- Gesture recognition
- Speech processing
- Financial data analysis
- Sensor data comparison
- Biomedical signal processing

Implementation Details
--------------------
In the distancia package, TWED is implemented with the following key parameters:

- `lambda_`: Stiffness parameter
- `nu`: Time penalty parameter
- `degree`: Power parameter p (default=2)
- `window`: Optional constraint on the matching window size

Example Usage
------------
.. code-block:: python

    from distancia import TWED
    
    # Initialize TWED with parameters
    twed = TWED(lambda_=1.0, nu=0.001)
    
    # Calculate distance between two time series
    distance = twed.calculate(series1, times1, series2, times2)

Complexity Analysis
-----------------
- Time Complexity: O(nm)
- Space Complexity: O(nm)

where n and m are the lengths of the input sequences.

Parameter Selection Guidelines
---------------------------
1. **Lambda (λ)**:
   - Controls deletion cost
   - Typical range: [0.001, 1.0]
   - Higher values: More rigid matching
   - Lower values: More elastic matching

2. **Nu (ν)**:
   - Controls temporal penalty
   - Typical range: [0.001, 0.1]
   - Higher values: Stronger temporal constraints
   - Lower values: More flexible temporal matching

Conclusion
---------
Time Warp Edit Distance (TWED) represents a sophisticated approach to time series comparison that effectively combines the benefits of edit distance and dynamic time warping while explicitly considering temporal aspects. Its metric properties and ability to handle both value and temporal differences make it particularly valuable for applications where time relationships are crucial.

The flexibility provided by its parameters allows TWED to be adapted to various domains and requirements, while its mathematical properties ensure consistent and reliable results. Its effectiveness in handling temporal distortions while maintaining metric properties makes it an excellent choice for time-sensitive applications.

.. note::
   Careful parameter tuning is essential for optimal performance. It's recommended to experiment with different λ and ν values based on the specific characteristics of your time series data and application requirements.

See Also
--------
- :class:`DTW`
- :class:`ERP`
- :class:`EDR`
