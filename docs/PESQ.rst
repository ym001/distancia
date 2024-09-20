PESQ
====

Introduction
------------
The **PESQ (Perceptual Evaluation of Speech Quality)** class measures the quality of speech signals by comparing a degraded signal to a reference signal. This objective method is widely used in telecommunications to assess the impact of network impairments on voice quality.

Sense of the Distance
---------------------
PESQ is a perceptual model that quantifies the perceived difference between two speech signals by simulating how the human ear evaluates voice quality. The closer the PESQ score is to the maximum value, the more similar the degraded signal is to the original reference signal.

Formal Representation
----------------------
PESQ evaluates the perceptual difference between a reference signal \( s_{ref}(t) \) and a degraded signal \( s_{deg}(t) \), based on a model of auditory perception. The PESQ score is computed as:
\[
PESQ(s_{ref}, s_{deg}) = \text{PESQ model output}
\]
where the score typically ranges from -0.5 to 4.5, with higher scores indicating better perceived quality.

.. code-block:: python

  reference_signal: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
  degraded_signal: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) + 0.01 * math.sin(2 * math.pi * 1000 * t / 16000) for t in range(16000)]

  pesq_calculator = PESQ(sample_rate=16000)

  pesq_score: float = pesq_calculator.compute_pesq(reference_signal, degraded_signal)

  print("PESQ Score:", pesq_score)

.. code-block:: bash

  >>>PESQ Score: 4.492250820344904


Academic Reference
------------------

:footcite:t:`PESQ`

.. footbibliography::

Conclusion
----------
The **PESQ** class provides a standardized method for evaluating the perceptual quality of speech signals, making it an essential tool in the evaluation of voice codecs, telecommunication systems, and network performance.
