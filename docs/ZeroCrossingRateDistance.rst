ZeroCrossingRateDistance
=========================

Introduction
------------
**Zero Crossing Rate (ZCR) Distance** is a metric used to compare the rate at which two signals cross the zero amplitude line. It is particularly useful for distinguishing between different types of signals, especially in audio processing, where ZCR is often used to detect changes in tone or frequency.

Sense of the Distance
---------------------
The Zero Crossing Rate measures the frequency of sign changes in a signal. The ZCR Distance compares the ZCR values of two signals to evaluate their similarity. A lower ZCR distance suggests that the signals exhibit similar rates of zero-crossing, while a higher value indicates greater differences.

Formal Representation
----------------------
The Zero Crossing Rate Distance between two signals \( x(t) \) and \( y(t) \) can be defined as:
\[
ZCR_{dist}(x, y) = | ZCR(x) - ZCR(y) |
\]
where \( ZCR(x) \) and \( ZCR(y) \) represent the zero-crossing rates of the signals \( x(t) \) and \( y(t) \), respectively. The distance is the absolute difference between these rates.

.. code-block:: python

  from distancia import ZeroCrossingRateDistance

  # Example usage:

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

  zcr_calculator = ZeroCrossingRateDistance()

  zcr_distance_value: float = zcr_calculator.compute_zcr_distance(signal1, signal2)

  print("Zero-Crossing Rate (ZCR) Distance:", zcr_distance_value)

.. code-block:: bash

>>>Zero-Crossing Rate (ZCR) Distance: 0.0006250000000000006



Academic Reference
------------------

:footcite:t:`ZeroCrossingRateDistance`

.. footbibliography::

Conclusion
----------
The **ZeroCrossingRateDistance** class provides a method for comparing the zero-crossing rates of two signals, making it a useful tool for signal classification, especially in the domain of audio processing.
