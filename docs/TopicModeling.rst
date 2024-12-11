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

.. code-block:: python


   # Example usage:
   from distancia  import TopicModeling

   documents: List[str] = [
       "The cat sat on the mat.",
       "Dogs are great companions.",
       "Cats and dogs are popular pets.",
       "I love my pet cat and dog."
   ]

   # Initialize TopicModelingDistance with LDA and 5 topics
   topic_model_distance = TopicModeling(method='LDA', num_topics=5)

   # Fit the model to a list of documents
   topic_model_distance.fit(documents)

   # Compute the distance between two new documents
   doc1: str = "The cat sat on the mat."
   doc2: str = "Dogs are great companions."
   distance: float = topic_model_distance.compute(doc1, doc2)
   print(f"Topic Distance (LDA): {distance}")

   # You can also use LSA by changing the method
   lsa_model_distance = TopicModelingDistance(method='LSA', num_topics=5)
   lsa_model_distance.fit(documents)
   distance_lsa: float = lsa_model_distance.compute(doc1, doc2)
   print(f"Topic Distance (LSA): {distance_lsa}")

Academic Reference
------------------
The **TopicModelingDistance** is rooted in the following methodologies:
:footcite:t:`TopicModelingDistance1`
:footcite:t:`TopicModelingDistance2`

.. footbibliography::

Conclusion
----------
The **TopicModelingDistance** provides a robust way to compare documents by analyzing their underlying thematic structures. It is widely used in fields like information retrieval, document clustering, and content analysis where identifying shared themes across texts is crucial.
