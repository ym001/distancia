.. Distancia documentation master file, created by
   sphinx-quickstart on Tue Aug 10 14:57:34 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Distancia's documentation!
======================================

**Distancia** is a comprehensive Python package that provides a wide range of distance metrics and similarity measures, making it easy to calculate and compare the proximity between various types of data. This documentation provides an in-depth guide to the package, including installation instructions, usage examples, and detailed descriptions of each available metric.

The documentation is divided into the following sections:

.. note::

   The code examples provided in this documentation are written for Python 3.x.
   The python code in this package has been optimized by static typing with Cython

Getting Started
---------------

Distancia is designed to be simple and intuitive, yet powerful and flexible. Whether you are working with numerical data, strings, or other types of data, Distancia provides the tools you need to measure the similarity or dissimilarity between objects.


For a quick introduction, check out the `quickstart`_ guide. If you want to dive straight into the code, head over to the `Euclidean`_ page.

.. quickstart: https://distancia.readthedocs.io/en/latest/quickstart.html

.. _Euclidean: https://distancia.readthedocs.io/en/latest/Euclidean.html

.. note::

   If you find any issues or have suggestions for improvements, feel free to contribute!

Installation
------------

You can install the distancia package with pip:

.. code-block:: bash

   pip install distancia

By default, this will install the core functionality of the package, suitable for users who only need basic distance metrics.

Optional Dependencies
The distancia package also supports optional modules to enable additional features. You can install these extras depending on your needs:

With pandas support: Install with additional support for working with tabular data:

.. code-block:: bash

   pip install distancia[pandas]

With all supported extras: Install all optional dependencies for maximum functionality:

.. code-block:: bash

   pip install distancia[all]

This modular installation allows you to keep your setup lightweight or include everything for full capabilities.

Quickstart
----------

Here are some common examples of how to use distancia:


.. code-block:: python
   :caption: Example 1: Calculating Euclidean Distance


   from distancia import Euclidean

   point1 = [1, 2, 3]
   point2 = [4, 5, 6]

   # Create an instance of Euclidean
   euclidean = Euclidean()

   # Calculate the Euclidean distance
   distance = euclidean.compute(point1, point2)

   print(f"Euclidean Distance: {distance:4f}")

.. code-block:: bash

   >>>Euclidean Distance: 5.196




.. code-block:: python
   :caption: Example 2: Calculating Levenshtein Distance

   from distancia import Levenshtein

   string1 = "kitten"
   string2 = "sitting"

   distance = Levenshtein().compute(string1, string2)
   print(f"Levenshtein Distance: {distance:4f}")

.. code:: bash

   >>>Levenshtein Distance: 3


For a complete list and detailed explanations of each metric, see the next section.

Available Metrics
-----------------

1. `Vector`_

   + `Euclidean`_
   + `Manhattan`_ 
   + `Jaro`_
   + `KendallTau`_
   + `Bhattacharyya`_
   + `Haversine`_
   + `Chebyshev`_
   + `ContextualDynamicDistance`_
   + `Canberra`_
   + `BrayCurtis`_
   + `RogersTanimoto`_
   + `RussellRao`_
   + `SokalMichener`_
   + `SokalSneath`_
   + `Wasserstein`_
   + `Gower`_
   + `CzekanowskiDice`_
   + `Hellinger`_
   + `MotzkinStraus`_
   + `EnhancedRogersTanimoto`_
   + `KullbackLeibler`_
   + `Jaccard`_
   + `GeneralizedJaccard`_
   + `Tanimoto`_
   + `InverseTanimoto`_
   + `Ochiai`_ 
   + `CzekanowskiDice`_
   + `Pearson`_
   + `Spearman`_ 
   + `FagerMcGowan`_
   + `Otsuka`_ 
   + `Gestalt`_

.. _Vector: https://distancia.readthedocs.io/en/latest/vectorDistance.html
.. _Manhattan: https://distancia.readthedocs.io/en/latest/Manhattan.html
.. _Jaro: https://distancia.readthedocs.io/en/latest/Jaro.html
.. _KendallTau: https://distancia.readthedocs.io/en/latest/KendallTau.html
.. _Bhattacharyya: https://distancia.readthedocs.io/en/latest/Bhattacharyya.html
.. _Haversine: https://distancia.readthedocs.io/en/latest/Haversine.html
.. _Chebyshev: https://distancia.readthedocs.io/en/latest/Chebyshev.html
.. _ContextualDynamicDistance: https://distancia.readthedocs.io/en/latest/ContextualDynamicDistance.html
.. _Canberra: https://distancia.readthedocs.io/en/latest/Canberra.html
.. _BrayCurtis: https://distancia.readthedocs.io/en/latest/BrayCurtis.html
.. _RogersTanimoto: https://distancia.readthedocs.io/en/latest/RogersTanimoto.html
.. _RussellRao: https://distancia.readthedocs.io/en/latest/RussellRao.html
.. _SokalMichener: https://distancia.readthedocs.io/en/latest/SokalMichener.html
.. _SokalSneath: https://distancia.readthedocs.io/en/latest/SokalSneath.html
.. _Wasserstein: https://distancia.readthedocs.io/en/latest/Wasserstein.html
.. _Gower: https://distancia.readthedocs.io/en/latest/Gower.html
.. _CzekanowskiDice: https://distancia.readthedocs.io/en/latest/CzekanowskiDice.html
.. _Hellinger: https://distancia.readthedocs.io/en/latest/Hellinger.html
.. _MotzkinStraus: https://distancia.readthedocs.io/en/latest/MotzkinStraus.html
.. _EnhancedRogersTanimoto: https://distancia.readthedocs.io/en/latest/EnhancedRogersTanimoto.html
.. _KullbackLeibler: https://distancia.readthedocs.io/en/latest/KullbackLeibler.html
.. _Jaccard: https://distancia.readthedocs.io/en/latest/Jaccard.html
.. _GeneralizedJaccard: https://distancia.readthedocs.io/en/latest/GeneralizedJaccard.html
.. _Tanimoto: https://distancia.readthedocs.io/en/latest/Tanimoto.html
.. _InverseTanimoto: https://distancia.readthedocs.io/en/latest/InverseTanimoto.html
.. _Ochiai: https://distancia.readthedocs.io/en/latest/Ochiai.html
.. _CzekanowskiDice: https://distancia.readthedocs.io/en/latest/CzekanowskiDice.html
.. _Pearson: https://distancia.readthedocs.io/en/latest/Pearson.html
.. _Spearman: https://distancia.readthedocs.io/en/latest/Spearman.html
.. _FagerMcGowan: https://distancia.readthedocs.io/en/latest/FagerMcGowan.html
.. _Otsuka: https://distancia.readthedocs.io/en/latest/Otsuka.html
.. _Gestalt: https://distancia.readthedocs.io/en/latest/Gestalt.html

 
2. `Matrix`_

   + `Mahalanobis`_
   + `MahalanobisTaguchi`_
   + `MatrixSpectral`_
   + `NormalizedSpectral`_
   + `PureDiffusion`_
   +  `RandomWalk`_
   + `HeatKernel`_
   + `GraphEditMatrix`_
   + `WeisfeilerLehman`_
   + `NetSimile`_
   + `TriangleMatrixDistance`_
   + `PatternBased`_
   + `CliqueBasedGraph`_
   + `CycleMatrixDistance`_
   + `GraphletMatrixDistance`_
   + `MinimumCutDistanceCalculator`_
   + `Percolation`_

.. _Matrix: https://distancia.readthedocs.io/en/latest/matrixDistance.html
.. _Mahalanobis: https://distancia.readthedocs.io/en/latest/Mahalanobis.html
.. _MahalanobisTaguchi: https://distancia.readthedocs.io/en/latest/MahalanobisTaguchi.html
.. _MatrixSpectral: https://distancia.readthedocs.io/en/latest/MatrixSpectral.html
.. _NormalizedSpectral: https://distancia.readthedocs.io/en/latest/NormalizedSpectral.html
.. _PureDiffusion: https://distancia.readthedocs.io/en/latest/PureDiffusion.html
.. _RandomWalk: https://distancia.readthedocs.io/en/latest/RandomWalk.html
.. _HeatKernel: https://distancia.readthedocs.io/en/latest/HeatKernel.html
.. _GraphEditMatrix: https://distancia.readthedocs.io/en/latest/GraphEditMatrix.html
.. _WeisfeilerLehman: https://distancia.readthedocs.io/en/latest/WeisfeilerLehman.html
.. _NetSimile: https://distancia.readthedocs.io/en/latest/NetSimile.html
.. _TriangleMatrixDistance: https://distancia.readthedocs.io/en/latest/TriangleMatrixDistance.html
.. _PatternBased: https://distancia.readthedocs.io/en/latest/PatternBased.html
.. _CliqueBasedGraph: https://distancia.readthedocs.io/en/latest/CliqueBasedGraph.html
.. _CycleMatrixDistance: https://distancia.readthedocs.io/en/latest/CycleMatrixDistance.html
.. _GraphletMatrixDistance: https://distancia.readthedocs.io/en/latest/GraphletMatrixDistance.html
.. _MinimumCutDistanceCalculator: https://distancia.readthedocs.io/en/latest/MinimumCutDistanceCalculator.html
.. _Percolation: https://distancia.readthedocs.io/en/latest/Percolation.html

3. `Text`_

.. _Text: https://distancia.readthedocs.io/en/latest/textDistance.html

   + `Levenshtein`_
.. _Levenshtein: https://distancia.readthedocs.io/en/latest/Levenshtein.html

   + `DamerauLevenshtein`_
.. _DamerauLevenshtein: https://distancia.readthedocs.io/en/latest/DamerauLevenshtein.html

   + `Hamming`_
.. _Hamming: https://distancia.readthedocs.io/en/latest/Hamming.html

   + `Cosine`_
.. _Cosine: https://distancia.readthedocs.io/en/latest/Cosine.html

   + `TFIDFDistance`_
.. _TFIDFDistance: https://distancia.readthedocs.io/en/latest/TFIDFDistance.html

   + `SimHash`_
.. _SimHash: https://distancia.readthedocs.io/en/latest/SimHash.html

   + `CosineTF`_
.. _CosineTF: https://distancia.readthedocs.io/en/latest/CosineTF.html

   + `WordMoversDistance`_
.. _WordMoversDistance: https://distancia.readthedocs.io/en/latest/WordMoversDistance.html

   + `BERTBasedDistance`_
.. _BERTBasedDistance: https://distancia.readthedocs.io/en/latest/BERTBasedDistance.html

   + `JaroWinkler`_
.. _JaroWinkler: https://distancia.readthedocs.io/en/latest/JaroWinkler.html

   + `OverlapCoefficient`_
.. _OverlapCoefficient: https://distancia.readthedocs.io/en/latest/OverlapCoefficient.html

   + `SorensenDice`_
.. _SorensenDice: https://distancia.readthedocs.io/en/latest/SorensenDice.html

   + `BagOfWordsDistance`_
.. _BagOfWordsDistance: https://distancia.readthedocs.io/en/latest/BagOfWordsDistance.html

   + `FastTextDistance`_
.. _FastTextDistance: https://distancia.readthedocs.io/en/latest/FastTextDistance.html

   + `Dice`_ 
.. _Dice: https://distancia.readthedocs.io/en/latest/Dice.html

   + `Tversky`_ 
.. _Tversky: https://distancia.readthedocs.io/en/latest/Tversky.html

   + `NgramDistance`_
.. _NgramDistance: https://distancia.readthedocs.io/en/latest/NgramDistance.html

   + `SmithWaterman`_
.. _SmithWaterman: https://distancia.readthedocs.io/en/latest/SmithWaterman.html

   + `RatcliffObershelp`_
.. _RatcliffObershelp: https://distancia.readthedocs.io/en/latest/RatcliffObershelp.html

   + `BLEUScore`_
.. _BLEUScore: https://distancia.readthedocs.io/en/latest/BLEUScore.html

   + `ROUGEScore`_
.. _ROUGEScore: https://distancia.readthedocs.io/en/latest/ROUGEScore.html

   + `SoftCosineSimilarity`_
.. _SoftCosineSimilarity: https://distancia.readthedocs.io/en/latest/SoftCosineSimilarity.html

   + `TopicModelingDistance`_
.. _TopicModelingDistance: https://distancia.readthedocs.io/en/latest/TopicModelingDistance.html

   + `AlignmentBasedMeasures`_
.. _AlignmentBasedMeasures: https://distancia.readthedocs.io/en/latest/AlignmentBasedMeasures.html

   + `GappyNGramDistance`_
.. _GappyNGramDistance: https://distancia.readthedocs.io/en/latest/GappyNGramDistance.html

   + `SoftJaccardSimilarity`_
.. _SoftJaccardSimilarity: https://distancia.readthedocs.io/en/latest/SoftJaccardSimilarity.html

   + `NormalizedCompressionDistance`_
.. _NormalizedCompressionDistance: https://distancia.readthedocs.io/en/latest/NormalizedCompressionDistance.html

   + `MongeElkanDistance`_
.. _MongeElkanDistance: https://distancia.readthedocs.io/en/latest/MongeElkanDistance.html

   + `JensenShannonDivergence`_
.. _JensenShannonDivergence: https://distancia.readthedocs.io/en/latest/JensenShannonDivergence.html

4. `Time`_

.. _Time: https://distancia.readthedocs.io/en/latest/timeDistance.html

   DynamicTimeWarping

   LongestCommonSubsequence

   Frechet

5. `Loss`_

.. _Loss: https://distancia.readthedocs.io/en/latest/lossDistance.html

   CrossEntropy

   MeanAbsoluteError

   MeanAbsolutePercentageError

   MeanSquaredError

   SquaredLogarithmicError

   GaloisWassersteinLoss


6. `Graph`_

.. _Graph: https://distancia.readthedocs.io/en/latest/graphDistance.html

   ShortestPath

   GraphEditDistance

   SpectralDistance

   WeisfeilerLehmanSimilarity

   ComparingRandomWalkStationaryDistributions

   Diffusion

   FrobeniusDistance

   GraphKernelDistance

   PatternBasedDistance

   GraphCompressionDistance

   DegreeDistributionDistance

   CommunityStructureDistance

7. `MarkovChaine`_

.. _MarkovChaine: https://distancia.readthedocs.io/en/latest/markovChainDistance.html

   MarkovChainKullbackLeibler

   MarkovChainWasserstein

   MarkovChainTotalVariation

   MarkovChainHellinger

   MarkovChainJensenShannon

   MarkovChainFrobenius

   MarkovChainSpectral

8. `Image`_

.. _Image: https://distancia.readthedocs.io/en/latest/imageDistance.html

   StructuralSimilarityIndex

   PeakSignalToNoiseRatio

   HistogramIntersection

   EarthMoversDistance

   ChiSquareDistance

   FeatureBasedDistance

   PerceptualHashing

   NormalizedCrossCorrelation

9. `Sound`_

.. _Sound: https://distancia.readthedocs.io/en/latest/soundDistance.html

   SpectralConvergence

   MFCCProcessor

   SignalProcessor

   PowerSpectralDensityDistance

   CrossCorrelation

   PhaseDifferenceCalculator

   TimeLagDistance

   PESQ

   LogSpectralDistance

   BarkSpectralDistortion

   ItakuraSaitoDistance

   SignalToNoiseRatio

   EnergyDistance

   EnvelopeCorrelation

   ZeroCrossingRateDistance

   CochleagramDistance

   ChromagramDistance

   SpectrogramDistance

   CQTDistance

10. `File`_


   + `ByteLevelDistance`_
   + `HashComparison`_
   + `NormalizedCompression`_
   + `KolmogorovComplexity`_
   + `DynamicBinaryInstrumentation`_
   + `FileMetadataComparison`_
   + `FileTypeDistance`_
   + `TreeEditDistance`_
   + `ZlibBasedDistance`_

.. _File: https://distancia.readthedocs.io/en/latest/fileDistance.html
.. _ByteLevelDistance: https://distancia.readthedocs.io/en/latest/ByteLevelDistance.html
.. _HashComparison: https://distancia.readthedocs.io/en/latest/HashComparison.html
.. _NormalizedCompression: https://distancia.readthedocs.io/en/latest/NormalizedCompression.html
.. _KolmogorovComplexity: https://distancia.readthedocs.io/en/latest/KolmogorovComplexity.html
.. _DynamicBinaryInstrumentation: https://distancia.readthedocs.io/en/latest/DynamicBinaryInstrumentation.html
.. _FileMetadataComparison: https://distancia.readthedocs.io/en/latest/FileMetadataComparison.html
.. _FileTypeDistance: https://distancia.readthedocs.io/en/latest/FileTypeDistance.html
.. _TreeEditDistance: https://distancia.readthedocs.io/en/latest/TreeEditDistance.html
.. _ZlibBasedDistance: https://distancia.readthedocs.io/en/latest/ZlibBasedDistance.html

And many more...

Overview
--------
The distancia package offers a comprehensive set of tools for computing and analyzing distances and similarities between data points. This package is particularly useful for tasks in data analysis, machine learning, and pattern recognition. Below is an overview of the key classes included in the package, each designed to address specific types of distance or similarity calculations.


   BatchDistance

Purpose: Facilitates batch processing of distance computations, enabling users to compute distances for large sets of pairs in a single operation.

Use Case: Essential in real-time systems or when working with large datasets where efficiency is critical. Batch processing saves time and computational resources by handling multiple distance computations in one go.


   ComprehensiveBenchmarking

Purpose: Provides tools for benchmarking the performance of various distance metrics on different types of data.

Use Case: Useful in performance-sensitive applications where choosing the optimal metric can greatly impact computational efficiency and accuracy. This class helps users make informed decisions about which distance metric to use for their specific task.


   CustomDistanceFunction

Purpose: Allows users to define custom distance functions by specifying a mathematical formula or providing a custom Python function.

Use Case: Useful for researchers or practitioners who need a specific metric that isn’t commonly used or already implemented.


   DistanceMatrix

Purpose: Automatically generates a distance matrix for a set of data points using a specified distance metric.

Use Case: Useful in clustering algorithms like k-means, hierarchical clustering, or in generating heatmaps for visualizing similarity/dissimilarity in datasets.


   DistanceMetricLearning

Purpose: Implements algorithms for learning an optimal distance metric from data based on a specific task, such as classification or clustering.

Use Case: Critical in machine learning tasks where the goal is to optimize a distance metric for maximum task-specific performance, improving the accuracy of models.

   IntegratedDistance

Purpose: Enables seamless integration of distance computations with popular data science libraries like pandas, scikit-learn, and numpy.

Use Case: This class enhances the usability of the distancia package, allowing users to incorporate distance calculations directly into their existing data analysis workflows.

   MetricFinder

Purpose: Identifies the most appropriate distance metric for two given data points based on their structure.

Use Case: Useful when dealing with various types of data, this class helps users automatically determine the best distance metric to apply, ensuring that the metric chosen is suitable for the data's characteristics.


   OutlierDetection

Purpose: Implements methods for detecting outliers in datasets by using distance metrics to identify points that deviate significantly from others.

Use Case: Essential in fields such as fraud detection, quality control, and data cleaning, where identifying and managing outliers is crucial for maintaining data integrity.


   ParallelandDistributedComputation

Purpose: Adds support for parallel or distributed computation of distances, particularly useful for large datasets.

Use Case: In big data scenarios, calculating distances between millions of data points can be computationally expensive. This class significantly reduces computation time by parallelizing these calculations across multiple processors or machines.


   Visualization

Purpose: Provides tools for visualizing distance matrices, dendrograms (for hierarchical clustering), and 2D/3D representations of data points based on distance metrics.

Use Case: Visualization is a powerful tool in exploratory data analysis (EDA), helping users understand the relationships between data points. This class is particularly useful for creating visual aids like heatmaps or dendrograms to better interpret the data.


   APICompatibility

The APICompatibility class in the distancia package bridges the gap between powerful distance computation tools and modern API-based architectures. By enabling the creation of REST endpoints for distance metrics, it facilitates the integration of distancia into a wide range of applications, from web services to distributed computing environments. This not only enhances the usability of the package but also ensures that it can be effectively deployed in real-world, production-grade systems.



   AutomatedDistanceMetricSelection

The AutomatedDistanceMetricSelection feature in the distancia package represents a significant advancement in the ease of use and accessibility of distance metric selection. By automating the process of metric recommendation, it helps users, especially those less familiar with the intricacies of different metrics, to achieve better results in their analyses. This feature not only saves time but also improves the accuracy of data-driven decisions, making distancia a more powerful and user-friendly tool for the data science community.


   ReportingAndDocumentation

The ReportingAndDocumentation class is a powerful tool for automating the analysis and documentation of distance metrics. By integrating report generation, matrix export, and property documentation, it provides users with a streamlined way to evaluate and present the results of their distance-based models. This class is especially valuable for machine learning practitioners who require a deeper understanding of the behavior of the metrics they employ.


   AdvancedAnalysis

The AdvancedAnalysis class provides essential tools for evaluating the performance, robustness, and sensitivity of distance metrics. These advanced analyses ensure that a metric is not only theoretically sound but also practical and reliable in diverse applications. By offering deep insights into the behavior of distance metrics under perturbations, noise, and dataset divisions, this class is crucial for building resilient models in real-world environments.


   DimensionalityReductionAndScaling

The `DimensionalityReductionAndScaling` class offers powerful methods for simplifying and scaling datasets. By providing tools for dimensionality reduction such as Multi-Dimensional Scaling (MDS), it allows users to project high-dimensional data into lower dimensions while retaining its key characteristics.


   ComparisonAndValidation

The ComparisonAndValidation class offers tools to analyze and validate the performance of a distance or similarity metric by comparing it with other metrics and using established benchmarks. This class is essential for evaluating the effectiveness of a metric in various tasks, such as clustering, classification, or retrieval. By providing cross-validation techniques and benchmarking methods, it allows users to gain a deeper understanding of the metric's strengths and weaknesses.


   StatisticalAnalysis

The StatisticalAnalysis class provides essential tools to analyze and interpret the statistical properties of distances or similarities within a dataset. Through the computation of mean, variance, and distance distributions, 

Contributing
------------

We welcome contributions! If you would like to contribute to distancia, please read the `contributing`_ guide to get started. We appreciate your help in making this project better.

.. contributing: https://distancia.readthedocs.io/en/latest/CONTRIBUTING.html


Link
----


+ `Notebook`_
   + `vectorDistance`_
   + `matrixDistance`_
   +  `textDistance`_
   +  `graphDistance`_
   +  `MarkovChain`_
   +  `Loss_function`_
   +  `distance`_
   +  `fileDistance`_
   +  `lossDistance`_
   +  `similarity`_
   +  `imageDistance`_
   +  `soundDistance`_
   +  `timeSeriesDistance`_

.. _Notebook: https://github.com/ym001/distancia/tree/master/notebook

.. _vectorDistance: https://github.com/ym001/distancia/blob/master/notebook/vectorDistance.ipynb

.. _matrixDistance: https://github.com/ym001/distancia/blob/master/notebook/matrixDistance.ipynb

.. _textDistance: https://github.com/ym001/distancia/blob/master/notebook/textDistance.ipynb

.. _graphDistance: https://github.com/ym001/distancia/blob/master/notebook/graphDistance.ipynb

.. _MarkovChain: https://github.com/ym001/distancia/blob/master/notebook/MarkovChain.ipynb

.. _Loss_function: https://github.com/ym001/distancia/blob/master/notebook/Loss_function.ipynb

.. _distance: https://github.com/ym001/distancia/blob/master/notebook/distance.ipynb

.. _fileDistance: https://github.com/ym001/distancia/blob/master/notebook/fileDistance.ipynb

.. _lossDistance: https://github.com/ym001/distancia/blob/master/notebook/lossDistance.ipynb

.. _similarity: https://github.com/ym001/distancia/blob/master/notebook/similarity.ipynb

.. _imageDistance: https://github.com/ym001/distancia/blob/master/notebook/imageDistance.ipynb

.. _soundDistance: https://github.com/ym001/distancia/blob/master/notebook/soundDistance.ipynb

.. _timeSeriesDistance: https://github.com/ym001/distancia/blob/master/notebook/timeSeriesDistance.ipynb




+ `Exemples`_
.. _Exemples: https://github.com/ym001/distancia/blob/master/src/exemple.py
+ `Pypi`_
.. _Pypi: https://pypi.org/project/distancia/
+ `Source`_
.. _Source: https://github.com/ym001/distancia
+ `Documentation`_
.. _Documentation: https://distancia.readthedocs.io/en/latest/
+ `License`_
.. _License: https://github.com/ym001/distancia/blob/master/LICENSE

Conclusion
----------

The distancia package offers a versatile toolkit for handling a wide range of distance and similarity calculations. Whether you're working with numeric data, categorical data, strings, or time series, the package's classes provide the necessary tools to accurately measure distances and similarities. By understanding and utilizing these classes, you can enhance your data analysis workflows and improve the performance of your machine learning models.

