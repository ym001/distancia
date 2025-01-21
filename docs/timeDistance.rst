Distances for Time Series
==========================

This section outlines a comprehensive list of distance measures designed for comparing time series data. These measures are essential for tasks such as clustering, classification, and anomaly detection. Each entry includes a brief description of its purpose and application.

Basic Statistical Distances
-------------------------------
#. `Euclidean Distance`_:
   Measures the straight-line distance between two time series of equal length. Assumes synchronized time points.
#. `Manhattan Distance`_:
   Computes the sum of absolute differences between corresponding points in two time series.
#. `Chebyshev Distance`_:
   Finds the maximum absolute difference between two time series values.
#. `Correlation Distance`_:
   Converts the correlation coefficient into a distance measure. Useful for determining the similarity in trends.

Dynamic Programming-Based Distances
-------------------------------

5. `Dynamic Time Warping (DTW)`_:
   Aligns two time series by allowing non-linear mapping of time, minimizing the overall distance.
#. `FastDTW`_:
   A computationally efficient approximation of DTW, useful for large-scale datasets.
#. `Edit Distance with Real Penalty (ERP)`_:
   A variation of edit distance, replacing gaps with a constant penalty and considering numerical values.
#. `Edit Distance on Real Sequences (EDR)`_:
   Accounts for numerical tolerance when comparing time series elements.
#. `Time Warp Edit Distance (TWED)`_:
   Combines edit distance with a time-based penalty, preserving temporal relationships.

Shape-Based Distances
-------------------------------

10. `Shape-Based Distance (SBD)`_:
    Uses normalized cross-correlation to compare the overall shape of two time series.
#. `Hausdorff Distance`_:
   Measures the similarity between two sets of points, considering the worst-case deviation.
#. `Fréchet Distance`_:
   Captures the similarity between curves, considering the sequence of points.

Frequency-Based Distances
-------------------------------

13. `Spectral Distance`_:
    Compares the frequency spectra of two time series, focusing on periodicity and frequency content.
#. `Fourier Transform Distance`_:
   Measures similarity in the frequency domain using transformed time series data.
#. `Wavelet-Based Distance`_:
   Uses wavelet decomposition to capture both frequency and temporal differences.

Feature-Based Distances
-------------------------------

16. `Derivative Dynamic Time Warping (DDTW)`_:
    Extends DTW to use the first derivatives of the time series, emphasizing shape similarity.
#. `Longest Common Subsequence (LCSS)`_:
   Identifies the longest shared subsequence between two time series, allowing for gaps.
#. `Piecewise Aggregate Approximation (PAA) Distance`_:
   Reduces dimensionality by summarizing time series into segments before comparison.
#. `Symbolic Aggregate Approximation (SAX) Distance`_:
   Converts time series into symbolic strings, facilitating fast distance computations.

Model-Based Distances
-------------------------------

20. `Hidden Markov Model (HMM) Distance`_:
    Measures the similarity between time series using fitted HMM parameters.
#. `Autoregressive Model Distance`_:
   Compares the parameters of autoregressive models fitted to the time series.
#. `Dynamic Bayesian Network Distance`_:
   Evaluates structural and parameter similarity in probabilistic models.

Elastic Distances
-------------------------------

23. `Soft-DTW`_:
    A differentiable version of DTW, useful for optimization-based methods like deep learning.
#. `Global Alignment Kernel (GAK)`_:
   Combines DTW alignment with a kernel-based similarity measure.
#. `Move-Split-Merge (MSM) Distance`_:
   An edit distance tailored for time series, allowing move, split, and merge operations.

Entropy-Based and Information-Theoretic Distances
-------------------------------

26. `Kullback-Leibler (KL) Divergence`_:
    Measures the difference between probability distributions of two time series.
#. `Jensen-Shannon Distance`_:
   A symmetric variant of KL divergence, emphasizing shared information.
#. `Permutation Entropy Distance`_:
   Compares time series based on their entropy using symbolic permutation.
#. `Cross-Entropy Distance`_:
   Evaluates the predictive similarity of two sequences.

Clustering and Anomaly-Specific Distances
-------------------------------

30. `Self-Organizing Map (SOM) Distance`_:
    Uses SOM embeddings for clustering similar time series.
#. `Isolation Forest Distance`_:
   Leverages anomaly detection techniques to compare series.
#. `Cluster Membership Distance`_:
   Measures similarity based on shared cluster assignments.

Other Specialized Measures
-------------------------------

33. `Earth Mover’s Distance (EMD)`_:
    Measures the effort needed to transform one time series distribution into another.
#. `Mahalanobis Distance`_:
   Incorporates covariance structure for multivariate time series.
#. `Cosine Similarity (as Distance)`_:
   Converts cosine similarity into a distance metric.



**Conclusion**
This exhaustive list highlights the diversity of distance measures for time series analysis. Each measure has specific strengths and limitations, making them suitable for different types of datasets and applications.


.. _Euclidean Distance: https://distancia.readthedocs.io/en/latest/Euclidean.html
.. _Manhattan Distance: https://distancia.readthedocs.io/en/latest/Manhattan.html
.. _Chebyshev Distance: https://distancia.readthedocs.io/en/latest/Chebyshev.html
.. _Correlation Distance: https://distancia.readthedocs.io/en/latest/CorrelationDistance.html
.. _Dynamic Time Warping (DTW): https://distancia.readthedocs.io/en/latest/DynamicTimeWarping.html
.. _FastDTW: https://distancia.readthedocs.io/en/latest/FastDTW.html
.. _Edit Distance with Real Penalty (ERP): https://distancia.readthedocs.io/en/latest/EditDistancewithRealPenalty.html
.. _Edit Distance on Real Sequences (EDR): https://distancia.readthedocs.io/en/latest/EditDistance.html
.. _Time Warp Edit Distance (TWED): https://distancia.readthedocs.io/en/latest/TimeWarpEditDistance.html
.. _Shape-Based Distance (SBD): https://distancia.readthedocs.io/en/latest/ShapeBasedDistance.html
.. _Hausdorff Distance: https://distancia.readthedocs.io/en/latest/Hausdorff.html
.. _Fréchet Distance: https://distancia.readthedocs.io/en/latest/Frechet.html
.. _Spectral Distance: https://distancia.readthedocs.io/en/latest/SpectralDistance.html
.. _Fourier Transform Distance: https://distancia.readthedocs.io/en/latest/FourierTransformDistance.html
.. _Wavelet-Based Distance: https://distancia.readthedocs.io/en/latest/WaveletBasedDistance.html
.. _Derivative Dynamic Time Warping (DDTW): https://distancia.readthedocs.io/en/latest/DerivativeDynamicTimeWarping.html
.. _Longest Common Subsequence (LCSS): https://distancia.readthedocs.io/en/latest/LongestCommonSubsequence.html
.. _Piecewise Aggregate Approximation (PAA) Distance: https://distancia.readthedocs.io/en/latest/PiecewiseAggregateApproximation.html
.. _Symbolic Aggregate Approximation (SAX) Distance: https://distancia.readthedocs.io/en/latest/SymbolicAggregateApproximation.html
.. _Hidden Markov Model (HMM) Distance: https://distancia.readthedocs.io/en/latest/HiddenMarkovModel.html
.. _Autoregressive Model Distance: https://distancia.readthedocs.io/en/latest/AutoregressiveModelDistance.html
.. _Dynamic Bayesian Network Distance: https://distancia.readthedocs.io/en/latest/DynamicBayesianNetworkDistance.html
.. _Soft-DTW: https://distancia.readthedocs.io/en/latest/SoftDTW.html
.. _Global Alignment Kernel (GAK): https://distancia.readthedocs.io/en/latest/GlobalAlignmentKernel.html
.. _Move-Split-Merge (MSM) Distance: https://distancia.readthedocs.io/en/latest/MoveSplitMerge.html
.. _Kullback-Leibler (KL) Divergence: https://distancia.readthedocs.io/en/latest/KullbackLeibler.html
.. _Jensen-Shannon Distance: https://distancia.readthedocs.io/en/latest/JensenShannonDivergence.html
.. _Permutation Entropy Distance: https://distancia.readthedocs.io/en/latest/PermutationEntropyDistance.html
.. _Cross-Entropy Distance: https://distancia.readthedocs.io/en/latest/CrossEntropy.html
.. _Self-Organizing Map (SOM) Distance: https://distancia.readthedocs.io/en/latest/SelfOrganizingMap.html
.. _Isolation Forest Distance: https://distancia.readthedocs.io/en/latest/IsolationForestDistance.html
.. _Cluster Membership Distance: https://distancia.readthedocs.io/en/latest/ClusterMembershipDistance.html
.. _Earth Mover’s Distance (EMD): https://distancia.readthedocs.io/en/latest/EarthMoversDistance.html
.. _Mahalanobis Distance: https://distancia.readthedocs.io/en/latest/Mahalanobis.html
.. _Cosine Similarity (as Distance): https://distancia.readthedocs.io/en/latest/Cosine.html

