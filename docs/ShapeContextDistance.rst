Shape Context Distance
==================

Introduction
-----------
The Shape Context distance is a sophisticated method for measuring similarity between shapes by analyzing the spatial distribution of points relative to each other. This measure is particularly powerful because it captures both local and global shape characteristics by considering how each point relates to all other points in the shape. The method is invariant to translation and scaling, and can be made robust to rotation.

Understanding the Measure
------------------------
Shape Context works by creating a rich descriptor for each point in a shape, capturing the distribution of other points relative to it using log-polar coordinates. These descriptors, called shape contexts, effectively encode the spatial arrangement of the entire shape relative to each point. The distance between two shapes is then computed by finding the best correspondence between points based on their shape contexts and calculating the matching cost.

Formal Definition
---------------
Given two shapes represented as point sets P = {p₁, ..., pₙ} and Q = {q₁, ..., qₙ}, the Shape Context distance is computed as follows:

1. For each point pᵢ, compute its shape context hᵢ(k):
   - Establish log-polar bins (r,θ)
   - hᵢ(k) = #{q ≠ pᵢ : (q - pᵢ) ∈ bin(k)}

2. Cost of matching points pᵢ and qⱼ:
   C(pᵢ,qⱼ) = 1/2 ∑ₖ [hᵢ(k) - hⱼ(k)]² / [hᵢ(k) + hⱼ(k)]

3. Total Shape Context distance:
   D(P,Q) = min_π ∑ᵢ C(pᵢ,qᵢ)

Where:
- bin(k) represents the k-th log-polar bin
- π is a permutation representing point correspondence
- hᵢ(k) is the histogram for point pᵢ in bin k

Application
----------
The Shape Context distance is particularly effective in:
- Object recognition and classification
- Character recognition and handwriting analysis
- Logo identification and trademark matching
- Biological shape analysis
- Archaeological artifact comparison
- Quality control in manufacturing
- Medical image analysis

Usage Example
------------
.. code-block:: python

    from distancia import ShapeContextDistance
    
    # Initialize the distance measure
    sc_distance = ShapeContextDistance(
        n_radial=5,  # Number of radial bins
        n_angular=12  # Number of angular bins
    )
    
    # Load and preprocess two shapes into point sets
    shape1 = load_shape("path/to/shape1.png")
    shape2 = load_shape("path/to/shape2.png")
    
    # Calculate distance
    distance = sc_distance.calculate(shape1, shape2)
    
    # Print result
    print(f"Shape Context distance: {distance}")
    # Output: Shape Context distance: 0.234

Computational Complexity
----------------------
The computational complexity can be broken down into several components:

- Shape context computation: O(n² log n) for n points
- Matching cost matrix computation: O(n² m) where m is the number of bins
- Hungarian algorithm for optimal matching: O(n³)
- Overall complexity: O(n³)

Space complexity:
- O(n² m) for storing shape contexts
- O(n²) for the cost matrix
- Additional O(n) for temporary storage during matching

Academic Citations
----------------
When using this distance measure, please cite the following papers:

.. [1] Belongie, S., Malik, J., & Puzicha, J. (2002). 
       Shape Matching and Object Recognition Using Shape Contexts.
       IEEE Transactions on Pattern Analysis and Machine Intelligence, 24(4), 509-522.

.. [2] Belongie, S., Malik, J., & Puzicha, J. (2000).
       Shape Context: A New Descriptor for Shape Matching and Object Recognition.
       Neural Information Processing Systems (NIPS), 831-837.

.. [3] Mori, G., Belongie, S., & Malik, J. (2005).
       Efficient Shape Matching Using Shape Contexts.
       IEEE Transactions on Pattern Analysis and Machine Intelligence, 27(11), 1832-1837.

Conclusion
---------
The Shape Context distance provides a powerful and discriminative approach to shape comparison by considering the spatial relationships between points in a shape. While computationally intensive, its ability to capture both local and global shape characteristics makes it particularly valuable for applications requiring detailed shape analysis. The measure's invariance to common transformations and its robust theoretical foundation have made it a standard tool in computer vision and pattern recognition. Modern implementations often incorporate various optimizations to make it practical for real-world applications while maintaining its distinctive ability to capture fine details of shape similarity.
