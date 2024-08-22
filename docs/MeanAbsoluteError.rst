=======================
Mean Absolute Error (MAE)
=======================

Introduction
============

The `Mean Absolute Error` (MAE) is a fundamental loss function used to evaluate the performance of regression models. It measures the average magnitude of the errors between predicted values and the actual values, without considering their direction. The MAE is a straightforward and interpretable metric that gives an idea of the average error in a model's predictions.

Mathematical Formula
====================

The Mean Absolute Error is mathematically defined as:

.. math::

    MAE = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|

where:

- :math:`N` is the number of observations.
  
- :math:`y_i` represents the actual value for the i-th observation.
  
- :math:`\hat{y}_i` represents the predicted value for the i-th observation.

Meaning and Concept Behind Mean Absolute Error
==============================================

The MAE provides a measure of the average absolute difference between the true values and the predicted values. It gives a clear indication of how much, on average, the predictions deviate from the actual values. Unlike other metrics such as Mean Squared Error (MSE), the MAE does not penalize larger errors more heavily than smaller ones. This characteristic makes MAE a robust measure for models where the importance of all errors is assumed to be equal.

**Interpretation:** The MAE is an easily interpretable measure, where lower values indicate better model performance, i.e., the predictions are closer to the actual values. An MAE of zero means perfect predictions.

  
History and Context
===================

The Mean Absolute Error has been a long-standing metric in the field of statistics and machine learning. It is one of the earliest measures used for error quantification in predictive modeling. Due to its simplicity and interpretability, MAE remains widely used across various domains, including economics, finance, meteorology, and many other areas where predictive modeling is essential.

While more sophisticated metrics have been developed, the MAE's intuitive nature ensures its continued relevance, especially when dealing with datasets that may contain outliers or when the model's predictions are expected to have uniform importance.

.. code-block:: python

    from distancia import MeanAbsoluteError

    # Example true and predicted values
    y_true = [3.0, -0.5, 2.0, 7.0]
    y_pred = [2.5, 0.0, 2.0, 8.0]

    # Create an instance of MeanAbsoluteError
    mae_loss = MeanAbsoluteError()

    # Calculate the Mean Absolute Error
    mae_value = mae_loss(y_true, y_pred)
    print(f'Mean Absolute Error: {mae_value}')

.. code-block:: bash

    >>>Mean Absolute Error: 0.5


Academic Reference
==================

For a comprehensive understanding of error metrics and their applications, the following reference is recommended:

.. bibliography::

    MeanAbsoluteError

- Willmott, C. J., & Matsuura, K. (2005). "Advantages of the Mean Absolute Error (MAE) over the Root Mean Square Error (RMSE) in Assessing Average Model Performance." *Climate Research*, 30(1), 79-82. [doi:10.3354/cr030079](https://doi.org/10.3354/cr030079)

Conclusion
==========

The `Mean Absolute Error` is a crucial loss function in regression analysis, valued for its simplicity and interpretability. It offers a direct measure of the average prediction error, making it an essential tool for evaluating model performance in a variety of applications. By understanding and applying the MAE, practitioners can gain insights into the accuracy of their predictive models and improve them accordingly.
