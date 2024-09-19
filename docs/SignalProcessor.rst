SignalProcessor
===============

Introduction
------------
The **SignalProcessor** class is a general-purpose tool for processing and analyzing audio signals. It provides functionalities for calculating distances and similarities between signals using various metrics. The class is designed to handle different types of audio data and facilitate comparison between them, making it useful for applications in sound processing, speech recognition, and audio analysis.

Sense of the Distance
---------------------
The distances computed by the **SignalProcessor** class measure the similarity or dissimilarity between two audio signals. Depending on the metric used, this distance can reflect differences in amplitude, frequency content, phase, or other characteristics of the signals. These distances provide a quantitative measure of how closely related or distinct two signals are in the given context.

Formal Representation
----------------------
The **SignalProcessor** class supports several formal distance measures, including but not limited to:
- Time-domain distances, such as Euclidean or Manhattan distances.
- Frequency-domain distances, such as spectral convergence, MFCC distance, and phase difference.
- Perceptual distances, including PESQ and Mel-Cepstral Distance.

Each distance metric is mathematically defined in its respective context, allowing for versatile comparison depending on the specific attributes of the signals being analyzed.

Academic Reference
------------------
Allen, J. B., & Rabiner, L. R. (1977). A unified approach to short-time Fourier analysis and synthesis. **Proceedings of the IEEE, 65**(11), 1558-1564. doi:10.1109/PROC.1977.10771

Conclusion
----------
The **SignalProcessor** class provides a comprehensive framework for comparing audio signals using a variety of distance measures. By offering a flexible and extensible set of tools, it is capable of handling a wide range of applications in audio analysis, speech recognition, and sound classification.
