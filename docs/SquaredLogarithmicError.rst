===============================
Squared Logarithmic Error (SLE)
===============================

Introduction
============

The `Squared Logarithmic Error` (SLE) is a loss function used in regression models to measure the difference between predicted and actual values in a way that reduces the impact of larger values. By taking the logarithm of the predictions and actual values, the SLE penalizes large discrepancies less severely than other error metrics, making it particularly useful when the target values span several orders of magnitude or when minimizing the effect of large predictions is important.

Mathematical Formula
====================

The Squared Logarithmic Error is mathematically defined as:

.. math::

    SLE = \frac{1}{N} \sum_{i=1}^{N} \left(\log(y_i + 1) - \log(\hat{y}_i + 1)\right)^2

where:

- :math:`N` is the number of observations.

- :math:`y_i` represents the actual value for the i-th observation.

- :math:`\hat{y}_i` represents the predicted value for the i-th observation.

- :math:`\log` denotes the natural logarithm function.

The formula calculates the average of the squared differences between the logarithms of the actual and predicted values, with a +1 offset to avoid taking the logarithm of zero.

Meaning and Concept Behind Squared Logarithmic Error
====================================================

The SLE transforms both the actual and predicted values using a logarithmic function, which helps to reduce the influence of large values on the error metric. By squaring the difference between these logarithmic values, the SLE still penalizes larger discrepancies more heavily than smaller ones but in a way that lessens the effect of extreme values.

**Interpretation:** Lower SLE values indicate a better fit of the model, as they represent a smaller average squared error in the log-transformed scale. This metric is particularly useful in scenarios where the range of values is large or when you want to dampen the impact of large errors on the overall loss.

.. code-block:: python

    from distancia.loss_functions import SquaredLogarithmicError

    # Example true and predicted values
    y_true = [1.0, 2.0, 3.0, 4.0]
    y_pred = [1.1, 1.9, 2.5, 3.8]

    # Create an instance of SquaredLogarithmicError
    sle_loss = SquaredLogarithmicError()

    # Calculate the Squared Logarithmic Error
    sle_value = sle_loss(y_true, y_pred)
    print(f'Squared Logarithmic Error: {sle_value}')

.. code-block:: bash

    >>>Squared Logarithmic Error: 0.0057567158446387885


History and Context
===================

The Squared Logarithmic Error has its roots in the method of using logarithmic transformations to stabilize variance and reduce the impact of outliers. This approach became more formalized in the 20th century as statistical and machine learning methods evolved to address various issues in error measurement.

While less commonly used than metrics like Mean Squared Error (MSE) or Mean Absolute Error (MAE), SLE is valuable in specific applications where the distribution of target values can vary greatly. It is particularly useful in fields such as finance, economics, and natural sciences, where data can span multiple orders of magnitude.

Academic Reference
==================

For a detailed exploration of error metrics including SLE and its applications, consider the following reference: :footcite:t:`squaredlogarithmicerror`

.. footbibliography::



Conclusion
==========

The `Squared Logarithmic Error` is a specialized loss function that is beneficial for regression tasks where the data range is large and minimizing the influence of extreme values is desired. By transforming values using the logarithm, SLE provides a measure that is less sensitive to large deviations, making it suitable for various practical applications. Despite its niche use, SLE offers valuable insights into model performance, especially when dealing with data that spans multiple orders of magnitude.
