=================================================
Self-Organizing Map (SOM) Distance
=================================================

Introduction
------------
The Self-Organizing Map (SOM) Distance is an innovative approach to measuring similarity between time series by leveraging the dimensional reduction and topology preservation properties of self-organizing maps. This method transforms time series into a lower-dimensional representation while preserving their topological relationships, enabling efficient comparison and clustering of temporal sequences. The SOM-based distance metric combines the advantages of neural network learning with traditional distance measures to create a robust similarity measure.

Intuition Behind the Formula
---------------------------
The SOM Distance operates on the principle that similar time series will be mapped to nearby locations in a trained self-organizing map. The process works through:

1. Training a SOM on a collection of time series segments
2. Mapping time series to trajectories on the SOM grid
3. Computing distances between these trajectories
4. Incorporating both spatial and temporal aspects of the mappings

This approach captures both local and global characteristics of the time series while providing dimensional reduction and noise resistance.

Formal Definition
----------------
For two time series :math:`X = (x_1, ..., x_n)` and :math:`Y = (y_1, ..., y_m)`, the SOM distance is defined as:

.. math::

    D_{SOM}(X,Y) = \sqrt{\sum_{i=1}^k \|\phi(X_i) - \phi(Y_i)\|^2}

where:
- :math:`\phi(·)` is the SOM mapping function
- :math:`X_i, Y_i` are corresponding segments of the time series
- :math:`k` is the number of segments
- The mapping function is defined as:

.. math::

    \phi(z) = argmin_{w_j} \{\|z - w_j\|^2\}

where :math:`w_j` are the SOM weight vectors.

Academic References
-----------------
1. Kohonen, T. (1990). "The Self-Organizing Map." Proceedings of the IEEE, 78(9), 1464-1480.

2. Barreto, G. A., & Aguayo, L. (2009). "Time Series Clustering for Anomaly Detection Using Competitive Neural Networks." International Workshop on Self-Organizing Maps.

3. Vesanto, J. (2002). "Data Exploration Process Based on the Self-Organizing Map." PhD Thesis, Helsinki University of Technology.

Conclusion
---------
The SOM Distance metric offers several unique advantages for time series analysis:

* Dimensional reduction while preserving topological relationships
* Robust handling of noise and outliers
* Ability to capture non-linear relationships
* Efficient computation after initial training
* Natural clustering properties

These characteristics make it particularly valuable in applications such as:

* Time series clustering
* Pattern discovery
* Anomaly detection
* Temporal data visualization
* Sequence classification

Installation
-----------
The SOM Distance metric is available as part of the ``distancia`` package and can be installed via pip:

.. code-block:: bash

   pip install distancia

Usage
-----
.. code-block:: python

   from distancia import SOMDistance
   
   # Initialize with desired parameters
   som_dist = SOMDistance(map_size=(10,10), 
                         learning_rate=0.1, 
                         neighborhood_size=1)
   
   # Train SOM with training data
   som_dist.train(training_series)
   
   # Calculate distance between two time series
   distance = som_dist.calculate(series1, series2)
   
   # Get SOM mapping for a time series
   mapping = som_dist.get_mapping(series1)
