BarkSpectralDistortion
======================

Introduction
------------
The **BarkSpectralDistortion (BSD)** class is based on the Bark scale, which approximates human auditory perception of frequency. It measures the distortion between two signals by comparing their frequency content within critical bands defined by the Bark scale.

Sense of the Distance
---------------------
Bark Spectral Distortion quantifies how similar or different two signals are in terms of their perceived frequency content, taking into account the non-linear way in which humans perceive sound frequencies. It is commonly used in audio coding, compression, and quality assessment.

Formal Representation
----------------------
The Bark Spectral Distortion between two signals \( x(t) \) and \( y(t) \) can be represented as:
\[
BSD(x, y) = \sum_{b=1}^{B} \left( S_x(b) - S_y(b) \right)^2
\]
where \( S_x(b) \) and \( S_y(b) \) are the power spectral densities of signals \( x(t) \) and \( y(t) \) in the Bark frequency band \( b \), and \( B \) is the total number of Bark bands.

.. code-block:: python


  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

  bsd_calculator = BarkSpectralDistortion(sample_rate=16000)

  bsd_value: float = bsd_calculator.compute_bsd(signal1, signal2)

  print("Bark Spectral Distortion:", bsd_value)

.. code-block:: bash

  >>>Bark Spectral Distortion: 14.65614015181136


Academic Reference
------------------


:footcite:t:`BarkSpectralDistortion`:

.. footbibliography::

Conclusion
----------
The **BarkSpectralDistortion** class provides an efficient method for evaluating signal differences in a way that mirrors human auditory perception, making it particularly useful in audio signal processing and evaluation tasks.
