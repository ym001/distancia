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

.. code-block:: python

#source : https://keras.io/examples/nlp/text_classification_with_transformer/

!pip install distancia==0.0.3

import keras
from keras import ops
from keras import layers
from distancia import ContextualDynamicDistance

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

def extract_contexts(sequences, window_size=2):
    """
    Extract contexts for each word in the given sequences.

    :param sequences: List of sequences (each sequence is a list of word indices).
    :param window_size: Number of words to consider on either side of the target word.

    :return: A numpy array of contexts with shape (num_sequences, sequence_length, 2 * window_size + 1).
    """
    num_sequences = len(sequences)
    sequence_length = len(sequences[0])
    contexts = np.zeros((num_sequences, sequence_length, 2 * window_size + 1), dtype=int)

    for i, seq in enumerate(sequences):
        for j in range(sequence_length):
            # Determine the context window bounds
            start_index = max(0, j - window_size)
            end_index = min(sequence_length, j + window_size + 1)
            context = seq[start_index:end_index]

            # Pad context to ensure it's of length 2 * window_size + 1
            if len(context) < 2 * window_size + 1:
                context = np.pad(context, (0, 2 * window_size + 1 - len(context)), 'constant')

            contexts[i, j] = context

    return contexts

vocab_size = 20000  # Only consider the top 20k words
maxlen = 200  # Only consider the first 200 words of each movie review
(x_train, y_train), (x_val, y_val) = keras.datasets.imdb.load_data(num_words=vocab_size)
print(len(x_train), "Training sequences")
print(len(x_val), "Validation sequences")

x_train = keras.utils.pad_sequences(x_train, maxlen=maxlen)
x_val = keras.utils.pad_sequences(x_val, maxlen=maxlen)

# Define the context window size
context_window_size = 2

# Extract contexts for training and validation sets
context_x_train = extract_contexts(x_train, window_size=context_window_size)
context_x_val = extract_contexts(x_val, window_size=context_window_size)

print("Context shapes:")
print("Training contexts:", context_x_train.shape)
print("Validation contexts:", context_x_val.shape)

# Custom loss function with ContextualDynamicDistance
def custom_loss_crossentropy(y_true, y_pred):
    basic_loss = tf.keras.losses.sparse_categorical_crossentropy(y_true, y_pred, from_logits=True)
    #context_distance = ContextualDynamicDistance().distance(y_true.numpy(), y_pred.numpy(), context_x, context_y)
    #total_loss = basic_loss + context_distance
    return basic_loss

def custom_loss_KLD(y_true, y_pred):
    basic_loss = tf.keras.losses.KLD(y_true, y_pred, from_logits=True)
    return basic_loss

# distancia/loss_functions.py

import math

class CrossEntropyLoss:
    def __init__(self):
        pass
    
    def __call__(self, y_true, y_pred):
        """
        Calcul de la perte Cross Entropy.
        
        :param y_true: Les véritables étiquettes, de forme (batch_size, seq_len)
        :param y_pred: Les prédictions du modèle, de forme (batch_size, seq_len, vocab_size)
        :return: La valeur moyenne de la perte Cross Entropy
        """
        batch_size = len(y_true)
        total_loss = 0.0
        
        for i in range(batch_size):
            for j in range(len(y_true[i])):
                true_label = y_true[i][j]
                pred_probs = self.softmax(y_pred[i][j])
                
                # Calculer la perte pour chaque échantillon
                total_loss += -math.log(pred_probs[true_label] + 1e-9)  # Ajout d'un epsilon pour éviter log(0)
        
        # Retourner la perte moyenne
        return total_loss / (batch_size * len(y_true[0]))
    
    def softmax(self, logits):
        """
        Calculer la softmax pour transformer les logits en probabilités.
        
        :param logits: Logits de forme (vocab_size,)
        :return: Probabilités de forme (vocab_size,)
        """
        max_logit = max(logits)  # Pour éviter des overflow dans l'exponentiation
        exp_logits = [math.exp(logit - max_logit) for logit in logits]
        sum_exp_logits = sum(exp_logits)
        
        # Retourner les probabilités
        return [exp_logit / sum_exp_logits for exp_logit in exp_logits]


History and Context
===================

Cross entropy has its roots in information theory, introduced by Claude Shannon in 1948. In this context, entropy measures the uncertainty of an information source. Cross entropy, on the other hand, measures the divergence between two probability distributions, thus linking concepts from information theory to modern machine learning.

The use of cross entropy as a loss function gained popularity with the development of artificial neural networks and is now one of the standard loss functions for classification tasks.



Academic Reference
==================

For a deeper understanding, you can refer to the foundational work by Claude Shannon on information theory:

- Shannon, C. E. (1948). "A Mathematical Theory of Communication." *The Bell System Technical Journal*, 27(3), 379-423. [doi:10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x)

Conclusion
==========

The `Cross Entropy Loss` is an essential loss function for classification models in machine learning. It guides the model by providing an error signal based on the divergence between the true and predicted distributions. Understanding and using this loss function is fundamental to developing effective and accurate classification models.
