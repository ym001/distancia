BRISQUE (Blind/Referenceless Image Spatial Quality Evaluator)
==========================================================

Introduction
-----------
BRISQUE (Blind/Referenceless Image Spatial Quality Evaluator) is an innovative no-reference image quality assessment metric that evaluates image quality without requiring a reference image. It operates by quantifying the naturalness of an image using scene statistics of locally normalized luminance coefficients and measuring the statistical regularities of natural images that are altered in the presence of distortions.

Understanding the Measure
------------------------
BRISQUE works by analyzing the natural scene statistics (NSS) of images in the spatial domain. It operates on the principle that natural images have certain statistical properties that are altered when distortions are present. The measure uses locally normalized luminance values and computes features that capture the "naturalness" of these statistics. These features are then used with a trained Support Vector Regressor (SVR) to predict image quality scores.

Formal Definition
---------------
Given an image I, BRISQUE computation follows these steps:

1. Local normalization for each pixel (i,j):
   Î(i,j) = (I(i,j) - μ(i,j))/(σ(i,j) + C)

where:
- μ(i,j) is the local mean
- σ(i,j) is the local standard deviation
- C is a stability constant

2. Feature extraction:
   - Compute MSCN (Mean Subtracted Contrast Normalized) coefficients
   - Extract pairwise products of neighboring MSCN coefficients
   - Fit asymmetric generalized Gaussian distribution (AGGD)

3. Quality score computation:
   BRISQUE(I) = SVR(φ(I))

where:
- φ(I) represents the extracted feature vector
- SVR is a trained support vector regressor

Application
----------
BRISQUE is particularly valuable in:
- Real-time image quality monitoring
- Automated quality control systems
- Image compression optimization
- Image restoration assessment
- Display quality evaluation
- Mobile device camera testing
- Social media platform image analysis
- Streaming service quality control

Usage Example
------------
.. code-block:: python

    from distancia import BRISQUEDistance
    
    # Initialize BRISQUE calculator
    brisque = BRISQUEDistance(
        model_path='path/to/model.pkl',  # Pre-trained SVR model
        normalize_scores=True  # Scale scores to [0,100]
    )
    
    # Load image
    image = load_image("path/to/image.jpg")
    
    # Calculate BRISQUE score
    quality_score = brisque.calculate(image)
    
    # Print result
    print(f"BRISQUE quality score: {quality_score}")
    # Output: BRISQUE quality score: 32.45
    # Lower scores indicate better quality

Computational Complexity
----------------------
The computational complexity can be broken down into several components:

Time Complexity:
- Local normalization: O(n × w²) where n is number of pixels, w is window size
- Feature extraction: O(n)
- AGGD fitting: O(k × n) where k is number of iterations
- SVR prediction: O(s × f) where s is support vectors, f is features
- Total complexity: O(n × w² + k × n + s × f)

Space Complexity:
- Image storage: O(n)
- Feature storage: O(f)
- Model parameters: O(s × f)
- Working memory: O(n)

Academic Citations
----------------
When using this measure, please cite the following papers:

.. [1] Mittal, A., Moorthy, A. K., & Bovik, A. C. (2012).
       No-Reference Image Quality Assessment in the Spatial Domain.
       IEEE Transactions on Image Processing, 21(12), 4695-4708.

.. [2] Mittal, A., Soundararajan, R., & Bovik, A. C. (2013).
       Making a "Completely Blind" Image Quality Analyzer.
       IEEE Signal Processing Letters, 20(3), 209-212.

.. [3] Saad, M. A., Bovik, A. C., & Charrier, C. (2012).
       Blind Image Quality Assessment: A Natural Scene Statistics Approach in the DCT Domain.
       IEEE Transactions on Image Processing, 21(8), 3339-3352.

Conclusion
---------
BRISQUE represents a significant advancement in no-reference image quality assessment by effectively leveraging natural scene statistics and machine learning. Its ability to evaluate image quality without requiring a reference image makes it particularly valuable in real-world applications where reference images are unavailable. While the measure requires training data and a pre-trained model, its computational efficiency and strong correlation with human perception make it a practical choice for automated quality assessment systems. The metric's foundation in natural scene statistics theory and its proven effectiveness across various types of image distortions have made it a standard tool in image quality assessment.
