Psychoacoustic Distance
=======================

Introduction
------------

The **Psychoacoustic Distance** is an advanced measure designed to quantify the perceptual difference between two audio signals by accounting for various aspects of human auditory perception. Unlike simple mathematical distances, this measure incorporates complex psychoacoustic phenomena such as frequency masking, temporal masking, and loudness perception to provide a more accurate representation of how humans perceive differences in sound.

This measure is particularly valuable in applications where human perception is the ultimate judge of audio quality or similarity, such as in audio coding, sound synthesis, and audio restoration.

Purpose and Significance
------------------------

The Psychoacoustic Distance serves several critical purposes in audio signal processing:

1. **Perceptual Audio Coding**: Optimizing compression algorithms by focusing on perceptually significant differences.
2. **Audio Quality Assessment**: Providing a more accurate measure of perceived audio quality than traditional signal-based metrics.
3. **Sound Synthesis and Matching**: Guiding the generation of sounds that are perceptually similar to target sounds.
4. **Acoustic Environment Simulation**: Evaluating the perceptual accuracy of simulated acoustic environments.

Theoretical Framework
---------------------

The Psychoacoustic Distance measure is based on several key concepts in auditory perception:

1. **Frequency Masking**: Louder sounds can mask quieter sounds at nearby frequencies.
2. **Temporal Masking**: Sounds can mask other sounds that occur shortly before or after them.
3. **Loudness Perception**: The perceived loudness of a sound is not linearly related to its physical intensity.
4. **Critical Bands**: The auditory system analyzes sounds in frequency bands of varying widths.

Formal Definition
-----------------

The Psychoacoustic Distance :math:`D_p` between two audio signals :math:`x(t)` and :math:`y(t)` can be formally expressed as:

.. math::

   D_p(x, y) = \int_0^T \sum_{b=1}^B w_b(t) \cdot d_b(E_x(b,t), E_y(b,t)) dt

Where:
- :math:`T` is the duration of the signals
- :math:`B` is the number of critical bands
- :math:`w_b(t)` is a time-varying weighting function for band :math:`b`
- :math:`E_x(b,t)` and :math:`E_y(b,t)` are the excitation patterns of signals :math:`x` and :math:`y` in band :math:`b` at time :math:`t`
- :math:`d_b` is a band-specific distance function that accounts for masking effects



Usage Example
-------------

Here's an example of how to use the Psychoacoustic Distance measure in the `distancia` package:

.. code-block:: python

   # Example usage
   from distancia import PsychoacousticDistance

   if __name__ == "__main__":
    # Sample audio signals (simplified for demonstration)
    signal1 = [math.sin(2 * math.pi * 440 * t / 44100) for t in range(44100)]  # 1-second 440 Hz sine wave
    signal2 = [math.sin(2 * math.pi * 880 * t / 44100) for t in range(44100)]  # 1-second 880 Hz sine wave
    
    psd = PsychoacousticDistance(signal1, signal2)
    distance = psd.calculate_distance()
    
    print(f"The Psychoacoustic Distance between the two signals is: {distance:.6f}")

Academic References
-------------------

1. Zwicker, E., & Fastl, H. (2013). Psychoacoustics: Facts and models (Vol. 22). Springer Science & Business Media.

2. Moore, B. C. (2012). An introduction to the psychology of hearing. Brill.

3. Beerends, J. G., & Stemerdink, J. A. (1992). A perceptual audio quality measure based on a psychoacoustic sound representation. Journal of the Audio Engineering Society, 40(12), 963-978.

4. Glasberg, B. R., & Moore, B. C. (1990). Derivation of auditory filter shapes from notched-noise data. Hearing research, 47(1-2), 103-138.

Conclusion
----------

The Psychoacoustic Distance measure implemented in the `distancia` package provides a sophisticated tool for evaluating perceptual differences between audio signals. By incorporating key aspects of human auditory perception, it offers a more meaningful assessment of audio similarity or quality than traditional signal-based measures. This makes it an invaluable tool for researchers and developers working in areas such as audio coding, sound synthesis, and acoustic environment simulation, where human perception is the ultimate arbiter of performance.

