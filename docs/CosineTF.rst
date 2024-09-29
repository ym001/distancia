CosineTF
========

Introduction
------------
**CosineTF** is a technique used to measure the similarity between two text documents by computing the cosine of the angle between their term frequency (TF) vectors. This metric is widely used in text mining and information retrieval, as it provides a measure of similarity regardless of the length of the documents.

Distance Meaning
----------------
The **Cosine Similarity** based on term frequency vectors measures how close two documents are in terms of the words they contain, normalized by the magnitude of the document vectors. A similarity score closer to 1 indicates that the documents are highly similar, while a score closer to 0 indicates dissimilarity.

Formal Definition
-----------------
Given two documents :math:`d_1` and :math:`d_2`, their term frequency vectors :math:`\mathbf{v_1}` and :math:`\mathbf{v_2}` are computed. The **Cosine Similarity** is defined as:

.. math::
    \text{Cosine\_Similarity}(d_1, d_2) = \frac{\mathbf{v_1} \cdot \mathbf{v_2}}{\|\mathbf{v_1}\| \|\mathbf{v_2}\|}

Where:
- :math:`\mathbf{v_1} \cdot \mathbf{v_2}` is the dot product of the term frequency vectors.
- :math:`\|\mathbf{v_1}\|` and :math:`\|\mathbf{v_2}\|` are the Euclidean norms (magnitudes) of the vectors.

.. code-block:: python

    cosine_similarity = CosineTF()

    # Two example documents
    doc1: str = "This is a sample document."
    doc2: str = "This is another sample document."

    # Compute cosine similarity between the two documents
    similarity_score: float = CosineTF().compute(doc1, doc2)

    # Print similarity score (0 means no similarity, 1 means identical)
    print(f"Cosine Similarity score between documents: {similarity_score}")

Academic Reference
------------------
For more information, refer to:

**Salton, G., Wong, A., & Yang, C. S.** "A vector space model for automatic indexing." *Communications of the ACM* 18.11 (1975): 613-620.

Conclusion
----------
The **CosineTF** class provides a robust method for comparing text documents by analyzing their term frequency vectors. This method is highly effective in information retrieval, document clustering, and text classification applications.
