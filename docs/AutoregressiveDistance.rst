Autoregressive Distance
======================

Introduction
-----------
The Autoregressive (AR) Distance is a model-based approach for measuring the similarity between time series by comparing their underlying autoregressive structures. This method captures the temporal dependencies and dynamics of the sequences through their fitted AR model parameters.

Meaning and Applications
-----------------------
The AR distance provides a way to compare time series based on their inherent linear temporal dependencies. This approach:

1. Fits AR models to each time series
2. Compares the resulting model parameters
3. Quantifies similarity based on how the series depend on their past values

This distance measure is particularly useful when:

* The temporal structure of the data is important
* The series exhibit clear autocorrelation patterns
* The underlying generating processes need to be compared

Formal Definition
----------------
For two time series X and Y, the AR distance is defined as:

.. math::

   D_{AR}(X, Y) = \|\phi_X - \phi_Y\|

where:

* :math:`\phi_X = [\phi_{1,X}, \phi_{2,X}, ..., \phi_{p,X}]` are the AR coefficients for series X
* :math:`\phi_Y = [\phi_{1,Y}, \phi_{2,Y}, ..., \phi_{p,Y}]` are the AR coefficients for series Y
* p is the order of the AR models
* :math:`\|\cdot\|` denotes an appropriate norm (typically Euclidean)

For an AR(p) model, each series is modeled as:

.. math::

   x_t = c + \sum_{i=1}^p \phi_i x_{t-i} + \epsilon_t

where:

* :math:`x_t` is the value at time t
* c is a constant
* :math:`\phi_i` are the autoregressive coefficients
* :math:`\epsilon_t` is white noise

Academic Citations
----------------
The AR distance measure is based on fundamental work in time series analysis and autoregressive modeling:

1. Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time series analysis: forecasting and control. John Wiley & Sons.

2. Piccolo, D. (1990). A distance measure for classifying ARIMA models. Journal of Time Series Analysis, 11(2), 153-164.

3. Maharaj, E. A. (2000). Clusters of time series. Journal of Classification, 17(2), 297-314.

Conclusion
---------
The AR Distance provides an effective method for comparing time series based on their temporal dependency structures. This approach is particularly valuable when:

* The series exhibit significant autocorrelation
* The linear temporal dependencies are key features
* The data generating processes need to be compared

Implementation in the distancia package allows for flexible computation of AR-based distances between time series, with options for different model orders and parameter settings to suit various applications.
