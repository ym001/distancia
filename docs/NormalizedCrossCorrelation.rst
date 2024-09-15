Normalized Cross-Correlation (NCC)
===================================

Introduction
------------
Normalized Cross-Correlation (NCC) is a statistical measure commonly used for image similarity and template matching. It computes the degree of similarity between two images by comparing their intensity values pixel by pixel, adjusting for the mean and scale of the intensity levels.

Sense of the Distance
---------------------
NCC measures the linear correlation between the pixel intensities of two images. It normalizes the comparison by subtracting the mean and dividing by the standard deviation, providing a scale-invariant comparison. A value close to 1 indicates high similarity, while values near -1 indicate dissimilarity.

Formal Definition
-----------------
The NCC between two images :math:`I_1` and :math:`I_2` of the same size is calculated as:

.. math::

    NCC(I_1, I_2) = \frac{\sum_{x, y} (I_1(x, y) - \mu_{I_1}) (I_2(x, y) - \mu_{I_2})}
    {\sqrt{\sum_{x, y} (I_1(x, y) - \mu_{I_1})^2 \sum_{x, y} (I_2(x, y) - \mu_{I_2})^2}}

Where:
- :math:`I_1(x, y)` and :math:`I_2(x, y)` are the pixel intensities of images :math:`I_1` and :math:`I_2` at coordinates :math:`(x, y)`.
- :math:`\mu_{I_1}` and :math:`\mu_{I_2}` are the mean pixel intensities of the two images.

Academic Reference
------------------
Lewis, J.P. "Fast Template Matching." Vision Interface, 1995.

Conclusion
----------
Normalized Cross-Correlation (NCC) is a widely used method for assessing the similarity between two images. Its normalized nature allows it to be robust to changes in lighting conditions or contrast, making it suitable for template matching and object detection tasks in images.
