

Welcome to Distancia's documentation!
======================================

**Distancia** is a comprehensive Python package that provides a wide range of distance metrics and similarity measures, making it easy to calculate and compare the proximity between various types of data. This documentation provides an in-depth guide to the package, including installation instructions, usage examples, and detailed descriptions of each available metric.


   The code examples provided in this documentation are written for Python 3.x.

Getting Started
---------------

Distancia is designed to be simple and intuitive, yet powerful and flexible. Whether you are working with numerical data, strings, or other types of data, Distancia provides the tools you need to measure the similarity or dissimilarity between objects.


For a quick introduction, check out the :doc:`quickstart` guide. If you want to dive straight into the code, head over to the :doc:`Euclidean` page.


   If you find any issues or have suggestions for improvements, feel free to contribute! See the :doc:`contributing` section for more details.

Installation
------------

To install distancia, simply use pip:

.. code-block:: bash

    pip install distancia

For more detailed instructions and additional options, see the :doc:`installation` section.

Quickstart
----------

Here are some common examples of how to use distancia:



   from distancia import Euclidean
   
   point1 = [1, 2, 3]
   
   point2 = [4, 5, 6]
   
   euclidean = Euclidean()
   
   distance = euclidean.calculate(point1, point2)
   
   print(f"Euclidean Distance: {distance}")


   >>>Euclidean Distance: 5.196152422706632


   from distancia import Levenshtein

   string1 = "kitten"
   string2 = "sitting"

   distance = Levenshtein().calculate(string1, string2)
   print(f"Levenshtein Distance: {distance}")


   >>>Levenshtein Distance: 3


For a complete list and detailed explanations of each metric, see the next section.

Available Metrics
-----------------

Distance
--------



   Euclidean

   Manhattan 

   Hamming

   Levenshtein

   RatcliffObershelp

   Jaro

   JaroWinkler

   KendallTau

   Bhattacharyya

   Mahalanobis

   MahalanobisTaguchi

   Haversine

   Chebyshev

   ContextualDynamicDistance

   Canberra

   BrayCurtis

   RogersTanimoto

   RussellRao

   SokalMichener

   SokalSneath

   DamerauLevenshtein

   SorensenDice

   Wasserstein

   Gower

   CzekanowskiDice

   Hellinger

   MotzkinStraus

   EnhancedRogersTanimoto

   KullbackLeibler

 
Similarity
----------


   Cosine

   Jaccard

   GeneralizedJaccard

   Tanimoto

   Tversky 

   Dice 

   InverseTanimoto

   Ochiai 

   CzekanowskiDice

   Pearson

   Spearman 

   FagerMcGowan

   Otsuka 

Time Series Distance Metrics
----------------------------


   DynamicTimeWarping

   LongestCommonSubsequence

   Frechet

Loss function
-------------


   CrossEntropy

   MeanAbsoluteError

   MeanAbsolutePercentageError

   MeanSquaredError

   SquaredLogarithmicError

   GaloisWassersteinLoss


Graph
-----

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

And many more...

Overview
--------
The distancia package offers a comprehensive set of tools for computing and analyzing distances and similarities between data points. This package is particularly useful for tasks in data analysis, machine learning, and pattern recognition. Below is an overview of the key classes included in the package, each designed to address specific types of distance or similarity calculations.



   BatchDistance
-----------------
Purpose: Facilitates batch processing of distance computations, enabling users to compute distances for large sets of pairs in a single operation.

Use Case: Essential in real-time systems or when working with large datasets where efficiency is critical. Batch processing saves time and computational resources by handling multiple distance computations in one go.



   ComprehensiveBenchmarking
----------------------------
Purpose: Provides tools for benchmarking the performance of various distance metrics on different types of data.

Use Case: Useful in performance-sensitive applications where choosing the optimal metric can greatly impact computational efficiency and accuracy. This class helps users make informed decisions about which distance metric to use for their specific task.


   CustomDistanceFunction
--------------------------
Purpose: Allows users to define custom distance functions by specifying a mathematical formula or providing a custom Python function.

Use Case: Useful for researchers or practitioners who need a specific metric that isn’t commonly used or already implemented.


   DistanceMatrix
-----------------
Purpose: Automatically generates a distance matrix for a set of data points using a specified distance metric.

Use Case: Useful in clustering algorithms like k-means, hierarchical clustering, or in generating heatmaps for visualizing similarity/dissimilarity in datasets.



   DistanceMetricLearning
---------------------------
Purpose: Implements algorithms for learning an optimal distance metric from data based on a specific task, such as classification or clustering.

Use Case: Critical in machine learning tasks where the goal is to optimize a distance metric for maximum task-specific performance, improving the accuracy of models.


   IntegratedDistance
---------------------

Purpose: Enables seamless integration of distance computations with popular data science libraries like pandas, scikit-learn, and numpy.

Use Case: This class enhances the usability of the distancia package, allowing users to incorporate distance calculations directly into their existing data analysis workflows.



   MetricFinder
----------------


Purpose: Identifies the most appropriate distance metric for two given data points based on their structure.

Use Case: Useful when dealing with various types of data, this class helps users automatically determine the best distance metric to apply, ensuring that the metric chosen is suitable for the data's characteristics.



   OutlierDetection
-------------------

Purpose: Implements methods for detecting outliers in datasets by using distance metrics to identify points that deviate significantly from others.

Use Case: Essential in fields such as fraud detection, quality control, and data cleaning, where identifying and managing outliers is crucial for maintaining data integrity.



   ParallelandDistributedComputation
------------------------------------

Purpose: Adds support for parallel or distributed computation of distances, particularly useful for large datasets.

Use Case: In big data scenarios, calculating distances between millions of data points can be computationally expensive. This class significantly reduces computation time by parallelizing these calculations across multiple processors or machines.



   Visualization
----------------

Purpose: Provides tools for visualizing distance matrices, dendrograms (for hierarchical clustering), and 2D/3D representations of data points based on distance metrics.

Use Case: Visualization is a powerful tool in exploratory data analysis (EDA), helping users understand the relationships between data points. This class is particularly useful for creating visual aids like heatmaps or dendrograms to better interpret the data.



   APICompatibility
--------------------

   AutomatedDistanceMetricSelection
-------------------------------------

Contributing
------------

We welcome contributions! If you would like to contribute to distancia, please read the :doc:`contributing` guide to get started. We appreciate your help in making this project better.

Changelog
---------

Stay up-to-date with the latest changes and improvements in distancia by reading the :doc:`changelog`.

Link
----

   Notebook<https://github.com/ym001/distancia/tree/master/notebook>
   
   Exemples<https://github.com/ym001/distancia/blob/master/src/exemple.py>
   
   Pypi<https://pypi.org/project/distancia/>
   
   Source<https://github.com/ym001/distancia>
   
   Documentation<https://distancia.readthedocs.io/en/latest/>
   
   License<https://github.com/ym001/distancia/blob/master/LICENSE>

Conclusion
----------

The distancia package offers a versatile toolkit for handling a wide range of distance and similarity calculations. Whether you're working with numeric data, categorical data, strings, or time series, the package's classes provide the necessary tools to accurately measure distances and similarities. By understanding and utilizing these classes, you can enhance your data analysis workflows and improve the performance of your machine learning models.

