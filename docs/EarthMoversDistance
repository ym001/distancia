EarthMoversDistance
====================

Introduction
------------
Earth Mover's Distance (EMD), also known as the Wasserstein Distance, is a measure used to quantify the difference between two probability distributions. It is often used in the context of comparing histograms or distributions of pixel intensities in images.

Sense of the Distance
---------------------
The Earth Mover's Distance calculates the minimum amount of "work" required to transform one distribution into another. The work is defined as the amount of distribution that needs to be moved, multiplied by the distance it is moved. A lower EMD value indicates more similarity between the two distributions.

Formal Definition
-----------------
Given two distributions \( H_1 \) and \( H_2 \), the Earth Mover's Distance can be expressed as:

.. math::

   EMD(H_1, H_2) = \sum_{i=1}^{n} |F_1[i] - F_2[i]|

Where:
- \( F_1[i] \) and \( F_2[i] \) are the cumulative distributions of histograms \( H_1 \) and \( H_2 \), and
- \( n \) is the number of bins.

The EMD measures the cumulative cost of moving mass from one distribution to match the other.

Academic Reference
------------------
Rubner, Y., Tomasi, C., & Guibas, L. J. (1998). A metric for distributions with applications to image databases. *Proceedings of the Sixth International Conference on Computer Vision (ICCV)*, 59-66.

Conclusion
----------
The Earth Mover's Distance is a powerful tool for measuring the similarity between two distributions, especially in applications like image processing and pattern recognition. It accounts for the distribution of data and provides a more nuanced measure of distance than simple bin-by-bin comparisons.
