=======================================================
Dynamic Bayesian Network Distance (DBN Distance)
=======================================================

Introduction
------------
The Dynamic Bayesian Network (DBN) Distance is a sophisticated metric designed to quantify the similarity between temporal sequences by evaluating both structural and parametric differences in their probabilistic representations. This measure is particularly useful in time series analysis, where understanding the underlying generative processes is as important as comparing the observed values themselves.

Intuition Behind the Formula
---------------------------
The DBN distance metric operates on the principle that two time series can be compared by examining how similar their underlying probabilistic structures are. It combines two key aspects:

1. Structural similarity: How closely the conditional dependencies between variables match across the two sequences
2. Parameter similarity: How similar the transition probabilities and emission distributions are between the networks

The resulting metric provides a comprehensive measure that captures both the topological and quantitative aspects of the temporal processes.

Formal Definition
----------------
Given two Dynamic Bayesian Networks :math:`DBN_1` and :math:`DBN_2`, the distance is defined as:

.. math::

   D_{DBN}(DBN_1, DBN_2) = \alpha S(G_1, G_2) + (1-\alpha) P(θ_1, θ_2)

where:
- :math:`S(G_1, G_2)` represents the structural distance between the graph structures
- :math:`P(θ_1, θ_2)` represents the parameter distance between the probability distributions
- :math:`\alpha \in [0,1]` is a weighting factor balancing structural and parameter contributions

Academic References
-----------------
1. Robinson, J. W., & Hartemink, A. J. (2010). "Learning Non-Stationary Dynamic Bayesian Networks." Journal of Machine Learning Research, 11, 3647-3680.

2. Zou, C., & Feng, J. (2009). "Granger causality vs. dynamic Bayesian network inference: a comparative study." BMC Bioinformatics, 10(1), 122.

3. Murphy, K. P. (2002). "Dynamic Bayesian Networks: Representation, Inference and Learning." PhD Thesis, University of California, Berkeley.

Conclusion
---------
The DBN Distance metric provides a robust framework for comparing temporal sequences by considering both their structural organization and probabilistic characteristics. This makes it particularly valuable in applications where understanding the underlying generative processes is crucial, such as:

* Anomaly detection in temporal systems
* Process monitoring and quality control
* Behavioral pattern analysis
* Time series classification

The metric's ability to balance structural and parametric similarities through the :math:`\alpha` parameter makes it adaptable to various application requirements.

Installation
-----------
The DBN Distance metric is available as part of the ``distancia`` package and can be installed via pip:

.. code-block:: bash

   pip install distancia

Usage
-----
.. code-block:: python

   from distancia import DBNDistance
   
   # Initialize the metric
   dbn_dist = DBNDistance(alpha=0.5)
   
   # Calculate distance between two time series
   distance = dbn_dist.calculate(series1, series2)
