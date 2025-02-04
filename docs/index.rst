.. meta::
   :description: Distancia is a comprehensive Python package that provides a wide range of distance metrics and similarity measures, making it easy to calculate and compare the proximity between various types of data. This documentation provides an in-depth guide to the package, including installation instructions, usage examples, and detailed descriptions of each available metric.


   :keywords: data science machine learning deep-learning neural-network graph text-classification text distance cython markov-chain file similarity image classification nlp machine learning loss functions distancia
   :keywords lang=en: machine learning, image processing, optimization,text similarity, NLP, search engine, document ranking
   
======================================
Welcome to Distancia's documentation!
======================================


**Distancia** is a comprehensive Python package that provides a wide range of distance metrics and similarity measures, making it easy to calculate and compare the proximity between various types of data. This documentation provides an in-depth guide to the package, including installation instructions, usage examples, and detailed descriptions of each available metric.

The documentation is divided into the following sections:

.. note::

   The code examples provided in this documentation are written for Python 3.x.
   The python code in this package has been optimized by static typing with Cython

*Getting Started*
-----------------

**Distancia** is designed to be simple and intuitive, yet powerful and flexible. Whether you are working with numerical data, strings, or other types of data, Distancia provides the tools you need to measure the distance or similarity between objects.


For a quick introduction, check out the `quickstart`_ guide. If you want to dive straight into the code, head over to the `Euclidean`_ page.

.. quickstart: https://distancia.readthedocs.io/en/latest/quickstart.html

.. _Euclidean: https://distancia.readthedocs.io/en/latest/Euclidean.html

.. note::

   If you find any issues or have suggestions for improvements, feel free to contribute!

*Installation*
--------------

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
------------

Here are some common examples of how to use **Distancia**:

.. code-block:: python

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

   from distancia import Levenshtein

   string1 = "kitten"
   string2 = "sitting"

   distance = Levenshtein().compute(string1, string2)
   print(f"Levenshtein Distance: {distance:4f}")

.. code:: bash

   >>>Levenshtein Distance: 3

For a complete list and detailed explanations of each metric, see the next section.

*Available measurement type*
----------------------------

.. _Vector Distance Measures: https://distancia.readthedocs.io/en/latest/vectorDistance.html
.. _Matrix Distance Measures: https://distancia.readthedocs.io/en/latest/matrixDistance.html
.. _Text Distance Measures: https://distancia.readthedocs.io/en/latest/textDistance.html
.. _Time Series Distance Measures: https://distancia.readthedocs.io/en/latest/timeDistance.html
.. _LOSS: https://distancia.readthedocs.io/en/latest/lossFunction.html
.. _GRAPH: https://distancia.readthedocs.io/en/latest/graphDistance.html
.. _MARKOVCHAIN: https://distancia.readthedocs.io/en/latest/markovChainDistance.html
.. _IMAGE: https://distancia.readthedocs.io/en/latest/imageDistance.html
.. _SOUND: https://distancia.readthedocs.io/en/latest/soundDistance.html
.. _FILE: https://distancia.readthedocs.io/en/latest/fileDistance.html

`Vector Distance Measures`_
============================

Distance measures between vectors are essential in machine learning, classification, and information retrieval. Here are five of the most commonly used:

1. **Euclidean Distance**  
   The Euclidean distance is the square root of the sum of the squared differences between the coordinates of two vectors. It is ideal for measuring similarity in geometric spaces.

2. **Manhattan Distance**  
   Also known as L1 distance, it is defined as the sum of the absolute differences between the coordinates of the vectors. It is well-suited for discrete spaces and grid-based environments.

3. **Cosine Distance**  
   It measures the angle between two vectors rather than their absolute distance. Commonly used in natural language processing and information retrieval (e.g., search engines).

4. **Jaccard Distance**  
   Based on the ratio of the intersection to the union of sets, it is effective for comparing sets of words, tags, or recommended items.

5. **Hamming Distance**  
   It counts the number of differing positions between two character or binary sequences. It is widely used in error detection and bioinformatics.

.. note::  
   These distance measures are widely used in various algorithms, including **clustering**, **supervised classification**, and **search engines**.

`Matrix Distance Measures`_
============================

Distance measures between matrices are widely used in **machine learning, image processing, and numerical analysis**. Below are five of the most commonly used:

1. **Frobenius Norm**  
   The Frobenius norm is the square root of the sum of the squared elements of the difference between two matrices. It generalizes the Euclidean distance to matrices and is commonly used in optimization problems.

2. **Spectral Norm**  
   Defined as the largest singular value of the difference between two matrices, the spectral norm is useful for analyzing stability in numerical methods.

3. **Trace Norm (Nuclear Norm)**  
   This norm is the sum of the singular values of the difference between matrices. It is often used in low-rank approximation and compressed sensing.

4. **Mahalanobis Distance**  
   A statistical distance measure that considers correlations between features, making it effective in **multivariate anomaly detection and classification**.

5. **Wasserstein Distance (Earth Mover’s Distance)**  
   This metric quantifies the optimal transport cost between two probability distributions, making it highly relevant in **image processing and deep learning**.

.. note::  
   These distance measures are widely applied in fields such as **computer vision, data clustering, and signal processing**.

+ `TEXT`_

`Text Distance Measures`_
==========================

Distance measures between texts are crucial in **natural language processing (NLP), search engines, and text similarity tasks**. Below are five of the most commonly used:

1. **Levenshtein Distance (Edit Distance)**  
   The minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one string into another. Used in **spell checkers and DNA sequence analysis**.

2. **Jaccard Similarity**  
   Measures the overlap between two sets of words or character n-grams, computed as the ratio of their intersection to their union. Useful in **document comparison and keyword matching**.

3. **Cosine Similarity**  
   Computes the cosine of the angle between two text vectors, often based on **TF-IDF or word embeddings**. Commonly used in **search engines and document ranking**.

4. **Damerau-Levenshtein Distance**  
   An extension of Levenshtein distance that also considers transpositions (swapping adjacent characters). More robust for **typographical error detection**.

5. **BLEU Score (Bilingual Evaluation Understudy)**  
   Measures the similarity between a candidate text and reference texts using **n-gram precision**. Widely used in **machine translation and text summarization**.

.. note::  
   These text distance measures are extensively used in **chatbots, plagiarism detection, and semantic search applications**.


`Time Series Distance Measures`_
================================

Distance measures between time series are essential in **forecasting, anomaly detection, and clustering of temporal data**. Below are five of the most commonly used:

1. **Dynamic Time Warping (DTW)**  
   Computes the optimal alignment between two time series by allowing non-linear warping along the time axis. Widely used in **speech recognition and gesture classification**.

2. **Euclidean Distance**  
   The sum of squared differences between corresponding points in two time series of equal length. Simple but sensitive to **time shifts and distortions**.

3. **Pearson Correlation Distance**  
   Measures how similar the shapes of two time series are by computing `1 - Pearson correlation coefficient`. Useful in **financial time series and sensor data analysis**.

4. **Frechet Distance**  
   Considers both the location and order of points, making it more robust than Euclidean distance for **trajectory analysis and movement comparison**.

5. **Longest Common Subsequence (LCSS)**  
   Identifies the longest matching subsequence between two time series while allowing gaps. Effective for **pattern recognition in noisy or incomplete data**.

.. note::  
   These distance measures are widely used in **time series classification, similarity search, and predictive analytics**.

`Loss Function-Based Distance Measures`_
========================================

Loss functions are widely used in **machine learning, deep learning, and optimization** to quantify the difference between predicted and actual values. Below are five of the most commonly used:

1. **Mean Squared Error (MSE)**  
   Computes the average squared difference between predicted and actual values. Sensitive to large errors, making it effective for **regression tasks where large deviations need penalization**.

2. **Mean Absolute Error (MAE)**  
   Calculates the average of absolute differences between predicted and actual values. Unlike MSE, it treats all errors equally and is **more robust to outliers**.

3. **Huber Loss**  
   Combines MSE and MAE by using a quadratic loss for small errors and a linear loss for large errors. Used in **robust regression** to handle outliers.

4. **Kullback-Leibler (KL) Divergence**  
   Measures the difference between two probability distributions. Essential in **variational inference, deep learning, and information theory**.

5. **Cross-Entropy Loss**  
   Used in classification tasks, it quantifies the difference between two probability distributions, typically between **true labels and predicted probabilities**. Crucial in **neural networks and logistic regression**.

.. note::  
   These loss functions are fundamental in **supervised learning, deep neural networks, and statistical modeling**.

+ `GRAPH`_

+ `MARKOVCHAIN`_

+ `IMAGE`_

+ `SOUND`_

+ `FILE`_


And many more...

*Overview*
-----------
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
---------------

We welcome contributions! If you would like to contribute to **Distancia**, please read the `contributing`_ guide to get started. We appreciate your help in making this project better.

.. contributing: https://distancia.readthedocs.io/en/latest/CONTRIBUTING.html


*Link*
------

+ `Notebook`_
   + `vectorDistance`_
   + `matrixDistance`_
   +  `textDistance`_
   +  `graphDistance`_
   +  `MarkovChainDistance`_
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
.. _Loss_function: https://github.com/ym001/distancia/blob/master/notebook/Loss_function.ipynb
.. _distance: https://github.com/ym001/distancia/blob/master/notebook/distance.ipynb
.. _fileDistance: https://github.com/ym001/distancia/blob/master/notebook/fileDistance.ipynb
.. _lossDistance: https://github.com/ym001/distancia/blob/master/notebook/lossDistance.ipynb
.. _similarity: https://github.com/ym001/distancia/blob/master/notebook/similarity.ipynb
.. _imageDistance: https://github.com/ym001/distancia/blob/master/notebook/imageDistance.ipynb
.. _soundDistance: https://github.com/ym001/distancia/blob/master/notebook/soundDistance.ipynb
.. _timeSeriesDistance: https://github.com/ym001/distancia/blob/master/notebook/timeSeriesDistance.ipynb
.. _MarkovChainDistance: https://github.com/ym001/distancia/blob/master/notebook/MarkovChain.ipynb

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

