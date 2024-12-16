Distance Measures for Time Series
=================================

Below is an enumerated list of distance measures specifically designed for analyzing time series data. This list is automatically numbered and will adjust as items are added or removed.

.. enumerate::

   **Euclidean Distance**
   Measures the straight-line distance between two time series of equal length. Assumes synchronized time points.

   **Dynamic Time Warping (DTW)**
   Aligns two time series by allowing non-linear mapping of time, minimizing the overall distance.

   **Edit Distance on Real Sequences (EDR)**
   Accounts for numerical tolerance when comparing time series elements.

   **Longest Common Subsequence (LCSS)**
   Identifies the longest shared subsequence between two time series, allowing for gaps.

   **Shape-Based Distance (SBD)**
   Uses normalized cross-correlation to compare the overall shape of two time series.

   **Spectral Distance**
   Compares the frequency spectra of two time series, focusing on periodicity and frequency content.

   **Piecewise Aggregate Approximation (PAA) Distance**
   Reduces dimensionality by summarizing time series into segments before comparison.

   **Symbolic Aggregate Approximation (SAX) Distance**
   Converts time series into symbolic strings, facilitating fast distance computations.

   **Hidden Markov Model (HMM) Distance**
   Measures the similarity between time series using fitted HMM parameters.

   **Soft-DTW**
   A differentiable version of DTW, useful for optimization-based methods like deep learning.

This approach ensures clear organization and flexibility for updates to the list.
