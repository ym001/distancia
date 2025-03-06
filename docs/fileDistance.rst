====================
File-Based Distances
====================
============================
File Distance Measures
============================

Introduction
=============
File distance measures are used to quantify the similarity or dissimilarity between files based on their content, structure, or metadata. These measures are critical in file deduplication, malware analysis, and version control systems.

In file comparison, evaluating the similarity or difference between two files requires diverse metrics depending on the nature of the files—whether they are text, binary, structured formats like XML, or multimedia. The **Distancia** package offers various distance measures designed to capture differences and similarities in multiple aspects, including file structure, content, and metadata. This range of distances ensures versatility when comparing files for various tasks, from text comparison to file type identification.

Below is a comprehensive list of file distance measures, grouped into relevant categories.

List of File-Based Distances
===============================

Binary and File Structure Distances
-----------------------------------

Binary and file structure distances focus on the raw bytes or the structural properties of the files, such as their control flow, byte sequences, or graph-based representations. These methods are useful for comparing executables, XML, JSON, or other structured file formats.

#. `ControlFlowGraph`_ : Compares the control flow graphs of two executables or structured files, measuring the structural differences in program logic or file structure.
#. `FileTypeDistance`_ : Identifies differences in file types based on their magic bytes or signatures, determining the nature of the files being compared.
#. `SystemCallTraceDistance`_ : Compares two executables by analyzing their system call traces during execution, identifying differences in runtime behavior.
#. `TreeEditDistance`_ : Measures how many modifications (inserts, deletes, or substitutions) are needed to transform the tree structure of one file into another, commonly used in XML or JSON comparisons.
#. `Hamming`_ : Compares two files at the binary or byte level by counting the number of different bits.
#. `Levenshtein`_ : Measures the minimum number of operations required to transform one file into another (insertion, deletion, or substitution of characters/bytes).
#. `Jaccard`_ : Compares the similarity between two sets of bytes or segments by calculating the ratio of common elements.
#. `Manhattan`_ : Sum of absolute differences between corresponding bytes of two files.
#. `Euclidean`_ : Square root of the sum of the squares of the byte differences between two files.
#. `AST (Abstract Syntax Tree) Distance`_ : Compares the syntactic structure of code files.
#. `Control Flow Graph (CFG) Distance`_ : Measures differences in the execution flow of program files.
#. `Tree Edit Distance`_ : Evaluates differences in hierarchical file structures (e.g., XML or JSON).

.. _ControlFlowGraph: https://distancia.readthedocs.io/en/latest/ControlFlowGraph.html
.. _FileTypeDistance: https://distancia.readthedocs.io/en/latest/FileTypeDistance.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Content-Based Measures
----------------------

13. `Hash-Based Distance`_ : Measures differences in file content using hash functions (e.g., MD5, SHA-256).
#. `Bytewise Hamming Distance`_ : Compares files byte by byte to identify dissimilarities.
#. `Entropy-Based Distance`_ : Quantifies the difference in informational content between files.
#. `Character Frequency Distance`_ : Evaluates differences in character distributions.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Hash-Based Distances
-----------------------

17. `HashComparison`_ : Measures the similarity between two files by comparing their cryptographic hash values 'MD5/SHA ).
#. `PerceptualHashing`_ : Utilisé pour comparer deux fichiers d'image ou multimédias en fonction de leur perception visuelle.
#. `SimHash`_ : Used to measure similarity between text documents, especially in the case of large collections of files.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Compression-Based Distances
---------------------------

20. `NormalizedCompressionDistance`_ : Measures the similarity between two files by comparing their individual compression sizes with the compression size of their concatenation, capturing shared structures and patterns.
#. `ZlibBasedDistance`_ : Uses the zlib compression algorithm to evaluate the similarity between files by comparing the effectiveness of compressing them together versus separately.
#. `KolmogorovComplexity`_ : Estimates similarity using algorithmic information theory.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Execution-Based Distances (for executable files)
------------------------------------------------

23. `DynamicBinaryInstrumentation`_ : Measures the difference in the execution behavior of two executable files.
#. `ControlFlowGraph`_ : Compares the control structure of two programs through their control flow graphs.
#. `SystemCallTrace`_ : Compares traces of system calls made by two executable files when they are executed.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Metadata-Based Distances
------------------------

These distances compare files based on their metadata, such as creation date, file size, or permissions. They are useful for identifying differences in file attributes without analyzing content.

26. `FileMetadataComparison`_ : Compares file metadata attributes such as file size, creation date, and permissions, without considering file content.
#. `FileSize`_ : A simple comparison based on the size of the two files, indicating differences in the amount of stored data.
#. `FileTypeDistance`_ : Compare les types de fichiers basés sur leur signature (magic bytes) ou leur format.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html


Text-Based Distances
--------------------

These distances compare files by analyzing their textual content. This category is ideal for comparing documents, code files, or any content-rich text, considering the frequency of words, structural patterns, or semantic meanings.

29. `NgramDistance`_ : Measures the similarity between two files based on the commonality of n-grams (subsequences of length n), useful for text comparison.
#. `BLEUScore`_ : Evaluates the similarity between two text files, typically used in translation quality measurement, by comparing n-grams between reference and candidate texts.
#. `BERTBasedDistance`_ : Uses embeddings generated by language models like BERT to calculate semantic similarity between two documents.
#. `LongestCommonSubsequence`_ : Finds the longest common subsequence between two text files.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Semantic-Based Measures
-----------------------

33. `Cosine`_ : Compares two text files by evaluating the angle between their term frequency vectors, focusing on word distribution and patterns.   
#. `TFIDFDistance`_ : Measures the importance of terms in each document relative to a corpus, providing insight into the textual similarity of two files.  
#. `WordMoversDistance`_ : Uses word vector representations to calculate the semantic distance between two text files.
#. `Embedding-Based Distance`_ : Measures semantic differences using pre-trained embeddings (e.g., FastText, GloVe).

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Image-Based Distances (for multimedia files)
--------------------------------------------

37. `StructuralSimilarityIndex`_ : Compares the perceived quality between two images or videos.
#. `PeakSignalToNoiseRatio`_ : Measures image or video quality based on the maximum possible intensity difference.
#. `HistogramIntersection`_ : Measures the similarity between intensity histograms of image files.
#. `EarthMoversDistance`_ : Used to compare color or texture distributions between two images.
#. `ChiSquareDistance`_ : Measures the similarity of the histograms of two images.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Audio-Based Distances (for audio files)
---------------------------------------

42. `Mel-frequencyCepstralCoefficients`_ : Compares the spectral characteristics of audio files.
#. `PerceptualEvaluationofSpeechQuality`_ : Rates audio quality based on human perception.
#. `CrossCorrelation`_ : Measures the correlation of spectra between two audio files.
#. `SpectrogramDistance`_ : Compares spectrograms of two audio files or sensor data.
#. `CepstralDistance`_ : Measures the difference between the cepstral representations of two audio or voice signals.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Network and Graph-Based Distances
---------------------------------

47. `GraphEditDistance`_ : Compares two files as graphs (like XML or JSON files) by measuring the number of operations needed to transform one graph into another.
#. `Jaccard`_ : Compares the similarity between two graphs based on their common sets of nodes and edges.
#. `Wasserstein`_ : Distance applicable to compare distributions or graphs by treating them as time series or networks.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Time Series-Based Distances (for logs or temporal data)
-------------------------------------------------------

50. `DynamicTimeWarping`_ : Measures the similarity between two time sequences, such as log files or event sequences.
#. `Hausdorff`_ : Used to compare two sets of points or time sequences.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Checksum-Based Measures
-----------------------

52. `CRC (Cyclic Redundancy Check) Distance`_ : Evaluates differences in checksums to detect errors.
#. `Adler-32 Similarity`_ : Measures lightweight checksum similarity.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Application-Specific Measures
-----------------------------

54. `Binary Code Similarity Distance`_ : Used for malware analysis and reverse engineering.
#. `Audio Fingerprint Distance`_ : Compares audio files using unique acoustic fingerprints.
#. `Image File Distance`_ : Compares pixel or feature-based distances for image files.
#. `Video File Distance`_ : Measures frame-based differences in video files.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html


Metadata-Based Measures
-----------------------

58. `File Size Distance`_ : Compares the sizes of files.
#. `Timestamp Distance`_ : Measures the temporal difference between file modification times.
#. `File Format Compatibility Distance`_ : Checks similarity based on file formats.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Signature-Based Measures
------------------------

61. `File Magic Number Distance`_ : Compares file signatures for type detection.
#. `Bloom Filter Similarity`_ : Measures content similarity using probabilistic data structures.
#. `Opcode Sequence Distance`_ : Used for analyzing compiled executable files.

.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html
.. _: https://distancia.readthedocs.io/en/latest/.html

Conclusion
==========

These file distance measures offer diverse methods for comparing files based on their content, structure, metadata, and specific use cases. By leveraging the appropriate distance measure, users can enhance tasks such as file deduplication, version control, and data analysis. This categorization helps in identifying the right measure for specific applications, ensuring optimal results.

The **Distancia** package offers a comprehensive set of file-based distance measures, making it a versatile tool for comparing files of various types and formats. Whether working with text documents, executable binaries, or structured data like XML, the range of distance metrics ensures that you can choose the most appropriate method for your specific needs. By covering different aspects such as content, structure, and metadata, **Distancia** allows for nuanced and robust file comparison, suitable for applications ranging from document analysis to software engineering.

.. _ByteLevelDistance: https://distancia.readthedocs.io/en/latest/ByteLevelDistance.html
.. _HashComparison: https://distancia.readthedocs.io/en/latest/HashComparison.html
.. _NormalizedCompression: https://distancia.readthedocs.io/en/latest/NormalizedCompression.html
.. _KolmogorovComplexity: https://distancia.readthedocs.io/en/latest/KolmogorovComplexity.html
.. _DynamicBinaryInstrumentation: https://distancia.readthedocs.io/en/latest/DynamicBinaryInstrumentation.html
.. _FileMetadataComparison: https://distancia.readthedocs.io/en/latest/FileMetadataComparison.html
.. _FileTypeDistance: https://distancia.readthedocs.io/en/latest/FileTypeDistance.html
.. _TreeEditDistance: https://distancia.readthedocs.io/en/latest/TreeEditDistance.html
.. _ZlibBasedDistance: https://distancia.readthedocs.io/en/latest/ZlibBasedDistance.html
