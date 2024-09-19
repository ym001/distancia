EnvelopeCorrelation
====================

Introduction
------------
**Envelope Correlation** is a distance metric that compares the amplitude envelopes of two signals to evaluate their similarity. This method is particularly useful when analyzing signals where amplitude modulation is a key feature, such as in audio or physiological signals.

Sense of the Distance
---------------------
Envelope Correlation assesses the global similarity between two signals by comparing their amplitude envelopes, capturing the overall energy variation over time. A higher correlation indicates greater similarity between the envelopes, while a lower correlation suggests greater divergence.

Formal Representation
----------------------
The Envelope Correlation between two signals \( x(t) \) and \( y(t) \) can be defined as:
\[
C_{env}(x, y) = \frac{\sum_{t} (E_x(t) - \bar{E_x})(E_y(t) - \bar{E_y})}{\sqrt{\sum_{t} (E_x(t) - \bar{E_x})^2} \sqrt{\sum_{t} (E_y(t) - \bar{E_y})^2}}
\]
where \( E_x(t) \) and \( E_y(t) \) are the amplitude envelopes of \( x(t) \) and \( y(t) \), and \( \bar{E_x} \) and \( \bar{E_y} \) are their respective means.

Academic Reference
------------------
Cohen, L. (1995). *Time-Frequency Analysis*. Prentice Hall.

Conclusion
----------
The **EnvelopeCorrelation** class provides a tool for comparing the amplitude envelopes of signals, making it an important metric in fields like audio analysis and biomedical signal processing.
