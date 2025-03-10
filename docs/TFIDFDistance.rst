TFIDFDistance
=============

Introduction
------------
The **TF-IDF Distance** measures the similarity between two text documents by analyzing the importance of individual terms (words) relative to the entire corpus. TF-IDF (Term Frequency-Inverse Document Frequency) is a widely used technique in information retrieval and text mining to weigh the relevance of terms in a document while reducing the influence of commonly occurring words.

Distance Meaning
----------------
The **TF-IDF Distance** quantifies the difference between two documents based on the term frequencies weighted by their inverse document frequency in the corpus. This measure helps distinguish documents by focusing on the terms that carry the most meaning in each text and reducing the influence of generic terms.

Formal Definition
-----------------
Let the TF-IDF vector for document :math:`d_1` be :math:`V_1` and the vector for document :math:`d_2` be :math:`V_2`. The distance between the two documents is typically computed as the cosine distance of their TF-IDF vectors:

.. math::
    \text{TFIDF\_Distance}(d_1, d_2) = 1 - \frac{V_1 \cdot V_2}{\|V_1\| \|V_2\|}

Where:
- :math:`V_1 \cdot V_2` is the dot product of the two vectors.
- :math:`\|V_1\|` and :math:`\|V_2\|` are the magnitudes (norms) of the vectors.
- The cosine similarity is transformed into a distance by subtracting from 1.

.. code-block:: python

    from distancia import TFIDF
    #Exemple d'utilisation
    corpus = [
    "the cat sat on the mat",
    "the dog sat on the mat",
    "the dog chased the cat"
]

    text1 = "the cat is sitting on the mat"
    text2 = "the dog is sitting on the mat"

    tfidf_distance = TFIDF(corpus)
    similarity_score: float = tfidf_distance.compute(text1, text2)

    print(f"TF-IDF Similarity: {similarity_score}")

.. code-block:: python

    # Example usage:
    if __name__ == "__main__":
        tfidf_similarity = TFIDFSimilarity()

        # Two example documents
        doc1: str = "This is a sample document."
        doc2: str = "This document is a simple example."

        # Corpus of documents for TF-IDF calculations
        corpus: List[str] = [
            "This is a document in the corpus.",
            "Another document is here for testing.",
            "This example is part of the corpus."
        ]

        # Compute TF-IDF similarity between the two documents
        similarity_score: float = tfidf_similarity.compute(doc1, doc2, corpus)

        # Print similarity score (0 means no similarity, 1 means identical)
        print(f"TF-IDF Similarity score between documents: {similarity_score}")

Academic Reference
------------------
For more details on TF-IDF and its applications in text comparison, see: :footcite:t:`TFIDFDistance` :

.. footbibliography::


Conclusion
----------
The **TF-IDF Distance** is an effective method for comparing text documents by emphasizing terms that are unique to each document, making it useful in tasks like document classification, search, and information retrieval.
