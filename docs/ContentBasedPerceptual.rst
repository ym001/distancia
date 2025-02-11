Content-Based Perceptual Distance (CPBD)
======================================

Introduction
-----------
The Content-Based Perceptual Distance (CPBD) is a sophisticated image similarity measure that aims to quantify differences between images in a way that correlates with human visual perception. Unlike purely mathematical measures, CPBD incorporates knowledge about the human visual system (HVS) and how it perceives image differences, making it particularly valuable for applications where human perception is crucial.

Understanding the Measure
------------------------
CPBD operates by analyzing various perceptual features of images, including:
- Local contrast sensitivity
- Edge preservation
- Structural information
- Texture patterns
- Color differences in perceptually uniform color spaces

The measure combines these features in a way that mimics human visual perception, giving more weight to differences that humans are more likely to notice and less weight to differences that are less perceptually significant.

Formal Definition
---------------
Given two images I₁ and I₂, the CPBD D(I₁, I₂) is computed as:

D(I₁, I₂) = w₁C(I₁, I₂) + w₂S(I₁, I₂) + w₃T(I₁, I₂)

where:
- C(I₁, I₂) is the contrast difference measure:
  C(I₁, I₂) = ∑ᵢⱼ |L₁(i,j) - L₂(i,j)| × CSF(f)

- S(I₁, I₂) is the structural difference measure:
  S(I₁, I₂) = (2μ₁μ₂ + C₁)/(μ₁² + μ₂² + C₁)

- T(I₁, I₂) is the texture difference measure:
  T(I₁, I₂) = ∑ᵢⱼ |G₁(i,j) - G₂(i,j)|

Where:
- w₁, w₂, w₃ are weighting factors
- CSF(f) is the contrast sensitivity function
- μᵢ represents local mean intensity
- G(i,j) represents gradient magnitude
- C₁ is a stabilizing constant

Application
----------
CPBD is particularly useful in:
- Image quality assessment
- Image compression optimization
- Digital watermarking
- Image enhancement evaluation
- Content-based image retrieval
- Medical image analysis
- Video quality monitoring
- Display technology evaluation

Usage Example
------------
.. code-block:: python

    from distancia import CPBDistance
    
    # Initialize the perceptual distance measure
    cpbd = CPBDistance(
        color_space='LAB',  # Use CIELAB color space
        contrast_weight=0.4,
        structure_weight=0.4,
        texture_weight=0.2
    )
    
    # Load two images
    image1 = load_image("path/to/image1.jpg")
    image2 = load_image("path/to/image2.jpg")
    
    # Calculate perceptual distance
    distance = cpbd.calculate(image1, image2)
    
    # Print result
    print(f"CPBD between images: {distance}")
    # Output: CPBD between images: 0.145

Computational Complexity
----------------------
The computational complexity of CPBD can be analyzed by components:

- Color space conversion: O(n) where n is the number of pixels
- Local contrast computation: O(n × w²) where w is the window size
- Structural analysis: O(n)
- Texture analysis: O(n)
- Overall complexity: O(n × w²)

Space complexity:
- O(n) for storing intermediate results
- O(w²) for filtering operations
- Additional O(n) for gradient computations

Academic Citations
----------------
When using this distance measure, please cite the following papers:

.. [1] Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004).
       Image Quality Assessment: From Error Visibility to Structural Similarity.
       IEEE Transactions on Image Processing, 13(4), 600-612.

.. [2] Zhang, L., Zhang, L., Mou, X., & Zhang, D. (2011).
       FSIM: A Feature Similarity Index for Image Quality Assessment.
       IEEE Transactions on Image Processing, 20(8), 2378-2386.

.. [3] Narwaria, M., & Lin, W. (2010).
       Objective Image Quality Assessment Based on Support Vector Regression.
       IEEE Transactions on Neural Networks, 21(3), 515-519.

Conclusion
---------
The Content-Based Perceptual Distance (CPBD) provides a sophisticated approach to image comparison that aligns well with human visual perception. By incorporating multiple aspects of the human visual system, it offers more meaningful results than purely mathematical measures for applications where human perception is important. While computationally more intensive than simple pixel-based measures, its ability to capture perceptually relevant differences makes it valuable for quality assessment and optimization tasks. The measure's foundation in human visual system research and its comprehensive approach to image comparison make it particularly suitable for applications where the end user's perception is the ultimate criterion of quality.
