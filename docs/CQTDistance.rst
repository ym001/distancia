CQTDistance
===========

Introduction
------------
**Constant-Q Transform (CQT) Distance** is a distance metric designed to compare the Constant-Q Transform representations of two audio signals. The CQT is commonly used in musical signal analysis due to its ability to provide a logarithmic frequency resolution, which corresponds more closely to human auditory perception, especially in the context of harmonic content.

Sense of the Distance
---------------------
The CQT Distance measures the dissimilarity between two signals by comparing their CQT representations. This distance is particularly useful for musical and harmonic content comparison, as it emphasizes differences in pitch and harmonic structure, making it ideal for applications in music information retrieval and audio classification.

Formal Representation
----------------------
The CQT Distance between two signals \( x(t) \) and \( y(t) \) can be defined as:
\[
CQT_{dist}(x, y) = \| CQT(x) - CQT(y) \|_p
\]
where \( CQT(x) \) and \( CQT(y) \) represent the Constant-Q Transform of the signals \( x(t) \) and \( y(t) \), respectively, and \( \| \cdot \|_p \) is a suitable distance metric (e.g., L2 norm) applied to the CQT matrices.

.. code-block:: python


  # Example usage:

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

  cqt_calculator = CQTDistance(num_bins=24, window_size=512)

  distance_value: float = cqt_calculator.compute_cqt_distance(signal1, signal2)

  print("CQT Distance:", distance_value)

.. code-block:: bash

Academic Reference
------------------
Brown, J. C. (1991). *Calculation of a constant Q spectral transform*. The Journal of the Acoustical Society of America, 89(1), 425-434.

Conclusion
----------
The **CQTDistance** class provides a method for comparing the Constant-Q Transform representations of two audio signals, making it especially valuable in tasks that involve musical and harmonic content analysis. It is well-suited for applications in music processing and other audio signal processing domains.
