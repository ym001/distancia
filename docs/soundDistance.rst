Audio-Based Distances in Distancia
==================================

Introduction
============
In the realm of audio signal processing, comparing sounds is a complex task that requires specialized distance measures. Whether analyzing music, voice, or environmental sounds, **Distancia** provides a variety of distance measures designed to capture different aspects of audio signals. These distances are categorized based on the features they focus on, such as frequency, timbre, and structural patterns.

Categories
==========

1. **Frequency-Based Distances**
2. **Time-Based Distances**
3. **Feature-Based Distances**
4. **Perceptual-Based Distances**
5. **Compression-Based Distances**

List of Audio-Based Distances


1. **Frequency-Based Distances**
-----------------------------

These distances focus on the frequency components of the audio signal, comparing the spectra or other frequency-domain transformations. They are ideal for comparing musical tones or the harmonic content of audio.

1. :doc:`CQTDistance`

   - Computes the Constant-Q Transform (CQT) distance, used primarily in musical applications for comparing pitch content.

2. :doc:`SpectrogramDistance`

   - Measures the difference between the spectrogram representations of two audio signals, comparing their frequency content over time.

2. **Time-Based Distances**
------------------------

Time-based distances measure similarities or differences directly in the time domain, analyzing how the waveforms of two audio signals evolve over time. These methods are useful for comparing temporal patterns in sound.

1. :doc:`WaveformDistance`

   - Directly compares the raw waveform of two signals, useful for detecting small time-domain differences.

2. :doc:`DynamicTimeWarping` 

   - Aligns two audio signals in time to measure their similarity, often used in speech processing.

3. **Feature-Based Distances**
---------------------------

Feature-based distances extract specific characteristics or features of audio signals, such as Mel-frequency cepstral coefficients (MFCCs), and compare these feature vectors. These methods are robust for capturing the overall characteristics of sounds.

1. :doc:`MFCCDistance`

   - Measures the difference between two audio signals by comparing their Mel-Frequency Cepstral Coefficients (MFCCs), which capture timbral characteristics.

2. :doc:`ChromaDistance`

   - Compares the chromagram features of two audio signals, capturing harmonic and tonal similarities.

4. **Perceptual-Based Distances**
------------------------------

Perceptual distances attempt to model how humans perceive differences in sounds. These measures take into account psychoacoustic models, making them more aligned with human auditory perception.

1. :doc:`PerceptualHashing`

   - Computes a hash based on how the human ear would perceive the sound, robust to noise and minor variations.

2. :doc:`PLPDistance`

   - Compares Perceptual Linear Predictive coefficients, which model how the ear processes sounds.

5. **Compression-Based Distances**
-------------------------------

Compression-based distances measure the similarity between audio signals by evaluating how efficiently they can be compressed together. These methods capture shared patterns and structures in the audio.

1. :doc:`ZlibCompressionDistance`

   - Compares two audio signals by evaluating the compression ratio when they are concatenated, capturing structural similarities.

2. :doc:`NormalizedCompressionDistance`

   - Uses compression to calculate the amount of shared information between two audio files, reflecting their overall similarity.

Conclusion
==========
The **Distancia** package offers a wide range of audio-based distance measures, making it versatile for tasks such as music information retrieval, voice recognition, and environmental sound analysis. By providing methods that span frequency, time, feature, perceptual, and compression-based approaches, **Distancia** ensures that users can select the most appropriate distance measure for their specific application. Whether the goal is to compare melodies, detect similarities in speech, or analyze environmental sounds, **Distancia** provides a comprehensive toolkit for robust audio comparison.
