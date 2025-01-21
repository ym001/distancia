Shape-Based Distance (SBD)
========================

Introduction
-----------
Shape-Based Distance (SBD) is a distance measure specifically designed to compare the morphological similarity between time series, regardless of their amplitude differences. Based on normalized cross-correlation (NCC), SBD focuses on the overall shape and pattern matching between sequences, making it particularly useful for applications where the trend and shape of the time series are more important than absolute values.

Mathematical Definition
---------------------
For two time series X = (x₁, ..., xₙ) and Y = (y₁, ..., yₙ) of equal length n, SBD is defined as:

.. math::

   SBD(X,Y) = 1 - max_{k} \left(\frac{CC_k(X,Y)}{\sqrt{CC_0(X,X) \cdot CC_0(Y,Y)}}\right)

where:

.. math::

   CC_k(X,Y) = \sum_{i=1}^{n} (x_i - \mu_X)(y_{(i+k)\bmod n} - \mu_Y)

and:
- :math:`\mu_X` and :math:`\mu_Y` are the means of X and Y respectively
- :math:`k` is the shift parameter for cross-correlation
- :math:`CC_k` is the cross-correlation at shift k
- The denominator normalizes the correlation to [-1, 1]

Properties
---------
SBD exhibits several important characteristics:

1. **Key Properties**:
   - Scale-invariant
   - Shift-invariant
   - Bounded output [0, 2]
   - Symmetric
   - Non-negative

2. **Advantages**:
   - Robust to amplitude variations
   - Captures shape similarity effectively
   - Handles phase shifts
   - Invariant to scaling and offset
   - Computationally efficient using FFT

3. **Considerations**:
   - Requires equal-length sequences
   - Sensitive to noise
   - May need preprocessing for trend removal
   - Best suited for shape-focused comparisons

Academic References
-----------------
1. Paparrizos, J., & Gravano, L. (2015). "k-Shape: Efficient and Accurate Clustering of Time Series." Proceedings of the 2015 ACM SIGMOD International Conference on Management of Data, 1855-1870.

2. Wang, X., Mueen, A., Ding, H., Trajcevski, G., Scheuermann, P., & Keogh, E. (2013). "Experimental Comparison of Representation Methods and Distance Measures for Time Series Data." Data Mining and Knowledge Discovery, 26(2), 275-309.

3. Sakoe, H., & Chiba, S. (1978). "Dynamic Programming Algorithm Optimization for Spoken Word Recognition." IEEE Transactions on Acoustics, Speech, and Signal Processing, 26(1), 43-49.

Use Cases
--------
SBD is particularly effective in:

- Pattern recognition in time series
- ECG signal comparison
- Financial market pattern analysis
- Gesture recognition
- Scientific data analysis
- Quality control in manufacturing
- Sensor data pattern matching

Implementation Details
--------------------
In the distancia package, SBD is implemented with the following features:

- Fast Fourier Transform (FFT) for efficient cross-correlation
- Automatic sequence length normalization
- Optional preprocessing steps
- Configurable correlation window

Example Usage
------------
.. code-block:: python

    from distancia import SBD
    
    # Initialize SBD
    sbd = SBD()
    
    # Calculate distance between two time series
    distance = sbd.calculate(series1, series2)
    
    # With preprocessing
    distance = sbd.calculate(series1, series2, preprocess=True)

Complexity Analysis
-----------------
Using FFT for cross-correlation computation:
- Time Complexity: O(n log n)
- Space Complexity: O(n)

where n is the length of the input sequences.

Preprocessing Options
-------------------
1. **Z-normalization**:
   - Removes mean
   - Scales to unit variance
   - Recommended for most applications

2. **Trend Removal**:
   - Linear trend removal
   - Moving average subtraction
   - Seasonal adjustment

3. **Noise Reduction**:
   - Moving average smoothing
   - Savitzky-Golay filtering
   - Wavelets denoising

Conclusion
---------
Shape-Based Distance (SBD) provides a robust and efficient method for comparing time series based on their morphological similarities. Its scale and shift invariance properties make it particularly suitable for applications where the pattern and shape of the sequences are more important than their absolute values.

The combination of normalized cross-correlation with efficient FFT-based computation makes SBD both effective and practical for large-scale time series analysis. Its ability to capture shape similarities while being invariant to scaling and offset makes it an excellent choice for pattern recognition tasks and shape-based clustering applications.

.. note::
   While SBD is highly effective for shape-based comparison, it requires equal-length sequences and may need appropriate preprocessing depending on the application. Consider the nature of your data and the importance of shape versus absolute values when choosing this distance measure.

See Also
--------
- :class:`DTW`
- :class:`CrossCorrelation`
- :class:`EuclideanDistance`
