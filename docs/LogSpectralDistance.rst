LogSpectralDistance
===================

Introduction
------------
The **LogSpectralDistance (LSD)** class measures the difference between the logarithmic power spectra of two signals. It is commonly used in speech and audio processing to quantify spectral distortion in a way that aligns with human auditory perception.

Sense of the Distance
---------------------
Log Spectral Distance captures how the spectral content of two signals differs on a logarithmic scale, reflecting human sensitivity to changes in the frequency spectrum. This distance is particularly useful when comparing signals that undergo transformations or degradations, such as compression or noise addition.

Formal Representation
----------------------
The Log Spectral Distance between two signals \( x(t) \) and \( y(t) \) is defined as:
\[
LSD(x, y) = \sqrt{ \frac{1}{N} \sum_{n=1}^{N} \left( \log S_x(f_n) - \log S_y(f_n) \right)^2 }
\]
where \( S_x(f_n) \) and \( S_y(f_n) \) are the power spectral densities of signals \( x(t) \) and \( y(t) \) at frequency \( f_n \), and \( N \) is the number of frequency components.

.. code-block:: python

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 450 * t / 16000) for t in range(16000)]  # Slightly different frequency

  lsd_calculator = LogSpectralDistance(sample_rate=16000)

  lsd_value: float = lsd_calculator.compute_lsd(signal1, signal2)

  print("Log Spectral Distance:", lsd_value)

Academic Reference
------------------
Gray, A. H., & Markel, J. D. (1976). Distance measures for speech processing. *IEEE Transactions on Acoustics, Speech, and Signal Processing*, 24(5), 380-391.

Conclusion
----------
The **LogSpectralDistance** class offers a perceptually meaningful way to measure differences between the spectra of two audio or speech signals, making it an essential tool in fields like audio restoration, coding, and synthesis.
