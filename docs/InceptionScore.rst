Inception Score (IS)
==================

Introduction
-----------
The Inception Score (IS) is a metric designed to evaluate the quality and diversity of generated images, particularly in the context of generative models. By leveraging a pre-trained Inception v3 network, IS measures both the confidence of the model's predictions (quality) and the distribution of predicted classes (diversity). Higher scores indicate that the generated images are both high quality and diverse.

Understanding the Measure
------------------------
The Inception Score operates on two key principles:
1. Quality: Generated images should result in confident predictions (low entropy)
2. Diversity: The marginal distribution over all generated images should have high entropy

These principles are combined using the KL divergence between the conditional and marginal class distributions, providing a single score that captures both aspects of generation quality.

Formal Definition
---------------
Given a set of generated images X, the Inception Score is computed as:

IS(X) = exp(𝔼ₓ Dₖₗ(p(y|x) || p(y)))

where:
- p(y|x) is the conditional class distribution for image x
- p(y) = 𝔼ₓ[p(y|x)] is the marginal class distribution
- Dₖₗ is the Kullback-Leibler divergence
- exp is the exponential function

The computation process:
1. Feature extraction:
   f(x) = Inception(x)

2. Conditional probabilities:
   p(y|x) = softmax(f(x))

3. Marginal distribution:
   p(y) = 1/N ∑ᵢ p(y|xᵢ)

4. Score calculation:
   IS = exp(1/N ∑ᵢ ∑ⱼ p(y=j|xᵢ) log(p(y=j|xᵢ)/p(y=j)))

Application
----------
The Inception Score is particularly useful in:
- GAN evaluation
- Image generation quality assessment
- Model comparison
- Training progress monitoring
- Architecture selection
- Hyperparameter tuning
- Transfer learning evaluation
- Data augmentation validation

Usage Example
------------
.. code-block:: python

    from distancia import InceptionScore
    
    # Initialize Inception Score calculator
    is_calculator = InceptionScore(
        batch_size=32,
        splits=10,  # Number of splits for score calculation
        device='cuda'  # Use GPU if available
    )
    
    # Load generated images
    generated_images = load_image_set("path/to/generated/")
    
    # Calculate Inception Score
    mean_score, std_score = is_calculator.calculate(generated_images)
    
    # Print results
    print(f"Inception Score: {mean_score:.2f} ± {std_score:.2f}")
    # Output: Inception Score: 7.32 ± 0.12

Computational Complexity
----------------------
The computational complexity can be analyzed across several components:

Time Complexity:
- Forward pass through Inception: O(n × c × h × w)
- Probability computations: O(n × k) where k is number of classes
- KL divergence calculation: O(n × k)
- Total complexity: O(n × (c × h × w + k))

Space Complexity:
- Image storage: O(n × c × h × w)
- Feature storage: O(n × k)
- Model parameters: O(P) where P is number of Inception parameters
- Working memory: O(n × k) for probability distributions

GPU Memory Requirements:
- Scales linearly with batch size
- Typically requires 2-4GB GPU memory for standard evaluation

Academic Citations
----------------
When using this measure, please cite the following papers:

.. [1] Salimans, T., Goodfellow, I., Zaremba, W., Cheung, V., Radford, A., & Chen, X. (2016).
       Improved Techniques for Training GANs.
       Advances in Neural Information Processing Systems (NeurIPS), 2234-2242.

.. [2] Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., & Wojna, Z. (2016).
       Rethinking the Inception Architecture for Computer Vision.
       IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2818-2826.

.. [3] Barratt, S., & Sharma, R. (2018).
       A Note on the Inception Score.
       ICML Workshop on Theoretical Foundations and Applications of Deep Generative Models.

Conclusion
---------
The Inception Score provides a practical way to evaluate generated images by combining measures of quality and diversity. While it has known limitations, such as not capturing mode collapse perfectly and being sensitive to image artifacts, it remains a valuable tool in the evaluation of generative models. Its widespread use in the research community and ease of implementation make it a standard benchmark, though it's often recommended to use it in conjunction with other metrics like FID for a more comprehensive evaluation. The score's intuitive interpretation and correlation with human judgment of image quality make it particularly useful during model development and comparison.
