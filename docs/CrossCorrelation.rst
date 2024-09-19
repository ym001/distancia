CrossCorrelation
================

Introduction
------------
The **CrossCorrelation** class calculates the similarity between two signals by measuring their cross-correlation. Cross-correlation is a widely used tool in signal processing to compare the shape of two signals and determine how one signal may be shifted in time relative to the other.

Sense of the Distance
---------------------
Cross-correlation measures the similarity between two signals as a function of the time-lag applied to one of them. It captures how well one signal matches the other at different time shifts, making it useful for detecting time delays and phase shifts between signals.

Formal Representation
----------------------
The cross-correlation \( R_{xy}(t) \) between two signals \( x(t) \) and \( y(t) \) is defined as:
\[
R_{xy}(\tau) = \int_{-\infty}^{\infty} x(t) y(t + \tau) \, dt
\]
where \( \tau \) is the time-lag between the two signals.

In discrete form, the cross-correlation can be expressed as:
\[
R_{xy}[k] = \sum_{n} x[n] y[n+k]
\]
where \( k \) is the discrete time-lag, and \( n \) indexes the sample points of the signals.

Academic Reference
------------------
Oppenheim, A. V., & Schafer, R. W. (2009). Discrete-Time Signal Processing. **Prentice Hall.**

Conclusion
----------
The **CrossCorrelation** class provides a method to compare signals by analyzing their similarity at different time shifts. It is especially useful in applications such as time-delay estimation, phase detection, and signal alignment in various domains, including communications and audio processing.
