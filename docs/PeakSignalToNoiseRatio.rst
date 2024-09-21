PeakSignalToNoiseRatio
======================

Introduction
------------
The Peak Signal-to-Noise Ratio (PSNR) is a widely used metric to measure the quality of a reconstructed or compressed image in comparison to the original. It expresses the ratio between the maximum possible power of a signal and the power of noise that affects its representation.

Sense of the Distance
---------------------
PSNR measures the fidelity of the reconstructed image by comparing it to the original. A higher PSNR value indicates better image quality, while a lower PSNR value suggests a higher level of distortion or noise introduced during compression or transmission.

Formal Definition
-----------------
The PSNR between two images \( I_1 \) and \( I_2 \) is defined as:

.. math::

   PSNR(I_1, I_2) = 10 \cdot \log_{10} \left( \frac{MAX^2}{MSE} \right)

Where:
- \( MAX \) is the maximum possible pixel value of the image (e.g., 255 for 8-bit grayscale images),
- \( MSE \) is the Mean Squared Error between the two images, given by:

.. math::

   MSE = \frac{1}{N} \sum_{i=1}^{N} (I_1[i] - I_2[i])^2

Here \( N \) is the total number of pixels, and \( I_1[i] \), \( I_2[i] \) are the pixel values of the two images at position \( i \).

Academic Reference
------------------

:footcite:t:`PeakSignalToNoiseRatio`

.. footbibliography::

Conclusion
----------
The Peak Signal-to-Noise Ratio (PSNR) is a simple yet effective method for quantifying image quality, especially in the context of lossy image compression. It is widely used in image processing and multimedia applications, offering an easily interpretable measure of distortion.
