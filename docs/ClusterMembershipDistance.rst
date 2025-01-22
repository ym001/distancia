=================================================
Cluster Membership Distance
=================================================

Introduction
------------
The Cluster Membership Distance (CMD) is a novel approach to measuring similarity between time series based on their cluster associations across multiple clustering scenarios. This metric leverages ensemble clustering techniques to establish a robust measure of similarity by examining how frequently two sequences are grouped together under various clustering configurations. The approach is particularly effective at capturing complex relationships that might not be apparent through direct comparison methods.

Intuition Behind the Formula
---------------------------
The Cluster Membership Distance operates on the principle that similar time series will tend to be grouped together across different clustering scenarios. The method works by:

1. Generating multiple clustering configurations with varying parameters
2. Recording co-occurrence patterns of time series pairs
3. Computing similarity based on shared cluster memberships
4. Aggregating results across different clustering runs

This approach provides a robust measure of similarity that is less sensitive to individual clustering parameters and can capture both local and global relationships in the data.

Formal Definition
----------------
For two time series :math:`X` and :math:`Y`, the Cluster Membership Distance is defined as:

.. math::

    D_{CMD}(X,Y) = 1 - \frac{1}{N}\sum_{i=1}^N I(C_i(X) = C_i(Y))

where:
- :math:`N` is the number of clustering configurations
- :math:`C_i(X)` is the cluster assignment of X in configuration i
- :math:`I(·)` is the indicator function
- The normalized distance can be refined as:

.. math::

    D_{CMD}^{norm}(X,Y) = \frac{\sum_{i=1}^N w_i·I(C_i(X) \neq C_i(Y))}{\sum_{i=1}^N w_i}

where :math:`w_i` are configuration-specific weights.

Academic References
-----------------
1. Fred, A. L., & Jain, A. K. (2005). "Combining Multiple Clusterings Using Evidence Accumulation." IEEE Transactions on Pattern Analysis and Machine Intelligence.

2. Strehl, A., & Ghosh, J. (2002). "Cluster Ensembles - A Knowledge Reuse Framework for Combining Multiple Partitions." Journal of Machine Learning Research.

3. Yang, Y., & Chen, K. (2011). "Temporal Data Clustering via Weighted Clustering Ensemble with Different Representations." IEEE Transactions on Knowledge and Data Engineering.

Conclusion
---------
The Cluster Membership Distance offers several advantages for time series analysis:

* Robust to parameter variations in individual clustering algorithms
* Captures complex relationships through ensemble approach
* Naturally handles variable-length sequences
* Provides interpretable similarity measures
* Scalable to large datasets

These properties make it particularly valuable in applications such as:

* Time series classification
* Pattern discovery
* Anomaly detection
* Sequence clustering
* Temporal data mining

Installation
-----------
The Cluster Membership Distance metric is available as part of the ``distancia`` package and can be installed via pip:

.. code-block:: bash

   pip install distancia

Usage
-----
.. code-block:: python

   from distancia import ClusterMembershipDistance
   
   # Initialize with desired parameters
   cmd = ClusterMembershipDistance(n_configurations=10,
                                 base_clusterer='kmeans',
                                 random_state=42)
   
   # Calculate distance between two time series
   distance = cmd.calculate(series1, series2)
   
   # Get cluster assignments for a series
   memberships = cmd.get_memberships(series1)
   
   # Calculate distance matrix for multiple series
   distance_matrix = cmd.distance_matrix(series_list)
