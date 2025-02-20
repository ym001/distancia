Spectral Flatness Measure (SFM): Quantifying Audio Signal Tonality
==================================================================

Introduction
------------

The Spectral Flatness Measure (SFM), also known as Wiener entropy, is a sophisticated audio signal processing metric that quantifies the tonal quality of sound signals. This implementation, part of the `distancia` Python package, offers a high-precision tool for calculating the SFM, providing crucial insights into the spectral distribution and tonal characteristics of audio signals.

Significance of the Measure
---------------------------

SFM is pivotal in audio signal analysis for:

- Differentiating between tonal (harmonic) and noisy (stochastic) audio components
- Assessing the degree of "peakiness" vs. "flatness" in audio spectra
- Enhancing audio codec efficiency in perceptual audio coding
- Facilitating automatic genre classification in music information retrieval
- Improving voice activity detection in speech processing systems

The SFM ranges from 0 to 1, where values close to 0 indicate a tonal signal (e.g., a sine wave), and values approaching 1 suggest a noise-like signal (e.g., white noise).

Formal Definition
-----------------

The SFM is mathematically defined as the ratio of the geometric mean to the arithmetic mean of the power spectral density components:

.. math::

   SFM = \frac{\exp(\frac{1}{N}\sum_{i=1}^N \ln(X[i]))}{\frac{1}{N}\sum_{i=1}^N X[i]}

Where:
- X[i] is the magnitude of bin number i of the power spectrum
- N is the number of frequency bins

This formula can be expressed in decibels:

.. math::

   SFM_{dB} = 10 \log_{10}(SFM)

Complexity Estimation
---------------------

The time complexity of the SFM calculation is O(N log N), where N is the number of samples in the audio frame. This includes:

- O(N log N) for the Fast Fourier Transform (FFT)
- O(N) for the geometric and arithmetic mean calculations

The space complexity is O(N) for storing the spectrum and intermediate results.

Usage Example
-------------

.. code-block:: python

   from distancia import SpectralFlatnessMeasure

   # Initialize with an audio signal (assuming mono, 44.1kHz sampling rate)
   audio_signal = [0.1, 0.2, -0.1, 0.3, ...]  # Your audio samples here
   sfm = SpectralFlatnessMeasure(frame_size=2048, hop_size=512)
   
   # Calculate the SFM for each frame
   sfm_values = sfm.calculate(audio_signal)
   
   print(f"SFM values across frames: {sfm_values}")
   print(f"Average SFM: {sum(sfm_values) / len(sfm_values)}")

Academic Citation
-----------------

When utilizing this implementation in academic work, please cite:

Dubnov, S. (2004). Generalization of spectral flatness measure for non-Gaussian linear processes. IEEE Signal Processing Letters, 11(8), 698-701.

Conclusion
----------

The Spectral Flatness Measure class in the `distancia` package provides a robust and efficient tool for analyzing the tonal characteristics of audio signals. Its implementation offers high precision and scalability, making it suitable for a wide range of applications from real-time audio processing to large-scale music information retrieval tasks. By quantifying the degree of tonality in audio signals, SFM enables more sophisticated audio analysis, enhancing capabilities in audio compression, music classification, and speech processing domains.
