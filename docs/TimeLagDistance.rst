TimeLagDistance
===============

Introduction
------------
The **TimeLagDistance** class calculates the optimal time lag between two signals to determine the best alignment. Time lag distance is often used in signal processing to find the temporal offset between two time-series signals, which maximizes their similarity or correlation.

Sense of the Distance
---------------------
Time lag distance measures the temporal shift between two signals that produces the highest correlation or the least amount of difference. It is useful in applications where signals may be time-shifted versions of each other, and identifying the correct lag is necessary for proper comparison or synchronization.

Formal Representation
----------------------
The time lag distance \( \tau_{opt} \) is defined as the value of \( \tau \) that maximizes the cross-correlation between two signals \( x(t) \) and \( y(t) \):
\[
\tau_{opt} = \arg \max_{\tau} \int_{-\infty}^{\infty} x(t) y(t + \tau) \, dt
\]
In a discrete form, this can be written as:
\[
\tau_{opt} = \arg \max_{k} \sum_{n} x[n] y[n + k]
\]
where \( \tau_{opt} \) represents the time shift that yields the highest similarity between the signals.

.. code-block:: python

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 440 * (t - 100) / 16000) for t in range(16000)]  # signal2 is shifted

  time_lag_calculator = TimeLagDistance(sample_rate=16000)

  best_lag: int = time_lag_calculator.compute_time_lag_distance(signal1, signal2, max_lag=500)

  print("Optimal time lag:", best_lag)

.. code-block:: bash

  >>>Optimal time lag: 9


Academic Reference
------------------

:footcite:t:`TimeLagDistance`

.. footbibliography::

Conclusion
----------
The **TimeLagDistance** class provides a useful tool for analyzing and aligning time-shifted signals. It is particularly helpful in fields like audio processing, speech recognition, and communications, where understanding the time delay between signals is crucial for proper analysis and synchronization.
