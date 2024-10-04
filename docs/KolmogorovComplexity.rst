KolmogorovComplexity
======================

Introduction
------------
The **KolmogorovComplexity** class measures the similarity between two files or sequences by approximating their Kolmogorov complexity via compression techniques. The Kolmogorov complexity of a string is the length of the shortest possible description (program) that can generate the string. This method uses compression algorithms to estimate this complexity, based on the idea that similar sequences will compress more efficiently when combined.

Distance Meaning
----------------
The distance between two sequences is determined by how much their combined compression differs from their individual compression. If two sequences are similar, their concatenated version will not increase significantly in size when compressed, leading to a smaller distance value.

Formal Definition
-----------------
Let `C(x)` be the compressed size of string `x`, and `C(xy)` the compressed size of the concatenation of strings `x` and `y`. The **KolmogorovComplexity** distance `D(x, y)` is defined as:

.. math::

   D(x, y) = \frac{C(xy) - \min(C(x), C(y))}{\max(C(x), C(y))}

Where `C(x)` and `C(y)` represent the compressed sizes of the individual sequences, and `C(xy)` is the compressed size of the concatenated sequences.

Academic Reference
------------------
For more details, see:

- Li, M., & Vitányi, P., *An Introduction to Kolmogorov Complexity and Its Applications*, Springer, 2008.

Conclusion
----------
The **KolmogorovComplexity** class provides a powerful approach for measuring similarity between sequences based on information theory. By using compression as a proxy for complexity, this method can be applied to a variety of domains such as text comparison, pattern recognition, and even biological sequence analysis. The elegance of this distance lies in its ability to capture both structural and informational content in data, offering a unique perspective on similarity beyond simple statistical measures.
