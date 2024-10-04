TreeEditDistance
=================

Introduction
------------
The **TreeEditDistance** class computes the distance between two tree-structured data representations, such as XML or JSON files. This metric measures the minimal set of operations (insertions, deletions, and substitutions of nodes) required to transform one tree into another. Tree edit distance is widely used in fields like bioinformatics, natural language processing, and structured document comparison.

Distance Meaning
----------------
The distance reflects the structural dissimilarity between two trees. A smaller distance indicates that the two tree structures are very similar, requiring fewer modifications to align them. Conversely, a larger distance suggests more substantial differences in the hierarchy or content of the trees. This distance is particularly useful for comparing structured data where hierarchical relationships are key, such as parse trees or data in XML/JSON format.

Formal Definition
-----------------
Let `T1` and `T2` be two trees. The **TreeEditDistance** `D(T1, T2)` is defined as the minimum number of operations (insertion, deletion, substitution) required to transform `T1` into `T2`. Formally:

.. math::

   D(T1, T2) = \min( \text{cost}(op_1, op_2, \ldots, op_n) )

where each operation `op` represents a single insertion, deletion, or substitution of a node in the tree, and the cost is a predefined weight associated with each operation. The algorithm used for calculating this distance can vary, with the Zhang-Shasha algorithm being one of the most well-known methods.

Academic Reference
------------------
For further reading on tree edit distance algorithms and their applications, see:

- K. Zhang, D. Shasha, "Simple Fast Algorithms for the Editing Distance Between Trees and Related Problems," SIAM Journal on Computing, 1989.

Conclusion
----------
The **TreeEditDistance** class offers a powerful and flexible tool for comparing hierarchical data structures by focusing on their structural transformations. Whether applied to document comparison, biological data analysis, or any domain with tree-like structures, this distance provides a meaningful measure of similarity or difference, allowing for efficient analysis of complex datasets.
