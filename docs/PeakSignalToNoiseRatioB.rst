PeakSignalToNoiseRatio
=======================

Introduction
------------
The **Peak Signal-to-Noise Ratio** (PSNR) is a metric used to assess the quality of reconstructed signals, such as images or audio, when compared to a reference signal. It is commonly applied in lossy compression algorithms to evaluate the degree of distortion introduced.

Sense of the Distance
---------------------
PSNR measures the peak error between a reference signal and a test signal. Higher PSNR values indicate that the reconstructed signal is closer to the reference, meaning less distortion has occurred during compression or transmission.

Formal Representation
----------------------
The Peak Signal-to-Noise Ratio (PSNR) is given by:
.. math::

  PSNR = 10 \log_{10} \left( \frac{MAX_I^2}{MSE} \right)

where :math:`MAX_I`  is the maximum possible pixel value of the image, and :math:`MSE`  represents the mean squared error between the reference and the test signal.

.. code-block:: python

  from distancia import PeakSignalToNoiseRatio

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

:footcite:t:`PeakSignalToNoiseRatioB`

.. footbibliography::


Conclusion
----------
The **PeakSignalToNoiseRatio** class is crucial for evaluating the performance of image and audio compression techniques, providing a straightforward way to quantify distortion with respect to a reference signal.
