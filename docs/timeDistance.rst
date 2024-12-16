Distances for Time Series
==========================

This section outlines a comprehensive list of distance measures designed for comparing time series data. These measures are essential for tasks such as clustering, classification, and anomaly detection. Each entry includes a brief description of its purpose and application.

---

Basic Statistical Distances
---------------------------
.. enumerate::

- **Euclidean Distance**:
  Measures the straight-line distance between two time series of equal length. Assumes synchronized time points.

- **Manhattan Distance**:
  Computes the sum of absolute differences between corresponding points in two time series.

- **Chebyshev Distance**:
  Finds the maximum absolute difference between two time series values.

- **Correlation Distance**:
  Converts the correlation coefficient into a distance measure. Useful for determining the similarity in trends.

---

Dynamic Programming-Based Distances
-----------------------------------
- **Dynamic Time Warping (DTW)**:
  Aligns two time series by allowing non-linear mapping of time, minimizing the overall distance.

- **FastDTW**:
  A computationally efficient approximation of DTW, useful for large-scale datasets.

- **Edit Distance with Real Penalty (ERP)**:
  A variation of edit distance, replacing gaps with a constant penalty and considering numerical values.

- **Edit Distance on Real Sequences (EDR)**:
  Accounts for numerical tolerance when comparing time series elements.

- **Time Warp Edit Distance (TWED)**:
  Combines edit distance with a time-based penalty, preserving temporal relationships.

---

Shape-Based Distances
---------------------
- **Shape-Based Distance (SBD)**:
  Uses normalized cross-correlation to compare the overall shape of two time series.

- **Hausdorff Distance**:
  Measures the similarity between two sets of points, considering the worst-case deviation.

- **Fréchet Distance**:
  Captures the similarity between curves, considering the sequence of points.

---

Frequency-Based Distances
-------------------------
- **Spectral Distance**:
  Compares the frequency spectra of two time series, focusing on periodicity and frequency content.

- **Fourier Transform Distance**:
  Measures similarity in the frequency domain using transformed time series data.

- **Wavelet-Based Distance**:
  Uses wavelet decomposition to capture both frequency and temporal differences.

---

Feature-Based Distances
------------------------
- **Derivative Dynamic Time Warping (DDTW)**:
  Extends DTW to use the first derivatives of the time series, emphasizing shape similarity.

- **Longest Common Subsequence (LCSS)**:
  Identifies the longest shared subsequence between two time series, allowing for gaps.

- **Piecewise Aggregate Approximation (PAA) Distance**:
  Reduces dimensionality by summarizing time series into segments before comparison.

- **Symbolic Aggregate Approximation (SAX) Distance**:
  Converts time series into symbolic strings, facilitating fast distance computations.

---

Model-Based Distances
----------------------
- **Hidden Markov Model (HMM) Distance**:
  Measures the similarity between time series using fitted HMM parameters.

- **Autoregressive Model Distance**:
  Compares the parameters of autoregressive models fitted to the time series.

- **Dynamic Bayesian Network Distance**:
  Evaluates structural and parameter similarity in probabilistic models.

---

Elastic Distances
-----------------
- **Soft-DTW**:
  A differentiable version of DTW, useful for optimization-based methods like deep learning.

- **Global Alignment Kernel (GAK)**:
  Combines DTW alignment with a kernel-based similarity measure.

- **Move-Split-Merge (MSM) Distance**:
  An edit distance tailored for time series, allowing move, split, and merge operations.

---

Entropy-Based and Information-Theoretic Distances
--------------------------------------------------
- **Kullback-Leibler (KL) Divergence**:
  Measures the difference between probability distributions of two time series.

- **Jensen-Shannon Distance**:
  A symmetric variant of KL divergence, emphasizing shared information.

- **Permutation Entropy Distance**:
  Compares time series based on their entropy using symbolic permutation.

- **Cross-Entropy Distance**:
  Evaluates the predictive similarity of two sequences.

---

Clustering and Anomaly-Specific Distances
-----------------------------------------
- **Self-Organizing Map (SOM) Distance**:
  Uses SOM embeddings for clustering similar time series.

- **Isolation Forest Distance**:
  Leverages anomaly detection techniques to compare series.

- **Cluster Membership Distance**:
  Measures similarity based on shared cluster assignments.

---

Other Specialized Measures
--------------------------
- **Earth Mover’s Distance (EMD)**:
  Measures the effort needed to transform one time series distribution into another.

- **Mahalanobis Distance**:
  Incorporates covariance structure for multivariate time series.

- **Cosine Similarity (as Distance)**:
  Converts cosine similarity into a distance metric.

---

**Conclusion**
This exhaustive list highlights the diversity of distance measures for time series analysis. Each measure has specific strengths and limitations, making them suitable for different types of datasets and applications.
