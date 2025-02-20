Log-Frequency Spectral Distance: Analyzing Audio Frequency Differences on a Perceptual Scale
============================================================================================

Introduction
------------

The Log-Frequency Spectral Distance (LFSD) is a powerful audio signal processing technique that captures differences in frequency representation on a logarithmic scale. This class, part of the `distancia` Python package, provides an efficient implementation for calculating the distance between audio spectra in a way that aligns with human auditory perception.

Significance of the Measure
---------------------------

LFSD is crucial for:

- Analyzing timbral differences between audio signals
- Enhancing music information retrieval systems
- Improving speech recognition algorithms
- Evaluating audio quality in signal processing applications
- Detecting subtle spectral changes in acoustic environments

This measure is particularly effective because it aligns with the human auditory system's logarithmic response to frequency, providing a perceptually relevant comparison of audio spectra[2].

Formal Definition
-----------------

The Log-Frequency Spectral Distance between two audio spectra X and Y is defined as:

$$
D_{LFSD} = \sqrt{\sum_{k=1}^{N} (log|X[m(k)]| - log|Y[m(k)]|)^2}
$$

Where:
- X[m(k)] and Y[m(k)] are the magnitudes of the k-th mel-frequency bin for spectra X and Y respectively
- N is the number of mel-frequency bins
- m(k) is the mapping function from linear to mel-frequency scale

The mel-frequency scale is approximated as:

$$
m(f) = 2595 \cdot log_{10}(1 + \frac{f}{700})
$$

Where f is the frequency in Hz[6].

Complexity Estimation
---------------------

The time complexity of the LFSD calculation is O(N log N), where N is the number of samples in the audio signal. This includes:

- O(N log N) for the Fast Fourier Transform (FFT) of each signal
- O(M) for the mel-frequency mapping and distance calculation, where M is the number of mel-frequency bins (typically M << N)

The space complexity is O(M) for storing the mel-frequency spectra and intermediate results.

Usage Example
-------------

```python
from distancia import LogFrequencySpectralDistance

# Initialize with two audio signals
signal1 = [0.1, 0.2, -0.1, 0.3, ...]  # Your first signal here
signal2 = [0.2, 0.1, -0.2, 0.4, ...]  # Your second signal here
lfsd = LogFrequencySpectralDistance(sample_rate=44100, n_mels=128)

# Calculate the Log-Frequency Spectral Distance
distance = lfsd.calculate(signal1, signal2)

print(f"The Log-Frequency Spectral Distance between the signals is: {distance}")
```

Academic Citation
-----------------

When using this implementation in academic work, please cite:

Erell, A., & Weintraub, M. (1990). Recognition of Noisy Speech: Using Minimum-Mean Log-Spectral Distance Estimation. In Proceedings of the Speech and Natural Language Workshop (pp. 341-345)[1].

Conclusion
----------

The Log-Frequency Spectral Distance class in the `distancia` package offers a perceptually relevant method for comparing audio spectra. By operating on a logarithmic frequency scale, it aligns with human auditory perception, making it particularly suitable for applications in music analysis, speech processing, and audio quality assessment. This implementation provides an efficient and accurate way to quantify spectral differences, enhancing capabilities in various audio signal processing tasks.
