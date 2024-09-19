PeakSignalToNoiseRatio
=======================

Introduction
------------
The **Peak Signal-to-Noise Ratio** (PSNR) is a metric used to assess the quality of reconstructed signals, such as images or audio, when compared to a reference signal. It is commonly applied in lossy compression algorithms to evaluate the degree of distortion introduced.

Sense of the Distance
---------------------
PSNR measures the peak error between a reference signal and a test signal. Higher PSNR values indicate that the reconstructed signal is closer to the reference, meaning less distortion has occurred during compression or transmission.

Formal Representation
----------------------
The Peak Signal-to-Noise Ratio (PSNR) is given by:
\[
PSNR = 10 \log_{10} \left( \frac{MAX_I^2}{MSE} \right)
\]
where \( MAX_I \) is the maximum possible pixel value of the image, and \( MSE \) represents the mean squared error between the reference and the test signal.

Academic Reference
------------------
Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). *Image quality assessment: From error visibility to structural similarity*. IEEE Transactions on Image Processing.

Conclusion
----------
The **PeakSignalToNoiseRatio** class is crucial for evaluating the performance of image and audio compression techniques, providing a straightforward way to quantify distortion with respect to a reference signal.
