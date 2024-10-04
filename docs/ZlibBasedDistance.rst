ZlibBasedDistance
==================

Introduction
------------
The **ZlibBasedDistance** class measures the similarity between two files or data streams by leveraging compression techniques. This method is based on the idea that if two files share similar patterns or structures, compressing their concatenation will result in a compressed size close to the sum of their individual compressed sizes. By using the Zlib compression algorithm, this distance is calculated based on how well the data compresses together compared to separately.

Distance Meaning
----------------
This distance quantifies how much structural or informational redundancy is shared between two files. If two files are very similar, their concatenated compression size will not significantly increase compared to their individual compressions. Conversely, if the files are dissimilar, the combined file will not compress much better than each file on its own. This method is particularly useful for comparing files in a domain-agnostic way, relying purely on the compressibility of the data.

Formal Definition
-----------------
Let `C(x)` represent the Zlib compression size of file `x`, and let `x` and `y` be two files. The **ZlibBasedDistance** `D(x, y)` is defined as:

.. math::

   D(x, y) = \frac{C(x \oplus y) - \min(C(x), C(y))}{\max(C(x), C(y))}

where `x \oplus y` denotes the concatenation of files `x` and `y`, and `C(x)` is the compressed size of file `x` using the Zlib algorithm. The distance is normalized by the maximum of the two individual compression sizes to ensure the result lies between 0 and 1.

Academic Reference
------------------
For more details on compression-based distances, see:

- M. Li, P. Vitányi, "An Introduction to Kolmogorov Complexity and Its Applications," Springer, 2008.

Conclusion
----------
The **ZlibBasedDistance** provides a unique approach to file comparison by utilizing data compression as a proxy for measuring similarity. This method can be applied across various types of data, from text to binary files, offering a flexible and domain-independent means of determining structural similarity or difference.
