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
 
Spectral-Based Measures
-----------------------

#. `Spectral Convergence Distance`_ :Measures the similarity of spectral envelopes between signals.
#. `Spectral Flatness Measure (SFM)`_ :Evaluates the tonality of a sound signal.
#. `Spectral Centroid Distance`_ :Calculates the perceptual brightness of audio signals.
#. `Spectral Flux`_ :Measures the difference in spectral power between consecutive frames.
#. `Mel-Frequency Cepstral Coefficient (MFCC) Distance`_ :Captures differences in audio timbre based on MFCC features.

Temporal-Based Measures
-----------------------

Time-based distances measure similarities or differences directly in the time domain, analyzing how the waveforms of two audio signals evolve over time. These methods are useful for comparing temporal patterns in sound.


6. `Dynamic Time Warping (DTW)`_ :Aligns temporal sequences of audio signals to measure similarity.
#. `Time Domain Cross-Correlation`_ :Compares temporal alignment of two signals.
#. `Envelope Cross-Distance`_ :Analyzes differences in the amplitude envelope of signals.
#. `Short-Time Energy Distance`_ :Evaluates variations in energy patterns of sound over time.
#. `WaveformDistance`_ :Directly compares the raw waveform of two signals, useful for detecting small time-domain differences.
#. `DynamicTimeWarping`_ :Aligns two audio signals in time to measure their similarity, often used in speech processing.
#. `TimeLagDistance`_ :


Frequency-Based Measures
------------------------

These distances focus on the frequency components of the audio signal, comparing the spectra or other frequency-domain transformations. They are ideal for comparing musical tones or the harmonic content of audio.

13. `Frequency Bin Distance`_ :Compares specific frequency bins of audio spectra.
#. `Pitch Distance (e.g., Harmonic Product Spectrum)`_ :Measures differences in pitch between signals.
#. `Log-Frequency Spectral Distance`_ :Captures differences in frequency representation on a logarithmic scale.
#. `CQTDistance`_ :Computes the Constant-Q Transform (CQT) distance, used primarily in musical applications for comparing pitch content.
#. `SpectrogramDistance`_ :Measures the difference between the spectrogram representations of two audio signals, comparing their frequency content over time.
#. `PowerSpectralDensityDistance`_ :
#. `LogSpectralDistance`_ :
#. `BarkSpectralDistortion`_ :
#. `SpectrogramDistance`_ :

Perceptual Measures
-------------------

Perceptual distances attempt to model how humans perceive differences in sounds. These measures take into account psychoacoustic models, making them more aligned with human auditory perception.

22. `Perceptual Evaluation of Audio Quality (PEAQ)`_ :Quantifies perceptual audio quality.
#. `Perceptual Spectral Divergence`_ :Evaluates perceived differences in spectral characteristics.
#. `Psychoacoustic Distance`_ :Accounts for human auditory perception, such as masking effects.
#. `Mel-Frequency Perceptual Distance`_ :Measures perceptual differences in mel-frequency representation.
#. `PerceptualHashing`_ :Computes a hash based on how the human ear would perceive the sound, robust to noise and minor variations.
#. `PLPDistance`_ :Compares Perceptual Linear Predictive coefficients, which model how the ear processes sounds.

Feature-Based Measures
----------------------

Feature-based distances extract specific characteristics or features of audio signals, such as Mel-frequency cepstral coefficients (MFCCs), and compare these feature vectors. These methods are robust for capturing the overall characteristics of sounds.

27. `Cosine Similarity on Feature Vectors`_ :Compares audio features like MFCCs or chroma.
#. `Euclidean Distance on Feature Space`_ :Measures straightforward differences in audio feature vectors.
#. `Mahalanobis Distance in Feature Space`_ :Considers correlations between audio features.
#. `KL-Divergence on Audio Distributions`_ :Evaluates divergence between probability distributions of audio features.
#. `MFCCProcessor`_ :Measures the difference between two audio signals by comparing their Mel-Frequency Cepstral Coefficients (MFCCs), which capture timbral characteristics.
#. `ChromaDistance`_ :Compares the chromagram features of two audio signals, capturing harmonic and tonal similarities.
#. `EnergyDistance`_ :

Waveform-Based Measures
-----------------------

34. `Root Mean Square (RMS) Energy Difference`_ :Compares overall energy levels in audio signals.
#. `Peak Signal Difference`_ :Measures the maximum amplitude variation between signals.
#. `Zero-Crossing Rate Distance`_ :Compares the rate of sign changes in waveforms.
#. `CrossCorrelation`_ :
#. `ZeroCrossingRateDistance`_ :
#. `PhaseDifferenceCalculator`_ :
#. `SignalToNoiseRatio`_ :
#. `EnvelopeCorrelation`_ :

Application-Specific Measures
-----------------------------

42. `Chord Similarity Distance`_ :Used for comparing harmonic content in music.
#. `Speech Recognition Error Rate (WER)`_ :Evaluates distance in spoken word sequences.
#. `Environmental Sound Matching Distance`_ :Measures similarity between environmental sounds for classification.
#. `SignalProcessor`_ :
#. `PESQ`_ :
#. `ItakuraSaitoDistance`_ :
#. `CochleagramDistance`_ :
#. `ChromagramDistance`_ :
#. `CQTDistance`_ :

Compression-Based Distances
---------------------------

Compression-based distances measure the similarity between audio signals by evaluating how efficiently they can be compressed together. These methods capture shared patterns and structures in the audio.

52. `ZlibCompressionDistance`_ :Compares two audio signals by evaluating the compression ratio when they are concatenated, capturing structural similarities.
#. `NormalizedCompressionDistanc`_ : Uses compression to calculate the amount of shared information between two audio files, reflecting their overall similarity.

Conclusion
==========
The choice of sound distance measure depends on the application and the characteristics of the audio signals being compared. Whether you're analyzing spectral features, temporal patterns, or perceptual differences, the listed measures provide robust tools for diverse tasks in audio analysis.

By carefully selecting the appropriate distance measure, users can achieve accurate and meaningful comparisons for tasks such as music recommendation, speech analysis, and environmental sound recognition.

The **Distancia** package offers a wide range of audio-based distance measures, making it versatile for tasks such as music information retrieval, voice recognition, and environmental sound analysis. By providing methods that span frequency, time, feature, perceptual, and compression-based approaches, **Distancia** ensures that users can select the most appropriate distance measure for their specific application. Whether the goal is to compare melodies, detect similarities in speech, or analyze environmental sounds, **Distancia** provides a comprehensive toolkit for robust audio comparison.

.. _Spectral Convergence Distance: https://distancia.readthedocs.io/en/latest/SpectralConvergence.html
.. _MFCCProcessor: https://distancia.readthedocs.io/en/latest/MFCCProcessor.html
.. _SignalProcessor: https://distancia.readthedocs.io/en/latest/SignalProcessor.html
.. _PowerSpectralDensityDistance: https://distancia.readthedocs.io/en/latest/PowerSpectralDensityDistance.html
.. _CrossCorrelation: https://distancia.readthedocs.io/en/latest/CrossCorrelation.html
.. _PhaseDifferenceCalculator: https://distancia.readthedocs.io/en/latest/PhaseDifferenceCalculator.html
.. _TimeLagDistance: https://distancia.readthedocs.io/en/latest/TimeLagDistance.html
.. _PESQ: https://distancia.readthedocs.io/en/latest/PESQ.html
.. _LogSpectralDistance: https://distancia.readthedocs.io/en/latest/LogSpectralDistance.html
.. _BarkSpectralDistortion: https://distancia.readthedocs.io/en/latest/BarkSpectralDistortion.html
.. _ItakuraSaitoDistance: https://distancia.readthedocs.io/en/latest/ItakuraSaitoDistance.html
.. _SignalToNoiseRatio: https://distancia.readthedocs.io/en/latest/SignalToNoiseRatio.html
.. _EnergyDistance: https://distancia.readthedocs.io/en/latest/EnergyDistance.html
.. _EnvelopeCorrelation: https://distancia.readthedocs.io/en/latest/EnvelopeCorrelation.html
.. _ZeroCrossingRateDistance: https://distancia.readthedocs.io/en/latest/ZeroCrossingRateDistance.html
.. _CochleagramDistance: https://distancia.readthedocs.io/en/latest/CochleagramDistance.html
.. _ChromagramDistance: https://distancia.readthedocs.io/en/latest/ChromagramDistance.html
.. _SpectrogramDistance: https://distancia.readthedocs.io/en/latest/SpectrogramDistance.html
.. _CQTDistance: https://distancia.readthedocs.io/en/latest/CQTDistance.html
