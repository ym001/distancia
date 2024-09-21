EnvelopeCorrelation
====================

Introduction
------------
**Envelope Correlation** is a distance metric that compares the amplitude envelopes of two signals to evaluate their similarity. This method is particularly useful when analyzing signals where amplitude modulation is a key feature, such as in audio or physiological signals.

Sense of the Distance
---------------------
Envelope Correlation assesses the global similarity between two signals by comparing their amplitude envelopes, capturing the overall energy variation over time. A higher correlation indicates greater similarity between the envelopes, while a lower correlation suggests greater divergence.

Formal Representation
----------------------
The Envelope Correlation between two signals \( x(t) \) and \( y(t) \) can be defined as:
\[
C_{env}(x, y) = \frac{\sum_{t} (E_x(t) - \bar{E_x})(E_y(t) - \bar{E_y})}{\sqrt{\sum_{t} (E_x(t) - \bar{E_x})^2} \sqrt{\sum_{t} (E_y(t) - \bar{E_y})^2}}
\]
where \( E_x(t) \) and \( E_y(t) \) are the amplitude envelopes of \( x(t) \) and \( y(t) \), and \( \bar{E_x} \) and \( \bar{E_y} \) are their respective means.

.. code-block:: python

  from distancia import EnvelopeCorrelation

  # Example usage:

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

  envelope_correlation_calculator = EnvelopeCorrelation()

  correlation_value: float = envelope_correlation_calculator.compute_envelope_correlation(signal1, signal2)

  print("Envelope Correlation:", correlation_value)

.. code-block:: bash

>>>Envelope Correlation: 0.0006076026733088895


Academic Reference
------------------

:footcite:t:`EnvelopeCorrelation`

.. footbibliography::

Conclusion
----------
The **EnvelopeCorrelation** class provides a tool for comparing the amplitude envelopes of signals, making it an important metric in fields like audio analysis and biomedical signal processing.
