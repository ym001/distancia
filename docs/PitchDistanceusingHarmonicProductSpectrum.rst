Pitch Distance using Harmonic Product Spectrum: Measuring Fundamental Frequency Differences
===========================================================================================

Introduction
------------

The Pitch Distance class, utilizing the Harmonic Product Spectrum (HPS) method, is a powerful tool for measuring differences in pitch between audio signals. This implementation, part of the `distancia` Python package, provides an efficient and accurate way to estimate and compare the fundamental frequencies of complex audio signals.

Significance of the Measure
---------------------------

Pitch Distance is crucial for:

- Comparing the tonal content of audio signals
- Analyzing musical intervals and harmonies
- Detecting pitch shifts in audio processing
- Enhancing music information retrieval systems
- Improving speech analysis and recognition algorithms

The HPS method is particularly effective for signals with a full set of harmonics, making it ideal for analyzing musical instruments and vocal recordings.

Formal Definition
-----------------

The Harmonic Product Spectrum is defined as:

$$
HPS(f) = \prod_{n=1}^{N} |X(nf)|
$$

Where:
- X(f) is the magnitude spectrum of the signal
- N is the number of harmonics considered (typically 2-5)

The pitch is estimated as the frequency that maximizes the HPS:

$$
f_0 = \arg\max_f HPS(f)
$$

The Pitch Distance between two signals is then calculated as:

$$
D_{pitch} = |f_{0,1} - f_{0,2}|
$$

Where f_{0,1} and f_{0,2} are the estimated fundamental frequencies of the two signals.

Complexity Estimation
---------------------

The time complexity of the Pitch Distance calculation using HPS is O(N log N), where N is the number of samples in the audio signal. This includes:

- O(N log N) for the Fast Fourier Transform (FFT)
- O(N) for the HPS calculation and peak finding

The space complexity is O(N) for storing the spectrum and intermediate results.

Usage Example
-------------

```python
from distancia import PitchDistance

# Initialize with two audio signals
signal1 = [0.1, 0.2, -0.1, 0.3, ...]  # Your first signal here
signal2 = [0.2, 0.1, -0.2, 0.4, ...]  # Your second signal here
pd = PitchDistance(sample_rate=44100, frame_size=2048)

# Calculate the Pitch Distance
distance = pd.calculate(signal1, signal2)

print(f"The Pitch Distance between the signals is: {distance} Hz")
```

Academic Citation
-----------------

When using this implementation in academic work, please cite:

Noll, A. M. (1970). Pitch determination of human speech by the harmonic product spectrum, the harmonic sum spectrum and a maximum likelihood estimate. In Proceedings of the symposium on computer processing in communications (Vol. 19, pp. 779-797).

Conclusion
----------

The Pitch Distance class using Harmonic Product Spectrum in the `distancia` package offers a robust method for comparing the pitch content of audio signals. Its implementation provides high accuracy for harmonic-rich signals, making it particularly suitable for music and speech analysis. By quantifying the differences in fundamental frequencies between signals, Pitch Distance enables sophisticated tonal analysis, enhancing capabilities in fields such as music information retrieval, audio fingerprinting, and speech processing.

