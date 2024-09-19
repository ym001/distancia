PhaseDifferenceCalculator
=========================

Introduction
------------
The **PhaseDifferenceCalculator** class computes the phase difference between two signals. Phase difference is a key concept in signal processing, especially when analyzing the relationship between periodic signals or signals in the frequency domain.

Sense of the Distance
---------------------
The phase difference measures the relative shift in phase between two signals at a given frequency or across multiple frequencies. It captures the alignment of the signals in terms of their periodic oscillations, and can be used to understand how signals are out of sync or phase-shifted.

Formal Representation
----------------------
Given two signals \( x(t) \) and \( y(t) \), their phase difference \( \Delta\phi(f) \) at a frequency \( f \) can be represented as:
\[
\Delta\phi(f) = \phi_y(f) - \phi_x(f)
\]
where \( \phi_x(f) \) and \( \phi_y(f) \) represent the phase angles of the respective signals at frequency \( f \).

The phase difference is typically calculated after transforming the signals into the frequency domain, often using the Fourier transform. The result is expressed in radians or degrees.

.. code-block:: python

  # Paramètres
  sample_rate: int = 44100  # Hz
  window_size: int = 1024   # échantillons
  hop_size: int = 512       # échantillons

  # Créer une instance du calculateur
  calculator: PhaseDifferenceCalculator = PhaseDifferenceCalculator(sample_rate, window_size, hop_size)

  # Supposons que nous ayons deux signaux signal1 et signal2
  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 880 * t / 16000) for t in range(16000)]

  # Analyser les signaux
  phase_differences: List[float]
  time_axis: List[float]
  phase_differences, time_axis = calculator.analyze_signals(signal1, signal2)

  # Afficher les résultats
  print("Différences de phase:", phase_differences[:10])  # Affiche les 10 premières valeurs
  print("Axe temporel:", time_axis[:10])  # Affiche les 10 premières valeurs

Academic Reference
------------------
Bracewell, R. N. (1999). The Fourier Transform and Its Applications. **McGraw-Hill.**

Conclusion
----------
The **PhaseDifferenceCalculator** class allows for a precise analysis of phase shifts between two signals. This tool is particularly useful in fields such as telecommunications, audio processing, and any domain where understanding the timing relationship between periodic signals is important.
