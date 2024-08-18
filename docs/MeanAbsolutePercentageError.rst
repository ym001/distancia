=====================================
Mean Absolute Percentage Error (MAPE)
=====================================

Introduction
============

The `Mean Absolute Percentage Error` (MAPE) is a commonly used loss function in regression analysis that measures the average absolute percentage difference between predicted and actual values. It provides a straightforward metric to evaluate the accuracy of predictive models, especially when the scale of the data varies or when comparing models across different datasets.

Mathematical Formula
====================

The Mean Absolute Percentage Error is mathematically defined as:

.. math::

    MAPE = \frac{100}{N} \sum_{i=1}^{N} \left|\frac{y_i - \hat{y}_i}{y_i}\right|

where:

- :math:`N` is the number of observations.

- :math:`y_i` represents the actual value for the i-th observation.

- :math:`\hat{y}_i` represents the predicted value for the i-th observation.

The result is expressed as a percentage, providing an intuitive measure of the error relative to the size of the actual values.

Meaning and Concept Behind Mean Absolute Percentage Error
=========================================================

MAPE quantifies the accuracy of a model by measuring the average magnitude of the errors as a percentage of the actual values. It is particularly useful in contexts where the magnitude of the values varies widely or when the relative error is more important than the absolute error. 

**Interpretation:** A lower MAPE indicates a better fit of the model, as it suggests that the predicted values are, on average, closer to the actual values in terms of percentage. However, MAPE has its limitations, particularly when actual values are near zero, as this can lead to extremely high or undefined percentage errors.

.. code-block:: python

    from distancia import MeanAbsolutePercentageError

    # Example true and predicted values
    y_true = [100, 200, 300, 400]
    y_pred = [110, 190, 310, 390]

    # Create an instance of MeanAbsolutePercentageError
    mape_loss = MeanAbsolutePercentageError()

    # Calculate the Mean Absolute Percentage Error
    mape_value = mape_loss(y_true, y_pred)
    print(f'Mean Absolute Percentage Error: {mape_value}%')

.. code-block:: python

    >>>Mean Absolute Percentage Error: 5.208333333333334%

History and Context
===================

The concept of using percentage errors in forecasting and regression has a long history, particularly in fields such as economics and finance, where understanding relative error is crucial. MAPE became popular due to its straightforward interpretation and ease of use. However, it has been subject to criticism for its sensitivity to low actual values, which can disproportionately inflate the error metric.

Despite its limitations, MAPE remains a widely used error metric, particularly in industries where the scale of the data can vary significantly, such as energy forecasting, retail, and supply chain management.

Academic Reference
==================

For a deeper understanding of MAPE and its applications, the following reference is recommended:

- Armstrong, J. S. (1985). "Long-range Forecasting: From Crystal Ball to Computer." *Wiley-Interscience.* [ISBN: 978-0471800288](https://www.wiley.com/en-us/Long+Range+Forecasting%3A+From+Crystal+Ball+to+Computer%2C+2nd+Edition-p-9780471800288)

Conclusion
==========

The `Mean Absolute Percentage Error` is a versatile and interpretable loss function used to measure the accuracy of predictive models. While it is particularly effective in assessing models across different scales, practitioners should be aware of its limitations, especially in datasets with values close to zero. Despite these limitations, MAPE remains a valuable tool in the toolkit of regression analysis and forecasting.
