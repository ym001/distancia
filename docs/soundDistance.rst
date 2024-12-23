Audio-Based Distances
=====================

Introduction
============
In the realm of audio signal processing, comparing sounds is a complex task that requires specialized distance measures. Whether analyzing music, voice, or environmental sounds, **Distancia** provides a variety of distance measures designed to capture different aspects of audio signals. These distances are categorized based on the features they focus on, such as frequency, timbre, and structural patterns.

List of Audio-Based Distances

=================================
Sound Distance Measures
=================================

Introduction
=============
Sound distance measures are essential for analyzing, comparing, and understanding audio signals in various applications such as music processing, speech recognition, and environmental sound classification. These measures focus on differences in spectral content, temporal patterns, or perceptual characteristics of audio signals.

Below is a comprehensive list of sound distance measures, categorized for clarity.

Categorized Distance Measures
=============================

1. **Spectral-Based Measures**
   - **Spectral Convergence Distance:** Measures the similarity of spectral envelopes between signals.
   - **Spectral Flatness Measure (SFM):** Evaluates the tonality of a sound signal.
   - **Spectral Centroid Distance:** Calculates the perceptual brightness of audio signals.
   - **Spectral Flux:** Measures the difference in spectral power between consecutive frames.
   - **Mel-Frequency Cepstral Coefficient (MFCC) Distance:** Captures differences in audio timbre based on MFCC features.

2. **Temporal-Based Measures**
   - **Dynamic Time Warping (DTW):** Aligns temporal sequences of audio signals to measure similarity.
   - **Time Domain Cross-Correlation:** Compares temporal alignment of two signals.
   - **Envelope Cross-Distance:** Analyzes differences in the amplitude envelope of signals.
   - **Short-Time Energy Distance:** Evaluates variations in energy patterns of sound over time.

3. **Frequency-Based Measures**
   - **Frequency Bin Distance:** Compares specific frequency bins of audio spectra.
   - **Pitch Distance (e.g., Harmonic Product Spectrum):** Measures differences in pitch between signals.
   - **Log-Frequency Spectral Distance:** Captures differences in frequency representation on a logarithmic scale.

4. **Perceptual Measures**
   - **Perceptual Evaluation of Audio Quality (PEAQ):** Quantifies perceptual audio quality.
   - **Perceptual Spectral Divergence:** Evaluates perceived differences in spectral characteristics.
   - **Psychoacoustic Distance:** Accounts for human auditory perception, such as masking effects.
   - **Mel-Frequency Perceptual Distance:** Measures perceptual differences in mel-frequency representation.

5. **Feature-Based Measures**
   - **Cosine Similarity on Feature Vectors:** Compares audio features like MFCCs or chroma.
   - **Euclidean Distance on Feature Space:** Measures straightforward differences in audio feature vectors.
   - **Mahalanobis Distance in Feature Space:** Considers correlations between audio features.
   - **KL-Divergence on Audio Distributions:** Evaluates divergence between probability distributions of audio features.

6. **Waveform-Based Measures**
   - **Root Mean Square (RMS) Energy Difference:** Compares overall energy levels in audio signals.
   - **Peak Signal Difference:** Measures the maximum amplitude variation between signals.
   - **Zero-Crossing Rate Distance:** Compares the rate of sign changes in waveforms.

7. **Application-Specific Measures**
   - **Chord Similarity Distance:** Used for comparing harmonic content in music.
   - **Speech Recognition Error Rate (WER):** Evaluates distance in spoken word sequences.
   - **Environmental Sound Matching Distance:** Measures similarity between environmental sounds for classification.



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
The choice of sound distance measure depends on the application and the characteristics of the audio signals being compared. Whether you're analyzing spectral features, temporal patterns, or perceptual differences, the listed measures provide robust tools for diverse tasks in audio analysis.

By carefully selecting the appropriate distance measure, users can achieve accurate and meaningful comparisons for tasks such as music recommendation, speech analysis, and environmental sound recognition.

The **Distancia** package offers a wide range of audio-based distance measures, making it versatile for tasks such as music information retrieval, voice recognition, and environmental sound analysis. By providing methods that span frequency, time, feature, perceptual, and compression-based approaches, **Distancia** ensures that users can select the most appropriate distance measure for their specific application. Whether the goal is to compare melodies, detect similarities in speech, or analyze environmental sounds, **Distancia** provides a comprehensive toolkit for robust audio comparison.


