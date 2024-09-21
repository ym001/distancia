CrossCorrelation
================

Introduction
------------
The **CrossCorrelation** class calculates the similarity between two signals by measuring their cross-correlation. Cross-correlation is a widely used tool in signal processing to compare the shape of two signals and determine how one signal may be shifted in time relative to the other.

Sense of the Distance
---------------------
Cross-correlation measures the similarity between two signals as a function of the time-lag applied to one of them. It captures how well one signal matches the other at different time shifts, making it useful for detecting time delays and phase shifts between signals.

Formal Representation
----------------------
The cross-correlation \( R_{xy}(t) \) between two signals \( x(t) \) and \( y(t) \) is defined as:
\[
R_{xy}(\tau) = \int_{-\infty}^{\infty} x(t) y(t + \tau) \, dt
\]
where \( \tau \) is the time-lag between the two signals.

In discrete form, the cross-correlation can be expressed as:
\[
R_{xy}[k] = \sum_{n} x[n] y[n+k]
\]
where \( k \) is the discrete time-lag, and \( n \) indexes the sample points of the signals.

.. code-block:: python

  from distancia import CrossCorrelation

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 880 * t / 16000) for t in range(16000)]

  cross_corr_calculator = CrossCorrelation(sample_rate=16000)

  cross_corr_value: float = cross_corr_calculator.compute_cross_correlation(signal1, signal2)

  print("Cross-correlation:", cross_corr_value)

.. code-block:: bash

  >>>Cross-correlation: 1.1540925550293483e-15


Academic Reference
------------------
:footcite:t:`CrossCorrelation`:

.. footbibliography::

Conclusion
----------
The **CrossCorrelation** class provides a method to compare signals by analyzing their similarity at different time shifts. It is especially useful in applications such as time-delay estimation, phase detection, and signal alignment in various domains, including communications and audio processing.
