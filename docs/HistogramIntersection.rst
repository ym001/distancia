HistogramIntersection
======================

Introduction
------------
The Histogram Intersection method is used to measure the similarity between two histograms. This technique is commonly applied in image processing and computer vision tasks, such as object recognition and image retrieval, where histograms are used to represent features.

Sense of the Distance
---------------------
Histogram Intersection computes the overlap between two histograms, treating the histograms as distributions of data. The resulting value represents how much two histograms share in common. A higher value indicates more similarity between the two distributions.

Formal Definition
-----------------
The Histogram Intersection between two histograms \( H_1 \) and \( H_2 \), each with \( n \) bins, is defined as:

.. math::

   I(H_1, H_2) = \sum_{i=1}^{n} \min(H_1[i], H_2[i])

Where:
- \( H_1[i] \) and \( H_2[i] \) are the values in the \(i\)-th bin of histograms \( H_1 \) and \( H_2 \).

Academic Reference
------------------

:footcite:t:`HistogramIntersection`

.. footbibliography::

Conclusion
----------
The Histogram Intersection method offers a simple and efficient way to measure the overlap between two distributions represented by histograms. It has been extensively used in applications like image retrieval and object detection where comparing features encoded as histograms is essential.
