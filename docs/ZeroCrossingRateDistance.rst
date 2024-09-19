ZeroCrossingRateDistance
=========================

Introduction
------------
**Zero Crossing Rate (ZCR) Distance** is a metric used to compare the rate at which two signals cross the zero amplitude line. It is particularly useful for distinguishing between different types of signals, especially in audio processing, where ZCR is often used to detect changes in tone or frequency.

Sense of the Distance
---------------------
The Zero Crossing Rate measures the frequency of sign changes in a signal. The ZCR Distance compares the ZCR values of two signals to evaluate their similarity. A lower ZCR distance suggests that the signals exhibit similar rates of zero-crossing, while a higher value indicates greater differences.

Formal Representation
----------------------
The Zero Crossing Rate Distance between two signals \( x(t) \) and \( y(t) \) can be defined as:
\[
ZCR_{dist}(x, y) = | ZCR(x) - ZCR(y) |
\]
where \( ZCR(x) \) and \( ZCR(y) \) represent the zero-crossing rates of the signals \( x(t) \) and \( y(t) \), respectively. The distance is the absolute difference between these rates.

Academic Reference
------------------
Peeters, G., & Rodet, X. (2002). *Automatic classification of large musical instrument databases using hierarchical classifiers with inertia ratio maximization*. Proceedings of the Audio Engineering Society.

Conclusion
----------
The **ZeroCrossingRateDistance** class provides a method for comparing the zero-crossing rates of two signals, making it a useful tool for signal classification, especially in the domain of audio processing.
