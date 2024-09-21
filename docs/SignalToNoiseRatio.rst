SignalToNoiseRatio
===================

Introduction
------------
The **SignalToNoiseRatio** (SNR) is a measure used to quantify the level of a signal relative to the background noise. It is a widely used metric in fields such as telecommunications, audio processing, and image analysis, to assess the quality of a signal or a system.

Sense of the Distance
---------------------
The Signal-to-Noise Ratio indicates how much stronger the signal is compared to the noise. A higher SNR means that the signal is clearer and less affected by noise, making it a crucial metric in evaluating the fidelity of a transmission or recording.

Formal Representation
----------------------
The Signal-to-Noise Ratio (SNR) is defined as:
\[
SNR = 10 \log_{10} \left( \frac{P_{signal}}{P_{noise}} \right)
\]
where \( P_{signal} \) is the power of the signal, and \( P_{noise} \) is the power of the noise. This formula expresses the ratio in decibels (dB).

.. code-block:: python


  # Example usage:

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

  max_signal_value: float = 1.0  # Maximum possible value for a normalized signal

  psnr_calculator = PeakSignalToNoiseRatio()

  psnr_value: float = psnr_calculator.compute_psnr(signal1, signal2, max_signal_value)

  print("Peak Signal-to-Noise Ratio (PSNR):", psnr_value)

.. code-block:: bash

  >>>Peak Signal-to-Noise Ratio (PSNR): 19.999999999999936


Academic Reference
------------------

:footcite:t:`SignalToNoiseRatio`

.. footbibliography::

Conclusion
----------
The **SignalToNoiseRatio** class is essential for measuring the clarity and quality of signals in various domains, offering a direct evaluation of how much noise affects the desired signal.
