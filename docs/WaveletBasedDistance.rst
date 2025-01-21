Wavelet-Based Distance
====================

Introduction
-----------
Wavelet-Based Distance (WBD) is an advanced similarity measure that combines both temporal and frequency domain analysis through wavelet decomposition. Unlike Fourier-based methods that only capture frequency information, wavelets provide multi-resolution analysis, allowing the comparison of time series at different scales and locations. This approach is particularly effective for non-stationary signals and time series with localized features.

Mathematical Definition
---------------------
For two time series X = (x₁, ..., xₙ) and Y = (y₁, ..., yₙ), the Wavelet-Based Distance is defined as:

.. math::

   WBD(X,Y) = \sqrt{\sum_{j=1}^J \sum_{k=1}^{K_j} w_j(D^X_{j,k} - D^Y_{j,k})^2 + w_J(A^X_J - A^Y_J)^2}

where:
- :math:`D^X_{j,k}, D^Y_{j,k}` are the detail coefficients at level j and position k
- :math:`A^X_J, A^Y_J` are the approximation coefficients at the final level J
- :math:`w_j` are level-dependent weights
- :math:`J` is the maximum decomposition level
- :math:`K_j` is the number of coefficients at level j

The wavelet decomposition is computed as:
.. math::

   D_{j,k} = \sum_{n} x[n]\psi_{j,k}[n]
   A_{J,k} = \sum_{n} x[n]\phi_{J,k}[n]

where:
- :math:`\psi_{j,k}[n]` is the wavelet function
- :math:`\phi_{J,k}[n]` is the scaling function

Properties
---------
WBD exhibits several important characteristics:

1. **Key Properties**:
   - Multi-resolution analysis
   - Time-frequency localization
   - Scale-dependent comparison
   - Energy preservation
   - Non-negativity

2. **Advantages**:
   - Captures local and global patterns
   - Handles non-stationary signals
   - Robust to noise
   - Efficient computation
   - Flexible resolution levels

3. **Characteristics**:
   - Hierarchical decomposition
   - Scale-specific comparisons
   - Customizable wavelet bases
   - Adaptable to signal characteristics

Academic References
-----------------
1. Mallat, S. (2008). "A Wavelet Tour of Signal Processing: The Sparse Way." Academic Press.

2. Chan, K. P., & Fu, A. W. C. (1999). "Efficient Time Series Matching by Wavelets." Proceedings of the 15th International Conference on Data Engineering, 126-133.

3. Percival, D. B., & Walden, A. T. (2000). "Wavelet Methods for Time Series Analysis." Cambridge University Press.

Use Cases
--------
WBD is particularly effective in:

- Financial time series analysis
- Biomedical signal processing
- Seismic data analysis
- Image similarity measurement
- Signal compression
- Pattern recognition
- Anomaly detection

Implementation Details
--------------------
In the distancia package, WBD is implemented with the following features:

- Multiple wavelet family support
- Configurable decomposition levels
- Custom weighting schemes
- Various distance metrics for coefficient comparison

Example Usage
------------
.. code-block:: python

    from distancia import WaveletDistance
    
    # Initialize with specific wavelet and level
    wbd = WaveletDistance(wavelet='db4', level=3)
    
    # Calculate distance between two time series
    distance = wbd.calculate(series1, series2)
    
    # With custom weights
    weights = {1: 1.0, 2: 0.7, 3: 0.5}  # Level-specific weights
    distance_weighted = wbd.calculate(series1, series2, weights=weights)

Complexity Analysis
-----------------
- Time Complexity: O(n)
- Space Complexity: O(n)

where n is the length of the input sequences.

Parameter Selection Guidelines
---------------------------
1. **Wavelet Family**:
   - Daubechies (db1-db20): General purpose
   - Haar (db1): Discontinuous signals
   - Symlets: Symmetrical wavelets
   - Coiflets: Better approximation properties

2. **Decomposition Level**:
   - Typically log₂(n) or fewer levels
   - Consider signal length
   - Balance detail vs. computation

3. **Weighting Schemes**:
   - Equal weights
   - Level-dependent weights
   - Energy-based weights
   - Application-specific schemes

Conclusion
---------
Wavelet-Based Distance provides a sophisticated approach to time series comparison by leveraging the power of wavelet transforms. Its ability to capture both temporal and frequency information at multiple scales makes it particularly valuable for analyzing complex, non-stationary signals. The method's flexibility in choosing wavelet bases and decomposition levels allows it to be adapted to various types of time series data and application requirements.

The combination of multi-resolution analysis with efficient computation makes WBD a powerful tool for modern time series analysis. Its effectiveness in handling non-stationary signals and localized features, while maintaining computational efficiency, makes it an excellent choice for applications requiring detailed signal comparison at multiple scales.

.. note::
   The choice of wavelet family, decomposition level, and weighting scheme can significantly impact results. It's recommended to experiment with different parameters based on your specific data characteristics and application requirements.

See Also
--------
- :class:`FourierDistance`
- :class:`MultiresolutionDistance`
- :class:`SpectralDistance`
