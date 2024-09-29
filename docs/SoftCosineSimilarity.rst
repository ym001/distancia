SoftCosineSimilarity
====================

Introduction
------------
The **SoftCosineSimilarity** class measures the similarity between two text documents by considering the semantic relationship between terms. Unlike traditional cosine similarity, which treats terms as independent, soft cosine similarity accounts for term similarity, allowing for more nuanced comparisons.

Distance Meaning
----------------
The **SoftCosineSimilarity** extends the standard cosine similarity by incorporating the relationships between words. It evaluates how semantically similar the terms in two documents are, making it more suitable for tasks where words with similar meanings (synonyms) should contribute to the similarity score.

Formal Definition
-----------------
The **SoftCosineSimilarity** is defined as:

.. math::
   \text{SoftCosine}(A, B) = \frac{\sum_{i=1}^{n} \sum_{j=1}^{n} A_i B_j S(i,j)}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{j=1}^{n} B_j^2}}

Where:
- :math:`A` and :math:`B` are the term frequency vectors for two documents.
- :math:`S(i, j)` represents the similarity between terms :math:`i` and :math:`j` (e.g., derived from word embeddings).
- :math:`A_i` and :math:`B_j` are the term frequencies of the :math:`i`-th and :math:`j`-th terms in documents :math:`A` and :math:`B`, respectively.

.. code-block:: python

   # Example usage:
   hypothesis: List[str] = "the cat is on the mat".split()
   references: List[List[str]] = [
       "the cat is on the mat".split(),
       "there is a cat on the mat".split()
   ]

   # Create an instance of the ROUGEScore class with bigrams (n=2)
   rouge = ROUGEScore(n_gram=2)

   # Compute the ROUGE-N score
   rouge_n_score: Dict[str, float] = rouge.rouge_n(hypothesis, references)
   print(f"ROUGE-N Score: {rouge_n_score}")

Academic Reference
------------------
The **SoftCosineSimilarity** metric is detailed in the following work:

**Charlet, Delphine, and Mathieu Lafourcade.** (2008). "A Soft Cosine Measure Based on Word Embeddings for Text Similarity." In *Proceedings of the Annual Conference of the European Association for Computational Linguistics*.

Conclusion
----------
The **SoftCosineSimilarity** provides a more robust similarity measure for text comparison by considering the semantic relationships between words. This makes it particularly useful for applications such as document clustering, information retrieval, and text classification, where simple cosine similarity might fail to capture deeper semantic connections.
