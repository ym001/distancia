Spectral Flux: Measuring Spectral Changes in Audio Signals
==========================================================

Introduction
------------

Spectral Flux is a crucial audio signal processing technique used to quantify the rate of change in the power spectrum of an audio signal over time. This class, part of the `distancia` Python package, provides an efficient implementation for calculating spectral flux between consecutive audio frames.

Significance of the Measure
---------------------------

Spectral flux is essential for:

- Detecting onsets in music and speech signals
- Analyzing timbral changes in audio
- Distinguishing between different types of audio content (e.g., music vs. speech)
- Segmenting audio streams based on spectral variations

Formal Definition
-----------------

Spectral flux is typically calculated as the L2-norm (Euclidean distance) between two normalized consecutive power spectra:

.. math::

   SF(t) = \sqrt{\sum_{k=1}^{N} (|X_t(k)| - |X_{t-1}(k)|)^2}

Where:
- X_t(k) is the k-th frequency bin of the power spectrum at frame t
- N is the number of frequency bins

Some implementations use the L1-norm or only consider positive changes in energy for onset detection[1].

Complexity Estimation
---------------------

The time complexity of the Spectral Flux calculation is O(N), where N is the number of frequency bins in the spectrum. This makes it an efficient measure for real-time audio processing and large-scale music information retrieval tasks.

Usage Example
-------------

.. code-block:: python

   from distancia import SpectralFlux

   # Initialize with audio frames
   sf = SpectralFlux(frame_size=2048, hop_size=512)
   
   # Calculate spectral flux for consecutive frames
   flux = sf.calculate(audio_frames)
   
   print(f"The Spectral Flux values: {flux}")

Academic Citation
-----------------

When using this implementation in academic work, please cite:

Dixon, S. (2006). Onset detection revisited. In Proceedings of the 9th International Conference on Digital Audio Effects (Vol. 120, pp. 133-137).

Conclusion
----------

The Spectral Flux class in the `distancia` package offers a powerful tool for analyzing spectral changes in audio signals. Its efficient implementation and versatility make it invaluable for various audio processing applications, from music onset detection to audio segmentation and classification tasks.

