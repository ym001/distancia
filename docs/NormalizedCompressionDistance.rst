NormalizedCompressionDistance
==============================

Introduction
------------
The **NormalizedCompressionDistance (NCD)** class calculates the distance between two texts by comparing their compressibility. This method is based on the idea that if two texts are similar, then concatenating them should not significantly increase the size after compression compared to compressing them individually.

Distance Meaning
----------------
**NCD** measures the similarity between two objects (in this case, texts) based on how well they compress together. The smaller the increase in size after compression, the more similar the objects are. The principle is that shared information between the two texts should reduce redundancy when they are concatenated and compressed together.

Formal Definition
-----------------
Let :math:`C(x)` represent the size of the compressed version of text :math:`x`. The Normalized Compression Distance between two texts :math:`x` and :math:`y` is defined as:

.. math::
   NCD(x, y) = \frac{C(xy) - \min(C(x), C(y))}{\max(C(x), C(y))}

where:
- :math:`C(xy)` is the size of the compressed concatenation of :math:`x` and :math:`y`,
- :math:`C(x)` and :math:`C(y)` are the compressed sizes of :math:`x` and :math:`y`, respectively.

.. code-block:: python

   # Example usage:
   text1: str = "the quick brown fox jumps over the lazy dog"
   text2: str = "the fast brown fox leaps over a sleepy dog"

   # Initialize the NCD class
   ncd_calculator = NormalizedCompressionDistance()

   # Compute the NCD between two texts
   ncd_value: float = ncd_calculator.ncd(text1, text2)

   # Output the result
   print(f"Normalized Compression Distance (NCD): {ncd_value:.4f}")

Academic Reference
------------------
Normalized Compression Distance is based on concepts from Kolmogorov complexity and has been widely used in various fields. A key reference is: :footcite:t:`NormalizedCompressionDistance`

.. footbibliography::
Conclusion
----------
The **NormalizedCompressionDistance** class offers a universal similarity metric that can be applied to any data type that can be compressed. By leveraging compression algorithms, this method provides a powerful, domain-independent measure of similarity that captures structural and informational redundancy between two texts.
