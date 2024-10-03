====================================
Image-Based Distances in Distancia
====================================

Introduction
============

The **distancia** package offers a comprehensive set of methods for comparing images using various distance metrics. These image-based distances can be used for tasks such as image retrieval, similarity searches, clustering, and object recognition. Each method provides a unique way to quantify the similarity or difference between images, whether based on pixel values, histograms, or more complex structural and feature-based approaches.

In this document, we categorize the image distance metrics available in **distancia** and provide brief descriptions of each method.

Categories of Image-Based Distances
===================================

Pixel-Based Distances
=====================
  
  1. :doc:`Euclidean`  
   
  Measures the straight-line distance between two images by treating them as high-dimensional vectors of pixel values. It is useful for comparing images with similar alignment and size.

  2. :doc:`Manhattan`

   Also known as the "taxicab" distance, this metric sums the absolute differences of the pixel values between two images. It's robust to small variations in pixel values.

  3. **Chebyshev Distance**  
   Measures the greatest difference between pixel values of two images across any dimension. It emphasizes the maximum change in intensity rather than the overall sum of changes.

  4. **Minkowski Distance**  
   A generalization of both Euclidean and Manhattan distances, it offers flexibility by allowing different levels of emphasis on small or large differences between pixel values.

Histogram-Based Distances
=========================

1. **Histogram Intersection**  
   Compares two images by computing the intersection of their color histograms. This method focuses on how many pixel colors overlap between the two images.

2. **Chi-Square Distance**  
   A distance metric commonly used to compare image histograms by measuring the difference between the distributions of pixel intensities in two images.

3. **Bhattacharyya Distance**  
   Measures the similarity between two image histograms by calculating the overlap between their probability distributions. It is often used in object recognition tasks.

4. **Kullback-Leibler Divergence**  
   A measure of how one probability distribution (histogram) differs from another, capturing the amount of information lost when one histogram is used to approximate another.

Feature-Based Distances
=======================

1. **SIFT-Based Distance**  
   Uses the Scale-Invariant Feature Transform (SIFT) algorithm to detect and compare keypoints and descriptors in two images, providing robustness to scale, rotation, and translation differences.

2. **SURF-Based Distance**  
   Similar to SIFT but faster, SURF (Speeded Up Robust Features) is used to extract and compare distinctive points between two images, particularly useful for object recognition tasks.

3. **ORB-Based Distance**  
   ORB (Oriented FAST and Rotated BRIEF) is an efficient alternative to SIFT and SURF, focusing on matching image keypoints and descriptors. It is fast and well-suited for real-time applications.

Structural and Transform-Based Distances
========================================

1. **Structural Similarity Index (SSIM)**  
   Measures the structural similarity between two images, focusing on luminance, contrast, and structure. It provides a perceptually meaningful comparison.

2. **Fourier Transform Distance**  
   Compares images in the frequency domain using their Fourier transforms. This distance is particularly useful for comparing images based on global patterns and periodic structures.

3. **Wavelet Transform Distance**  
   Measures the difference between two images after decomposing them into their wavelet components. Wavelet-based methods are effective for capturing local image details at multiple scales.

Deep Learning-Based Distances
=============================

1. **VGG16-Based Distance**  
   Uses the VGG16 deep convolutional neural network to extract high-level features from images and computes the distance between these feature representations. Suitable for high-level content comparison.

2. **Inception-Based Distance**  
   Employs the Inception architecture to extract feature vectors from images and compares them using a chosen distance metric. It is effective for capturing complex features in images.

3. **ResNet-Based Distance**  
   Utilizes the ResNet architecture to compare the deep features of images, enabling robust comparison of complex, high-dimensional image representations.

Compression-Based Distances
===========================

1. **Normalized Compression Distance (NCD)**  
   Measures the similarity between two images by comparing the compression of the images concatenated together with their individual compressions. It captures the redundancy and shared information between images.

2. **Zlib-Based Distance**  
   A variant of compression-based distance that uses the zlib algorithm to compare images based on their compressibility, reflecting how much the structure of two images is alike.

Conclusion
==========

The **distancia** package provides a broad selection of image distance metrics, allowing for flexible and tailored comparison of images based on a variety of features—ranging from pixel intensities to deep learning representations. Whether you are working on object recognition, image retrieval, or similarity detection, **distancia** offers the right tools to measure distance in ways that match your specific requirements.

For detailed information on the implementation and usage of each distance, refer to the specific documentation for each metric.
