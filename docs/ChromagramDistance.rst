ChromagramDistance
===================

Introduction
------------
**Chromagram Distance** is a metric designed to compare the chromagram representations of two audio signals. The chromagram is a time-frequency representation that captures the energy distribution of a signal in terms of its pitch classes. It is widely used in music-related tasks due to its alignment with musical concepts like harmony and melody.

Sense of the Distance
---------------------
Chromagram Distance measures the dissimilarity between two signals by comparing their chromagram representations. It is particularly useful in musical signal analysis, where the perception of pitch and harmony plays a crucial role in identifying the similarity between two signals.

Formal Representation
----------------------
The Chromagram Distance between two signals \( x(t) \) and \( y(t) \) can be mathematically expressed as:
\[
Chroma_{dist}(x, y) = \| Chromagram(x) - Chromagram(y) \|_p
\]
where \( Chromagram(x) \) and \( Chromagram(y) \) represent the chromagram transformations of the signals \( x(t) \) and \( y(t) \), respectively, and \( \| \cdot \|_p \) is a suitable distance measure (e.g., L2 norm) applied to the chromagram matrices.

.. code-block:: python

  # Example usage:

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

  chromagram_calculator = ChromagramDistance(num_bins=12)

  distance_value: float = chromagram_calculator.compute_chromagram_distance(signal1, signal2)

  print("Chromagram Distance:", distance_value)

.. code-block:: bash

Academic Reference
------------------

:footcite:t:`ChromagramDistance`:  
  
.. footbibliography::

Conclusion
----------
The **ChromagramDistance** class offers a valuable tool for measuring similarity between two audio signals, particularly in the context of musical applications where pitch and harmonic structures are essential.
