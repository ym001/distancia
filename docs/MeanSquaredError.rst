==========================
Mean Squared Error (MSE)
==========================

Introduction
============

The `Mean Squared Error` (MSE) is a popular metric used in regression analysis to quantify the average squared difference between predicted and actual values. It is widely used in machine learning and statistical modeling to assess the accuracy of predictions. The MSE provides an indication of how well a model is performing by penalizing larger errors more than smaller ones.

Mathematical Formula
====================

The Mean Squared Error is mathematically defined as:

.. math::

    MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2

where:

- :math:`N` is the number of observations.
  
- :math:`y_i` represents the actual value for the i-th observation.
  
- :math:`\hat{y}_i` represents the predicted value for the i-th observation.

The formula calculates the average of the squared differences between actual and predicted values.

Meaning and Concept Behind Mean Squared Error
=============================================

The MSE measures the average squared error between predictions and actual values. By squaring the errors, MSE penalizes larger discrepancies more heavily than smaller ones, which makes it sensitive to outliers. This characteristic ensures that models with larger errors are more heavily penalized, potentially leading to better model performance.

**Interpretation:** Lower MSE values indicate a better fit of the model, as they represent a smaller average squared error. A MSE of zero signifies a perfect fit, where predictions are exactly equal to the actual values.

.. code-block:: python

    from distancia.loss_functions import MeanSquaredError

    # Example true and predicted values
    y_true = [3.0, -0.5, 2.0, 7.0]
    y_pred = [2.5, 0.0, 2.0, 8.0]

    # Create an instance of MeanSquaredError
    mse_loss = MeanSquaredError()

    # Calculate the Mean Squared Error
    mse_value = mse_loss(y_true, y_pred)
    print(f'Mean Squared Error: {mse_value}')

.. code-block:: bash
    >>>Mean Squared Error: 0.375



History and Context
===================

The Mean Squared Error has been a cornerstone of statistical analysis and machine learning since the early days of these fields. The concept of minimizing squared errors dates back to the method of least squares introduced by Carl Friedrich Gauss in the early 19th century. Gauss developed this method to improve the accuracy of astronomical observations and it has since become a foundational tool in regression analysis.

Over time, MSE has been widely adopted in various domains, including economics, engineering, and data science. Despite its simplicity, MSE remains a critical metric for evaluating and optimizing predictive models.

Academic Reference
==================

For a comprehensive overview of regression analysis and error metrics, consider the following reference:

- Draper, N. R., & Smith, H. (1998). "Applied Regression Analysis." *Wiley-Interscience.* [ISBN: 978-0470284888](https://www.wiley.com/en-us/Applied+Regression+Analysis%2C+3rd+Edition-p-9780470284888)

Conclusion
==========

The `Mean Squared Error` is a fundamental loss function in regression analysis, valued for its ability to penalize larger errors more heavily than smaller ones. It provides a clear measure of model performance, making it a critical tool in the development and evaluation of predictive models. Despite its sensitivity to outliers, MSE remains a widely used metric due to its straightforward interpretation and historical significance in statistical analysis.
