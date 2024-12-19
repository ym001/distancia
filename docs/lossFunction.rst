Loss Functions
==============

Loss functions are critical components in optimization and machine learning, as they quantify the difference between predicted outcomes and actual values. These functions guide algorithms during training by providing feedback to adjust model parameters and improve accuracy. Below is a comprehensive list of loss functions commonly used across various domains, including regression, classification, and generative models.

**List of Loss Functions**

Regression Losses
-----------------

#. `MeanSquaredError`_  (MSE): Measures the average squared difference between predictions and actual values, penalizing larger errors.
#. `MeanAbsoluteError`_  (MAE): Computes the average absolute differences between predicted and true values.
#. `MeanAbsolutePercentageError`_  (MAPE): 
#. `SquaredLogarithmicError`_  : 
#. `GaloisWassersteinLoss`_  : 

#. `Huber Loss`_ : A combination of MSE and MAE, robust to outliers.
#. `Log-Cosh Loss`_ : A smooth approximation of MAE using hyperbolic cosine.

Classification Losses
----------------------

8. `CrossEntropy`_ : Quantifies the difference between true and predicted probability distributions.
#. `Hinge Loss`_ : Commonly used for training Support Vector Machines (SVMs).
#. `Kullback-Leibler Divergence (KL Divergence)`_ : Measures how one probability distribution diverges from a reference distribution.
#. `Focal Loss`_ : Focuses on hard-to-classify examples by assigning them higher weights.
#. `Sparse Categorical Cross-Entropy`_ : A variation of cross-entropy for integer-labeled classes.

Probabilistic Losses
---------------------

13. `Negative Log-Likelihood (NLL)`_ : Maximizes the probability of the observed data under the model.
#. `Poisson Loss`_ : Suitable for count-based predictions.

Ranking and Metric Learning Losses
-----------------------------------

15. `Contrastive Loss`_ : Minimizes distances between similar samples while maximizing distances between dissimilar ones.
#. `Triplet Loss`_ : Encourages the correct ranking of anchor, positive, and negative samples.
#. `Cosine Embedding Loss`_ : Optimizes cosine similarity for embedding-based models.

Generative Model Losses
------------------------

18. `Wasserstein Loss`_ : A metric used in Generative Adversarial Networks (GANs) for stable training.
#. `Reconstruction Loss`_ : Used in autoencoders, measures the difference between input and reconstructed data.
#. `Variational Loss`_ : Combines reconstruction loss with KL divergence for Variational Autoencoders (VAEs).

Custom and Domain-Specific Losses
---------------------------------

21. `Custom Weighted Losses`_ : Weighted combinations of losses to suit specific applications.
#. `Temporal Losses`_ : Designed for time-series data, accounting for temporal dependencies.
#. `Sequence-to-Sequence Loss`_ : Specific to applications like translation or text generation.

Conclusion
----------

The selection of a loss function depends on the problem domain, data type, and model requirements. Using appropriate loss functions is essential for efficient training and achieving optimal performance in machine learning models. For further details on implementation and use cases, refer to the accompanying documentation for each loss function.

.. _CrossEntropy: https://distancia.readthedocs.io/en/latest/CrossEntropy.html
.. _MeanAbsoluteError: https://distancia.readthedocs.io/en/latest/MeanAbsoluteError.html
.. _MeanAbsolutePercentageError: https://distancia.readthedocs.io/en/latest/MeanAbsolutePercentageError.html
.. _MeanSquaredError: https://distancia.readthedocs.io/en/latest/MeanSquaredError.html
.. _SquaredLogarithmicError: https://distancia.readthedocs.io/en/latest/SquaredLogarithmicError.html
.. _GaloisWassersteinLoss: https://distancia.readthedocs.io/en/latest/GaloisWassersteinLoss.html
