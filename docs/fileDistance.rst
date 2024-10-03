File-Based Distances in Distancia
=================================

Introduction
============
In the world of data analysis and file comparison, measuring the similarity or difference between files is a crucial task. Files can be compared based on a variety of characteristics such as metadata, content, structure, or compression efficiency. **Distancia** offers a rich set of distance measures to compare files of various types, including text documents, binary files, and structured formats like JSON or XML. This document categorizes and describes the file-based distances available in the package.

Categories of File-Based Distances
==================================

1. **Metadata-Based Distances**
2. **Content-Based Distances**
3. **Structural-Based Distances**
4. **Compression-Based Distances**
5. **Hash-Based Distances**

Description of Each Category
============================

Metadata-Based Distances
------------------------

Content-Based Distances
-----------------------

Structural-Based Distances
--------------------------

Compression-Based Distances
---------------------------

Hash-Based Distances
--------------------

List of Distances
=================

**Metadata-Based Distances**
----------------------------

  These distances rely on the comparison of file metadata, such as size, creation date, permissions, or modification date. They provide a way to quickly assess file differences without examining the file content directly.

1. :doc:`FileMetadataComparison`
  
   - Compares files based on their metadata attributes like size, creation time, and access permissions.
  
2. :doc:`FileSize`
  
   - Measures the difference between the sizes of two files, useful for quick assessments of large files.

**Content-Based Distances**
---------------------------

Content-based distances focus on the actual content of the files, comparing characters, bytes, or words. These methods are suitable for comparing text documents, binary files, or even encoded content such as base64 strings.

1. :doc:`Levenshtein`

   - Calculates the number of single-character edits (insertions, deletions, or substitutions) required to transform one file's content into another.

2. :doc:`Jaccard`

   - Compares the sets of words or characters in two files, providing a ratio of shared elements versus total unique elements.

**Structural-Based Distances**
------------------------------

These distances compare the structure of files, particularly useful for structured formats like JSON, XML, or HTML. By comparing trees or nested hierarchies, they capture differences in the organization and relationships between elements.

1. :doc:`TreeEditDistance`

   - Measures the difference between two tree structures, such as XML or JSON, based on the number of node insertions, deletions, or updates required to transform one tree into another.

2. :doc:`CFGDistance`

   - Compares the control flow graphs (CFGs) of two files, particularly useful for executable or code files, by analyzing the differences in their execution structure.

**Compression-Based Distances**
-------------------------------

These distances rely on compression techniques to measure how much two files share in common by comparing their individual and combined compression rates. These approaches are highly effective for files with repetitive structures or large amounts of redundant data.

1. :doc:`ZlibCompressionDistance`

   - Uses zlib compression to evaluate how much two files share in terms of common patterns and structures.

2. :doc:`NormalizedCompressionDistance`

   - Measures file similarity by comparing the combined compression of the two files with their individual compressions.

**Hash-Based Distances**
------------------------

Hash-based distances compare files by computing and comparing their cryptographic hash values. These methods are efficient and suitable for detecting even small changes between files.

1. :doc:`SimHashDistance`

   - Generates SimHashes of the two files and computes the Hamming distance between them, providing an efficient method for comparing large sets of files.

2. :doc:`MD5HashDistance`

   - Compares the MD5 hash values of two files, useful for detecting exact or near-exact duplicates.

Conclusion
==========
The **Distancia** package provides a wide range of file comparison methods, addressing various file types and comparison needs. Whether you're working with metadata, raw content, structured data, or compressible formats, **Distancia** offers efficient and effective distance measures. These distances can be applied to diverse scenarios, such as detecting duplicates, comparing document versions, analyzing code structures, or optimizing file storage. By categorizing the comparison methods into metadata, content, structure, compression, and hash-based approaches, **Distancia** ensures that users have the right tools for their file comparison tasks, regardless of the file format or the level of detail required.
