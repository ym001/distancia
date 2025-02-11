SURF-Based Distance
==================

Introduction
-----------
The SURF-Based distance measure implements the Speeded Up Robust Features (SURF) algorithm to compute similarity between images. As an evolution of SIFT, SURF was designed to be computationally more efficient while maintaining robust feature detection and matching capabilities. This measure is particularly effective for real-time applications where computational speed is crucial without significantly compromising accuracy.

Understanding the Measure
------------------------
SURF accelerates feature detection and description through the use of integral images and box filters, approximating Gaussian derivatives. The algorithm identifies blob-like features in the image and describes them using a distribution of Haar-like responses. This approach leads to faster computation compared to SIFT while maintaining comparable robustness to image transformations such as scaling and rotation.

Formal Definition
---------------
Given two images I₁ and I₂, the SURF-Based distance D(I₁, I₂) is computed through the following steps:

1. Extract SURF keypoints and descriptors from both images:
   K₁, D₁ = SURF(I₁)
   K₂, D₂ = SURF(I₂)

2. Match descriptors using Fast Approximate Nearest Neighbors:
   M = FLANN(D₁, D₂)

3. Apply distance ratio test for match filtering:
   G = {m ∈ M | dist(m₁) / dist(m₂) < threshold}

4. Calculate normalized distance score:
   D(I₁, I₂) = 1 - |G| / min(|K₁|, |K₂|)

Where:
- |G| represents the number of good matches
- |K₁|, |K₂| are the keypoint counts in each image
- threshold is typically set to 0.7

Application
----------
The SURF-Based distance measure is particularly suitable for:
- Real-time object detection systems
- High-speed image matching
- Mobile applications
- Augmented reality systems
- Large-scale image retrieval

Usage Example
------------
.. code-block:: python

    from distancia import SURFDistance
    
    # Initialize the distance measure
    surf_distance = SURFDistance()
    
    # Load two images
    image1 = load_image("path/to/image1.jpg")
    image2 = load_image("path/to/image2.jpg")
    
    # Calculate distance
    distance = surf_distance.calculate(image1, image2)
    
    # Print result
    print(f"SURF-Based distance between images: {distance}")
    # Output: SURF-Based distance between images: 0.285

Computational Complexity
----------------------
The SURF algorithm offers improved computational efficiency compared to SIFT:

- Feature detection: O(n) where n is the number of pixels, due to integral image usage
- Descriptor computation: O(k) where k is the number of keypoints
- Descriptor matching: O(k log k)
- Overall complexity: O(n + k log k)

Memory complexity is O(n) for the integral image and O(k) for storing keypoints and descriptors.

Academic Citations
----------------
When using this distance measure, please cite the following papers:

.. [1] Bay, H., Tuytelaars, T., & Van Gool, L. (2006). SURF: Speeded Up Robust Features. 
       European Conference on Computer Vision (ECCV), 404-417.

.. [2] Bay, H., Ess, A., Tuytelaars, T., & Van Gool, L. (2008). Speeded-Up Robust Features (SURF).
       Computer Vision and Image Understanding, 110(3), 346-359.

Conclusion
---------
The SURF-Based distance measure provides an efficient alternative to SIFT while maintaining robust image matching capabilities. Its primary advantage lies in its computational efficiency, making it particularly suitable for applications where speed is critical. While it may occasionally be slightly less accurate than SIFT for some specific cases, the performance gain often makes it the preferred choice for real-time applications and large-scale image processing tasks.
