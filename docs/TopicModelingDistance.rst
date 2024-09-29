TopicModelingDistance
======================

Introduction
------------
The **TopicModelingDistance** class calculates the similarity between two text documents based on their underlying topics. It leverages topic modeling techniques like Latent Dirichlet Allocation (LDA) or Latent Semantic Analysis (LSA) to represent documents as distributions over a set of topics and then measures the distance between these distributions.

Distance Meaning
----------------
The **TopicModelingDistance** focuses on the thematic content of the documents. Instead of comparing individual words, this distance compares how two documents are distributed over a set of topics. This makes it especially effective for analyzing large corpora of text where documents may discuss similar themes using different vocabularies.

Formal Definition
-----------------
Let :math:`T_A` and :math:`T_B` be the topic distributions for two documents, :math:`A` and :math:`B`, respectively. The distance between these distributions can be calculated using a metric like the Jensen-Shannon divergence:

.. math::
   D(T_A, T_B) = \frac{1}{2} \left( D_{KL}(T_A \| M) + D_{KL}(T_B \| M) \right)

where:
- :math:`D_{KL}` is the Kullback-Leibler divergence,
- :math:`M = \frac{1}{2}(T_A + T_B)` is the average topic distribution.

Other measures such as the Euclidean distance or cosine similarity can also be applied to the topic distributions.

Academic Reference
------------------
The **TopicModelingDistance** is rooted in the following methodologies:

**Blei, David M., Andrew Y. Ng, and Michael I. Jordan.** (2003). "Latent Dirichlet Allocation." In *Journal of Machine Learning Research*.  
**Deerwester, Scott, et al.** (1990). "Indexing by Latent Semantic Analysis." In *Journal of the American Society for Information Science*.

Conclusion
----------
The **TopicModelingDistance** provides a robust way to compare documents by analyzing their underlying thematic structures. It is widely used in fields like information retrieval, document clustering, and content analysis where identifying shared themes across texts is crucial.
