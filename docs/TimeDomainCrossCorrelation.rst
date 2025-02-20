Time Domain Cross-Correlation: Temporal Signal Alignment Analysis
=================================================================

Introduction
------------

Time Domain Cross-Correlation (TDCC) is a fundamental signal processing technique used to measure the similarity between two signals as a function of time lag. The TDCC class in the `distancia` Python package provides an efficient implementation for calculating the cross-correlation between two time-domain signals, offering valuable insights into their temporal alignment and similarity.

Significance of the Measure
---------------------------

TDCC is essential for:

- Detecting time delays between similar signals
- Identifying echoes or reflections in audio signals
- Pattern recognition in time series data
- Voice activity detection in speech processing
- Synchronizing signals in multi-sensor systems

TDCC is particularly useful in applications such as radar systems, speech recognition, and image processing where temporal alignment is crucial[1].

Formal Definition
-----------------

The Time Domain Cross-Correlation function for discrete-time signals x[n] and y[n] is defined as:

.. math::

   R_{xy}[k] = \sum_{n=k}^{N-1} x[n] \cdot y[n - k]

Where:
- R_xy[k] is the cross-correlation function
- k is the time lag
- N is the number of samples in the signals

The time lag that maximizes R_xy[k] indicates the optimal alignment between the two signals[2].

Complexity Estimation
---------------------

The time complexity of the TDCC calculation is O(N^2) for signals of length N when computed directly in the time domain. However, for large datasets, a frequency-domain implementation using Fast Fourier Transform (FFT) can reduce the complexity to O(N log N)[2][3].

The space complexity is O(N) for storing the input signals and the resulting cross-correlation function.

Usage Example
-------------

.. code-block:: python

   from distancia import TimeDomainCrossCorrelation

   # Initialize with two audio signals
   signal1 = [0.1, 0.2, -0.1, 0.3, ...]  # Your first signal here
   signal2 = [0.2, 0.1, -0.2, 0.4, ...]  # Your second signal here
   tdcc = TimeDomainCrossCorrelation()
   
   # Calculate the cross-correlation
   correlation = tdcc.calculate(signal1, signal2)
   
   # Find the time lag with maximum correlation
   max_lag = tdcc.find_max_correlation_lag(correlation)
   
   print(f"Maximum correlation occurs at lag: {max_lag}")

Academic Citation
-----------------

When using this implementation in academic work, please cite:

Knapp, C., & Carter, G. (1976). The generalized correlation method for estimation of time delay. IEEE Transactions on Acoustics, Speech, and Signal Processing, 24(4), 320-327.

Conclusion
----------

The Time Domain Cross-Correlation class in the `distancia` package offers a powerful tool for analyzing temporal relationships between signals. Its implementation provides high precision and flexibility, making it suitable for a wide range of applications from audio processing to radar systems. By quantifying the similarity and time delay between signals, TDCC enables sophisticated analysis in fields such as speech recognition, echo detection, and multi-sensor data alignment.
