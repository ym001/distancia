FileTypeDistance
=================

Introduction
------------
The **FileTypeDistance** class compares two files based on their type, as determined by their file signatures (also known as magic bytes) or formats. This method helps identify whether two files belong to the same type or differ fundamentally in structure and format. The approach is particularly useful when handling diverse file formats or when content-based comparison is not feasible.

Distance Meaning
----------------
The distance measures the degree of difference between the types of two files. If two files share the same file signature or belong to the same format category, the distance will be smaller. Conversely, files of different types or formats will have a larger distance. This metric is commonly used in file management, security, and forensic analysis to quickly identify and categorize files.

Formal Definition
-----------------
Let `F1` and `F2` be two files, and `T(F1)` and `T(F2)` represent their file types as determined by their signatures or formats. The **FileTypeDistance** `D(F1, F2)` is defined as:

.. math::

   D(F1, F2) = \begin{cases} 
   0 & \text{if } T(F1) = T(F2) \\
   1 & \text{if } T(F1) \neq T(F2)
   \end{cases}

This distance takes the value 0 if the file types are identical and 1 if they differ. Extensions to this basic model can involve more granular metrics based on file type hierarchies or format families.

Academic Reference
------------------
For further reading on file type identification and comparison, see:

- D. Malin, E. K. Lee, Z. Shen, *Information Security and Digital Forensics*, Wiley, 2011.

Conclusion
----------
The **FileTypeDistance** class offers a simple and efficient method to compare files based on their types, as determined by file signatures or formats. It is particularly useful in environments where managing, classifying, or identifying files based on their type is important, such as in digital forensics or data management systems. This approach enables fast categorization without delving into the content of the files, making it a lightweight yet effective comparison technique.
