.. _contrastive-loss-probability:

===========================================================
Contrastive Loss for Probabilistic Analysis
===========================================================

Introduction
------------

Contrastive Loss represents an innovative probabilistic distance measure designed to capture the intrinsic structural relationships within complex time series data. This sophisticated metric provides a powerful mechanism for learning representational similarities and differences across probabilistic distributions by strategically manipulating the embedding space of data samples.

Theoretical Foundations
----------------------

Formula Interpretation
~~~~~~~~~~~~~~~~~~~~~

The Contrastive Loss methodology distinguishes itself through:

- Dynamic optimization of sample representations
- Simultaneous minimization of intra-class distances
- Maximization of inter-class separations
- Intelligent mapping of probabilistic time series into meaningful embedding spaces

Formal Mathematical Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For paired samples with similarity label y ∈ {0, 1}, Contrastive Loss is mathematically defined as:

.. math::

   L_{contrastive}(x_1, x_2, y) = (1-y) \cdot \frac{1}{2}\left(\max(0, m - \|f(x_1) - f(x_2)\|)\right)^2 + y \cdot \|f(x_1) - f(x_2)\|^2

Where:

- :math:`x_1, x_2` represent input time series samples
- :math:`f()` represents the embedding function
- :math:`y \in \{0, 1\}` indicates sample similarity (0: similar, 1: dissimilar)
- :math:`m` represents the margin hyperparameter
- :math:`\|\cdot\|` denotes Euclidean distance

Key Mathematical Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Enables non-linear similarity learning
- Provides adaptive distance metric optimization
- Supports complex probabilistic representation learning
- Facilitates robust feature extraction

Computational Complexity
-----------------------

Time Complexity
~~~~~~~~~~~~~~

- **O(n)**: Linear computational complexity
- Efficient processing of probabilistic time series
- Scalable across diverse dataset dimensions

Space Complexity
~~~~~~~~~~~~~~~

- **O(k)**: Linear memory requirements
- Proportional to embedding dimensionality
- Optimal memory utilization during representation learning

Academic References
------------------

1. Hadsell, R., Chopra, S., & LeCun, Y. (2006). Dimensionality Reduction by Learning an Invariant Mapping. *IEEE Conference on Computer Vision and Pattern Recognition*, 1735-1742.

2. Chopra, S., Hadsell, R., & LeCun, Y. (2005). Learning a Similarity Metric Discriminatively, with Application to Face Verification. *IEEE Conference on Computer Vision and Pattern Recognition*, 539-546.

Implementation Considerations
----------------------------

Key Advantages
~~~~~~~~~~~~~~

- Advanced probabilistic representation learning
- Robust handling of complex time series structures
- Flexible similarity measurement across diverse domains
- Enhanced feature extraction capabilities
- Sophisticated embedding space optimization

Practical Applications
~~~~~~~~~~~~~~~~~~~~~

- Time series similarity detection
- Pattern recognition
- Anomaly identification
- Dimensionality reduction
- Transfer learning
- Clustering and classification tasks

Conclusion
----------

Contrastive Loss emerges as a sophisticated probabilistic distance measure, offering an intelligent approach to understanding intricate relationships within time series data. By dynamically learning representational similarities, this metric provides researchers and data scientists with a powerful tool for extracting meaningful insights from complex probabilistic distributions.

.. note::
   This implementation is part of the Distancia package and designed for advanced statistical analysis.

.. warning::
   Careful hyperparameter selection and appropriate embedding function design are critical for optimal performance.
