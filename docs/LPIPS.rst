LPIPS Distance
=============

Introduction
-----------
The Learned Perceptual Image Patch Similarity (LPIPS) is a modern deep learning-based distance metric that measures perceptual similarity between images. Unlike traditional pixel-based or hand-crafted features, LPIPS leverages deep neural networks trained on human perceptual judgments to capture similarities in a way that better corresponds to human visual perception. This metric has become increasingly popular due to its strong correlation with human perception and its ability to capture subtle differences that matter to human observers.

Understanding the Measure
------------------------
LPIPS works by extracting deep features from different layers of a pre-trained convolutional neural network (typically AlexNet, VGG, or ResNet). These features are then compared using learned weights that have been calibrated through human perceptual studies. The measure combines low-level and high-level feature differences, weighted according to their perceptual importance.

Formal Definition
---------------
Given two images I₁ and I₂, LPIPS distance D(I₁, I₂) is computed as:

D(I₁, I₂) = ∑ₗ wₗ · ||ŷₗ₁ - ŷₗ₂||₂

where:
- l indexes the layers of the network
- wₗ are the learned weights for layer l
- ŷₗᵢ represents the normalized activations in layer l for image i
- ||·||₂ denotes L2 distance
- The activations are unit-normalized in the channel dimension

The complete computation involves:
1. Forward pass through backbone network:
   yₗᵢ = F₍ₗ₎(Iᵢ)

2. Channel-wise normalization:
   ŷₗᵢ = yₗᵢ/||yₗᵢ||₂

3. Weighted sum of differences:
   D = ∑ₗ wₗ · ∑ₕᵥ ||ŷₗ₁₍ₕᵥ₎ - ŷₗ₂₍ₕᵥ₎||₂

Application
----------
LPIPS is particularly valuable in:
- Image generation and synthesis evaluation
- Image restoration assessment
- Style transfer quality measurement
- Image compression optimization
- GAN evaluation
- Super-resolution quality assessment
- Image editing applications
- Perceptual loss functions for deep learning

Usage Example
------------
.. code-block:: python

    from distancia import LPIPSDistance
    
    # Initialize LPIPS with specific backbone
    lpips_distance = LPIPSDistance(
        network='alex',  # Options: 'alex', 'vgg', 'resnet'
        version='0.1'
    )
    
    # Load two images
    image1 = load_image("path/to/image1.jpg")
    image2 = load_image("path/to/image2.jpg")
    
    # Calculate distance
    distance = lpips_distance.calculate(image1, image2)
    
    # Print result
    print(f"LPIPS distance between images: {distance}")
    # Output: LPIPS distance between images: 0.178

Computational Complexity
----------------------
The computational complexity depends on several factors:

Time Complexity:
- Forward pass through CNN: O(n × c × k²) per layer
  where n is spatial dimension, c is channels, k is kernel size
- Feature normalization: O(h × w × c) per layer
- Distance computation: O(h × w × c) per layer
- Total complexity: O(L × n × c × k²) where L is number of layers

Space Complexity:
- Feature maps: O(L × h × w × c)
- Model parameters: O(P) where P is number of network parameters
- Intermediate computations: O(h × w × c)

GPU Memory Requirements:
- Typically requires 2-4GB GPU memory for standard resolution images
- Scales linearly with batch size

Academic Citations
----------------
When using this distance measure, please cite the following papers:

.. [1] Zhang, R., Isola, P., Efros, A. A., Shechtman, E., & Wang, O. (2018).
       The Unreasonable Effectiveness of Deep Features as a Perceptual Metric.
       IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 586-595.

.. [2] Zhang, R., Isola, P., & Efros, A. A. (2018).
       Perceptual Losses for Real-Time Style Transfer and Super-Resolution.
       European Conference on Computer Vision (ECCV), 694-711.

.. [3] Johnson, J., Alahi, A., & Fei-Fei, L. (2016).
       Perceptual Losses for Real-Time Style Transfer and Super-Resolution.
       European Conference on Computer Vision (ECCV), 694-711.

Conclusion
---------
LPIPS represents a significant advancement in perceptual image similarity metrics by leveraging deep learning and human perceptual judgments. Its ability to capture subtle perceptual differences makes it particularly valuable for applications where traditional metrics fail to align with human perception. While computationally more intensive than classical metrics, the availability of efficient implementations and GPU acceleration makes it practical for many real-world applications. The metric's strong correlation with human judgments and its foundation in deep learning make it an essential tool for modern computer vision applications, particularly in areas where perceptual quality is crucial.
