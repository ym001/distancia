Spectral Centroid Distance: Measuring Audio Brightness
======================================================

Introduction
------------

The Spectral Centroid Distance is a crucial audio signal processing technique used to quantify the perceptual brightness of sound. This class, part of the ``distancia`` Python package, provides an efficient implementation for calculating and comparing the spectral centroids of audio signals.

Significance of the Measure
---------------------------

The spectral centroid represents the center of mass of a sound's spectrum, strongly correlating with the perceived brightness of audio. By calculating the distance between spectral centroids, we can:

- Compare the timbral qualities of different sounds
- Analyze changes in audio brightness over time
- Classify audio based on spectral characteristics

Formal Definition
-----------------

The spectral centroid is defined as:

.. math::

   \text{Centroid} = \frac{\sum_{n=0}^{N-1} f(n)x(n)}{\sum_{n=0}^{N-1} x(n)}

Where:
- f(n) is the frequency of bin n
- x(n) is the magnitude of bin n
- N is the number of frequency bins

The Spectral Centroid Distance is then calculated as the Euclidean distance between two centroids.

Complexity Estimation
---------------------

The time complexity of the Spectral Centroid Distance calculation is O(N), where N is the number of frequency bins in the audio spectrum. This makes it an efficient measure for real-time audio processing and large-scale music information retrieval tasks.

Usage Example
-------------

.. code-block:: python

   from distancia import SpectralCentroidDistance

   # Initialize with two audio signals
   scd = SpectralCentroidDistance(signal1, signal2)
   
   # Calculate the distance
   distance = scd.calculate_distance()
   
   print(f"The Spectral Centroid Distance is: {distance}")

Academic Citation
-----------------

When using this implementation in academic work, please cite:

Grey, J. M., & Gordon, J. W. (1978). Perceptual effects of spectral modifications on musical timbres. The Journal of the Acoustical Society of America, 63(5), 1493-1500.

Conclusion
----------

The Spectral Centroid Distance class in the ``distancia`` package offers a powerful tool for audio brightness analysis. Its efficient implementation and strong perceptual correlation make it invaluable for various audio processing applications, from music similarity assessment to sound design and audio quality evaluation.
