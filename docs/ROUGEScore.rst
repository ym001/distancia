ROUGEScore
==========

Introduction
------------
The **ROUGEScore** (Recall-Oriented Understudy for Gisting Evaluation) is a set of metrics used to evaluate the quality of machine-generated summaries or translations. It measures the overlap between n-grams, word sequences, and word pairs of the machine-generated output and reference texts, focusing on recall as the primary measure of similarity.

Distance Meaning
----------------
The **ROUGEScore** is designed to assess the similarity between a candidate summary or text and one or more reference texts. It calculates how many units (such as n-grams, words, or sequences) from the reference text appear in the candidate text. The higher the overlap, the more similar the two texts are considered to be. The most commonly used variants of ROUGE include ROUGE-N (for n-grams), ROUGE-L (for longest common subsequence), and ROUGE-W (for weighted longest common subsequence).

Formal Definition
-----------------
ROUGE-N, the most common form of ROUGE, is formally defined as:

.. math::
   ROUGE\text{-}N = \frac{\sum_{S \in \text{RefSummaries}} \sum_{\text{gram}_n \in S} \text{Count}_{match}(\text{gram}_n)}{\sum_{S \in \text{RefSummaries}} \sum_{\text{gram}_n \in S} \text{Count}(\text{gram}_n)}

Where:
- :math:`N` is the length of the n-gram (e.g., ROUGE-1 for unigrams, ROUGE-2 for bigrams).
- :math:`\text{Count}_{match}(\text{gram}_n)` is the number of n-grams in the candidate text that also appear in the reference text.
- :math:`\text{Count}(\text{gram}_n)` is the total number of n-grams in the reference text.

The **ROUGEL** (Longest Common Subsequence) score is calculated based on the longest matching sequence of words, which allows for non-contiguous matches.

Academic Reference
------------------
The **ROUGEScore** was introduced in the following paper:

**Lin, Chin-Yew.** (2004). "ROUGE: A Package for Automatic Evaluation of Summaries." In *Text Summarization Branches Out: Proceedings of the ACL-04 Workshop* (pp. 74-81).

Conclusion
----------
The **ROUGEScore** has become a widely adopted metric for summarization and translation tasks. Its focus on recall makes it particularly useful for applications where capturing the full content of the reference text is important. The metric's various forms (ROUGE-N, ROUGE-L, ROUGE-W) offer flexibility in evaluating different aspects of text similarity.
