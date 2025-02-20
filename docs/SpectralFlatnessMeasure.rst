Spectral Flatness Measure (SFM): Evaluating Audio Signal Tonality
=================================================================

Introduction
------------

The Spectral Flatness Measure (SFM) is a crucial audio signal processing technique used to quantify the tonality of sound signals. This class, part of the `distancia` Python package, provides an efficient implementation for calculating the SFM of audio signals, offering valuable insights into their spectral characteristics.

Significance of the Measure
---------------------------

SFM is essential for:

- Distinguishing between tonal and noisy audio signals
- Analyzing the harmonic content of music and speech
- Audio compression applications
- Sound classification and music information retrieval

The SFM of a noisy signal tends towards 1, while for a pure tone signal, it approaches 0[8].

Formal Definition
-----------------

SFM is defined as the ratio of the geometric mean to the arithmetic mean of the power spectral density components:

.. math::

   SFM = \frac{N \times \sqrt[N]{\prod_{i=1}^N y_i}}{\sum_{i=1}^N y_i}

Where:
- y_i is the relative amplitude of the i-th frequency
- N is the number of frequencies[9]

Complexity Estimation
---------------------

The time complexity of the SFM calculation is O(N), where N is the number of frequency bins in the spectrum. This makes it an efficient measure for real-time audio processing and large-scale music information retrieval tasks.

Usage Example
-------------

.. code-block:: python

   from distancia import SpectralFlatnessMeasure

   # Initialize with an audio signal
   sfm = SpectralFlatnessMeasure(audio_signal, sample_rate=44100)
   
   # Calculate the SFM
   flatness = sfm.calculate()
   
   print(f"The Spectral Flatness Measure is: {flatness}")

Academic Citation
-----------------

When using this implementation in academic work, please cite:

Johnston, J. D. (1988). Transform coding of audio signals using perceptual noise criteria. IEEE Journal on selected areas in communications, 6(2), 314-323.

Conclusion
----------

The Spectral Flatness Measure class in the `distancia` package offers a powerful tool for analyzing the tonality of audio signals. Its efficient implementation and strong correlation with perceptual characteristics make it invaluable for various audio processing applications, from music analysis to speech processing and audio compression.
