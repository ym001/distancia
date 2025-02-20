Short-Time Energy Distance: Analyzing Temporal Energy Patterns in Audio
=======================================================================

Introduction
------------

The Short-Time Energy (STE) Distance is a crucial audio signal processing technique used to quantify variations in energy patterns of sound over time. This class, part of the `distancia` Python package, provides an efficient implementation for calculating and comparing the short-time energy of audio signals, offering valuable insights into their temporal energy characteristics.

Significance of the Measure
---------------------------

STE Distance is essential for:

- Detecting voice activity in speech processing
- Distinguishing between voiced and unvoiced speech segments
- Analyzing music onset detection and beat tracking
- Identifying silence regions in audio streams
- Evaluating audio signal dynamics and loudness variations

The STE Distance helps capture the time-varying nature of audio energy, making it particularly useful for applications that require temporal analysis of sound intensity.

Formal Definition
-----------------

The Short-Time Energy for a discrete-time signal x[n] is defined as:

.. math::

   E[m] = \sum_{n=-\infty}^{\infty} (x[n]w[mR-n])^2

Where:
- E[m] is the short-time energy for the m-th frame
- w[n] is the window function
- R is the hop size between successive frames

The STE Distance between two signals can then be computed as the Euclidean distance between their STE values:

.. math::

   D_{STE} = \sqrt{\sum_{m=1}^{M} (E_1[m] - E_2[m])^2}

Where E_1[m] and E_2[m] are the STE values for the two signals being compared.

Complexity Estimation
---------------------

The time complexity of the STE Distance calculation is O(N + M), where:
- N is the total number of samples in the audio signals
- M is the number of frames

This includes:
- O(N) for computing the STE for each signal
- O(M) for calculating the Euclidean distance between STE values

The space complexity is O(M) for storing the STE values of each frame.

Usage Example
-------------

.. code-block:: python

   from distancia import ShortTimeEnergyDistance

   # Initialize with two audio signals
   signal1 = [0.1, 0.2, -0.1, 0.3, ...]  # Your first signal here
   signal2 = [0.2, 0.1, -0.2, 0.4, ...]  # Your second signal here
   ste_distance = ShortTimeEnergyDistance(frame_size=1024, hop_size=512)
   
   # Calculate the STE Distance
   distance = ste_distance.calculate(signal1, signal2)
   
   print(f"The Short-Time Energy Distance between the signals is: {distance}")

Academic Citation
-----------------

When using this implementation in academic work, please cite:

Rabiner, L. R., & Schafer, R. W. (2007). Introduction to digital speech processing. Foundations and Trends in Signal Processing, 1(1–2), 1-194.

Conclusion
----------

The Short-Time Energy Distance class in the `distancia` package offers a powerful tool for analyzing temporal energy patterns in audio signals. Its implementation provides high precision and flexibility, making it suitable for a wide range of applications from speech processing to music analysis. By quantifying the differences in energy variations between signals, STE Distance enables sophisticated analysis in fields such as voice activity detection, speech segmentation, and audio event detection.
