=================================================
Isolation Forest Distance
=================================================

Introduction
------------
The Isolation Forest Distance is an innovative similarity measure for time series that leverages the principles of anomaly detection through isolation forests. This metric compares time series based on their isolation patterns within randomly constructed decision trees. By measuring how similarly two sequences are isolated within the forest structure, this approach provides a unique perspective on time series similarity that is particularly sensitive to unusual patterns and structural differences.

Intuition Behind the Formula
---------------------------
The Isolation Forest Distance works on the principle that similar time series will display similar isolation patterns within random forests. The method operates by:

1. Creating isolation trees for the time series data
2. Computing isolation paths for sequence segments
3. Comparing the average isolation depths
4. Aggregating isolation patterns across multiple trees

The key insight is that similar sequences will require similar numbers of splits to be isolated, and will be isolated in similar regions of the feature space.

Formal Definition
----------------
For two time series :math:`X = (x_1, ..., x_n)` and :math:`Y = (y_1, ..., y_m)`, the Isolation Forest distance is defined as:

.. math::

    D_{IF}(X,Y) = \|h(X) - h(Y)\| + λ·d_{path}(X,Y)

where:
- :math:`h(X)` is the average path length for sequence X
- :math:`d_{path}(X,Y)` is the path similarity measure
- :math:`λ` is a weighting parameter

The average path length is computed as:

.. math::

    h(X) = \frac{1}{t}\sum_{i=1}^t E(h_i(X))

where:
- :math:`t` is the number of trees
- :math:`h_i(X)` is the path length in tree i
- :math:`E(h)` is the expected path length

Academic References
-----------------
1. Liu, F. T., Ting, K. M., & Zhou, Z. H. (2008). "Isolation Forest." IEEE International Conference on Data Mining.

2. Ding, Z., & Fei, M. (2013). "An Anomaly Detection Approach Based on Isolation Forest Algorithm for Streaming Data using Sliding Window." IFAC Proceedings Volumes.

3. Hariri, S., Kind, M. C., & Brunner, R. J. (2019). "Extended Isolation Forest." IEEE Transactions on Knowledge and Data Engineering.

Conclusion
---------
The Isolation Forest Distance offers several unique advantages for time series analysis:

* Robust detection of structural differences
* Sensitivity to unusual patterns and anomalies
* Efficient computation through tree-based structures
* Natural handling of variable-length sequences
* Scalability to large datasets

These properties make it particularly valuable in applications such as:

* Anomaly detection in temporal data
* Pattern discovery
* Time series classification
* Change point detection
* Outlier analysis

Installation
-----------
The Isolation Forest Distance metric is available as part of the ``distancia`` package and can be installed via pip:

.. code-block:: bash

   pip install distancia

Usage
-----
.. code-block:: python

   from distancia import IsolationForestDistance
   
   # Initialize with desired parameters
   if_dist = IsolationForestDistance(n_trees=100, 
                                   max_samples='auto',
                                   contamination=0.1)
   
   # Calculate distance between two time series
   distance = if_dist.calculate(series1, series2)
   
   # Get isolation scores for a single series
   isolation_score = if_dist.get_isolation_score(series1)
