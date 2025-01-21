Fourier Transform Distance
========================

Introduction
-----------
Fourier Transform Distance (FTD) is a frequency-domain approach to measuring similarity between time series by comparing their spectral components. This distance metric transforms time series data into the frequency domain using the Discrete Fourier Transform (DFT), allowing comparison of sequences based on their frequency characteristics rather than their time-domain representations. This approach is particularly effective for detecting similarities in periodic patterns and is robust to phase shifts and noise.

Mathematical Definition
---------------------
For two time series X = (x₁, ..., xₙ) and Y = (y₁, ..., yₙ), the Fourier Transform Distance is defined as:

.. math::

   FTD(X,Y) = \sqrt{\sum_{k=0}^{N-1} |F_X(k) - F_Y(k)|^2}

where:
- :math:`F_X(k)` and :math:`F_Y(k)` are the Discrete Fourier Transforms of X and Y respectively
- :math:`N` is the number of frequency components considered
- :math:`F_X(k) = \sum_{n=0}^{N-1} x_n e^{-2\pi i kn/N}`

The DFT components are complex numbers representing:
- Magnitude: :math:`|F(k)| = \sqrt{Re(F(k))^2 + Im(F(k))^2}`
- Phase: :math:`\phi(k) = \arctan(Im(F(k))/Re(F(k)))`

Properties
---------
FTD exhibits several important characteristics:

1. **Key Properties**:
   - Frequency domain comparison
   - Phase shift invariant (when using magnitude spectrum)
   - Linear time complexity using FFT
   - Preserves Parseval's theorem
   - Handles periodic patterns effectively

2. **Advantages**:
   - Robust to noise
   - Effective for periodic data
   - Computationally efficient
   - Captures frequency components
   - Allows dimension reduction

3. **Considerations**:
   - Requires equal-length sequences
   - May need padding or truncation
   - Sensitive to sampling rate
   - Best suited for periodic patterns

Academic References
-----------------
1. Agrawal, R., Faloutsos, C., & Swami, A. (1993). "Efficient Similarity Search in Sequence Databases." Proceedings of the 4th International Conference on Foundations of Data Organization and Algorithms, 69-84.

2. Oppenheim, A. V., & Schafer, R. W. (2009). "Discrete-Time Signal Processing." Prentice Hall.

3. Rafiei, D., & Mendelzon, A. (2000). "Similarity-Based Queries for Time Series Data." Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data, 13-25.

Use Cases
--------
FTD is particularly effective in:

- Periodic pattern detection
- Signal processing applications
- Audio similarity analysis
- Vibration analysis
- Scientific data comparison
- Seasonal pattern detection
- Anomaly detection in periodic signals

Implementation Details
--------------------
In the distancia package, FTD is implemented with the following features:

- Fast Fourier Transform (FFT) algorithm
- Configurable frequency range
- Optional preprocessing steps
- Support for different distance metrics in frequency domain

Example Usage
------------
.. code-block:: python

    from distancia import FourierDistance
    
    # Initialize Fourier Distance
    ftd = FourierDistance(num_components=None)  # Use all components
    
    # Calculate distance between two time series
    distance = ftd.calculate(series1, series2)
    
    # With specific number of components
    ftd_reduced = FourierDistance(num_components=10)
    distance_reduced = ftd_reduced.calculate(series1, series2)

Complexity Analysis
-----------------
- Time Complexity: O(n log n) using FFT
- Space Complexity: O(n)

where n is the length of the input sequences.

Parameter Selection
-----------------
1. **Number of Components**:
   - Controls dimensionality reduction
   - Trade-off between accuracy and computation
   - Typically 10-20% of sequence length
   - Can be selected based on energy retention

2. **Preprocessing Options**:
   - Detrending
   - Normalization
   - Zero-padding
   - Window functions (Hamming, Hanning, etc.)

Conclusion
---------
Fourier Transform Distance provides a powerful approach to time series comparison by operating in the frequency domain. Its ability to capture periodic patterns and frequency components makes it particularly valuable for applications involving cyclic or periodic data. The use of FFT ensures computational efficiency, while the option to reduce dimensions by selecting fewer frequency components provides flexibility in handling large datasets.

The method's robustness to noise and phase shifts, combined with its efficient implementation, makes it an excellent choice for applications where frequency content is more relevant than time-domain features. However, users should consider their data's characteristics, particularly periodicity and sampling rate, when choosing this distance measure.

.. note::
   The selection of appropriate preprocessing steps and the number of frequency components is crucial for optimal performance. Consider the nature of your data and computational requirements when configuring these parameters.

See Also
--------
- :class:`WaveletDistance`
- :class:`SpectralDistance`
- :class:`AutocorrelationDistance`
