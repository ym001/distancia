File-Based Distances
====================

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


**Hash-Based Distances**
------------------------

MD5/SHA Hash Comparison : Mesure la similarité entre deux fichiers en comparant leurs valeurs de hachage cryptographiques.

Perceptual Hash (pHash) : Utilisé pour comparer deux fichiers d'image ou multimédias en fonction de leur perception visuelle.

SimHash : Utilisé pour mesurer la similarité entre documents textuels, en particulier dans le cas des grandes collections de fichiers.


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

   - Mesure la différence dans le comportement d'exécution de deux fichiers exécutables.

2. :doc:`ControlFlowGraph`

   - Compare la structure de contrôle de deux programmes à travers leurs graphes de flux de contrôle.

3. :doc:`SystemCallTrace` 

   - Compare les traces d'appels système effectués par deux fichiers exécutables lors de leur exécution.


**Image-Based Distances (for multimedia files)**
------------------------------------------------

1. :doc:`StructuralSimilarityIndex` 

   - Compare la qualité perçue entre deux images ou vidéos.

2. :doc:`PeakSignal-to-NoiseRatio` 

   - Mesure la qualité de l'image ou de la vidéo en se basant sur la différence maximale d'intensité possible.

3. :doc:`HistogramIntersection` 

   - Mesure la similarité entre les histogrammes d'intensité des fichiers d'image.

4. :doc:`EarthMoverDistance` 

   - Utilisé pour comparer les distributions de couleur ou de texture entre deux images.

5. :doc:`Chi-Square` 

   - Mesure la similarité des histogrammes de deux images.

**Audio-Based Distances (for audio files)**
-------------------------------------------

1. :doc:`Mel-frequencyCepstralCoefficients` 

   - Compare les caractéristiques spectrales des fichiers audio.

2. :doc:`PerceptualEvaluationofSpeechQuality` 

   - Évalue la qualité audio en fonction de la perception humaine.

3. :doc:`Cross-Correlation`

   - Mesure la corrélation des spectres entre deux fichiers audio.

**Network and Graph-Based Distances**
-------------------------------------

1. :doc:`Graph Edit Distance`

   - Compare deux fichiers en tant que graphes (comme les fichiers XML ou JSON) en mesurant le nombre d'opérations nécessaires pour transformer un graphe en un autre.

2. :doc:`Jaccard` 

   - Compare la similarité entre deux graphes basés sur leurs ensembles de nœuds et d’arêtes communs.

3. :doc:`Wasserstein Distance`

   - Distance applicable pour comparer des distributions ou des graphes en les traitant comme des séries temporelles ou des réseaux.


**Metadata-Based Distances**
----------------------------

1. :doc:`FileMetadataComparison`

   - Compare les métadonnées des fichiers, comme les tailles, dates de création, permissions, etc.

2. :doc:`FileTypeDistance` 

   - Compare les types de fichiers basés sur leur signature (magic bytes) ou leur format.


**Signal Processing Distances (for audio and sensor data)**
-----------------------------------------------------------

1. :doc:`Spectrogram Distance`

   - Compare les spectrogrammes de deux fichiers audio ou de données de capteurs.

2. :doc:`Cepstral Distance`

   - Mesure la différence entre les représentations cepstrales de deux signaux audio ou voix.

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
   - Utilise les représentations vectorielles de mots pour calculer la distance sémantique entre deux fichiers texte.

6. :doc:`BERT-BasedDistance` 

   - Utilise les embeddings générés par les modèles de langage comme BERT pour calculer la similarité sémantique entre deux documents.

7. :doc:`LongestCommonSubsequence`

   - Trouve la plus longue sous-séquence commune entre deux fichiers texte.

**Binary and File Structure Distances**
--------------------------------------

Binary and file structure distances focus on the raw bytes or the structural properties of the files, such as their control flow, byte sequences, or graph-based representations. These methods are useful for comparing executables, XML, JSON, or other structured file formats.

1. :doc:`ControlFlowGraph`

   - Compares the control flow graphs of two executables or structured files, measuring the structural differences in program logic or file structure.

2. :doc:`FileTypeDistance`

   - Identifies differences in file types based on their magic bytes or signatures, determining the nature of the files being compared.

3. :doc:`SystemCallTraceDistance`

   - Compares two executables by analyzing their system call traces during execution, identifying differences in runtime behavior.

4. :doc:`TreeEditDistance`

   - Measures how many modifications (inserts, deletes, or substitutions) are needed to transform the tree structure of one file into another, commonly used in XML or JSON comparisons.

5. :doc:`Hamming`

   -Compare deux fichiers au niveau binaire ou des octets en comptant le nombre de bits différents.

6. :doc:`Levenshtein` 

   - Mesure le nombre minimum d'opérations nécessaires pour transformer un fichier en un autre (insertion, suppression, ou substitution de caractères/bytes).

7. :doc:`Jaccard` 

   - Compare la similarité entre deux ensembles d’octets ou de segments en calculant le rapport des éléments en commun.

8. :doc:`Manhattan` 

   - Somme des différences absolues entre les octets correspondants des deux fichiers.

9. :doc:`Euclidean` 

   -Racine carrée de la somme des carrés des différences des octets entre deux fichiers.

**Metadata-Based Distances**
----------------------------

These distances compare files based on their metadata, such as creation date, file size, or permissions. They are useful for identifying differences in file attributes without analyzing content.

1. :doc:`FileMetadataComparison`

   - Compares file metadata attributes such as file size, creation date, and permissions, without considering file content.

2. :doc:`FileSize`

   - A simple comparison based on the size of the two files, indicating differences in the amount of stored data.

**Time Series-Based Distances (for logs or temporal data)**
-----------------------------------------------------------

1. :doc:`DynamicTimeWarping`

   - Mesure la similarité entre deux séquences temporelles, comme des fichiers de log ou des séquences d'événements.

2. :doc:`Hausdorff Distance`

   - Utilisé pour comparer deux ensembles de points ou de séquences temporelles.



Conclusion
==========
The **Distancia** package offers a comprehensive set of file-based distance measures, making it a versatile tool for comparing files of various types and formats. Whether working with text documents, executable binaries, or structured data like XML, the range of distance metrics ensures that you can choose the most appropriate method for your specific needs. By covering different aspects such as content, structure, and metadata, **Distancia** allows for nuanced and robust file comparison, suitable for applications ranging from document analysis to software engineering.
