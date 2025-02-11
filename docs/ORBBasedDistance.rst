ORB-Based Distance
==================

Introduction
-----------
The ORB-Based distance measure implements the Oriented FAST and Rotated BRIEF (ORB) algorithm to compute similarity between images. ORB was designed as a computationally efficient alternative to SIFT and SURF, particularly valuable for resource-constrained environments. This measure combines modified versions of the FAST keypoint detector and BRIEF descriptor, making it both fast and robust while being free from patent restrictions.

Understanding the Measure
------------------------
ORB operates by first detecting keypoints using FAST (Features from Accelerated Segment Test) with added orientation computation. It then describes these keypoints using a modified version of BRIEF (Binary Robust Independent Elementary Features) that takes rotation into account. The binary nature of the descriptors allows for very fast matching using Hamming distance calculations instead of Euclidean distance.

Formal Definition
---------------
Given two images I₁ and I₂, the ORB-Based distance D(I₁, I₂) is computed as follows:

1. Extract ORB keypoints and descriptors from both images:
   K₁, D₁ = ORB(I₁)
   K₂, D₂ = ORB(I₂)

2. Match binary descriptors using Hamming distance:
   M = BruteForceHamming(D₁, D₂)

3. Apply distance ratio test for match filtering:
   G = {m ∈ M | hamming_dist(m₁) / hamming_dist(m₂) < threshold}

4. Calculate final distance score:
   D(I₁, I₂) = 1 - |G| / min(|K₁|, |K₂|)

Where:
- |G| is the number of good matches
- |K₁|, |K₂| are the keypoint counts
- threshold is typically set to 0.75
- hamming_dist represents Hamming distance between binary descriptors

Application
----------
The ORB-Based distance measure is particularly effective for:
- Mobile and embedded systems
- Real-time object tracking
- Augmented reality applications
- Resource-constrained environments
- Large-scale image matching systems
- Open-source projects requiring patent-free solutions

Usage Example
------------
.. code-block:: python

    from distancia import ORBDistance
    
    # Initialize the distance measure
    orb_distance = ORBDistance()
    
    # Load two images
    image1 = load_image("path/to/image1.jpg")
    image2 = load_image("path/to/image2.jpg")
    
    # Calculate distance
    distance = orb_distance.calculate(image1, image2)
    
    # Print result
    print(f"ORB-Based distance between images: {distance}")
    # Output: ORB-Based distance between images: 0.312

Computational Complexity
----------------------
ORB provides significant computational advantages:

- FAST keypoint detection: O(n) where n is the number of pixels
- Orientation computation: O(k) where k is the number of keypoints
- BRIEF descriptor computation: O(k)
- Binary descriptor matching: O(k²) using brute force, or O(k log k) with LSH
- Overall complexity: O(n + k log k) with optimized matching

Memory complexity is O(k) for storing keypoints and binary descriptors, which are more compact than SIFT/SURF's float descriptors.

Academic Citations
----------------
When using this distance measure, please cite the following papers:

.. [1] Rublee, E., Rabaud, V., Konolige, K., & Bradski, G. (2011). ORB: An efficient alternative to SIFT or SURF.
       International Conference on Computer Vision (ICCV), 2564-2571.

.. [2] Rosten, E., & Drummond, T. (2006). Machine learning for high-speed corner detection.
       European Conference on Computer Vision (ECCV), 430-443.

.. [3] Calonder, M., Lepetit, V., Strecha, C., & Fua, P. (2010). BRIEF: Binary Robust Independent Elementary Features.
       European Conference on Computer Vision (ECCV), 778-792.

Conclusion
---------
The ORB-Based distance measure represents an excellent balance between computational efficiency and matching performance. Its binary descriptor nature and efficient computation make it particularly suitable for real-time applications and resource-constrained environments. While it may not achieve the same level of accuracy as SIFT in some scenarios, its speed, memory efficiency, and lack of patent restrictions make it an attractive choice for many practical applications. The measure is especially valuable in situations where computational resources are limited or when using proprietary algorithms is not feasible.
