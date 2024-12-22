=====================
Image-Based Distances
=====================

Introduction
============

The **distancia** package offers a comprehensive set of methods for comparing images using various distance metrics. These image-based distances can be used for tasks such as image retrieval, similarity searches, clustering, and object recognition. Each method provides a unique way to quantify the similarity or difference between images, whether based on pixel values, histograms, or more complex structural and feature-based approaches.

In this document, we categorize the image distance metrics available in **distancia** and provide brief descriptions of each method.

List of Image-Based Distances
===================================

Pixel-Based Distances
=====================

Pixel-based distances compare images directly at the pixel level, treating each image as a high-dimensional vector of intensity values. These methods are sensitive to alignment, noise, and small pixel differences, making them useful for basic image comparison when images are nearly identical in size and content.

  
#. `Euclidean`_  : Measures the straight-line distance between two images by treating them as high-dimensional vectors of pixel values. It is useful for comparing images with similar alignment and size.
#. `Manhattan`_ : Also known as the "taxicab" distance, this metric sums the absolute differences of the pixel values between two images. It's robust to small variations in pixel values.
#. `Chebyshev`_ : Measures the greatest difference between pixel values of two images across any dimension. It emphasizes the maximum change in intensity rather than the overall sum of changes.
#. `Minkowski`_ : A generalization of both Euclidean and Manhattan distances, it offers flexibility by allowing different levels of emphasis on small or large differences between pixel values.
#. `ChiSquareDistance`_

Histogram-Based Distances
=========================

Histogram-based distances focus on comparing the distribution of color or pixel intensities between two images. Instead of comparing pixel-to-pixel, these methods compare the frequency distribution of pixel values, making them robust to small shifts or variations in image content.


6. `HistogramIntersection`_ : Compares two images by computing the intersection of their color histograms. This method focuses on how many pixel colors overlap between the two images.
#. `Bhattacharyya`_ : Measures the similarity between two image histograms by calculating the overlap between their probability distributions. It is often used in object recognition tasks.
#. `KullbackLeibler`_ : A measure of how one probability distribution (histogram) differs from another, capturing the amount of information lost when one histogram is used to approximate another.

Feature-Based Distances
=======================

Feature-based distances extract key points or descriptors from images and compare them instead of pixel values. These methods, such as SIFT or ORB, are robust to transformations like scaling, rotation, or translation, making them ideal for object recognition and image matching tasks.


9. `SIFT-Based`_ : Uses the Scale-Invariant Feature Transform (SIFT) algorithm to detect and compare keypoints and descriptors in two images, providing robustness to scale, rotation, and translation differences.
#. `SURF-Based`_ : Similar to SIFT but faster, SURF (Speeded Up Robust Features) is used to extract and compare distinctive points between two images, particularly useful for object recognition tasks.
#. `ORB-Based`_ : ORB (Oriented FAST and Rotated BRIEF) is an efficient alternative to SIFT and SURF, focusing on matching image keypoints and descriptors. It is fast and well-suited for real-time applications.
#. `PeakSignalToNoiseRatio`_
#. `FeatureBasedDistance`_

Structural and Transform-Based Distances
========================================

These distances analyze the overall structure of images or operate in the frequency domain by transforming the image. Metrics like SSIM or Fourier Transform Distance provide a higher-level comparison that reflects structural or periodic patterns, often used in image quality assessment.

14. `StructuralSimilarityIndex`_ : Measures the structural similarity between two images, focusing on luminance, contrast, and structure. It provides a perceptually meaningful comparison.
#. `FourierTransform`_ : Compares images in the frequency domain using their Fourier transforms. This distance is particularly useful for comparing images based on global patterns and periodic structures.
#. `WaveletTransform`_ : Measures the difference between two images after decomposing them into their wavelet components. Wavelet-based methods are effective for capturing local image details at multiple scales.

Deep Learning-Based Distances
=============================

Deep learning-based distances rely on pre-trained convolutional neural networks (CNNs) to extract high-level feature vectors from images. These methods are highly effective for capturing complex, abstract representations of images and are widely used for tasks like image retrieval or content-based comparison.

17. `VGG16-Based`_ : Uses the VGG16 deep convolutional neural network to extract high-level features from images and computes the distance between these feature representations. Suitable for high-level content comparison.
#. `Inception-Based`_ : Employs the Inception architecture to extract feature vectors from images and compares them using a chosen distance metric. It is effective for capturing complex features in images.
#. `ResNet-Based`_ : Utilizes the ResNet architecture to compare the deep features of images, enabling robust comparison of complex, high-dimensional image representations.
#. `EarthMoversDistance`_

Compression-Based Distances
===========================

Compression-based distances measure the similarity between two images based on their compressibility, reflecting the shared information and structure. Methods like Normalized Compression Distance (NCD) evaluate how efficiently two images can be compressed together, capturing redundancy in their data.

21. `NormalizedCompression`_ : Measures the similarity between two images by comparing the compression of the images concatenated together with their individual compressions. It captures the redundancy and shared information between images.
#. `ZlibBasedDistance`_ : A variant of compression-based distance that uses the zlib algorithm to compare images based on their compressibility, reflecting how much the structure of two images is alike.
#. `PerceptualHashing`_
#. `NormalizedCrossCorrelation`_

Conclusion
==========

The **distancia** package provides a broad selection of image distance metrics, allowing for flexible and tailored comparison of images based on a variety of features—ranging from pixel intensities to deep learning representations. Whether you are working on object recognition, image retrieval, or similarity detection, **distancia** offers the right tools to measure distance in ways that match your specific requirements.

For detailed information on the implementation and usage of each distance, refer to the specific documentation for each metric.


.. _Image: https://distancia.readthedocs.io/en/latest/imageDistance.html
.. _StructuralSimilarityIndex: https://distancia.readthedocs.io/en/latest/StructuralSimilarityIndex.html
.. _PeakSignalToNoiseRatio: https://distancia.readthedocs.io/en/latest/PeakSignalToNoiseRatio.html
.. _HistogramIntersection: https://distancia.readthedocs.io/en/latest/HistogramIntersection.html
.. _EarthMoversDistance: https://distancia.readthedocs.io/en/latest/EarthMoversDistance.html
.. _ChiSquareDistance: https://distancia.readthedocs.io/en/latest/ChiSquareDistance.html
.. _FeatureBasedDistance: https://distancia.readthedocs.io/en/latest/FeatureBasedDistance.html
.. _PerceptualHashing: https://distancia.readthedocs.io/en/latest/PerceptualHashing.html
.. _NormalizedCrossCorrelation: https://distancia.readthedocs.io/en/latest/NormalizedCrossCorrelation.html

.. _Euclidean: https://distancia.readthedocs.io/en/latest/Euclidean.html
.. _Minkowski: https://distancia.readthedocs.io/en/latest/Minkowski.html
.. _Chebyshev: https://distancia.readthedocs.io/en/latest/Chebyshev.html
.. _Manhattan: https://distancia.readthedocs.io/en/latest/Manhattan.html
.. _ChiSquareDistance: https://distancia.readthedocs.io/en/latest/ChiSquareDistance.html
.. _KullbackLeibler: https://distancia.readthedocs.io/en/latest/KullbackLeibler.html
.. _Bhattacharyya: https://distancia.readthedocs.io/en/latest/Bhattacharyya.html
.. _NormalizedCompression: https://distancia.readthedocs.io/en/latest/NormalizedCompression.html
.. _ZlibBasedDistance: https://distancia.readthedocs.io/en/latest/ZlibBasedDistance.html
