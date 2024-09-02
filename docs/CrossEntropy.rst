=======================
Cross Entropy Loss
=======================

Introduction
============

The `Cross Entropy Loss` is a widely used measure to evaluate the difference between two probability distributions. In the context of neural networks, it is primarily used to assess the performance of classification models, particularly in multi-class classification tasks.

Mathematical Formula
====================

The cross entropy loss function is mathematically defined as follows:

.. math::

    L(y, \hat{y}) = -\sum_{i=1}^{N} y_i \log(\hat{y}_i)

where:

- :math:`y` represents the vector of true labels (a probability distribution where only one class is assigned a value of 1, and the others are 0).
  
- :math:`\hat{y}` represents the vector of model predictions (the predicted probabilities for each class).
  
- :math:`N` is the number of classes.

Meaning and Concept Behind Cross Entropy
========================================

The central idea behind Cross Entropy is to quantify the "disagreement" between the true and predicted probability distributions. If the probabilities predicted by the model are close to the true probabilities (the labels), the loss will be low. Conversely, if the predictions are far from the true labels, the loss will be high. This measure encourages the model to refine its predictions to better match the observed truths.

**Interpretation:** A cross entropy loss of zero means the model has perfectly predicted the correct class for all examples, while a high loss indicates that the model often assigned low probabilities to the correct classes.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the Cosine Similarity between two vectors using the `distancia` package:

.. code-block:: python

    from distancia import CrossEntropy

    # Exemple de données
    y_true = [[1, 2], [0, 1]]  # Étiquettes réelles
    y_pred = [[[0.1, 0.2, 0.7], [0.3, 0.4, 0.3]], 
          [[0.5, 0.2, 0.3], [0.6, 0.3, 0.1]]]  # Prédictions du modèle

    # Créer une instance de CrossEntropy
    loss_fn = CrossEntropy()

    # Calculer la perte
    loss_value = loss_fn(y_true, y_pred)
    print(f'Cross Entropy Loss: {loss_value}')

.. code-block:: bash

    >>>Cross Entropy Loss: -0.2534601641198856


Here is a second example of more developed neural classification

.. code-block:: python

    #source : https://keras.io/examples/nlp/text_classification_with_transformer/

    !pip install distancia

    import keras
    from keras import ops
    from keras import layers
    from distancia import *

    class TransformerBlock(layers.Layer):
        def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
            super().__init__()
            self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
            self.ffn = keras.Sequential(
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]
            )
            self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
            self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
            self.dropout1 = layers.Dropout(rate)
            self.dropout2 = layers.Dropout(rate)

        def call(self, inputs):
            attn_output = self.att(inputs, inputs)
            attn_output = self.dropout1(attn_output)
            out1 = self.layernorm1(inputs + attn_output)
            ffn_output = self.ffn(out1)
            ffn_output = self.dropout2(ffn_output)
            return self.layernorm2(out1 + ffn_output)

    class TokenAndPositionEmbedding(layers.Layer):
        def __init__(self, maxlen, vocab_size, embed_dim):
            super().__init__()
            self.token_emb = layers.Embedding(input_dim=vocab_size, output_dim=embed_dim)
            self.pos_emb = layers.Embedding(input_dim=maxlen, output_dim=embed_dim)

        def call(self, x):
            maxlen = ops.shape(x)[-1]
            positions = ops.arange(start=0, stop=maxlen, step=1)
            positions = self.pos_emb(positions)
            x = self.token_emb(x)
            return x + positions
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras



    vocab_size = 20000  # Only consider the top 20k words
    maxlen = 200  # Only consider the first 200 words of each movie review
    (x_train, y_train), (x_val, y_val) = keras.datasets.imdb.load_data(num_words=vocab_size)
    print(len(x_train), "Training sequences")
    print(len(x_val), "Validation sequences")

    x_train = keras.utils.pad_sequences(x_train, maxlen=maxlen)
    x_val = keras.utils.pad_sequences(x_val, maxlen=maxlen)

    embed_dim = 32  # Embedding size for each token
    num_heads = 2  # Number of attention heads
    ff_dim = 32  # Hidden layer size in feed forward network inside transformer

    inputs = layers.Input(shape=(maxlen,))
    embedding_layer = TokenAndPositionEmbedding(maxlen, vocab_size, embed_dim)
    x = embedding_layer(inputs)
    transformer_block = TransformerBlock(embed_dim, num_heads, ff_dim)
    x = transformer_block(x)
    x = layers.GlobalAveragePooling1D()(x)
    x = layers.Dropout(0.1)(x)
    x = layers.Dense(20, activation="relu")(x)
    x = layers.Dropout(0.1)(x)
    outputs = layers.Dense(2, activation="softmax")(x)

    model = keras.Model(inputs=inputs, outputs=outputs)

    loss_crossentropy=CrossEntropyLoss()
    model.compile(optimizer="adam", loss=custom_loss_crossentropy, metrics=["accuracy"])
    history = model.fit(x_train, y_train, batch_size=32, epochs=3, validation_data=(x_val, y_val))

    import matplotlib.pyplot as plt

    # Visualisation des courbes de précision
    plt.figure(figsize=(12, 6))

    plt.plot(history.history['accuracy'], label='Cross Entropy')
    plt.title('Accuracy Distancia')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.show()


History and Context
===================

Cross entropy has its roots in information theory, introduced by Claude Shannon in 1948. In this context, entropy measures the uncertainty of an information source. Cross entropy, on the other hand, measures the divergence between two probability distributions, thus linking concepts from information theory to modern machine learning.

The use of cross entropy as a loss function gained popularity with the development of artificial neural networks and is now one of the standard loss functions for classification tasks.



Academic Reference
==================

For a deeper understanding, you can refer to the foundational work by Claude Shannon on information theory :footcite:t:`crossentropy`:

.. footbibliography::

    


Conclusion
==========

The `Cross Entropy Loss` is an essential loss function for classification models in machine learning. It guides the model by providing an error signal based on the divergence between the true and predicted distributions. Understanding and using this loss function is fundamental to developing effective and accurate classification models.
