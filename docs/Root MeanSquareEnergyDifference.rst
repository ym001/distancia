Root Mean Square (RMS) Energy Difference
========================================

Introduction
------------

The **Root Mean Square (RMS) Energy Difference** is a fundamental measure used to compare the overall energy levels between two audio signals. This measure provides a simple yet effective way to quantify the difference in loudness or intensity between audio samples, making it particularly useful in various audio processing and analysis tasks.

Purpose and Applications
------------------------

The RMS Energy Difference serves several key purposes in audio signal processing:

1. **Loudness Comparison**: Evaluating the relative loudness between two audio signals or segments.
2. **Audio Normalization**: Determining the scaling factor needed to match the energy levels of different audio files.
3. **Voice Activity Detection**: Distinguishing between speech and silence in audio recordings.
4. **Audio Quality Assessment**: Providing a basic measure of difference in audio quality or degradation.

Theoretical Background
----------------------

The RMS energy of an audio signal is a measure of its average power over time. It is calculated by taking the square root of the mean of the squared amplitude values of the signal. The RMS energy difference between two signals is then computed as the absolute difference between their respective RMS energies.

Formal Definition
-----------------

Given two discrete-time audio signals :math:`x[n]` and :math:`y[n]`, each of length :math:`N`, the RMS Energy Difference is defined as:

.. math::

   RMS\_Diff(x, y) = \left|\sqrt{\frac{1}{N}\sum_{n=0}^{N-1} x[n]^2} - \sqrt{\frac{1}{N}\sum_{n=0}^{N-1} y[n]^2}\right|

Where:
- :math:`x[n]` and :math:`y[n]` are the amplitude values of the two audio signals at sample :math:`n`.
- :math:`N` is the total number of samples in each signal.

  

Academic References
-------------------

1. Recommendation ITU-R BS.1770-4 (2015). Algorithms to measure audio programme loudness and true-peak audio level. International Telecommunication Union.

2. Skovenborg, E., & Nielsen, S. H. (2004). Evaluation of different loudness models with music and speech material. In Audio Engineering Society Convention 117. Audio Engineering Society.

3. Glasberg, B. R., & Moore, B. C. (2002). A model of loudness applicable to time-varying sounds. Journal of the Audio Engineering Society, 50(5), 331-342.

4. Soulodre, G. A. (2004). Evaluation of objective loudness meters. In Audio Engineering Society Convention 116. Audio Engineering Society.

Conclusion
----------

The Root Mean Square (RMS) Energy Difference measure, as implemented in the `distancia` package, provides a straightforward and efficient method for comparing the overall energy levels between audio signals. While simple in concept, this measure finds wide application in various audio processing tasks, from basic loudness comparison to more complex audio analysis scenarios.

Its computational efficiency and direct relationship to perceived loudness make it a valuable tool for researchers and developers working in audio signal processing, music information retrieval, and related fields. However, it's important to note that while RMS energy difference provides useful insights into overall signal intensity, it does not account for psychoacoustic factors or frequency-dependent loudness perception.

For more comprehensive loudness comparisons, especially in professional audio applications, this measure can be complemented with more advanced psychoacoustic models. Nonetheless, the RMS Energy Difference remains a fundamental and widely used metric in the audio processing toolkit, offering a quick and reliable way to assess energy-level differences between audio signals.
