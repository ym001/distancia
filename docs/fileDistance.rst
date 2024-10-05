File-Based Distances
====================

Introduction
============
In file comparison, evaluating the similarity or difference between two files requires diverse metrics depending on the nature of the files—whether they are text, binary, structured formats like XML, or multimedia. The **Distancia** package offers various distance measures designed to capture differences and similarities in multiple aspects, including file structure, content, and metadata. This range of distances ensures versatility when comparing files for various tasks, from text comparison to file type identification.

Categories 
==========

1. **Binary and File Structure Distances**

#. **Hash-Based Distances**

3. **Compression-Based Distances**

4. **Execution-Based Distances** 
5. **Metadata-Based Distances**
6. **Image-Based Distances**
7. **Text-Based Distances**
8. **Audio-Based Distances**
9. **Network and Graph-Based Distances**
10. **Time Series-Based Distances**

List of of File-Based Distances
===============================

1. **Binary and File Structure Distances**
--------------------------------------

Binary and file structure distances focus on the raw bytes or the structural properties of the files, such as their control flow, byte sequences, or graph-based representations. These methods are useful for comparing executables, XML, JSON, or other structured file formats.

1. :doc:`ControlFlowGraph`

   - Compares the control flow graphs of two executables or structured files, measuring the structural differences in program logic or file structure.

#. :doc:`FileTypeDistance`

   - Identifies differences in file types based on their magic bytes or signatures, determining the nature of the files being compared.

#. :doc:`SystemCallTraceDistance`

   - Compares two executables by analyzing their system call traces during execution, identifying differences in runtime behavior.

4. :doc:`TreeEditDistance`

   - Measures how many modifications (inserts, deletes, or substitutions) are needed to transform the tree structure of one file into another, commonly used in XML or JSON comparisons.

5. :doc:`Hamming`

   - Compares two files at the binary or byte level by counting the number of different bits.

6. :doc:`Levenshtein` 

   - Measures the minimum number of operations required to transform one file into another (insertion, deletion, or substitution of characters/bytes).

7. :doc:`Jaccard` 

- Compares the similarity between two sets of bytes or segments by calculating the ratio of common elements.

8. :doc:`Manhattan` 

   - Sum of absolute differences between corresponding bytes of two files.

9. :doc:`Euclidean` 

-Square root of the sum of the squares of the byte differences between two files.

#. **Hash-Based Distances**
------------------------

1. :doc:`MD5/SHA Hash Comparison`

   - Measures the similarity between two files by comparing their cryptographic hash values.
Perceptual Hash (pHash) : Utilisé pour comparer deux fichiers d'image ou multimédias en fonction de leur perception visuelle.

2. :doc:`SimHash` 

- Used to measure similarity between text documents, especially in the case of large collections of files.

**Compression-Based Distances**
-------------------------------

1. :doc:`NormalizedCompression`

   - Measures the similarity between two files by comparing their individual compression sizes with the compression size of their concatenation, capturing shared structures and patterns.

2. :doc:`Kolmogorov Complexity`

   - Approximée via la compression, elle mesure la quantité d'information partagée entre deux fichiers.

3. :doc:`ZlibCompression`

   - Uses the zlib compression algorithm to evaluate the similarity between files by comparing the effectiveness of compressing them together versus separately.

**Execution-Based Distances (for executable files)**
----------------------------------------------------

1. :doc:`DynamicBinaryInstrumentation` 

   - Measures the difference in the execution behavior of two executable files.

2. :doc:`ControlFlowGraph`

   - Compares the control structure of two programs through their control flow graphs.

3. :doc:`SystemCallTrace` 

   - Compares traces of system calls made by two executable files when they are executed.

**Metadata-Based Distances**
----------------------------

These distances compare files based on their metadata, such as creation date, file size, or permissions. They are useful for identifying differences in file attributes without analyzing content.

1. :doc:`FileMetadataComparison`

   - Compares file metadata attributes such as file size, creation date, and permissions, without considering file content.

2. :doc:`FileSize`

   - A simple comparison based on the size of the two files, indicating differences in the amount of stored data.

3. :doc:`FileTypeDistance` 

   - Compare les types de fichiers basés sur leur signature (magic bytes) ou leur format.

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

5. :doc:`WordMoverDistance`

- Uses word vector representations to calculate the semantic distance between two text files.

6. :doc:`BERT-BasedDistance` 

- Uses embeddings generated by language models like BERT to calculate semantic similarity between two documents.

7. :doc:`LongestCommonSubsequence`

- Finds the longest common subsequence between two text files.

**Image-Based Distances (for multimedia files)**
------------------------------------------------

1. :doc:`StructuralSimilarityIndex` 

- Compares the perceived quality between two images or videos.

2. :doc:`PeakSignal-to-NoiseRatio` 

- Measures image or video quality based on the maximum possible intensity difference.

3. :doc:`HistogramIntersection` 

- Measures the similarity between intensity histograms of image files.

4. :doc:`EarthMoverDistance` 

- Used to compare color or texture distributions between two images.

5. :doc:`Chi-Square` 

- Measures the similarity of the histograms of two images.

**Audio-Based Distances (for audio files)**
-------------------------------------------

1. :doc:`Mel-frequencyCepstralCoefficients` 

- Compares the spectral characteristics of audio files.

2. :doc:`PerceptualEvaluationofSpeechQuality` 

- Rates audio quality based on human perception.

3. :doc:`Cross-Correlation`

- Measures the correlation of spectra between two audio files.

4. :doc:`SpectrogramDistance`

- Compares spectrograms of two audio files or sensor data.

5. :doc:`CepstralDistance`

- Measures the difference between the cepstral representations of two audio or voice signals.

**Network and Graph-Based Distances**
-------------------------------------

1. :doc:`Graph Edit Distance`

- Compares two files as graphs (like XML or JSON files) by measuring the number of operations needed to transform one graph into another.

2. :doc:`Jaccard` 

- Compares the similarity between two graphs based on their common sets of nodes and edges.

3. :doc:`Wasserstein Distance`

- Distance applicable to compare distributions or graphs by treating them as time series or networks.

**Time Series-Based Distances (for logs or temporal data)**
-----------------------------------------------------------

1. :doc:`DynamicTimeWarping`

- Measures the similarity between two time sequences, such as log files or event sequences.

2. :doc:`Hausdorff Distance`

- Used to compare two sets of points or time sequences.


Conclusion
==========
The **Distancia** package offers a comprehensive set of file-based distance measures, making it a versatile tool for comparing files of various types and formats. Whether working with text documents, executable binaries, or structured data like XML, the range of distance metrics ensures that you can choose the most appropriate method for your specific needs. By covering different aspects such as content, structure, and metadata, **Distancia** allows for nuanced and robust file comparison, suitable for applications ranging from document analysis to software engineering.
