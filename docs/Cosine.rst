Cosine Similarity
=================

**Cosine Similarity** is a metric used to measure how similar two vectors are, irrespective of their magnitude. It calculates the cosine of the angle between two non-zero vectors in an inner product space, which represents the cosine of the angle between them.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Cosine Similarity between two vectors :math:`\mathbf{A}` and :math:`\mathbf{B}` is defined as:

.. math::

   \text{Cosine Similarity} = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}

Where:

- :math:`\mathbf{A} = (A_1, A_2, \dots, A_n)` is the first vector.

- :math:`\mathbf{B} = (B_1, B_2, \dots, B_n)` is the second vector.

- :math:`n` is the number of dimensions.

The result of Cosine Similarity ranges from -1 to 1:

- A value of 1 indicates that the two vectors are identical in orientation.

- A value of 0 indicates that the vectors are orthogonal (no similarity).

- A value of -1 indicates that the vectors are diametrically opposed.

History
-------

The concept of Cosine Similarity has its roots in vector space models and information retrieval. It gained prominence in the 1960s and 1970s when researchers in the field of information retrieval started to explore the mathematical representation of documents and queries. The similarity between documents and queries could be quantified using Cosine Similarity, which is particularly effective in high-dimensional spaces.

Cosine Similarity is widely used in various applications, such as text mining, natural language processing, and information retrieval, due to its effectiveness in measuring the orientation (rather than magnitude) of the vectors.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the Cosine Similarity between two vectors using the `distancia` package:

.. code-block:: python

   from distancia import Cosine

   def main():
       cosine_dist = Cosine()

       print("Exemple avec des chaînes de caractères:")
       text1 = "La programmation en Python est amusante et puissante"
       text2 = "Python est un langage de programmation populaire et puissant"
       text3 = "Les chats sont des animaux fascinants"

       distance1_2 = cosine_dist.compute(text1, text2)
       distance1_3 = cosine_dist.compute(text1, text3)
       distance2_3 = cosine_dist.compute(text2, text3)

       print(f"Distance entre text1 et text2: {distance1_2:.4f}")
       print(f"Distance entre text1 et text3: {distance1_3:.4f}")
       print(f"Distance entre text2 et text3: {distance2_3:.4f}")

       print("\nExemple avec des vecteurs de nombres flottants:")
       vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
       vector2 = [1.0, 2.0, 3.0, 4.0, 5.0]  # Identique à vector1
       vector3 = [5.0, 4.0, 3.0, 2.0, 1.0]  # Inverse de vector1
       vector4 = [0.0, 0.0, 0.0, 0.0, 0.0]  # Vecteur nul

       distance_v1_v2 = cosine_dist.compute(vector1, vector2)
       distance_v1_v3 = cosine_dist.compute(vector1, vector3)
       distance_v1_v4 = cosine_dist.compute(vector1, vector4)

       print(f"Distance entre vector1 et vector2 (identiques): {distance_v1_v2:.4f}")
       print(f"Distance entre vector1 et vector3 (inverses): {distance_v1_v3:.4f}")
       print(f"Distance entre vector1 et vector4 (nul): {distance_v1_v4:.4f}")

   if __name__ == "__main__":
       main()

.. code-block:: bash

   >>>Exemple avec des chaînes de caractères:
   >>>Distance entre text1 et text2: 0.5286
   >>>Distance entre text1 et text3: 1.0000
   >>>Distance entre text2 et text3: 1.0000

   >>>Exemple avec des vecteurs de nombres flottants:
   >>>Distance entre vector1 et vector2 (identiques): 0.0000
   >>>Distance entre vector1 et vector3 (inverses): 0.3636
   >>>Distance entre vector1 et vector4 (nul): 1.0000


In this example, the vectors :math:`\mathbf{A} = (1, 2, 3)` and :math:`\mathbf{B} = (4, 5, 6)` are compared. The Cosine Similarity between these vectors is calculated and printed.

Applications
------------

Cosine Similarity is widely used in various domains, including:

- **Text Mining**: To measure the similarity between documents by representing them as term frequency vectors.
- **Natural Language Processing (NLP)**: For comparing the similarity of two word embeddings or sentence embeddings.
- **Recommendation Systems**: To compute the similarity between user preferences or item attributes.
- **Information Retrieval**: For ranking the relevance of documents with respect to a given query.

Reference
---------

For an academic reference, you can refer to the following article that discusses the use of Cosine Similarity in text mining and information retrieval :footcite:t:`cosine` :

.. footbibliography::

   


This textbook is a comprehensive resource on information retrieval and text mining, with an emphasis on vector space models and the role of Cosine Similarity.

Conclusion
----------

Cosine Similarity is a powerful and widely-used metric for comparing vectors, especially in the context of text and document analysis. Its ability to measure orientation rather than magnitude makes it particularly suitable for high-dimensional data, where differences in scale can distort other similarity measures.

