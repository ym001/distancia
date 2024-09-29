GappyNGramDistance
==================

Introduction
------------
The **GappyNGramDistance** class computes the distance between two texts based on the Gappy N-Gram model. This model extends the traditional N-Gram approach by allowing gaps between the elements of the n-gram, making it more flexible for capturing meaningful word patterns in text that are not strictly contiguous.

Distance Meaning
----------------
The **GappyNGramDistance** measures the similarity between two texts by considering the occurrence of n-grams with possible gaps between their elements. Unlike traditional n-gram models, which only consider sequences of adjacent words, the gappy n-gram approach captures patterns that may be interrupted by other words, thus better reflecting the flexibility of natural language.

Formal Definition
-----------------
Let :math:`T_1` and :math:`T_2` be two text sequences. A gappy n-gram is defined as an ordered sequence of :math:`n` elements from the text, where gaps are allowed between the elements. The distance is calculated by comparing the sets of gappy n-grams from each text:

.. math::
   D(T_1, T_2) = 1 - \frac{|G_n(T_1) \cap G_n(T_2)|}{|G_n(T_1) \cup G_n(T_2)|}

where:
- :math:`G_n(T)` represents the set of gappy n-grams in text :math:`T`,
- The formula calculates the Jaccard similarity between the gappy n-grams of the two texts, and the distance is defined as 1 minus this similarity.

Academic Reference
------------------
The gappy n-gram approach is frequently used in the context of text classification and natural language processing, particularly for tasks like information retrieval and machine translation:

**Shawe-Taylor, John, and Nello Cristianini.** (2004). "Kernel Methods for Pattern Analysis." Cambridge University Press.

Conclusion
----------
The **GappyNGramDistance** class provides a more flexible and powerful method for comparing text documents by incorporating gaps within n-grams. This makes it well-suited for analyzing complex text patterns where traditional n-grams may fail to capture relevant information, particularly in cases where word sequences are interrupted by other elements.
