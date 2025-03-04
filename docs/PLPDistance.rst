PLPDistance (Perceptual Linear Predictive Distance)
===================================================

Introduction
------------

The **PLPDistance** is an advanced measure for comparing audio signals based on Perceptual Linear Predictive (PLP) coefficients. This method, rooted in speech processing, models how the human ear processes sounds, making it particularly effective for tasks that require human-like auditory perception.

PLP analysis combines several concepts from psychoacoustics, including critical-band spectral resolution, equal-loudness curve, and intensity-loudness power law. By utilizing these perceptual features, PLPDistance offers a more psychoacoustically relevant comparison between audio signals than traditional spectral measures.

Purpose and Applications
------------------------

The PLPDistance measure serves several key purposes in audio signal processing:

1. **Speech Recognition**: Evaluating the similarity of speech signals in a perceptually meaningful way.
2. **Speaker Identification**: Comparing voice characteristics for speaker recognition systems.
3. **Audio Quality Assessment**: Assessing the perceptual quality of processed or transmitted audio.
4. **Acoustic Model Comparison**: Evaluating the performance of different acoustic models in speech processing.

Theoretical Background
----------------------

Perceptual Linear Prediction, introduced by Hermansky in 1990, is based on the short-term spectrum of speech. The PLP method modifies the short-term spectrum of the speech by several psychophysically based transformations:

1. Critical-band spectral resolution
2. Equal-loudness pre-emphasis
3. Intensity-loudness power law

These modifications are designed to approximate the auditory processing of the human ear, resulting in a representation that's more closely aligned with human perception.

Formal Definition
-----------------

Given two audio signals :math:`x(t)` and :math:`y(t)`, the PLPDistance can be formally defined as:

.. math::

   PLPDistance(x, y) = D(PLP(x), PLP(y))

Where:
- :math:`PLP(x)` and :math:`PLP(y)` are the PLP coefficient vectors of signals :math:`x` and :math:`y` respectively.
- :math:`D(\cdot, \cdot)` is a distance function, often chosen to be the Euclidean distance or Mahalanobis distance.

The PLP coefficients are typically computed as follows:
1. Compute the power spectrum of the signal
2. Apply a bark-scale filter bank
3. Pre-emphasize the spectrum according to an equal-loudness curve
4. Compress the loudness
5. Compute an all-pole model of the resulting spectrum

Usage Example
-------------

Here's an example of how to use the PLPDistance measure in the `distancia` package:

.. code-block:: python

   from distancia import PLPDistance

   # Example usage
   if __name__ == "__main__":
    # Set up parameters
    sample_rate = 22050  # Common sample rate for audio analysis
    frame_size = 2048
    hop_length = 512
    n_mels = 128
    n_plp = 13

    # Create an instance of PLPDistance
    plp_distance = PLPDistance(sample_rate, frame_size, hop_length, n_mels, n_plp)

    # Generate two different sine waves as example sounds
    #duration = 1.0  # 1 second
    #t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    #sound1 = np.sin(2 * np.pi * 440 * t)  # 440 Hz sine wave
    #sound2 = np.sin(2 * np.pi * 880 * t)  # 880 Hz sine wave

    # Calculate the PLP distance
    distance = plp_distance.calculate_distance(sound1, sound2)

    print(f"PLP distance between the two sounds: {distance}")

Academic References
-------------------

1. Hermansky, H. (1990). Perceptual linear predictive (PLP) analysis of speech. The Journal of the Acoustical Society of America, 87(4), 1738-1752.

2. Hönig, F., Stemmer, G., Hacker, C., & Brugnara, F. (2005). Revising perceptual linear prediction (PLP). In Ninth European Conference on Speech Communication and Technology.

3. Psutka, J., Müller, L., & Psutka, J. V. (2001). Comparison of MFCC and PLP parameterizations in the speaker independent continuous speech recognition task. In Seventh European Conference on Speech Communication and Technology.

4. Woodland, P. C. (2001). Speaker adaptation for continuous density HMMs: A review. In ISCA Tutorial and Research Workshop (ITRW) on Adaptation Methods for Speech Recognition.

Conclusion
----------

The PLPDistance measure, as implemented in the `distancia` package, provides a sophisticated tool for comparing audio signals based on perceptually relevant features. By leveraging the psychoacoustic principles embedded in PLP analysis, this measure offers insights that are closely aligned with human auditory perception. This makes it particularly valuable for applications in speech processing, speaker recognition, and audio quality assessment. Researchers and developers working with speech and audio signals can benefit from PLPDistance's ability to capture perceptually significant differences, leading to more effective and human-centric audio analysis systems.

