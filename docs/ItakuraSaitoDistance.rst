ItakuraSaitoDistance
=====================

Introduction
------------
The **ItakuraSaitoDistance** is a measure commonly used in speech processing and audio signal analysis. It is particularly useful for comparing two probability distributions, often in the context of power spectral densities, as it measures how one distribution can be used to efficiently approximate another.

Sense of the Distance
---------------------
The Itakura-Saito distance evaluates the similarity between two signals by focusing on the shape of their spectral representations. It is asymmetric and is sensitive to small differences in power spectra, making it highly relevant for tasks like speech recognition, audio coding, and signal reconstruction.

Formal Representation
----------------------
The Itakura-Saito distance between two signals \( P_x(f) \) and \( P_y(f) \) is given by:
\[
D_{IS}(P_x || P_y) = \int \left( \frac{P_x(f)}{P_y(f)} - \log \frac{P_x(f)}{P_y(f)} - 1 \right) df
\]
where \( P_x(f) \) and \( P_y(f) \) represent the power spectral densities of the two signals, and \( f \) denotes the frequency.

.. code-block:: python

  # Example usage:

  from distancia import ItakuraSaitoDistance

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

  isd_calculator = ItakuraSaitoDistance()

  isd_value: float = isd_calculator.compute_is_distance(signal1, signal2)

  print("Itakura-Saito Distance:", isd_value)

.. code-block:: bash

  >>>Itakura-Saito Distance: 6386946.368221848


Academic Reference
------------------


:footcite:t:`ItakuraSaitoDistance`

.. footbibliography::

Conclusion
----------
The **ItakuraSaitoDistance** class provides a specialized metric for evaluating the differences between signals' spectral representations, making it highly effective for tasks in speech recognition, audio analysis, and signal processing.
