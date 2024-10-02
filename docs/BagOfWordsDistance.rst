BagOfWordsDistance
===================

Introduction
------------
**BagOfWordsDistance** is a method used to compare text documents based on their word frequency, disregarding word order. The "Bag of Words" (BoW) model treats documents as unordered collections of words, focusing on the presence or absence of words and their frequencies. It is commonly used in text mining, natural language processing (NLP), and document similarity tasks.

Distance Meaning
----------------
The **BagOfWordsDistance** measures the similarity or distance between two documents by comparing the frequency of common words. The comparison does not consider the order of words, which means the texts are viewed as bags of their constituent words. The method focuses on the vector representation of word frequencies, and the distance can be computed using various metrics (such as cosine similarity, Euclidean distance, etc.).

Formal Definition
-----------------
Let :math:`d_1` and :math:`d_2` be two documents, and let :math:`V` be the set of unique words (the vocabulary) across both documents. The documents are represented as word frequency vectors :math:`v_1` and :math:`v_2`, where each element of the vectors corresponds to the frequency of a word in :math:`V`.

The distance between two documents can then be calculated using a chosen metric, such as:

- **Cosine similarity**:
  .. math::
      \text{Cosine}(v_1, v_2) = \frac{v_1 \cdot v_2}{||v_1|| ||v_2||}
  
- **Euclidean distance**:
  .. math::
      \text{Euclidean}(v_1, v_2) = \sqrt{\sum_{i=1}^{n} (v_1[i] - v_2[i])^2}

Where:
- :math:`v_1 \cdot v_2` is the dot product of the two vectors.
- :math:`||v_1||` and :math:`||v_2||` are the magnitudes (lengths) of the vectors.

.. code-block:: python

  # Exemple d'utilisation
  text1 = "the cat sat on the mat"
  text2 = "the dog sat on the mat"

  bow_distance = BagOfWordsDistance()
  similarity_score: float = bow_distance.compute(text1, text2)

  print(f"Bag-of-Words Distance: {similarity_score}")

Academic Reference
------------------
For more information on the Bag of Words model, see:


Conclusion
----------
The **BagOfWordsDistance** provides a simple yet powerful way to measure the similarity between text documents by focusing on word frequencies. This method is widely used in text classification, information retrieval, and other areas of natural language processing, where word order is not as important as the presence and frequency of words.
