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

Academic Reference
------------------
Zwicker, E., & Terhardt, E. (1980). Analytical expressions for critical-band rate and critical bandwidth as a function of frequency. *The Journal of the Acoustical Society of America*, 68(5), 1523-1525.

Conclusion
----------
The **BarkSpectralDistortion** class provides an efficient method for evaluating signal differences in a way that mirrors human auditory perception, making it particularly useful in audio signal processing and evaluation tasks.
