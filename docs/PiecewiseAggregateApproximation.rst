Piecewise Aggregate Approximation (PAA) Distance
=============================================

Introduction
-----------
Piecewise Aggregate Approximation (PAA) Distance is a dimensionality reduction-based similarity measure for time series data. PAA first segments the time series into equal-sized intervals and represents each segment by its mean value, creating a lower-dimensional representation. This approach significantly reduces computation time and storage requirements while preserving the essential characteristics of the time series for similarity comparison.

Mathematical Definition
---------------------
For a time series X = (x₁, ..., xₙ) to be reduced to w dimensions, PAA creates a w-dimensional vector :math:`\bar{X} = (\bar{x}_1, ..., \bar{x}_w)` where:

.. math::

   \bar{x}_i = \frac{w}{n} \sum_{j=\frac{n}{w}(i-1)+1}^{\frac{n}{w}i} x_j

The PAA distance between two time series X and Y is then defined as:

.. math::

   PAA\_Distance(X,Y) = \sqrt{\frac{n}{w} \sum_{i=1}^w (\bar{x}_i - \bar{y}_i)^2}

where:
- n is the original time series length
- w is the number of segments (reduced dimension)
- :math:`\bar{x}_i` and :math:`\bar{y}_i` are the i-th PAA coefficients

Properties
---------
PAA Distance exhibits several important characteristics:

1. **Key Properties**:
   - Dimensionality reduction
   - Lower bound of Euclidean distance
   - Preserves main trends
   - Linear computational complexity
   - Distance measure between segments

2. **Advantages**:
   - Fast computation
   - Reduced storage requirements
   - Maintains essential patterns
   - Supports multi-resolution analysis
   - Efficient indexing

3. **Characteristics**:
   - Parameter-dependent (segment size)
   - Scale-sensitive
   - Temporal order preservation
   - Equal-width segments

Academic References
-----------------
1. Keogh, E., Chakrabarti, K., Pazzani, M., & Mehrotra, S. (2001). "Dimensionality Reduction for Fast Similarity Search in Large Time Series Databases." Knowledge and Information Systems, 3(3), 263-286.

2. Yi, B. K., & Faloutsos, C. (2000). "Fast Time Sequence Indexing for Arbitrary Lp Norms." Proceedings of the 26th International Conference on Very Large Data Bases, 385-394.

3. Lin, J., Keogh, E., Wei, L., & Lonardi, S. (2007). "Experiencing SAX: A Novel Symbolic Representation of Time Series." Data Mining and Knowledge Discovery, 15(2), 107-144.

Use Cases
--------
PAA Distance is particularly effective in:

- Large-scale time series databases
- Fast similarity search
- Data streaming applications
- Pattern discovery
- Time series clustering
- Real-time classification
- Approximate matching

Implementation Details
--------------------
In the distancia package, PAA Distance is implemented with the following features:

- Configurable segment size
- Multiple distance metrics
- Automatic length normalization
- Optional preprocessing steps

Example Usage
------------
.. code-block:: python

    from distancia import PAADistance
    
    # Initialize PAA with number of segments
    paa = PAADistance(segments=8)
    
    # Calculate distance between two time series
    distance = paa.calculate(series1, series2)
    
    # With different segment size
    paa_detailed = PAADistance(segments=16)
    distance_detailed = paa_detailed.calculate(series1, series2)

Complexity Analysis
-----------------
- Time Complexity: O(n)
- Space Complexity: O(w)

where n is the original sequence length and w is the number of segments.

Parameter Selection Guidelines
---------------------------
1. **Number of Segments**:
   - Trade-off between speed and accuracy
   - Typically 8-16 segments for initial testing
   - Data-dependent selection
   - Cross-validation for optimization

2. **Preprocessing Options**:
   - Z-normalization
   - Trend removal
   - Noise reduction
   - Length normalization

Conclusion
---------
Piecewise Aggregate Approximation Distance provides an efficient and effective approach to time series comparison through dimensionality reduction. Its ability to preserve essential patterns while significantly reducing computational requirements makes it particularly valuable for large-scale time series analysis and real-time applications.

The method's simplicity, combined with its theoretical guarantees as a lower bound for Euclidean distance, makes it a practical choice for many applications. While the reduced representation may lose some fine details, the trade-off between accuracy and computational efficiency is often favorable for many real-world scenarios.

.. note::
   The choice of segment size significantly impacts both performance and accuracy. It's recommended to experiment with different segment sizes based on your specific application requirements and computational constraints.

See Also
--------
- :class:`SAXDistance`
- :class:`DWTDistance`
- :class:`PLADistance`
