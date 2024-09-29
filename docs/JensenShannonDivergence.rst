JensenShannonDivergence
========================

Introduction
------------
The **JensenShannonDivergence** class computes the similarity between two probability distributions. It is a symmetric and smoothed version of the Kullback-Leibler (KL) divergence, often used to measure the difference between two distributions in fields such as information theory and machine learning.

Distance Meaning
----------------
The **Jensen-Shannon Divergence (JSD)** measures how much two probability distributions diverge from a common mean distribution. Unlike the Kullback-Leibler divergence, JSD is symmetric and always yields a finite value, making it a practical choice for comparing distributions of text, signals, or data.

Formal Definition
-----------------
Given two probability distributions :math:`P` and :math:`Q`, the Jensen-Shannon Divergence is defined as:

.. math::
   D_{JS}(P \parallel Q) = \frac{1}{2} D_{KL}(P \parallel M) + \frac{1}{2} D_{KL}(Q \parallel M)

where:
- :math:`M = \frac{1}{2}(P + Q)` is the pointwise mean of :math:`P` and :math:`Q`,
- :math:`D_{KL}(P \parallel Q)` is the Kullback-Leibler divergence between distributions :math:`P` and :math:`Q`.

The Jensen-Shannon Divergence takes values in the range [0, 1], where 0 indicates identical distributions and higher values indicate more divergence.

# Exemple d'utilisation avec des textes
text1: str = "The quick brown fox jumps over the lazy dog"
text2: str = "The fast brown fox leaps over the lazy dog"

# Vocabulaire global (tous les mots apparaissant dans les textes)
vocabulary: List[str] = list(set(text1.split()) | set(text2.split()))

# Créer une instance de la classe Jensen-Shannon Divergence
js_divergence = JensenShannonDivergence()

# Convertir les textes en distributions de probabilités
dist1: List[float] = js_divergence.text_to_distribution(text1, vocabulary)
dist2: List[float] = js_divergence.text_to_distribution(text2, vocabulary)

# Calculer la Jensen-Shannon Divergence entre les deux textes
divergence: float = js_divergence.compute(dist1, dist2)
print(f"Jensen-Shannon Divergence: {divergence}")

Academic Reference
------------------
A key reference for the Jensen-Shannon Divergence is:

**Lin, J.** (1991). "Divergence measures based on the Shannon entropy." *IEEE Transactions on Information Theory*, 37(1), 145–151.

Conclusion
----------
The **JensenShannonDivergence** class offers a robust and symmetric method for comparing probability distributions. Its mathematical properties make it suitable for various applications, including text analysis, speech recognition, and data clustering, where distributional similarity is crucial.
