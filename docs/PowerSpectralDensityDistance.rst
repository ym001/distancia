PowerSpectralDensityDistance
============================

Introduction
------------
The **PowerSpectralDensityDistance** class calculates the distance between two signals based on their Power Spectral Density (PSD). PSD represents how the power of a signal is distributed over different frequency components, and comparing PSDs can reveal significant differences in frequency content between signals.

Sense of the Distance
---------------------
The Power Spectral Density (PSD) distance measures the dissimilarity between the energy distributions of two signals across frequencies. It is particularly useful in comparing signals that differ in their spectral properties, and it captures variations in the frequency domain.

Formal Representation
----------------------
The distance between two signals' Power Spectral Densities is typically calculated using metrics such as:
- Euclidean distance between the PSD vectors.
- Other possible metrics include Kullback-Leibler divergence or spectral overlap.

Let \( P_x(f) \) and \( P_y(f) \) represent the Power Spectral Densities of two signals \( x(t) \) and \( y(t) \). The distance \( D \) can be formally expressed as:
\[
D(P_x, P_y) = \sqrt{\sum_f \left( P_x(f) - P_y(f) \right)^2}
\]
where \( f \) represents the frequency components over which the PSDs are computed.

.. code-block:: python

  from distancia import PowerSpectralDensityDistance

  signal1 = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2 = [0.1 * math.sin(2 * math.pi * 880 * t / 16000) for t in range(16000)]

  psd_calculator = PowerSpectralDensityDistance(sample_rate=16000)

  psd_distance = psd_calculator.compute_psd_distance(signal1, signal2)

  print("PSD Distance:", psd_distance)

.. code-block:: bash

  >>>[(1.5+0j), (0.2381966011250105+0.1902113032590307j), (0.2999999999999998+0j), (0.36180339887498947-0.1902113032590307j), 0]
PSD Distance: 513514.8559149296
Academic Reference
------------------

:footcite:t:`PowerSpectralDensityDistance`

.. footbibliography::

Conclusion
----------
The **PowerSpectralDensityDistance** class provides a robust mechanism for comparing the frequency content of two signals. By focusing on how power is distributed across frequencies, it allows for meaningful comparisons in applications such as signal classification, sound analysis, and noise detection.
