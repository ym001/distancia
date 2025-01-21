Symbolic Aggregate Approximation (SAX) Distance
===========================================

Introduction
-----------
Symbolic Aggregate Approximation (SAX) Distance is an innovative approach to time series comparison that combines dimensionality reduction with symbolic representation. SAX first transforms numerical time series into discrete symbolic strings, enabling the use of string processing algorithms for time series analysis. By converting continuous values into a discrete alphabet, SAX provides both data compression and a lower bounding distance measure that supports fast similarity search.

Mathematical Definition
---------------------
The SAX transformation and distance calculation involves several steps:

1. Normalize the time series to zero mean and unit variance
2. Perform PAA (Piecewise Aggregate Approximation)
3. Convert PAA coefficients to symbols using breakpoints that produce equal-sized areas under a Gaussian curve

For two time series X and Y converted to SAX representations :math:`\hat{X}` and :math:`\hat{Y}` with alphabet size α:

.. math::

   MINDIST(\hat{X}, \hat{Y}) = \sqrt{\frac{n}{w}} \sqrt{\sum_{i=1}^w (dist({\hat{x}_i, \hat{y}_i}))^2}

where:
- n is the original time series length
- w is the number of PAA segments
- :math:`dist(a,b)` is the distance between symbols defined by the lookup table:
.. math::

   dist(a,b) = DIST\_TABLE[a,b] = \beta[max(a,b)] - \beta[min(a,b)]

- :math:`\beta` contains the Gaussian breakpoints for alphabet size α

Properties
---------
SAX Distance exhibits several important characteristics:

1. **Key Properties**:
   - Symbolic representation
   - Lower bounding guarantee
   - Dimensionality reduction
   - Alphabet size parameter
   - Distance lookup table

2. **Advantages**:
   - Fast computation
   - Space efficient
   - Supports string algorithms
   - Noise resistant
   - Index-friendly

3. **Characteristics**:
   - Parameter-dependent
   - Discrete output
   - Normalized input requirement
   - Equal-probability symbols

Academic References
-----------------
1. Lin, J., Keogh, E., Lonardi, S., & Chiu, B. (2003). "A Symbolic Representation of Time Series, with Implications for Streaming Algorithms." Proceedings of the 8th ACM SIGMOD Workshop on Research Issues in Data Mining and Knowledge Discovery, 2-11.

2. Lin, J., Keogh, E., Wei, L., & Lonardi, S. (2007). "Experiencing SAX: A Novel Symbolic Representation of Time Series." Data Mining and Knowledge Discovery, 15(2), 107-144.

3. Shieh, J., & Keogh, E. (2008). "iSAX: Indexing and Mining Terabyte Sized Time Series." Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 623-631.

Use Cases
--------
SAX Distance is particularly effective in:

- Time series indexing
- Pattern discovery
- Anomaly detection
- Motif discovery
- Discord identification
- Streaming data analysis
- Fast similarity search

Implementation Details
--------------------
In the distancia package, SAX Distance is implemented with the following features:

- Configurable alphabet size
- Adjustable word size (PAA segments)
- Pre-computed distance tables
- Z-normalization handling

Example Usage
------------
.. code-block:: python

    from distancia import SAXDistance
    
    # Initialize SAX with parameters
    sax = SAXDistance(word_size=8, alphabet_size=4)
    
    # Calculate distance between two time series
    distance = sax.calculate(series1, series2)
    
    # Get SAX representation
    sax_string = sax.transform(series1)

Complexity Analysis
-----------------
- Time Complexity: O(n) for transformation
- Space Complexity: O(w) where w is word size
- Distance Computation: O(w) using lookup table

Parameter Selection Guidelines
---------------------------
1. **Alphabet Size (α)**:
   - Typical values: 3-10
   - Trade-off: resolution vs. noise resistance
   - Domain-specific considerations

2. **Word Size (w)**:
   - Trade-off: detail vs. compression
   - Typically 8-16 segments
   - Data length dependent

Conclusion
---------
Symbolic Aggregate Approximation Distance provides a powerful framework for time series comparison by combining dimensionality reduction with symbolic representation. Its ability to support fast similarity search while maintaining a lower bounding guarantee makes it particularly valuable for large-scale time series analysis and data mining applications.

The method's efficiency in both computation and storage, combined with its support for string-based algorithms, makes it an excellent choice for applications requiring fast similarity search or pattern discovery. While the discretization process may lose some information, the trade-off between accuracy and computational efficiency is often favorable for many real-world scenarios.

.. note::
   The selection of appropriate alphabet size and word length parameters is crucial for optimal performance. Consider your specific application requirements and data characteristics when choosing these parameters.

See Also
--------
- :class:`PAADistance`
- :class:`iSAXDistance`
- :class:`SymbolicDistance`
