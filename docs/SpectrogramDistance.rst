SpectrogramDistance
====================

Introduction
------------
**Spectrogram Distance** is a distance metric designed to compare the time-frequency representations (spectrograms) of two audio signals. A spectrogram displays the signal's frequency spectrum as it varies with time, making it a useful representation for analyzing sound, particularly in speech and music applications.

Sense of the Distance
---------------------
The Spectrogram Distance measures the dissimilarity between two signals by comparing their spectrograms. This metric is particularly useful for detecting differences in frequency content over time, making it applicable to tasks such as audio comparison, noise analysis, and speech recognition.

Formal Representation
----------------------
The Spectrogram Distance between two signals \( x(t) \) and \( y(t) \) can be defined as:
\[
Spec_{dist}(x, y) = \| Spectrogram(x) - Spectrogram(y) \|_p
\]
where \( Spectrogram(x) \) and \( Spectrogram(y) \) represent the spectrograms of the signals \( x(t) \) and \( y(t) \), respectively, and \( \| \cdot \|_p \) is a suitable distance metric (e.g., L2 norm) applied to the spectrogram matrices.

.. code-block:: python

  # Example usage:

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

  spectrogram_calculator = SpectrogramDistance(window_size=256, overlap=128)

  distance_value: float = spectrogram_calculator.compute_spectrogram_distance(signal1, signal2)

  print("Spectrogram Distance:", distance_value)

.. code-block:: bash

Academic Reference
------------------


:footcite:t:`SpectrogramDistance`

.. footbibliography::

Conclusion
----------
The **SpectrogramDistance** class provides a method for comparing the spectrogram representations of two audio signals, offering insights into how their frequency content varies over time. It is especially useful for audio analysis, music processing, and other signal processing tasks.
