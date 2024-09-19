ChiSquareDistance
==================

Introduction
------------
The Chi-Square Distance is a statistical measure often used to compare two histograms or distributions. It quantifies the difference between two distributions by calculating the normalized squared difference between corresponding bin values.

Sense of the Distance
---------------------
The Chi-Square Distance computes how two histograms differ by comparing the bin values. This distance is sensitive to both the magnitude of the difference between the bins and their overall sizes, making it useful in many contexts such as image processing and histogram comparison.

Formal Definition
-----------------
The Chi-Square Distance between two histograms \( H_1 \) and \( H_2 \) is given by:

.. math::

   \chi^2(H_1, H_2) = \sum_{i=1}^{n} \frac{(H_1[i] - H_2[i])^2}{H_1[i] + H_2[i]}

Where:
- \( H_1[i] \) and \( H_2[i] \) represent the values in the \(i\)-th bin of histograms \( H_1 \) and \( H_2 \),
- \( n \) is the number of bins in the histograms.

Academic Reference
------------------

:footcite:t:`ChiSquareDistance`:

.. footbibliography::



Conclusion
----------
The Chi-Square Distance provides an effective method for comparing distributions, particularly histograms of pixel intensities or color distributions. Its sensitivity to the relative size of bin values makes it well-suited for tasks involving statistical comparison.
