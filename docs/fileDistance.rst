File-Based Distances in Distancia
=================================

Introduction
============
In file comparison, evaluating the similarity or difference between two files requires diverse metrics depending on the nature of the files—whether they are text, binary, structured formats like XML, or multimedia. The **Distancia** package offers various distance measures designed to capture differences and similarities in multiple aspects, including file structure, content, and metadata. This range of distances ensures versatility when comparing files for various tasks, from text comparison to file type identification.

Categories 
==========

1. **Text-Based Distances**
2. **Binary and File Structure Distances**
3. **Metadata-Based Distances**
4. **Compression-Based Distances**

List of of File-Based Distances
===============================

**Text-Based Distances**
------------------------

These distances compare files by analyzing their textual content. This category is ideal for comparing documents, code files, or any content-rich text, considering the frequency of words, structural patterns, or semantic meanings.

1. :doc:`TF-IDF`
   - Measures the importance of terms in each document relative to a corpus, providing insight into the textual similarity of two files.

2. :doc:`Cosine`

   - Compares two text files by evaluating the angle between their term frequency vectors, focusing on word distribution and patterns.

3. :doc:`N-gram`

   - Measures the similarity between two files based on the commonality of n-grams (subsequences of length n), useful for text comparison.

4. :doc:`BLEU Score`

   - Evaluates the similarity between two text files, typically used in translation quality measurement, by comparing n-grams between reference and candidate texts.

**Binary and File Structure Distances**
--------------------------------------

Binary and file structure distances focus on the raw bytes or the structural properties of the files, such as their control flow, byte sequences, or graph-based representations. These methods are useful for comparing executables, XML, JSON, or other structured file formats.

1. :doc:`Control Flow Graph (CFG) Distance`

   - Compares the control flow graphs of two executables or structured files, measuring the structural differences in program logic or file structure.

2. :doc:`File Type Distance`

   - Identifies differences in file types based on their magic bytes or signatures, determining the nature of the files being compared.

3. :doc:`System Call Trace Distance`

   - Compares two executables by analyzing their system call traces during execution, identifying differences in runtime behavior.

4. :doc:`Tree Edit Distance`

   - Measures how many modifications (inserts, deletes, or substitutions) are needed to transform the tree structure of one file into another, commonly used in XML or JSON comparisons.

**Metadata-Based Distances**
----------------------------

These distances compare files based on their metadata, such as creation date, file size, or permissions. They are useful for identifying differences in file attributes without analyzing content.

1. :doc:`FileMetadataComparison`

   - Compares file metadata attributes such as file size, creation date, and permissions, without considering file content.

2. :doc:`FileSize`

   - A simple comparison based on the size of the two files, indicating differences in the amount of stored data.

**Compression-Based Distances**
-------------------------------

Compression-based distances measure the similarity between files by evaluating how efficiently the files can be compressed together. This approach captures structural and content similarities, applicable to all file types.

1. :doc:`NormalizedCompression`

   - Measures the similarity between two files by comparing their individual compression sizes with the compression size of their concatenation, capturing shared structures and patterns.

2. :doc:`ZlibCompression`

   - Uses the zlib compression algorithm to evaluate the similarity between files by comparing the effectiveness of compressing them together versus separately.

Conclusion
==========
The **Distancia** package offers a comprehensive set of file-based distance measures, making it a versatile tool for comparing files of various types and formats. Whether working with text documents, executable binaries, or structured data like XML, the range of distance metrics ensures that you can choose the most appropriate method for your specific needs. By covering different aspects such as content, structure, and metadata, **Distancia** allows for nuanced and robust file comparison, suitable for applications ranging from document analysis to software engineering.
