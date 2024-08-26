Dynamic Time Warping (DTW)
==========================

Introduction
------------

Dynamic Time Warping (DTW) is a well-known algorithm used to measure the similarity between two temporal sequences that may vary in time or speed. This technique has been widely applied in various fields such as speech recognition, data mining, time-series analysis, and bioinformatics. DTW finds an optimal alignment between two time-dependent sequences and calculates the minimal distance based on this alignment.

Idea
----

The fundamental idea behind DTW is to align two sequences in a way that minimizes the cumulative distance between them. Unlike simple distance metrics, which may fail to align sequences of different lengths or those with varying temporal dynamics, DTW allows elastic shifting of the time axis. 

The DTW algorithm computes a cost matrix, where each element represents the distance between elements of the sequences at specific time points. The optimal alignment path is then traced through this matrix, minimizing the overall distance. The final DTW distance is the value in the bottom-right corner of this matrix, which represents the minimum cumulative distance required to align the two sequences.

Example
-------

Consider two time series, `series_a` and `series_b`, as shown below:

.. code-block:: python

      # Sample time series data
      series_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      series_b = [1, 3, 4, 6, 7, 8, 9, 10]

      # Create an instance of the DynamicTimeWarping class
      dtw = DynamicTimeWarping(series_a, series_b)
  
      # Compute the DTW distance
      distance = dtw.compute()
      print(f"DTW Distance: {distance}")

      # Get the optimal path for alignment
      optimal_path = dtw.get_optimal_path()
      print(f"Optimal Path: {optimal_path}")

.. code-block:: bash

  DTW Distance: 3
  Optimal Path: [(0, 0), (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6), (8, 7)]

In this example, the `DynamicTimeWarping` class computes the DTW distance between `series_a` and `series_b`, taking into account the varying lengths and speeds of the sequences. The `get_optimal_path` method provides the best alignment between the sequences, allowing for elastic shifts in the time axis.

Academic Reference
------------------

The concept of Dynamic Time Warping was first introduced in the context of speech recognition by :footcite:t:`dynamictimewarping1` and :footcite:t:`dynamictimewarping2`. The algorithm has since been applied to various domains, making it a versatile tool for time-series analysis. 

.. footbibliography::


Conclusion
----------

Dynamic Time Warping is a powerful and flexible tool for analyzing time series data that vary in length and speed. By allowing elastic shifts in the time axis, DTW provides an optimal alignment between sequences, making it particularly useful in fields like speech recognition and bioinformatics. Integrating DTW into the `distancia` package enables users to perform sophisticated time-series comparisons, further enhancing the package's versatility in data analysis.

