SimHash
=======

Introduction
------------
**SimHash** is a technique used to measure the similarity between large sets of documents by converting them into fixed-length binary fingerprints. It is particularly useful in detecting near-duplicate documents in large datasets due to its efficiency in handling large-scale text comparisons.

Distance Meaning
----------------
The **SimHash Distance** is derived from the Hamming distance between the SimHash fingerprints of two documents. The smaller the Hamming distance, the more similar the documents are, as fewer bit flips are required to transform one hash into the other.

Formal Definition
-----------------
Given two documents :math:`d_1` and :math:`d_2`, their SimHash fingerprints :math:`h_1` and :math:`h_2` are calculated. The **SimHash Distance** is the Hamming distance between these two hashes:

.. math::
    \text{SimHash\_Distance}(d_1, d_2) = \sum_{i=1}^{n} \mathbb{1}(h_1[i] \neq h_2[i])

Where:
- :math:`h_1[i]` and :math:`h_2[i]` are the i-th bits of the SimHash fingerprints.
- :math:`\mathbb{1}(h_1[i] \neq h_2[i])` is an indicator function that is 1 if the bits differ and 0 otherwise.
- The sum counts the number of differing bits (Hamming distance).

.. code-block:: python


    # Example usage:
    if __name__ == "__main__":
        simhash = SimHash()

        # Two example documents
        doc1: str = "This is a sample document."
        doc2: str = "This is another sample document."

        # Compute similarity between the two documents
        similarity_score: float = simhash.similarity(doc1, doc2)

        # Print similarity score (0 means completely different, 1 means identical)
        print(f"Similarity score between documents: {similarity_score}")

Academic Reference
------------------
For more details on SimHash, refer to:


Conclusion
----------
The **SimHash Distance** is an efficient and scalable method for comparing text documents by creating compact representations of documents, making it useful for large-scale similarity detection and near-duplicate document identification.
