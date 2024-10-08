SoftJaccardSimilarity
======================

Introduction
------------
The **SoftJaccardSimilarity** class calculates the similarity between two texts using a soft version of the Jaccard index. This approach extends the traditional Jaccard similarity by considering partial matches between terms, allowing for a more nuanced measure of similarity that accounts for approximate rather than exact matches.

Distance Meaning
----------------
The **SoftJaccardSimilarity** measures how similar two sets of terms are by not only considering the exact matches (as in traditional Jaccard) but also including terms that are similar based on a predefined similarity function. This makes the measure more flexible for comparing texts that may use different but related words, such as synonyms or misspelled words.

Formal Definition
-----------------
Let :math:`T_1` and :math:`T_2` represent two sets of terms from the text documents. The Soft Jaccard Similarity is defined as:

.. math::
   S(T_1, T_2) = \frac{\sum_{w_1 \in T_1} \max_{w_2 \in T_2} \text{sim}(w_1, w_2)}{|T_1| + |T_2| - \sum_{w_1 \in T_1} \max_{w_2 \in T_2} \text{sim}(w_1, w_2)}

where:
- :math:`\text{sim}(w_1, w_2)` is a similarity function that measures the likeness between two words :math:`w_1` and :math:`w_2`,
- The numerator sums the highest similarity values for each term in :math:`T_1` with the corresponding term in :math:`T_2`,
- The denominator ensures the result is normalized, similar to the traditional Jaccard index.

.. code-block:: python

   # Example usage:
   text1: str = "the quick brown fox jumps over the lazy dog"
   text2: str = "the fast brown fox leaps over a sleepy dog"

   # Initialize SoftJaccardSimilarity class with a threshold of 0.5 (50% similarity for matching)
   soft_jaccard = SoftJaccardSimilarity(threshold=0.5)

   # Compute the soft Jaccard similarity
   similarity_score: float = soft_jaccard.soft_jaccard_similarity(text1, text2)

   # Output the result
   print(f"Soft Jaccard Similarity Score: {similarity_score:.4f}")

Academic Reference
------------------
Soft Jaccard similarity has been widely used in tasks involving approximate string matching and information retrieval. For further details, refer to:

:footcite:t:`SoftJaccardSimilarity`

.. footbibliography::

Conclusion
----------
The **SoftJaccardSimilarity** class provides a flexible and robust method for comparing text documents where exact word matches may not be possible. By incorporating a similarity function between terms, it captures a broader range of semantic or lexical similarities, making it useful in applications such as fuzzy matching, paraphrase detection, and text classification.
