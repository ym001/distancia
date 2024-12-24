====================
File-Based Distances
====================

.. sectnum::
   start: 3

Introduction
============
In file comparison, evaluating the similarity or difference between two files requires diverse metrics depending on the nature of the files—whether they are text, binary, structured formats like XML, or multimedia. The **Distancia** package offers various distance measures designed to capture differences and similarities in multiple aspects, including file structure, content, and metadata. This range of distances ensures versatility when comparing files for various tasks, from text comparison to file type identification.

Categories 
==========

1. **Binary and File Structure Distances**

#. **Hash-Based Distances**

#. **Compression-Based Distances**

#. **Execution-Based Distances** 

#. **Metadata-Based Distances**

#. **Image-Based Distances**

#. **Text-Based Distances**

#. **Audio-Based Distances**

#. **Network and Graph-Based Distances**

#. **Time Series-Based Distances**

List of File-Based Distances
===============================


Binary and File Structure Distances
-----------------------------------

Binary and file structure distances focus on the raw bytes or the structural properties of the files, such as their control flow, byte sequences, or graph-based representations. These methods are useful for comparing executables, XML, JSON, or other structured file formats.

   1. :doc:`ControlFlowGraph`

      - Compares the control flow graphs of two executables or structured files, measuring the structural differences in program logic or file structure.

   #. :doc:`FileTypeDistance`

      - Identifies differences in file types based on their magic bytes or signatures, determining the nature of the files being compared.

   #. :doc:`SystemCallTraceDistance`

      - Compares two executables by analyzing their system call traces during execution, identifying differences in runtime behavior.

   #. :doc:`TreeEditDistance`

      - Measures how many modifications (inserts, deletes, or substitutions) are needed to transform the tree structure of one file into another, commonly used in XML or JSON comparisons.

   #. :doc:`Hamming`

      - Compares two files at the binary or byte level by counting the number of different bits.

   #. :doc:`Levenshtein` 

      - Measures the minimum number of operations required to transform one file into another (insertion, deletion, or substitution of characters/bytes).

   #. :doc:`Jaccard` 

      - Compares the similarity between two sets of bytes or segments by calculating the ratio of common elements.

   #. :doc:`Manhattan` 

      - Sum of absolute differences between corresponding bytes of two files.

   #. :doc:`Euclidean` 

      - Square root of the sum of the squares of the byte differences between two files.

Content-Based Measures
----------------------

   - **Hash-Based Distance:** Measures differences in file content using hash functions (e.g., MD5, SHA-256).
   - **Bytewise Hamming Distance:** Compares files byte by byte to identify dissimilarities.
   - **Entropy-Based Distance:** Quantifies the difference in informational content between files.
   - **Character Frequency Distance:** Evaluates differences in character distributions.

Hash-Based Distances
-----------------------

   1. :doc:`HashComparison`

      - Measures the similarity between two files by comparing their cryptographic hash values 'MD5/SHA ).

   #. :doc:`PerceptualHashing` 

      - Utilisé pour comparer deux fichiers d'image ou multimédias en fonction de leur perception visuelle.

   #. :doc:`SimHash` 

      - Used to measure similarity between text documents, especially in the case of large collections of files.

Compression-Based Distances
---------------------------

   1. :doc:`NormalizedCompressionDistance` Measures the similarity between two files by comparing their individual compression sizes with the compression size of their concatenation, capturing shared structures and patterns.
   #. :doc:`ZlibBasedDistance` Uses the zlib compression algorithm to evaluate the similarity between files by comparing the effectiveness of compressing them together versus separately.
   - **KolmogorovComplexity:** Estimates similarity using algorithmic information theory.

Execution-Based Distances (for executable files)
------------------------------------------------

   1. :doc:`DynamicBinaryInstrumentation` 

      - Measures the difference in the execution behavior of two executable files.

   #. :doc:`ControlFlowGraph`

      - Compares the control structure of two programs through their control flow graphs.

   #. :doc:`SystemCallTrace` 

      - Compares traces of system calls made by two executable files when they are executed.

Metadata-Based Distances
------------------------

These distances compare files based on their metadata, such as creation date, file size, or permissions. They are useful for identifying differences in file attributes without analyzing content.

   1. :doc:`FileMetadataComparison`

      - Compares file metadata attributes such as file size, creation date, and permissions, without considering file content.
   
   #. :doc:`FileSize`

      - A simple comparison based on the size of the two files, indicating differences in the amount of stored data.

   #. :doc:`FileTypeDistance` 

      - Compare les types de fichiers basés sur leur signature (magic bytes) ou leur format.


Text-Based Distances
--------------------

These distances compare files by analyzing their textual content. This category is ideal for comparing documents, code files, or any content-rich text, considering the frequency of words, structural patterns, or semantic meanings.

#. :doc:`NgramDistance` Measures the similarity between two files based on the commonality of n-grams (subsequences of length n), useful for text comparison.
#. :doc:`BLEUScore` Evaluates the similarity between two text files, typically used in translation quality measurement, by comparing n-grams between reference and candidate texts.
#. :doc:`BERTBasedDistance` Uses embeddings generated by language models like BERT to calculate semantic similarity between two documents.
#. :doc:`LongestCommonSubsequence` Finds the longest common subsequence between two text files.

Semantic-Based Measures
-----------------------

#. :doc:`Cosine` Compares two text files by evaluating the angle between their term frequency vectors, focusing on word distribution and patterns.   
1. :doc:`TFIDFDistance` Measures the importance of terms in each document relative to a corpus, providing insight into the textual similarity of two files.  
#. :doc:`WordMoversDistance` Uses word vector representations to calculate the semantic distance between two text files.
   - **Embedding-Based Distance:** Measures semantic differences using pre-trained embeddings (e.g., FastText, GloVe).

Image-Based Distances (for multimedia files)
--------------------------------------------

   1. :doc:`StructuralSimilarityIndex` 

      - Compares the perceived quality between two images or videos.

   #. :doc:`PeakSignalToNoiseRatio` 

      - Measures image or video quality based on the maximum possible intensity difference.

   #. :doc:`HistogramIntersection` 

      - Measures the similarity between intensity histograms of image files.

   #. :doc:`EarthMoversDistance` 

      - Used to compare color or texture distributions between two images.

   #. :doc:`ChiSquareDistance` 

      - Measures the similarity of the histograms of two images.

Audio-Based Distances (for audio files)
---------------------------------------

   1. :doc:`Mel-frequencyCepstralCoefficients` 
   
      - Compares the spectral characteristics of audio files.

   #. :doc:`PerceptualEvaluationofSpeechQuality` 

      - Rates audio quality based on human perception.

   #. :doc:`CrossCorrelation`

      - Measures the correlation of spectra between two audio files.

   #. :doc:`SpectrogramDistance`

      - Compares spectrograms of two audio files or sensor data.

   #. :doc:`CepstralDistance`

      - Measures the difference between the cepstral representations of two audio or voice signals.

Network and Graph-Based Distances
---------------------------------

   1. :doc:`GraphEditDistance`

      - Compares two files as graphs (like XML or JSON files) by measuring the number of operations needed to transform one graph into another.

   #. :doc:`Jaccard` 

      - Compares the similarity between two graphs based on their common sets of nodes and edges.

   #. :doc:`Wasserstein`

      - Distance applicable to compare distributions or graphs by treating them as time series or networks.

Time Series-Based Distances (for logs or temporal data)
-------------------------------------------------------

   1. :doc:`DynamicTimeWarping`

      - Measures the similarity between two time sequences, such as log files or event sequences.

   #. :doc:`Hausdorff`

      - Used to compare two sets of points or time sequences.

Checksum-Based Measures
-----------------------

   - **CRC (Cyclic Redundancy Check) Distance:** Evaluates differences in checksums to detect errors.
   - **Adler-32 Similarity:** Measures lightweight checksum similarity.

Application-Specific Measures
-----------------------------

   - **Binary Code Similarity Distance:** Used for malware analysis and reverse engineering.
   - **Audio Fingerprint Distance:** Compares audio files using unique acoustic fingerprints.
   - **Image File Distance:** Compares pixel or feature-based distances for image files.
   - **Video File Distance:** Measures frame-based differences in video files.
============================
File Distance Measures
============================

Introduction
=============
File distance measures are used to quantify the similarity or dissimilarity between files based on their content, structure, or metadata. These measures are critical in file deduplication, malware analysis, and version control systems.

Below is a comprehensive list of file distance measures, grouped into relevant categories.

Categorized Distance Measures
=============================



2. **Structure-Based Measures**
   - **AST (Abstract Syntax Tree) Distance:** Compares the syntactic structure of code files.
   - **Control Flow Graph (CFG) Distance:** Measures differences in the execution flow of program files.
   - **Tree Edit Distance:** Evaluates differences in hierarchical file structures (e.g., XML or JSON).


4. **Metadata-Based Measures**
   - **File Size Distance:** Compares the sizes of files.
   - **Timestamp Distance:** Measures the temporal difference between file modification times.
   - **File Format Compatibility Distance:** Checks similarity based on file formats.





7. **Signature-Based Measures**
   - **File Magic Number Distance:** Compares file signatures for type detection.
   - **Bloom Filter Similarity:** Measures content similarity using probabilistic data structures.
   - **Opcode Sequence Distance:** Used for analyzing compiled executable files.



Conclusion
==========
These file distance measures offer diverse methods for comparing files based on their content, structure, metadata, and specific use cases. By leveraging the appropriate distance measure, users can enhance tasks such as file deduplication, version control, and data analysis. This categorization helps in identifying the right measure for specific applications, ensuring optimal results.


The **Distancia** package offers a comprehensive set of file-based distance measures, making it a versatile tool for comparing files of various types and formats. Whether working with text documents, executable binaries, or structured data like XML, the range of distance metrics ensures that you can choose the most appropriate method for your specific needs. By covering different aspects such as content, structure, and metadata, **Distancia** allows for nuanced and robust file comparison, suitable for applications ranging from document analysis to software engineering.
