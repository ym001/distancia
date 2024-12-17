.. meta::
   :description: Distancia is a comprehensive Python package that provides a wide range of distance metrics and similarity measures, making it easy to calculate and compare the proximity between various types of data. This documentation provides an in-depth guide to the package, including installation instructions, usage examples, and detailed descriptions of each available metric.


   :keywords: data-science machine-learning deep-learning neural-network graph text-classification text distance cython markov-chain file similarity image-classification nlp-machine-learning loss-functions distancia
   :keywords lang=en: data-science machine-learning deep-learning neural-network graph text-classification text distance cython markov-chain file similarity image-classification nlp-machine-learning loss-functions distancia
======================================
Welcome to Distancia's documentation!
======================================


**Distancia** is a comprehensive Python package that provides a wide range of distance metrics and similarity measures, making it easy to calculate and compare the proximity between various types of data. This documentation provides an in-depth guide to the package, including installation instructions, usage examples, and detailed descriptions of each available metric.

The documentation is divided into the following sections:

.. note::

   The code examples provided in this documentation are written for Python 3.x.
   The python code in this package has been optimized by static typing with Cython

*Getting Started*
---------------

**Distancia** is designed to be simple and intuitive, yet powerful and flexible. Whether you are working with numerical data, strings, or other types of data, Distancia provides the tools you need to measure the distance or similarity between objects.


For a quick introduction, check out the `quickstart`_ guide. If you want to dive straight into the code, head over to the `Euclidean`_ page.

.. quickstart: https://distancia.readthedocs.io/en/latest/quickstart.html

.. _Euclidean: https://distancia.readthedocs.io/en/latest/Euclidean.html

.. note::

   If you find any issues or have suggestions for improvements, feel free to contribute!

*Installation*
------------

You can install the distancia package with pip:

.. code-block:: bash

   pip install distancia

By default, this will install the core functionality of the package, suitable for users who only need basic distance metrics.

Optional Dependencies
The **Distancia** package also supports optional modules to enable additional features. You can install these extras depending on your needs:

With pandas support: Install with additional support for working with tabular data:

.. code-block:: bash

   pip install distancia[pandas]

With all supported extras: Install all optional dependencies for maximum functionality:

.. code-block:: bash

   pip install distancia[all]

This modular installation allows you to keep your setup lightweight or include everything for full capabilities.

*Quickstart*
----------

Here are some common examples of how to use **Distancia**:

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

*Available Metrics*
-------------------

.. _Vector: https://distancia.readthedocs.io/en/latest/vectorDistance.html
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


.. _Text: https://distancia.readthedocs.io/en/latest/textDistance.html
.. _Levenshtein: https://distancia.readthedocs.io/en/latest/Levenshtein.html
.. _DamerauLevenshtein: https://distancia.readthedocs.io/en/latest/DamerauLevenshtein.html
.. _Hamming: https://distancia.readthedocs.io/en/latest/Hamming.html
.. _Cosine: https://distancia.readthedocs.io/en/latest/Cosine.html
.. _TFIDFDistance: https://distancia.readthedocs.io/en/latest/TFIDFDistance.html
.. _SimHash: https://distancia.readthedocs.io/en/latest/SimHash.html
.. _CosineTF: https://distancia.readthedocs.io/en/latest/CosineTF.html
.. _WordMoversDistance: https://distancia.readthedocs.io/en/latest/WordMoversDistance.html
.. _BERTBasedDistance: https://distancia.readthedocs.io/en/latest/BERTBasedDistance.html
.. _JaroWinkler: https://distancia.readthedocs.io/en/latest/JaroWinkler.html
.. _OverlapCoefficient: https://distancia.readthedocs.io/en/latest/OverlapCoefficient.html
.. _SorensenDice: https://distancia.readthedocs.io/en/latest/SorensenDice.html
.. _BagOfWordsDistance: https://distancia.readthedocs.io/en/latest/BagOfWordsDistance.html
.. _FastTextDistance: https://distancia.readthedocs.io/en/latest/FastTextDistance.html
.. _Dice: https://distancia.readthedocs.io/en/latest/Dice.html
.. _Tversky: https://distancia.readthedocs.io/en/latest/Tversky.html
.. _NgramDistance: https://distancia.readthedocs.io/en/latest/NgramDistance.html
.. _SmithWaterman: https://distancia.readthedocs.io/en/latest/SmithWaterman.html
.. _RatcliffObershelp: https://distancia.readthedocs.io/en/latest/RatcliffObershelp.html
.. _BLEUScore: https://distancia.readthedocs.io/en/latest/BLEUScore.html
.. _ROUGEScore: https://distancia.readthedocs.io/en/latest/ROUGEScore.html
.. _SoftCosineSimilarity: https://distancia.readthedocs.io/en/latest/SoftCosineSimilarity.html
.. _TopicModelingDistance: https://distancia.readthedocs.io/en/latest/TopicModelingDistance.html
.. _AlignmentBasedMeasures: https://distancia.readthedocs.io/en/latest/AlignmentBasedMeasures.html
.. _GappyNGramDistance: https://distancia.readthedocs.io/en/latest/GappyNGramDistance.html
.. _SoftJaccardSimilarity: https://distancia.readthedocs.io/en/latest/SoftJaccardSimilarity.html
.. _NormalizedCompressionDistance: https://distancia.readthedocs.io/en/latest/NormalizedCompressionDistance.html
.. _MongeElkanDistance: https://distancia.readthedocs.io/en/latest/MongeElkanDistance.html
.. _JensenShannonDivergence: https://distancia.readthedocs.io/en/latest/JensenShannonDivergence.html


.. _Time: https://distancia.readthedocs.io/en/latest/timeDistance.html
.. _DynamicTimeWarping: https://distancia.readthedocs.io/en/latest/DynamicTimeWarping.html
.. _LongestCommonSubsequence: https://distancia.readthedocs.io/en/latest/LongestCommonSubsequence.html
.. _Frechet: https://distancia.readthedocs.io/en/latest/Frechet.html

+ `Vector`_ 
    - `Euclidean`_
    - `Manhattan`_ 
    - `Bhattacharyya`_
    - `Haversine`_
    - `Chebyshev`_
    - `ContextualDynamicDistance`_
    - `Canberra`_
    - `BrayCurtis`_
    - `RogersTanimoto`_
    - `RussellRao`_
    - `SokalMichener`_
    - `SokalSneath`_
    - `Wasserstein`_
    - `Gower`_
    - `CzekanowskiDice`_
    - `Hellinger`_
    - `MotzkinStraus`_
    - `EnhancedRogersTanimoto`_
    - `KullbackLeibler`_
    - `Jaccard`_
    - `GeneralizedJaccard`_
    - `Tanimoto`_
    - `InverseTanimoto`_
    - `Ochiai`_ 
    - `CzekanowskiDice`_
    - `Pearson`_
    - `Spearman`_ 
    - `FagerMcGowan`_
    - `Otsuka`_ 
    - `Gestalt`_

+ `Matrix`_
    - `Mahalanobis`_
    - `MahalanobisTaguchi`_
    - `MatrixSpectral`_
    - `NormalizedSpectral`_
    - `PureDiffusion`_
    - `RandomWalk`_
    - `HeatKernel`_
    - `GraphEditMatrix`_
    - `WeisfeilerLehman`_
    - `NetSimile`_
    - `TriangleMatrixDistance`_
    - `PatternBased`_
    - `CliqueBasedGraph`_
    - `CycleMatrixDistance`_
    - `GraphletMatrixDistance`_
    - `MinimumCutDistanceCalculator`_
    - `Percolation`_

+ `Text`_
    - `Levenshtein`_
    - `DamerauLevenshtein`_
    - `Hamming`_
    - `Cosine`_
    - `TFIDFDistance`_
    - `SimHash`_
    - `CosineTF`_
    - `WordMoversDistance`_
    - `BERTBasedDistance`_
    - `Jaro`_
    - `JaroWinkler`_
    - `OverlapCoefficient`_
    - `SorensenDice`_
    - `BagOfWordsDistance`_
    - `FastTextDistance`_
    - `Dice`_ 
    - `Tversky`_ 
    - `NgramDistance`_
    - `SmithWaterman`_
    - `RatcliffObershelp`_
    - `BLEUScore`_
    - `ROUGEScore`_
    - `SoftCosineSimilarity`_
    - `TopicModelingDistance`_
    - `AlignmentBasedMeasures`_
    - `GappyNGramDistance`_
    - `SoftJaccardSimilarity`_
    - `NormalizedCompressionDistance`_
    - `MongeElkanDistance`_
    - `JensenShannonDivergence`_
+ 'statistics'
    - `KendallTau`_

+ `Time`_
    - `DynamicTimeWarping`_
    - `LongestCommonSubsequence`_
    - `Frechet`_


+ `Loss`_
    - `CrossEntropy`_
    - `MeanAbsoluteError`_
    - `MeanAbsolutePercentageError`_
    - `MeanSquaredError`_
    - `SquaredLogarithmicError`_
    - `GaloisWassersteinLoss`_

.. _Loss: https://distancia.readthedocs.io/en/latest/lossDistance.html
.. _CrossEntropy: https://distancia.readthedocs.io/en/latest/CrossEntropy.html
.. _MeanAbsoluteError: https://distancia.readthedocs.io/en/latest/MeanAbsoluteError.html
.. _MeanAbsolutePercentageError: https://distancia.readthedocs.io/en/latest/MeanAbsolutePercentageError.html
.. _MeanSquaredError: https://distancia.readthedocs.io/en/latest/MeanSquaredError.html
.. _SquaredLogarithmicError: https://distancia.readthedocs.io/en/latest/SquaredLogarithmicError.html
.. _GaloisWassersteinLoss: https://distancia.readthedocs.io/en/latest/GaloisWassersteinLoss.html

+ `Graph`_
    - `ShortestPath`_
    - `GraphEditDistance`_
    - `SpectralDistance`_
    - `WeisfeilerLehmanSimilarity`_
    - `ComparingRandomWalkStationaryDistributions`_
    - `Diffusion`_
    - `FrobeniusDistance`_
    - `GraphKernelDistance`_
    - `PatternBasedDistance`_
    - `GraphCompressionDistance`_
    - `DegreeDistributionDistance`_
    - `CommunityStructureDistance`_

.. _Graph: https://distancia.readthedocs.io/en/latest/graphDistance.html
.. _ShortestPath: https://distancia.readthedocs.io/en/latest/ShortestPath.html
.. _GraphEditDistance: https://distancia.readthedocs.io/en/latest/GraphEditDistance.html
.. _SpectralDistance: https://distancia.readthedocs.io/en/latest/SpectralDistance.html
.. _WeisfeilerLehmanSimilarity: https://distancia.readthedocs.io/en/latest/WeisfeilerLehmanSimilarity.html
.. _ComparingRandomWalkStationaryDistributions: https://distancia.readthedocs.io/en/latest/ComparingRandomWalkStationaryDistributions.html
.. _Diffusion: https://distancia.readthedocs.io/en/latest/Diffusion.html
.. _FrobeniusDistance: https://distancia.readthedocs.io/en/latest/FrobeniusDistance.html
.. _GraphKernelDistance: https://distancia.readthedocs.io/en/latest/GraphKernelDistance.html
.. _PatternBasedDistance: https://distancia.readthedocs.io/en/latest/PatternBasedDistance.html
.. _GraphCompressionDistance: https://distancia.readthedocs.io/en/latest/GraphCompressionDistance.html
.. _DegreeDistributionDistance: https://distancia.readthedocs.io/en/latest/DegreeDistributionDistance.html
.. _CommunityStructureDistance: https://distancia.readthedocs.io/en/latest/CommunityStructureDistance.html

+ `MarkovChaine`_
    - `MarkovChainKullbackLeibler`_
    - `MarkovChainWasserstein`_
    - `MarkovChainTotalVariation`_
    - `MarkovChainHellinger`_
    - `MarkovChainJensenShannon`_
    - `MarkovChainFrobenius`_
    - `MarkovChainSpectral`_

.. _MarkovChaine: https://distancia.readthedocs.io/en/latest/markovChainDistance.html
.. _MarkovChainKullbackLeibler: https://distancia.readthedocs.io/en/latest/MarkovChainKullbackLeibler.html
.. _MarkovChainWasserstein: https://distancia.readthedocs.io/en/latest/MarkovChainWasserstein.html
.. _MarkovChainTotalVariation: https://distancia.readthedocs.io/en/latest/MarkovChainTotalVariation.html
.. _MarkovChainHellinger: https://distancia.readthedocs.io/en/latest/MarkovChainHellinger.html
.. _MarkovChainJensenShannon: https://distancia.readthedocs.io/en/latest/MarkovChainJensenShannon.html
.. _MarkovChainFrobenius: https://distancia.readthedocs.io/en/latest/MarkovChainFrobenius.html
.. _MarkovChainSpectral: https://distancia.readthedocs.io/en/latest/MarkovChainSpectral.html

+ `Image`_
    - `StructuralSimilarityIndex`_
    - `PeakSignalToNoiseRatio`_
    - `HistogramIntersection`_
    - `EarthMoversDistance`_
    - `ChiSquareDistance`_
    - `FeatureBasedDistance`_
    - `PerceptualHashing`_
    - `NormalizedCrossCorrelation`_

.. _Image: https://distancia.readthedocs.io/en/latest/imageDistance.html
.. _StructuralSimilarityIndex: https://distancia.readthedocs.io/en/latest/StructuralSimilarityIndex.html
.. _PeakSignalToNoiseRatio: https://distancia.readthedocs.io/en/latest/PeakSignalToNoiseRatio.html
.. _HistogramIntersection: https://distancia.readthedocs.io/en/latest/HistogramIntersection.html
.. _EarthMoversDistance: https://distancia.readthedocs.io/en/latest/EarthMoversDistance.html
.. _ChiSquareDistance: https://distancia.readthedocs.io/en/latest/ChiSquareDistance.html
.. _FeatureBasedDistance: https://distancia.readthedocs.io/en/latest/FeatureBasedDistance.html
.. _PerceptualHashing: https://distancia.readthedocs.io/en/latest/PerceptualHashing.html
.. _NormalizedCrossCorrelation: https://distancia.readthedocs.io/en/latest/NormalizedCrossCorrelation.html

+ `Sound`_
    - `SpectralConvergence`_
    - `MFCCProcessor`_
    - `SignalProcessor`_
    - `PowerSpectralDensityDistance`_
    - `CrossCorrelation`_
    - `PhaseDifferenceCalculator`_
    - `TimeLagDistance`_
    - `PESQ`_
    -  `LogSpectralDistance`_
    - `BarkSpectralDistortion`_
    - `ItakuraSaitoDistance`_
    - `SignalToNoiseRatio`_
    - `EnergyDistance`_
    -  `EnvelopeCorrelation`_
    - `ZeroCrossingRateDistance`_
    - `CochleagramDistance`_
    - `ChromagramDistance`_
    - `SpectrogramDistance`_
    - `CQTDistance`_

.. _Sound: https://distancia.readthedocs.io/en/latest/soundDistance.html
.. _SpectralConvergence: https://distancia.readthedocs.io/en/latest/SpectralConvergence.html
.. _MFCCProcessor: https://distancia.readthedocs.io/en/latest/MFCCProcessor.html
.. _SignalProcessor: https://distancia.readthedocs.io/en/latest/SignalProcessor.html
.. _PowerSpectralDensityDistance: https://distancia.readthedocs.io/en/latest/PowerSpectralDensityDistance.html
.. _CrossCorrelation: https://distancia.readthedocs.io/en/latest/CrossCorrelation.html
.. _PhaseDifferenceCalculator: https://distancia.readthedocs.io/en/latest/PhaseDifferenceCalculator.html
.. _TimeLagDistance: https://distancia.readthedocs.io/en/latest/TimeLagDistance.html
.. _PESQ: https://distancia.readthedocs.io/en/latest/PESQ.html
.. _LogSpectralDistance: https://distancia.readthedocs.io/en/latest/LogSpectralDistance.html
.. _BarkSpectralDistortion: https://distancia.readthedocs.io/en/latest/BarkSpectralDistortion.html
.. _ItakuraSaitoDistance: https://distancia.readthedocs.io/en/latest/ItakuraSaitoDistance.html
.. _SignalToNoiseRatio: https://distancia.readthedocs.io/en/latest/SignalToNoiseRatio.html
.. _EnergyDistance: https://distancia.readthedocs.io/en/latest/EnergyDistance.html
.. _EnvelopeCorrelation: https://distancia.readthedocs.io/en/latest/EnvelopeCorrelation.html
.. _ZeroCrossingRateDistance: https://distancia.readthedocs.io/en/latest/ZeroCrossingRateDistance.html
.. _CochleagramDistance: https://distancia.readthedocs.io/en/latest/CochleagramDistance.html
.. _ChromagramDistance: https://distancia.readthedocs.io/en/latest/ChromagramDistance.html
.. _SpectrogramDistance: https://distancia.readthedocs.io/en/latest/SpectrogramDistance.html
.. _CQTDistance: https://distancia.readthedocs.io/en/latest/CQTDistance.html

+ `File`_
    - `ByteLevelDistance`_
    - `HashComparison`_
    - `NormalizedCompression`_
    - `KolmogorovComplexity`_
    - `DynamicBinaryInstrumentation`_
    - `FileMetadataComparison`_
    - `FileTypeDistance`_
    - `TreeEditDistance`_
    - `ZlibBasedDistance`_

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

*Overview*
--------
The distancia package offers a comprehensive set of tools for computing and analyzing distances and similarities between data points. This package is particularly useful for tasks in data analysis, machine learning, and pattern recognition. Below is an overview of the key classes included in the package, each designed to address specific types of distance or similarity calculations.


+ `BatchDistance`_

.. _BatchDistance: https://distancia.readthedocs.io/en/latest/BatchDistance.html

Purpose: Facilitates batch processing of distance computations, enabling users to compute distances for large sets of pairs in a single operation.

Use Case: Essential in real-time systems or when working with large datasets where efficiency is critical. Batch processing saves time and computational resources by handling multiple distance computations in one go.

+ `ComprehensiveBenchmarking`_

.. _ComprehensiveBenchmarking: https://distancia.readthedocs.io/en/latest/ComprehensiveBenchmarking.html

Purpose: Provides tools for benchmarking the performance of various distance metrics on different types of data.

Use Case: Useful in performance-sensitive applications where choosing the optimal metric can greatly impact computational efficiency and accuracy. This class helps users make informed decisions about which distance metric to use for their specific task.

+ `CustomDistanceFunction`_
.. _CustomDistanceFunction: https://distancia.readthedocs.io/en/latest/CustomDistanceFunction.html

Purpose: Allows users to define custom distance functions by specifying a mathematical formula or providing a custom Python function.

Use Case: Useful for researchers or practitioners who need a specific metric that isn’t commonly used or already implemented.

+ `DistanceMatrix`_
.. _DistanceMatrix: https://distancia.readthedocs.io/en/latest/DistanceMatrix.html

Purpose: Automatically generates a distance matrix for a set of data points using a specified distance metric.

Use Case: Useful in clustering algorithms like k-means, hierarchical clustering, or in generating heatmaps for visualizing similarity/dissimilarity in datasets.

+ `DistanceMetricLearning`_
.. _DistanceMetricLearning: https://distancia.readthedocs.io/en/latest/DistanceMetricLearning.html

Purpose: Implements algorithms for learning an optimal distance metric from data based on a specific task, such as classification or clustering.

Use Case: Critical in machine learning tasks where the goal is to optimize a distance metric for maximum task-specific performance, improving the accuracy of models.

+ `IntegratedDistance`_
.. _IntegratedDistance: https://distancia.readthedocs.io/en/latest/IntegratedDistance.html

Purpose: Enables seamless integration of distance computations with popular data science libraries like pandas, scikit-learn, and numpy.

Use Case: This class enhances the usability of the distancia package, allowing users to incorporate distance calculations directly into their existing data analysis workflows.

+ `MetricFinder`_
.. _MetricFinder: https://distancia.readthedocs.io/en/latest/MetricFinder.html

Purpose: Identifies the most appropriate distance metric for two given data points based on their structure.

Use Case: Useful when dealing with various types of data, this class helps users automatically determine the best distance metric to apply, ensuring that the metric chosen is suitable for the data's characteristics.

+ `OutlierDetection`_
.. _OutlierDetection: https://distancia.readthedocs.io/en/latest/OutlierDetection.html

Purpose: Implements methods for detecting outliers in datasets by using distance metrics to identify points that deviate significantly from others.

Use Case: Essential in fields such as fraud detection, quality control, and data cleaning, where identifying and managing outliers is crucial for maintaining data integrity.

+ `ParallelandDistributedComputation`_
.. _ParallelandDistributedComputation: https://distancia.readthedocs.io/en/latest/ParallelandDistributedComputation.html

Purpose: Adds support for parallel or distributed computation of distances, particularly useful for large datasets.

Use Case: In big data scenarios, calculating distances between millions of data points can be computationally expensive. This class significantly reduces computation time by parallelizing these calculations across multiple processors or machines.

+ `Visualization`_
.. _Visualization: https://distancia.readthedocs.io/en/latest/Visualization.html

Purpose: Provides tools for visualizing distance matrices, dendrograms (for hierarchical clustering), and 2D/3D representations of data points based on distance metrics.

Use Case: Visualization is a powerful tool in exploratory data analysis (EDA), helping users understand the relationships between data points. This class is particularly useful for creating visual aids like heatmaps or dendrograms to better interpret the data.

+ `APICompatibility`_
.. _APICompatibility: https://distancia.readthedocs.io/en/latest/APICompatibility.html

The APICompatibility class in the distancia package bridges the gap between powerful distance computation tools and modern API-based architectures. By enabling the creation of REST endpoints for distance metrics, it facilitates the integration of distancia into a wide range of applications, from web services to distributed computing environments. This not only enhances the usability of the package but also ensures that it can be effectively deployed in real-world, production-grade systems.

+ `AutomatedDistanceMetricSelection`_
.. _AutomatedDistanceMetricSelection: https://distancia.readthedocs.io/en/latest/AutomatedDistanceMetricSelection.html

The AutomatedDistanceMetricSelection feature in the distancia package represents a significant advancement in the ease of use and accessibility of distance metric selection. By automating the process of metric recommendation, it helps users, especially those less familiar with the intricacies of different metrics, to achieve better results in their analyses. This feature not only saves time but also improves the accuracy of data-driven decisions, making distancia a more powerful and user-friendly tool for the data science community.

+ `ReportingAndDocumentation`_
.. _ReportingAndDocumentation: https://distancia.readthedocs.io/en/latest/ReportingAndDocumentation.html

The ReportingAndDocumentation class is a powerful tool for automating the analysis and documentation of distance metrics. By integrating report generation, matrix export, and property documentation, it provides users with a streamlined way to evaluate and present the results of their distance-based models. This class is especially valuable for machine learning practitioners who require a deeper understanding of the behavior of the metrics they employ.


+AdvancedAnalysis`_

.. _AdvancedAnalysis: https://distancia.readthedocs.io/en/latest/AdvancedAnalysis.html

The AdvancedAnalysis class provides essential tools for evaluating the performance, robustness, and sensitivity of distance metrics. These advanced analyses ensure that a metric is not only theoretically sound but also practical and reliable in diverse applications. By offering deep insights into the behavior of distance metrics under perturbations, noise, and dataset divisions, this class is crucial for building resilient models in real-world environments.


+ `DimensionalityReductionAndScaling`_
.. _DimensionalityReductionAndScaling: https://distancia.readthedocs.io/en/latest/DimensionalityReductionAndScaling.html

The `DimensionalityReductionAndScaling` class offers powerful methods for simplifying and scaling datasets. By providing tools for dimensionality reduction such as Multi-Dimensional Scaling (MDS), it allows users to project high-dimensional data into lower dimensions while retaining its key characteristics.


+ `ComparisonAndValidation`_
.. _ComparisonAndValidation: https://distancia.readthedocs.io/en/latest/ComparisonAndValidation.html

The ComparisonAndValidation class offers tools to analyze and validate the performance of a distance or similarity metric by comparing it with other metrics and using established benchmarks. This class is essential for evaluating the effectiveness of a metric in various tasks, such as clustering, classification, or retrieval. By providing cross-validation techniques and benchmarking methods, it allows users to gain a deeper understanding of the metric's strengths and weaknesses.


+ `StatisticalAnalysis`_
.. _StatisticalAnalysis: https://distancia.readthedocs.io/en/latest/StatisticalAnalysis.html

The StatisticalAnalysis class provides essential tools to analyze and interpret the statistical properties of distances or similarities within a dataset. Through the computation of mean, variance, and distance distributions, 

*Contributing*
------------

We welcome contributions! If you would like to contribute to **Distancia**, please read the `contributing`_ guide to get started. We appreciate your help in making this project better.

.. contributing: https://distancia.readthedocs.io/en/latest/CONTRIBUTING.html


*Link*
------

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

+ `Examples`_
.. _Examples: https://github.com/ym001/distancia/blob/master/src/example.py

+ `Pypi`_
.. _Pypi: https://pypi.org/project/distancia/

+ `Source`_
.. _Source: https://github.com/ym001/distancia

+ `Documentation`_
.. _Documentation: https://distancia.readthedocs.io/en/latest/

+ `License`_
.. _License: https://github.com/ym001/distancia/blob/master/LICENSE

*Conclusion*
------------

The *Distancia* package offers a versatile toolkit for handling a wide range of distance and similarity calculations. Whether you're working with numeric data, categorical data, strings, or time series, the package's classes provide the necessary tools to accurately measure distances and similarities. By understanding and utilizing these classes, you can enhance your data analysis workflows and improve the performance of your machine learning models.

