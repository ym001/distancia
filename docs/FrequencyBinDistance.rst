Frequency Bin Distance: Precise Spectral Comparison of Audio Signals
====================================================================

Introduction
------------

The Frequency Bin Distance is a powerful audio signal processing technique used to compare specific frequency components between two audio spectra. This class, part of the `distancia` Python package, provides an efficient implementation for calculating the distance between corresponding frequency bins of audio signals, offering detailed insights into their spectral differences.

Significance of the Measure
---------------------------

Frequency Bin Distance is crucial for:

- Detecting subtle spectral differences between audio signals
- Analyzing harmonic content in music and speech
- Identifying specific frequency changes in audio processing
- Enhancing audio fingerprinting and music information retrieval
- Improving audio quality assessment in signal processing applications

This measure allows for a fine-grained comparison of spectral content, making it particularly useful for applications requiring precise frequency analysis.

Formal Definition
-----------------

The Frequency Bin Distance between two audio spectra X and Y is defined as:

.. math::

   D_{FB} = \sqrt{\sum_{k=1}^{N} (|X[k]| - |Y[k]|)^2}

Where:
- X[k] and Y[k] are the magnitudes of the k-th frequency bin for spectra X and Y respectively
- N is the number of frequency bins being compared

Each frequency bin represents a specific frequency range, calculated as:

.. math::

   f_k = k \cdot \frac{f_s}{N_{FFT}}

Where:
- f_k is the center frequency of the k-th bin
- f_s is the sampling frequency
- N_FFT is the FFT size

Complexity Estimation
---------------------

The time complexity of the Frequency Bin Distance calculation is O(N), where N is the number of frequency bins being compared. This includes:

- O(N log N) for the Fast Fourier Transform (FFT) of each signal (performed once per signal)
- O(N) for the bin-wise distance calculation

The space complexity is O(N) for storing the spectral data and intermediate results.

Usage Example
-------------

.. code-block:: python

   from distancia import FrequencyBinDistance

   # Initialize with two audio signals
   signal1 = [0.1, 0.2, -0.1, 0.3, ...]  # Your first signal here
   signal2 = [0.2, 0.1, -0.2, 0.4, ...]  # Your second signal here
   fbd = FrequencyBinDistance(fft_size=2048, sample_rate=44100)
   
   # Calculate the Frequency Bin Distance
   distance = fbd.calculate(signal1, signal2, start_bin=10, end_bin=100)
   
   print(f"The Frequency Bin Distance between bins 10-100 is: {distance}")

Academic Citation
-----------------

When using this implementation in academic work, please cite:

Müller, M., Ellis, D. P., Klapuri, A., & Richard, G. (2011). Signal processing for music analysis. IEEE Journal of Selected Topics in Signal Processing, 5(6), 1088-1110.

Conclusion
----------

The Frequency Bin Distance class in the `distancia` package offers a precise tool for comparing spectral content of audio signals. Its implementation provides high accuracy and flexibility, making it suitable for a wide range of applications from music analysis to audio forensics. By quantifying the differences in specific frequency ranges between signals, Frequency Bin Distance enables sophisticated spectral analysis, enhancing capabilities in fields such as audio similarity measurement, sound classification, and audio quality assessment[1][5].
