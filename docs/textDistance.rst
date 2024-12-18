Text-Based Distances
====================

Introduction
============
When comparing two texts, it's important to account for various aspects such as word frequency, sentence structure, semantic meaning, and syntactic patterns. The **Distancia** package provides a wide range of distance measures to evaluate textual similarity and dissimilarity based on these factors. These metrics can be used for tasks like document comparison, plagiarism detection, and machine translation evaluation. 

Text-Based Distance Measures
============================

This section categorizes and details an exhaustive list of distance measures specifically designed for text data. These measures serve diverse applications in natural language processing, computational linguistics, and related fields.

**Edit-Based Distances**
---------------------
#. `Levenshtein`_ : Edit Distance, measures the minimum number of insertions, deletions, and substitutions needed to transform one string into another.

#. `DamerauLevenshtein`_ :Extends Levenshtein by allowing transpositions of adjacent characters.
#. `Hamming`_ :Counts character mismatches between two strings of equal length.
#. `SmithWaterman`_ :A local alignment method commonly used for comparing text or biological sequences.
#. `RatcliffObershelp`_ :Computes similarity by identifying the longest common subsequence of two strings.
#. `Monge-Elkan Distance`_ :Aggregates pairwise comparisons between elements of two sequences.

**Phonetic and String Matching**
----------------------------

#. `Jaro Distance`_ :Focuses on matching characters and minimizing transpositions.
#. `JaroWinkler`_ :Extends Jaro by giving extra weight to matches at the start of strings.
#. `NgramDistance`_ :Compares substrings of size *n* between two strings.
#. `GappyNGramDistance`_ :Considers n-grams that may skip characters or words.
#. `SimHash`_ :A hash-based method to identify approximate matches.

**Set and Token-Based Measures**
-----------------------------

#. `Jaccard`_ :Compares the overlap of word sets between two strings.
#. `SoftJaccardSimilarity`_ :Extends Jaccard by considering similarity between tokens.
#. `SorensenDice`_ :Measures similarity as twice the size of the intersection divided by the total size of both sets
#. `OverlapCoefficient`_ :Normalizes the intersection of two sets by the size of the smaller set.
#. `BagOfWordsDistance`_ :Measures dissimilarity between word frequency vectors.

**Semantic and Contextual Measures**
---------------------------------

#. `CosineTF`_ :Computes the cosine of the angle between two text vectors.
#. `TF-IDF`_ :Weights terms by their importance in documents and uses cosine similarity.
#. `WordMoversDistance`_ :Quantifies semantic distance between text documents using word embeddings.
#. `FastTextDistance`_ :Employs FastText embeddings for semantic comparison.
#. `BERTBasedDistance`_ :Uses embeddings from BERT models to measure semantic similarity.
#. `SoftCosineSimilarity`_ :Incorporates pairwise token similarities into cosine calculations.
#. `TopicModelingDistance`_ :Measures similarity using probabilistic topic distributions.
#. `AlignmentBasedMeasures`_ :Aligns and compares text sequences at word or phrase levels.

**Statistical and Compression-Based Measures**
------------------------------------------

#. `NormalizedCompressionDistance`_ :Uses compression techniques to measure shared information.
#. `Kullback-Leibler Divergence`_ :Measures divergence between two probability distributions.
#. `JensenShannonDivergence`_ :A symmetric measure derived from Kullback-Leibler divergence.
#. `Tversky`_ :A generalized Jaccard similarity that allows weighting of set components.
#. `Bhattacharyya`_ :Evaluates the similarity between two probability distributions.
#. `Dice`_ :
#. `MongeElkanDistance`_ :


**Evaluation and NLP Metrics**
--------------------------

#. `BLEUScore`_ :Assesses machine translation quality by comparing n-grams with a reference.
#. `ROUGEScore`_ :Evaluates text summarization by comparing overlapping units with a reference.

Applications
------------
These distance measures are critical for tasks such as:

- **Text Classification:** Classifying documents or short texts into predefined categories.
- **Information Retrieval:** Ranking documents based on query relevance.
- **Machine Translation:** Evaluating translation quality with BLEU or ROUGE.
- **Plagiarism Detection:** Identifying similar or identical sections across texts.
- **Semantic Analysis:** Extracting and comparing semantic meaning from text data.

References
----------
1. Levenshtein, V. I. (1966). Binary codes capable of correcting deletions, insertions, and reversals. *Soviet Physics Doklady*.
2. Damerau, F. J. (1964). A technique for computer detection and correction of spelling errors. *Communications of the ACM*.
3. Jurafsky, D., & Martin, J. H. (2019). *Speech and Language Processing*. Pearson.
4. Mikolov, T., et al. (2013). Distributed representations of words and phrases and their compositionality. *Neural Information Processing Systems (NIPS)*.



**Lexical Distances**
---------------------

  Lexical distances are based on the direct comparison of the words and characters in the text. These methods focus on the exact terms or sequences used and are often sensitive to spelling and grammatical variations.

1. :doc:`BagofWords`

   - Compares two texts by analyzing the frequency of words, ignoring word order but focusing on the content overlap.

2. :doc:`N-gram`

  - Measures the similarity between two texts by comparing subsequences of length n (n-grams), capturing local patterns in the text.

3. :doc:`Levenshtein`

  - Calculates the minimum number of edits (insertions, deletions, substitutions) needed to transform one text into another.

**Semantic Distances**
----------------------

  Semantic distances consider the meaning of the words and sentences in the text. These methods use word embeddings or topic modeling to capture the contextual or thematic relationships between the words, allowing for a deeper understanding of the text’s meaning.

1. :doc:`WordMoverDistance`

   - Measures the semantic distance between two texts by finding the minimum distance words from one text need to "travel" to match words in another.

2. :doc:`FastText`

- Uses word vectors generated by the FastText model to compare texts, capturing both word morphology and meaning.

3. :doc:`BERT-Based`

   - Leverages the BERT model to generate sentence embeddings, comparing the texts at a contextual, semantic level.

4. :doc:`Jensen-Shannon Divergence`

   - Measures the similarity between two probability distributions (e.g., word distributions) by symmetrizing Kullback-Leibler divergence.

**Structural Distances**
------------------------

  Structural distances evaluate how the words and sentences are organized in the text. These distances take into account sentence alignment, syntactic structures, and patterns, making them ideal for comparing translations or different versions of the same text.

1. :doc:`Smith-Waterman`

   - Compares texts by identifying the optimal local alignments between their words or sentences, often used for sentence-level comparison.

2. :doc:`Monge-Elkan`

   - A flexible method for comparing sequences by evaluating the best matches between individual components of the texts (e.g., words or phrases).

3. :doc:`BLEUScore`

   - Evaluates the similarity between two texts by comparing n-grams with a reference text, widely used for machine translation evaluation.

4. :doc:`ROUGEScore`

   - Measures the quality of summaries or translations by focusing on overlapping n-grams, word sequences, or sentence pairs.

**Statistical Distances**
-------------------------

Statistical distances measure similarity based on frequency counts, probability distributions, or shared patterns in the text. These distances are useful for identifying common terms, topic distributions, or shared stylistic features between texts.


1. :doc:`TF-IDF`

   - Compares two texts based on term frequency-inverse document frequency (TF-IDF) vectors, highlighting significant terms in both texts.

2. :doc:`Cosine`

   - Measures the cosine of the angle between two TF-IDF vectors, determining the similarity of the texts based on word importance.

3. :doc:`SoftCosine`

   - A variation of cosine similarity that takes into account the semantic similarity between words in addition to their frequency.

4. :doc:`TopicModeling`

   - Compares texts by evaluating the distributions of latent topics inferred through methods like Latent Dirichlet Allocation (LDA) or Latent Semantic Analysis (LSA).

Conclusion
==========
The **Distancia** package offers a comprehensive set of text-based distance measures, providing powerful tools for comparing documents, analyzing textual similarity, and evaluating translations. By categorizing distances into lexical, semantic, structural, and statistical, users can choose the most suitable method depending on the nature of their comparison task. Whether you are interested in the exact match of words or the deeper semantic relationship between texts, **Distancia** has a solution that fits your needs.


.. _Levenshtein: https://distancia.readthedocs.io/en/latest/Levenshtein.html
.. _DamerauLevenshtein: https://distancia.readthedocs.io/en/latest/DamerauLevenshtein.html
.. _Hamming: https://distancia.readthedocs.io/en/latest/Hamming.html
.. _Cosine: https://distancia.readthedocs.io/en/latest/Cosine.html
.. _TFIDF: https://distancia.readthedocs.io/en/latest/TFIDFDistance.html
.. _SimHash: https://distancia.readthedocs.io/en/latest/SimHash.html
.. _CosineTF: https://distancia.readthedocs.io/en/latest/CosineTF.html
.. _WordMoversDistance: https://distancia.readthedocs.io/en/latest/WordMoversDistance.html
.. _BERTBasedDistance: https://distancia.readthedocs.io/en/latest/BERTBasedDistance.html
.. _JaroWinkler: https://distancia.readthedocs.io/en/latest/JaroWinkler.html
.. _OverlapCoefficient: https://distancia.readthedocs.io/en/latest/OverlapCoefficient.html
.. _SorensenDice: https://distancia.readthedocs.io/en/latest/SorensenDice.html
.. _BagOfWordsDistance: https://distancia.readthedocs.io/en/latest/BagOfWordsDistance.html
.. _FastTextDistance: https://distancia.readthedocs.io/en/latest/FastTextDistance.html
.. _Dice: https://distancia.readthedocs.io/en/latest/Dice.html
.. _Tversky: https://distancia.readthedocs.io/en/latest/Tversky.html
.. _NgramDistance: https://distancia.readthedocs.io/en/latest/NgramDistance.html
.. _SmithWaterman: https://distancia.readthedocs.io/en/latest/SmithWaterman.html
.. _RatcliffObershelp: https://distancia.readthedocs.io/en/latest/RatcliffObershelp.html
.. _BLEUScore: https://distancia.readthedocs.io/en/latest/BLEUScore.html
.. _ROUGEScore: https://distancia.readthedocs.io/en/latest/ROUGEScore.html
.. _SoftCosineSimilarity: https://distancia.readthedocs.io/en/latest/SoftCosineSimilarity.html
.. _TopicModelingDistance: https://distancia.readthedocs.io/en/latest/TopicModelingDistance.html
.. _AlignmentBasedMeasures: https://distancia.readthedocs.io/en/latest/AlignmentBasedMeasures.html
.. _GappyNGramDistance: https://distancia.readthedocs.io/en/latest/GappyNGramDistance.html
.. _SoftJaccardSimilarity: https://distancia.readthedocs.io/en/latest/SoftJaccardSimilarity.html
.. _NormalizedCompressionDistance: https://distancia.readthedocs.io/en/latest/NormalizedCompressionDistance.html
.. _MongeElkanDistance: https://distancia.readthedocs.io/en/latest/MongeElkanDistance.html
.. _JensenShannonDivergence: https://distancia.readthedocs.io/en/latest/JensenShannonDivergence.html
