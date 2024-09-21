EnergyDistance
==============

Introduction
------------
**Energy Distance** is a statistical distance used to measure the dissimilarity between two probability distributions. It is often applied in the context of comparing distributions of data or signals, where it quantifies the energy required to transform one distribution into another.

Sense of the Distance
---------------------
Energy Distance evaluates the difference between two distributions based on their energy, with a focus on both the distance between distributions and the internal spread of the distributions themselves. Smaller values indicate that the two distributions are more similar.

Formal Representation
----------------------
The Energy Distance between two distributions \( P \) and \( Q \) is formally expressed as:
\[
D_E(P, Q) = 2 \mathbb{E} \| X - Y \| - \mathbb{E} \| X - X' \| - \mathbb{E} \| Y - Y' \|
\]
where \( X \) and \( X' \) are independent samples from \( P \), and \( Y \) and \( Y' \) are independent samples from \( Q \).

.. code-block:: python

  from distancia import EnergyDistance

  # Example usage:

  signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

  energy_distance_calculator = EnergyDistance()

  energy_distance_value: float = energy_distance_calculator.compute_energy_distance(signal1, signal2)

  print("Energy Distance:", energy_distance_value)

.. code-block:: bash

  >>>Energy Distance: 9.805489753489383e-13


Academic Reference
------------------


:footcite:t:`EnergyDistance`

.. footbibliography::

Conclusion
----------
The **EnergyDistance** class provides a robust framework for comparing distributions, making it suitable for various applications in signal processing and statistical analysis, where distribution comparison is essential.
