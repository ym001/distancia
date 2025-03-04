Perceptual Spectral Divergence
==============================

Introduction
------------

The **Perceptual Spectral Divergence (PSD)** is a measure designed to evaluate the perceived differences in the spectral characteristics of two audio signals. Unlike purely mathematical distance metrics, PSD incorporates psychoacoustic principles to align with human auditory perception. This makes it particularly useful in applications such as audio quality assessment, codec evaluation, and sound synthesis.

The spectral characteristics of an audio signal play a crucial role in how it is perceived by listeners. By quantifying these differences, PSD provides insights into how closely a processed or degraded signal resembles the original reference signal in terms of its spectral content.

Purpose and Applications
------------------------

The Perceptual Spectral Divergence measure is widely used in scenarios where the fidelity of spectral information is critical. Common applications include:

- **Audio Codec Evaluation**: Assessing how well compression algorithms preserve spectral details.
- **Audio Restoration**: Measuring the effectiveness of noise reduction or dereverberation techniques.
- **Sound Synthesis**: Comparing synthesized sounds to their intended targets.

Formal Definition
-----------------

The Perceptual Spectral Divergence between two signals, a reference signal :math:`x(t)` and a test signal :math:`y(t)`, is computed by comparing their respective short-time magnitude spectra. The measure can be expressed as:

.. math::

   PSD(x, y) = \frac{1}{N} \sum_{n=1}^{N} D(S_x(n), S_y(n))

Where:
- :math:`S_x(n)` and :math:`S_y(n)` are the short-time Fourier magnitude spectra of the reference and test signals for frame :math:`n`.
- :math:`D(S_x(n), S_y(n))` is a frame-wise divergence function that evaluates the perceptual difference between the two spectra.
- :math:`N` is the total number of frames.

The divergence function :math:`D` may incorporate psychoacoustic weighting to emphasize frequency bands that are more perceptually significant.



Usage Example
-------------

Here's an example of how to use the Perceptual Spectral Divergence measure in `distancia`:

.. code-block:: python
   # Example usage
   from distancia import PerceptualSpectralDivergence

   if __name__ == "__main__":
    # Sample audio signals (simplified for demonstration)
    signal1 = [math.sin(2 * math.pi * 440 * t / 44100) for t in range(44100)]  # 1-second 440 Hz sine wave
    signal2 = [math.sin(2 * math.pi * 880 * t / 44100) for t in range(44100)]  # 1-second 880 Hz sine wave
    
    psd = PerceptualSpectralDivergence(signal1, signal2)
    divergence = psd.calculate_divergence()
    
    print(f"The Perceptual Spectral Divergence between the two signals is: {divergence:.6f}")

Academic References
-------------------

1. Zwicker, E., & Fastl, H. (2013). *Psychoacoustics: Facts and Models*. Springer Science & Business Media.  
   This book provides foundational knowledge on psychoacoustic principles relevant to perceptual measures like PSD.

2. Allen, J. B., & Rabiner, L. R. (1977). "A unified approach to short-time Fourier analysis and synthesis." *Proceedings of the IEEE*, 65(11), 1558-1564.  
   This paper describes the short-time Fourier transform (STFT), which forms the basis for spectral analysis in PSD.

3. Moore, B. C. J. (2012). *An Introduction to the Psychology of Hearing*. Brill Academic Publishers.  
   This resource explores auditory perception and its implications for perceptual measures.

Conclusion
----------

The **Perceptual Spectral Divergence** measure implemented in the `distancia` package provides a robust tool for evaluating perceived spectral differences between audio signals. By incorporating psychoacoustic principles into its design, PSD offers a meaningful metric that aligns with human auditory perception. Whether you are working on audio compression algorithms, restoration techniques, or sound synthesis models, this measure can help you quantify and optimize spectral fidelity effectively.

