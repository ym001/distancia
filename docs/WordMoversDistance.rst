WordMoversDistance
===================

Introduction
------------
**WordMoversDistance** (WMD) is a distance metric used to compare two text documents by calculating the minimum cumulative distance that words in one document must travel to match the words in the other document. It leverages word embeddings, where semantically similar words are located closer to each other in the embedding space.

Distance Meaning
----------------
The **WordMoversDistance** measures the dissimilarity between two documents based on the semantic distance between their word embeddings. Unlike traditional methods that consider only the presence or absence of words, WMD accounts for the semantic meaning of the words, making it more suitable for capturing the underlying relationships between documents.

Formal Definition
-----------------
Let :math:`D_1` and :math:`D_2` be two documents represented by word embeddings. The **WordMoversDistance** is defined as:

.. math::
    \text{WMD}(D_1, D_2) = \min_{\mathbf{T} \geq 0} \sum_{i,j} \mathbf{T}_{ij} \cdot d(\mathbf{w}_i, \mathbf{w}_j)

Where:
- :math:`\mathbf{w}_i` and :math:`\mathbf{w}_j` are word embeddings in documents :math:`D_1` and :math:`D_2`.
- :math:`d(\mathbf{w}_i, \mathbf{w}_j)` represents the distance between word embeddings, usually the Euclidean distance.
- :math:`\mathbf{T}_{ij}` is the flow matrix that minimizes the total distance.

Academic Reference
------------------
For more information, refer to:

**Kusner, M. J., Sun, Y., Kolkin, N. I., & Weinberger, K. Q.** "From word embeddings to document distances." *Proceedings of the 32nd International Conference on Machine Learning (ICML)*. 2015.

Conclusion
----------
The **WordMoversDistance** provides a powerful way to compare text documents by taking into account the semantic distances between words, enabling more meaningful comparisons in tasks such as document clustering, classification, and semantic search.
