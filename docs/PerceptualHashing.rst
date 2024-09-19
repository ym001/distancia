Perceptual Hashing (pHash)
===========================

Introduction
------------
Perceptual Hashing (pHash) is a technique used to generate a compact and unique hash for an image based on its visual characteristics. Unlike cryptographic hashes, pHash focuses on creating hashes that reflect the perceptual differences between images, making it suitable for image comparison tasks.

Sense of the Distance
---------------------
The perceptual hash is calculated in such a way that visually similar images will have small differences in their hashes. To measure the similarity between two images, the Hamming distance between their respective perceptual hashes is computed. A small Hamming distance indicates a high degree of visual similarity, whereas a larger Hamming distance suggests greater dissimilarity.

Formal Definition
-----------------
Given two images, the perceptual hashes of these images are generated using Discrete Cosine Transform (DCT) on the grayscale, resized version of the images. The binary hash is created by comparing each pixel's DCT coefficient with the mean DCT value, resulting in a hash string.

The Hamming distance is calculated as:

.. math::

    D_{Hamming}(H_1, H_2) = \sum_{i=1}^{n} (H_1[i] \neq H_2[i])

Where:

- :math:`H_1` and :math:`H_2` are the perceptual hashes of the two images.
- :math:`n` is the length of the hash string.
- :math:`D_{Hamming}` is the Hamming distance between the two hashes.

Academic Reference
------------------

:footcite:t:`PerceptualHashing`

.. footbibliography::


Conclusion
----------
Perceptual Hashing (pHash) is an effective method for comparing images based on their visual content. By calculating the Hamming distance between the hashes of two images, one can measure their perceptual similarity. This technique is particularly useful in identifying near-duplicate images and detecting minor variations between images.
