.. Distancia documentation master file, created by
   sphinx-quickstart on Tue Aug 10 14:57:34 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Distancia's documentation!
======================================

**Distancia** is a comprehensive Python package that provides a wide range of distance metrics and similarity measures, making it easy to calculate and compare the proximity between various types of data. This documentation provides an in-depth guide to the package, including installation instructions, usage examples, and detailed descriptions of each available metric.

The documentation is divided into the following sections:

.. contents::
   :local:
   :depth: 2

.. note::

   The code examples provided in this documentation are written for Python 3.x.
   The python code in this package has been optimized by static typing with Cython

Getting Started
---------------

Distancia is designed to be simple and intuitive, yet powerful and flexible. Whether you are working with numerical data, strings, or other types of data, Distancia provides the tools you need to measure the similarity or dissimilarity between objects.


For a quick introduction, check out the :doc:`quickstart` guide. If you want to dive straight into the code, head over to the :doc:`Euclidean` page.

.. note::

   If you find any issues or have suggestions for improvements, feel free to contribute! See the :doc:`contributing` section for more details.

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
1. :doc:`vectorDistance`

.. toctree::
   :maxdepth: 1


   Euclidean

   Manhattan 

   Jaro

   KendallTau

   Bhattacharyya

   Haversine

   Chebyshev

   ContextualDynamicDistance

   Canberra

   BrayCurtis

   RogersTanimoto

   RussellRao

   SokalMichener

   SokalSneath

   Wasserstein

   Gower

   CzekanowskiDice

   Hellinger

   MotzkinStraus

   EnhancedRogersTanimoto

   KullbackLeibler

   Jaccard

   GeneralizedJaccard

   Tanimoto

   InverseTanimoto

   Ochiai 

   CzekanowskiDice

   Pearson

   Spearman 

   FagerMcGowan

   Otsuka 

   Gestalt


 
2. :doc:`matrixDistance`

.. toctree::
   :maxdepth: 1

   Mahalanobis

   MahalanobisTaguchi

   MatrixSpectral

   NormalizedSpectral

   PureDiffusion

   RandomWalk

   HeatKernel

   GraphEditMatrix

   WeisfeilerLehman

   NetSimile

   TriangleMatrixDistance

   PatternBased

   CliqueBasedGraph

   CycleMatrixDistance

   GraphletMatrixDistance

   MinimumCutDistanceCalculator

   Percolation
   
3. :doc:`textDistance`

.. toctree::
   :maxdepth: 1

   Levenshtein

   DamerauLevenshtein

   Hamming

   Cosine

   TFIDFDistance

   SimHash

   CosineTF

   WordMoversDistance

   BERTBasedDistance

   JaroWinkler

   OverlapCoefficient

   SorensenDice

   BagOfWordsDistance

   FastTextDistance

   Dice 

   Tversky 

   NgramDistance

   SmithWaterman

   RatcliffObershelp

   BLEUScore

   ROUGEScore

   SoftCosineSimilarity

   TopicModelingDistance

   AlignmentBasedMeasures

   GappyNGramDistance

   SoftJaccardSimilarity

   NormalizedCompressionDistance

   MongeElkanDistance

   JensenShannonDivergence

4. :doc:`timeDistance`

.. toctree::
   :maxdepth: 1

   DynamicTimeWarping

   LongestCommonSubsequence

   Frechet

5. :doc:`lossFunction`

.. toctree::
   :maxdepth: 1

   CrossEntropy

   MeanAbsoluteError

   MeanAbsolutePercentageError

   MeanSquaredError

   SquaredLogarithmicError

   GaloisWassersteinLoss


6. :doc:`graphDistance`

.. toctree::
   :maxdepth: 1

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

7. :doc:`markovChainDistance`

.. toctree::
   :maxdepth: 1

   MarkovChainKullbackLeibler

   MarkovChainWasserstein

   MarkovChainTotalVariation

   MarkovChainHellinger

   MarkovChainJensenShannon

   MarkovChainFrobenius

   MarkovChainSpectral

8. :doc:`imageDistance`

.. toctree::
   :maxdepth: 1

   StructuralSimilarityIndex

   PeakSignalToNoiseRatio

   HistogramIntersection

   EarthMoversDistance

   ChiSquareDistance

   FeatureBasedDistance

   PerceptualHashing

   NormalizedCrossCorrelation

9. :doc:`soundDistance`

.. toctree::
   :maxdepth: 1

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

10. :doc:`fileDistance`

* :doc:`ByteLevelDistance`

* :doc:`HashComparison`

* :doc:`NormalizedCompression`

* :doc:`KolmogorovComplexity`

* :doc:`DynamicBinaryInstrumentation`

* :doc:`FileMetadataComparison`

* :doc:`FileTypeDistance`

* :doc:`TreeEditDistance`

* :doc:`ZlibBasedDistance`

And many more...

Overview
--------
The distancia package offers a comprehensive set of tools for computing and analyzing distances and similarities between data points. This package is particularly useful for tasks in data analysis, machine learning, and pattern recognition. Below is an overview of the key classes included in the package, each designed to address specific types of distance or similarity calculations.

.. toctree::
   :maxdepth: 1

   BatchDistance

Purpose: Facilitates batch processing of distance computations, enabling users to compute distances for large sets of pairs in a single operation.

Use Case: Essential in real-time systems or when working with large datasets where efficiency is critical. Batch processing saves time and computational resources by handling multiple distance computations in one go.

.. toctree::
   :maxdepth: 1

   ComprehensiveBenchmarking

Purpose: Provides tools for benchmarking the performance of various distance metrics on different types of data.

Use Case: Useful in performance-sensitive applications where choosing the optimal metric can greatly impact computational efficiency and accuracy. This class helps users make informed decisions about which distance metric to use for their specific task.

.. toctree::
   :maxdepth: 1

   CustomDistanceFunction

Purpose: Allows users to define custom distance functions by specifying a mathematical formula or providing a custom Python function.

Use Case: Useful for researchers or practitioners who need a specific metric that isn’t commonly used or already implemented.

.. toctree::
   :maxdepth: 1

   DistanceMatrix

Purpose: Automatically generates a distance matrix for a set of data points using a specified distance metric.

Use Case: Useful in clustering algorithms like k-means, hierarchical clustering, or in generating heatmaps for visualizing similarity/dissimilarity in datasets.

.. toctree::
   :maxdepth: 1

   DistanceMetricLearning

Purpose: Implements algorithms for learning an optimal distance metric from data based on a specific task, such as classification or clustering.

Use Case: Critical in machine learning tasks where the goal is to optimize a distance metric for maximum task-specific performance, improving the accuracy of models.

.. toctree::
   :maxdepth: 1

   IntegratedDistance

Purpose: Enables seamless integration of distance computations with popular data science libraries like pandas, scikit-learn, and numpy.

Use Case: This class enhances the usability of the distancia package, allowing users to incorporate distance calculations directly into their existing data analysis workflows.

.. toctree::
   :maxdepth: 1

   MetricFinder

Purpose: Identifies the most appropriate distance metric for two given data points based on their structure.

Use Case: Useful when dealing with various types of data, this class helps users automatically determine the best distance metric to apply, ensuring that the metric chosen is suitable for the data's characteristics.

.. toctree::
   :maxdepth: 1

   OutlierDetection

Purpose: Implements methods for detecting outliers in datasets by using distance metrics to identify points that deviate significantly from others.

Use Case: Essential in fields such as fraud detection, quality control, and data cleaning, where identifying and managing outliers is crucial for maintaining data integrity.

.. toctree::
   :maxdepth: 1

   ParallelandDistributedComputation

Purpose: Adds support for parallel or distributed computation of distances, particularly useful for large datasets.

Use Case: In big data scenarios, calculating distances between millions of data points can be computationally expensive. This class significantly reduces computation time by parallelizing these calculations across multiple processors or machines.

.. toctree::
   :maxdepth: 1

   Visualization

Purpose: Provides tools for visualizing distance matrices, dendrograms (for hierarchical clustering), and 2D/3D representations of data points based on distance metrics.

Use Case: Visualization is a powerful tool in exploratory data analysis (EDA), helping users understand the relationships between data points. This class is particularly useful for creating visual aids like heatmaps or dendrograms to better interpret the data.

.. toctree::
   :maxdepth: 1

   APICompatibility

The APICompatibility class in the distancia package bridges the gap between powerful distance computation tools and modern API-based architectures. By enabling the creation of REST endpoints for distance metrics, it facilitates the integration of distancia into a wide range of applications, from web services to distributed computing environments. This not only enhances the usability of the package but also ensures that it can be effectively deployed in real-world, production-grade systems.


.. toctree::
   :maxdepth: 1

   AutomatedDistanceMetricSelection

The AutomatedDistanceMetricSelection feature in the distancia package represents a significant advancement in the ease of use and accessibility of distance metric selection. By automating the process of metric recommendation, it helps users, especially those less familiar with the intricacies of different metrics, to achieve better results in their analyses. This feature not only saves time but also improves the accuracy of data-driven decisions, making distancia a more powerful and user-friendly tool for the data science community.



.. toctree::
   :maxdepth: 1

   ReportingAndDocumentation

The ReportingAndDocumentation class is a powerful tool for automating the analysis and documentation of distance metrics. By integrating report generation, matrix export, and property documentation, it provides users with a streamlined way to evaluate and present the results of their distance-based models. This class is especially valuable for machine learning practitioners who require a deeper understanding of the behavior of the metrics they employ.

.. toctree::
   :maxdepth: 1

   AdvancedAnalysis

The AdvancedAnalysis class provides essential tools for evaluating the performance, robustness, and sensitivity of distance metrics. These advanced analyses ensure that a metric is not only theoretically sound but also practical and reliable in diverse applications. By offering deep insights into the behavior of distance metrics under perturbations, noise, and dataset divisions, this class is crucial for building resilient models in real-world environments.

.. toctree::
   :maxdepth: 1

   DimensionalityReductionAndScaling

The `DimensionalityReductionAndScaling` class offers powerful methods for simplifying and scaling datasets. By providing tools for dimensionality reduction such as Multi-Dimensional Scaling (MDS), it allows users to project high-dimensional data into lower dimensions while retaining its key characteristics.

.. toctree::
   :maxdepth: 1

   ComparisonAndValidation

The ComparisonAndValidation class offers tools to analyze and validate the performance of a distance or similarity metric by comparing it with other metrics and using established benchmarks. This class is essential for evaluating the effectiveness of a metric in various tasks, such as clustering, classification, or retrieval. By providing cross-validation techniques and benchmarking methods, it allows users to gain a deeper understanding of the metric's strengths and weaknesses.

.. toctree::
   :maxdepth: 1

   StatisticalAnalysis

The StatisticalAnalysis class provides essential tools to analyze and interpret the statistical properties of distances or similarities within a dataset. Through the computation of mean, variance, and distance distributions, 

Contributing
------------

We welcome contributions! If you would like to contribute to distancia, please read the :doc:`contributing` guide to get started. We appreciate your help in making this project better.


Link
----


+ `Notebook`_
.. _Notebook: https://github.com/ym001/distancia/tree/master/notebook

   - `vectorDistance`
.. vectorDistance: https://github.com/ym001/distancia/blob/master/notebook/vectorDistance.ipynb

   - matrixDistance<https://github.com/ym001/distancia/blob/master/notebook/matrixDistance.ipynb>
   - textDistance<https://github.com/ym001/distancia/blob/master/notebook/textDistance.ipynb>

   - graphDistance<https://github.com/ym001/distancia/blob/master/notebook/graphDistance.ipynb>
   - MarkovChain<https://github.com/ym001/distancia/blob/master/notebook/MarkovChain.ipynb>

   - Loss_function<https://github.com/ym001/distancia/blob/master/notebook/Loss_function.ipynb>
   - distance<https://github.com/ym001/distancia/blob/master/notebook/distance.ipynb>
   - fileDistance<https://github.com/ym001/distancia/blob/master/notebook/fileDistance.ipynb>
   - graph<https://github.com/ym001/distancia/blob/master/notebook/graph.ipynb>
   - lossDistance<https://github.com/ym001/distancia/blob/master/notebook/lossDistance.ipynb>
   - similarity<https://github.com/ym001/distancia/blob/master/notebook/similarity.ipynb>
   - imageDistance<https://github.com/ym001/distancia/blob/master/notebook/imageDistance.ipynb>
   - soundDistance<https://github.com/ym001/distancia/blob/master/notebook/soundDistance.ipynb>
   - timeSeriesDistance<https://github.com/ym001/distancia/blob/master/notebook/timeSeriesDistance.ipynb>



+ Exemples<https://github.com/ym001/distancia/blob/master/src/exemple.py>
+ Pypi<https://pypi.org/project/distancia/>
+ Source<https://github.com/ym001/distancia>
+ Documentation<https://distancia.readthedocs.io/en/latest/>
+ License<https://github.com/ym001/distancia/blob/master/LICENSE>

Conclusion
----------

The distancia package offers a versatile toolkit for handling a wide range of distance and similarity calculations. Whether you're working with numeric data, categorical data, strings, or time series, the package's classes provide the necessary tools to accurately measure distances and similarities. By understanding and utilizing these classes, you can enhance your data analysis workflows and improve the performance of your machine learning models.

