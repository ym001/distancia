BLEUScore
=========

Introduction
------------
The **BLEUScore** (Bilingual Evaluation Understudy) is a metric widely used in natural language processing (NLP) to evaluate the quality of machine-generated text, such as translations or summaries, by comparing them to one or more reference texts. The BLEU score measures the correspondence between n-grams in the candidate text and the reference texts, thus providing an indication of the translation or text quality.

Distance Meaning
----------------
The **BLEUScore** calculates the similarity between two texts by evaluating how many n-grams from the candidate text appear in the reference text(s). The metric is based on precision of n-grams and introduces a brevity penalty to penalize overly short translations. The score ranges from 0 to 1, where a higher score indicates a closer match to the reference.

Formal Definition
-----------------
Given a candidate text and one or more reference texts, the **BLEUScore** is computed as:

.. math::
   BLEU = BP \cdot \exp\left(\sum_{n=1}^N w_n \log p_n\right)

Where:
- :math:`BP` is the brevity penalty to avoid favoring shorter candidate texts.
- :math:`p_n` is the precision of n-grams of length n.
- :math:`w_n` is the weight for the precision at each n-gram length, typically set to uniform values (e.g., :math:`w_n = \frac{1}{N}`).
- :math:`N` is the maximum n-gram length, often set to 4 for BLEU-4.

The brevity penalty is calculated as:

.. math::
   BP = \begin{cases}
   1, & \text{if } c > r \\
   \exp\left(1 - \frac{r}{c}\right), & \text{if } c \leq r
   \end{cases}

Where:
- :math:`c` is the length of the candidate translation.
- :math:`r` is the effective reference length.

.. code-block:: python

   # Exemple d'utilisation
   hypothesis: List[str] = "the cat is on the mat".split()
   references: List[List[str]] = [
       "the cat is on the mat".split(),
       "there is a cat on the mat".split()
   ]

   # Créer une instance de la classe BLEUScore
   bleu = BLEUScore()

   # Calculer le BLEU Score
   score: float = bleu.compute(hypothesis, references)
   print(f"BLEU Score: {score}")

Academic Reference
------------------
The **BLEUScore** was introduced in the following paper:

**Papineni, K., Roukos, S., Ward, T., & Zhu, W.J.** (2002). "BLEU: a Method for Automatic Evaluation of Machine Translation." In *Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics* (pp. 311-318).

Conclusion
----------
The **BLEUScore** has become one of the most widely used metrics for evaluating the quality of machine-generated text. It provides an objective measure of text similarity by comparing n-gram overlaps between candidate and reference texts, while accounting for brevity to prevent gaming the metric with excessively short outputs.
