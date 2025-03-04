Mel-Frequency Perceptual Distance
=================================

Introduction
------------

The **Mel-Frequency Perceptual Distance (MFPD)** is a sophisticated measure designed to quantify the perceptual difference between two audio signals based on their mel-frequency representations. This measure leverages the mel scale, which approximates the human auditory system's perception of pitch, to provide a more psychoacoustically relevant comparison of audio signals.

By utilizing the mel-frequency domain, MFPD captures spectral differences in a way that aligns closely with human auditory perception, making it particularly useful in applications such as speech recognition, music information retrieval, and audio quality assessment.

Purpose and Applications
------------------------

The Mel-Frequency Perceptual Distance serves several key purposes in audio signal processing:

1. **Speech and Speaker Recognition**: Evaluating the similarity of speech signals in a perceptually meaningful way.
2. **Audio Codec Evaluation**: Assessing the perceptual quality of compressed audio.
3. **Music Similarity Analysis**: Comparing musical pieces based on their timbral characteristics.
4. **Audio Fingerprinting**: Generating robust audio fingerprints for content identification.

Theoretical Background
----------------------

The mel scale, proposed by Stevens, Volkmann, and Newman in 1937, is a perceptual scale of pitches judged by listeners to be equal in distance from one another. The conversion from frequency :math:`f` (in Hz) to mel :math:`m` is typically approximated as:

.. math::

   m = 2595 \log_{10}(1 + \frac{f}{700})

The MFPD measure uses this scale to transform the frequency content of audio signals before computing their distance.

Formal Definition
-----------------

Given two audio signals :math:`x(t)` and :math:`y(t)`, the Mel-Frequency Perceptual Distance can be formally defined as:

.. math::

   MFPD(x, y) = D(MF(x), MF(y))

Where:
- :math:`MF(x)` and :math:`MF(y)` are the mel-frequency representations of signals :math:`x` and :math:`y` respectively.
- :math:`D(\cdot, \cdot)` is a distance function in the mel-frequency domain, often chosen to be the Euclidean distance or Kullback-Leibler divergence.

The mel-frequency representation typically involves:
1. Computing the short-time Fourier transform (STFT) of the signal.
2. Applying a mel-filterbank to the power spectrum.
3. Taking the logarithm of the filterbank energies.

Usage Example
-------------

Here's an example of how to use the Mel-Frequency Perceptual Distance measure in the `distancia` package:

.. code-block:: python

  from typing import List
  import random
  import math

  # First, let's define our MelFrequencyPerceptualDistance class (as provided in the previous answer)
  # ... (insert the entire class definition here) ...

  # Now, let's create an example of how to use this class

  def generate_sine_wave(frequency: float, duration: float, sample_rate: int) -> List[float]:
    """
    Generate a sine wave.

    Args:
        frequency (float): The frequency of the sine wave in Hz.
        duration (float): The duration of the sound in seconds.
        sample_rate (int): The sample rate in Hz.

    Returns:
        List[float]: The generated sine wave as a list of float values.
    """
    num_samples = int(duration * sample_rate)
    return [math.sin(2 * math.pi * frequency * t / sample_rate) for t in range(num_samples)]
  #####################################################
  # Example usage
  from distancia import MelFrequencyPerceptualDistance

  if __name__ == "__main__":
    # Set up parameters
    sample_rate = 44100  # 44.1 kHz
    frame_size = 2048
    hop_length = 512
    duration = 1.0  # 1 second

    # Create an instance of MelFrequencyPerceptualDistance
    mfpd = MelFrequencyPerceptualDistance(sample_rate, frame_size, hop_length)

    # Generate two different sine waves
    sound1 = generate_sine_wave(440, duration, sample_rate)  # 440 Hz (A4 note)
    sound2 = generate_sine_wave(880, duration, sample_rate)  # 880 Hz (A5 note, one octave higher)

    # Add some noise to the second sound to make it slightly different
    sound2 = [s + random.uniform(-0.1, 0.1) for s in sound2]

    # Calculate the Mel-Frequency Perceptual Distance
    distance = mfpd.calculate_distance(sound1, sound2)

    print(f"Mel-Frequency Perceptual Distance between the two sounds: {distance}")

    # Now, let's compare two more similar sounds
    sound3 = generate_sine_wave(440, duration, sample_rate)
    sound4 = generate_sine_wave(445, duration, sample_rate)  # Slightly different frequency

    # Calculate the distance between these more similar sounds
    distance_similar = mfpd.calculate_distance(sound3, sound4)

    print(f"Mel-Frequency Perceptual Distance between two similar sounds: {distance_similar}")

Academic References
-------------------

1. Stevens, S. S., Volkmann, J., & Newman, E. B. (1937). A scale for the measurement of the psychological magnitude pitch. The Journal of the Acoustical Society of America, 8(3), 185-190.

2. Davis, S. B., & Mermelstein, P. (1980). Comparison of parametric representations for monosyllabic word recognition in continuously spoken sentences. IEEE transactions on acoustics, speech, and signal processing, 28(4), 357-366.

3. Logan, B. (2000). Mel Frequency Cepstral Coefficients for Music Modeling. In ISMIR (Vol. 270, pp. 1-11).

4. Aucouturier, J. J., & Pachet, F. (2002). Music similarity measures: What's the use?. In ISMIR (pp. 13-17).

Conclusion
----------

The Mel-Frequency Perceptual Distance measure, as implemented in the `distancia` package, provides a powerful tool for comparing audio signals in a perceptually meaningful way. By leveraging the mel scale, which aligns closely with human auditory perception, MFPD offers insights that are more relevant to how humans perceive differences in sound. This makes it an invaluable measure for a wide range of applications in audio signal processing, from speech recognition to music information retrieval. Researchers and developers working with audio signals can benefit from this measure's ability to capture perceptually significant differences, leading to more effective and human-centric audio analysis systems.

