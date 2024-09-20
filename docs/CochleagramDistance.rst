CochleagramDistance
====================

Introduction
------------
**Cochleagram Distance** is a metric designed to compare the cochleagram representations of two audio signals. The cochleagram is based on the functioning of the human cochlea and represents how sound is processed by the auditory system. This distance measure is particularly useful for applications where human perception of sound plays a critical role.

Sense of the Distance
---------------------
Cochleagram Distance quantifies the dissimilarity between two signals by comparing their cochleagram representations, which capture the frequency and temporal aspects of sound as perceived by the human auditory system.

Formal Representation
----------------------
The Cochleagram Distance between two signals \( x(t) \) and \( y(t) \) can be mathematically represented as:
\[
Cochlea_{dist}(x, y) = \| Cochleagram(x) - Cochleagram(y) \|_p
\]
where \( Cochleagram(x) \) and \( Cochleagram(y) \) represent the cochleagram transformations of the signals \( x(t) \) and \( y(t) \), respectively, and \( \| \cdot \|_p \) denotes an appropriate distance measure (such as the L2 norm) applied to the cochleagram representations.

.. code-block:: python

# Example usage:

signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

cochleagram_calculator = CochleagramDistance(num_bands=40)

distance_value: float = cochleagram_calculator.compute_cochleagram_distance(signal1, signal2)

print("Cochleagram Distance:", distance_value)

.. code-block:: bash

  >>>Cochleagram Distance: 0.000833203125000008


Academic Reference
------------------
Wang, D., & Brown, G. J. (2006). *Computational auditory scene analysis: Principles, algorithms, and applications*. IEEE Press.

Conclusion
----------
The **CochleagramDistance** class provides a perceptually relevant distance measure by comparing the cochleagram representations of two audio signals, making it suitable for tasks where human auditory perception is central.
