StructuralSimilarityIndex
=========================

Introduction
------------
The Structural Similarity Index (SSIM) is a perceptual metric used for measuring the similarity between two images. Unlike other pixel-based comparison metrics, SSIM considers changes in structural information, luminance, and contrast to assess image quality. It is widely used in image processing tasks, especially for image compression and quality assessment.

Sense of the Distance
---------------------
The SSIM distance measures the perceptual difference between two images. It considers the structural information of an image, which is a more meaningful way to assess similarity, as opposed to simply comparing pixel values. The distance is a value between -1 and 1, where a value of 1 indicates identical images, and a lower value indicates perceptual differences.

Formal Definition
-----------------
The SSIM between two images \(I_1\) and \(I_2\) is calculated as follows:

.. math::

   SSIM(I_1, I_2) = \frac{(2 \mu_1 \mu_2 + C_1)(2 \sigma_{12} + C_2)}{(\mu_1^2 + \mu_2^2 + C_1)(\sigma_1^2 + \sigma_2^2 + C_2)}

Where:

- \( \mu_1 \) and \( \mu_2 \) are the mean pixel values of images \(I_1\) and \(I_2\),
- \( \sigma_1^2 \) and \( \sigma_2^2 \) are the variances of the images,
- \( \sigma_{12} \) is the covariance between the two images,
- \( C_1 = (k_1 \cdot L)^2 \) and \( C_2 = (k_2 \cdot L)^2 \) are constants used to avoid division by zero, where \(L\) is the dynamic range of pixel values (e.g., 255 for 8-bit grayscale images), and \(k_1, k_2\) are small constants.

Academic Reference
------------------
:footcite:t:`StructuralSimilarityIndex`

.. footbibliography::

Conclusion
----------
The Structural Similarity Index (SSIM) provides a robust metric for comparing images based on their perceptual quality. It is widely recognized in the field of image processing for its effectiveness in capturing image similarity beyond mere pixel-based differences. SSIM is particularly valuable in applications such as image compression, denoising, and image quality assessment.
