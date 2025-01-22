================================================
Move-Split-Merge (MSM) Distance
================================================

Introduction
------------
The Move-Split-Merge (MSM) distance is an edit distance metric specifically designed for time series data. Unlike traditional edit distances that focus on insertion, deletion, and substitution operations, MSM introduces three intuitive operations: move, split, and merge. These operations better capture the natural transformations that occur in temporal sequences, making it particularly suitable for analyzing real-world time series data where elements can shift, combine, or separate over time.

Intuition Behind the Formula
---------------------------
The MSM distance measures the minimum cost required to transform one time series into another using three fundamental operations:

1. Move: Changing the value of an element while maintaining its temporal position
2. Split: Dividing one element into two adjacent elements
3. Merge: Combining two adjacent elements into a single element

These operations are inspired by real-world phenomena in time series data, where:
- Values might need adjustment (move)
- Single events might split into multiple sub-events (split)
- Multiple events might combine into a single event (merge)

Formal Definition
----------------
For two time series :math:`X = (x_1, ..., x_n)` and :math:`Y = (y_1, ..., y_m)`, the MSM distance is defined as:

.. math::

    MSM(X, Y) = min\{C(S) | S \text{ transforms } X \text{ into } Y\}

where:
- :math:`C(S)` is the cost of a sequence of operations S
- The cost of operations is defined as:
    * Move(x → y) = |x - y|
    * Split(x → y,z) = c
    * Merge(x,y → z) = c

with c being a cost parameter that balances the preference between move operations and split/merge operations.

The dynamic programming recurrence is:

.. math::

    D[i,j] = min\begin{cases}
    D[i-1,j-1] + |x_i - y_j| & \text{(move)}\\
    D[i-1,j] + c & \text{(split)}\\
    D[i,j-1] + c & \text{(merge)}
    \end{cases}

Academic References
-----------------
1. Stefan, A., Athitsos, V., & Das, G. (2013). "The Move-Split-Merge Metric for Time Series." IEEE Transactions on Knowledge and Data Engineering, 25(6), 1425-1438.

2. Stefan, A., Athitsos, V., & Das, G. (2012). "Reference-based similarity search in time series using the Move-Split-Merge distance." 21st ACM International Conference on Information and Knowledge Management.

3. Vidal, E., Casacuberta, F., & Rodriguez, L. (1988). "Fast computation of normalized edit distances." IEEE Transactions on Pattern Analysis and Machine Intelligence, 10(4).

Conclusion
---------
The MSM distance metric offers several advantages for time series analysis:

* Intuitive operations that mirror real-world temporal transformations
* Robust handling of temporal distortions and value shifts
* Flexible parameter tuning through the cost parameter c
* Efficient computation through dynamic programming

These properties make MSM particularly valuable in applications such as:

* Pattern recognition in temporal sequences
* Time series classification
* Anomaly detection
* Gesture recognition
* Speech processing

Installation
-----------
The MSM metric is available as part of the ``distancia`` package and can be installed via pip:

.. code-block:: bash

   pip install distancia

Usage
-----
.. code-block:: python

   from distancia import MSMDistance
   
   # Initialize with desired cost parameter
   msm = MSMDistance(c=0.1)
   
   # Calculate distance between two time series
   distance = msm.calculate(series1, series2)
   
   # Get the optimal operation sequence
   operations = msm.get_operations(series1, series2)
