Fréchet Inception Distance (FID)
==============================

Introduction
-----------
The Fréchet Inception Distance (FID) is a sophisticated metric for evaluating the quality and diversity of generated images by comparing them to a set of reference images. Originally developed for evaluating generative adversarial networks (GANs), FID has become a standard metric in the field of image generation. It captures both the quality and diversity of generated images by comparing the statistics of extracted features rather than raw pixels.

Understanding the Measure
------------------------
FID works by passing both real and generated images through a pre-trained Inception v3 network and extracting features from an intermediate layer. These features are then modeled as multivariate Gaussian distributions, and the Fréchet distance (also known as Wasserstein-2 distance) between these distributions is computed. Lower FID scores indicate more similar distributions and thus better quality and diversity of generated images.

Formal Definition
---------------
Given two sets of images X₁ and X₂, the FID is computed as:

FID(X₁, X₂) = ||μ₁ - μ₂||² + Tr(Σ₁ + Σ₂ - 2(Σ₁Σ₂)^(1/2))

where:
- μᵢ is the mean of the feature embeddings for set i
- Σᵢ is the covariance matrix of the feature embeddings for set i
- Tr denotes the trace operator
- ||·||² is the L2 norm
- (Σ₁Σ₂)^(1/2) is the matrix square root

The computation process involves:
1. Feature extraction through Inception v3:
   f(x) = Inception(x) ∈ ℝᵈ

2. Computing statistics:
   μᵢ = E[f(Xᵢ)]
   Σᵢ = E[(f(Xᵢ) - μᵢ)(f(Xᵢ) - μᵢ)ᵀ]

Application
----------
FID is particularly valuable in:
- GAN evaluation and comparison
- Image generation quality assessment
- Domain adaptation evaluation
- Style transfer assessment
- Image restoration evaluation
- Data augmentation quality verification
- Transfer learning assessment
- Synthetic data evaluation

Usage Example
------------
.. code-block:: python

    from distancia import FIDDistance
    
    # Initialize FID calculator
    fid_calculator = FIDDistance(
        batch_size=64,
        device='cuda'  # Use GPU if available
    )
    
    # Load sets of images
    real_images = load_image_set("path/to/real/")
    generated_images = load_image_set("path/to/generated/")
    
    # Calculate FID score
    fid_score = fid_calculator.calculate(real_images, generated_images)
    
    # Print result
    print(f"FID Score: {fid_score}")
    # Output: FID Score: 24.32

Computational Complexity
----------------------
The computational complexity can be broken down into several components:

Time Complexity:
- Feature extraction: O(n × c × h × w) per image
- Statistics computation: O(n × d²) where d is feature dimension
- Matrix operations: O(d³) for matrix square root
- Total complexity: O(n × (c × h × w + d²) + d³)

Space Complexity:
- Feature storage: O(n × d) where n is number of images
- Covariance matrices: O(d²)
- Inception model: O(P) where P is number of model parameters

GPU Memory Requirements:
- Scales with batch size and image resolution
- Typically requires 4-8GB GPU memory for standard evaluation

Academic Citations
----------------
When using this distance measure, please cite the following papers:

.. [1] Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B., & Hochreiter, S. (2017).
       GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium.
       Advances in Neural Information Processing Systems (NeurIPS), 6626-6637.

.. [2] Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., & Wojna, Z. (2016).
       Rethinking the Inception Architecture for Computer Vision.
       IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2818-2826.

.. [3] Lucic, M., Kurach, K., Michalski, M., Gelly, S., & Bousquet, O. (2018).
       Are GANs Created Equal? A Large-Scale Study.
       Advances in Neural Information Processing Systems (NeurIPS), 700-709.

Conclusion
---------
The Fréchet Inception Distance represents a robust and theoretically sound approach to evaluating image generation quality. Its ability to capture both the fidelity and diversity of generated images makes it particularly valuable in the field of generative modeling. While computationally intensive, especially for large datasets, its strong correlation with human perception and widespread adoption in the research community make it an essential metric. The measure's foundation in both deep learning and statistical theory provides a reliable way to compare different generative models and track improvements in image generation quality.
