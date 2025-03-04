Perceptual Evaluation of Audio Quality (PEAQ)
=============================================

Introduction
------------

The Perceptual Evaluation of Audio Quality (PEAQ) is a sophisticated objective measurement method designed to assess the perceived quality of audio signals. Developed by the International Telecommunication Union (ITU) and standardized as ITU-R BS.1387, PEAQ aims to automate the process of evaluating audio quality, traditionally performed through subjective listening tests.

Purpose and Significance
------------------------

PEAQ serves several critical purposes in audio signal processing and telecommunications:

1. Objective Quality Assessment: It provides a quantitative measure of audio quality that closely correlates with human perception.
2. Efficiency: PEAQ enables rapid and consistent evaluation of large volumes of audio data, surpassing the limitations of human listening tests.
3. Standardization: As an ITU standard, PEAQ offers a unified approach to audio quality assessment across different applications and industries.

Theoretical Framework
---------------------

PEAQ is based on psychoacoustic principles and incorporates complex models of human auditory perception. The algorithm operates by:

1. Analyzing both the reference and test signals using a time-frequency decomposition.
2. Extracting a set of Model Output Variables (MOVs) that represent various perceptual attributes.
3. Combining these MOVs using a neural network to produce a single quality score.

Formal Definition
-----------------

The PEAQ algorithm can be formally expressed as a function :math:`f_{PEAQ}` that takes two inputs: a reference signal :math:`x(t)` and a test signal :math:`y(t)`, and produces an Objective Difference Grade (ODG):

.. math::

   ODG = f_{PEAQ}(x(t), y(t))

Where:
- :math:`ODG` is the Objective Difference Grade, ranging from -4 (very annoying difference) to 0 (imperceptible difference).
- :math:`x(t)` is the reference audio signal.
- :math:`y(t)` is the test audio signal.

Usage Example
-------------

Here's an example of how to use the PEAQ measure in the `distancia` package:

.. code-block:: python

   # Example usage
   from distancia import PEAQ

   if __name__ == "__main__":
    # Sample audio signals (simplified for demonstration)
    reference = [math.sin(2 * math.pi * 440 * t / 44100) for t in range(44100)]
    test = [math.sin(2 * math.pi * 440 * t / 44100) + 0.1 * math.sin(2 * math.pi * 880 * t / 44100) for t in range(44100)]
    
    peaq = PEAQ(reference, test)
    odg = peaq.calculate_odg()
    
    print(f"The Objective Difference Grade (ODG) is: {odg:.2f}")

Academic References
-------------------

1. ITU-R Recommendation BS.1387-1, "Method for objective measurements of perceived audio quality," International Telecommunication Union, Geneva, Switzerland, 2001.

2. T. Thiede et al., "PEAQ - The ITU Standard for Objective Measurement of Perceived Audio Quality," Journal of the Audio Engineering Society, vol. 48, no. 1/2, pp. 3-29, 2000.

3. P. Kabal, "An Examination and Interpretation of ITU-R BS.1387: Perceptual Evaluation of Audio Quality," TSP Lab Technical Report, Dept. Electrical & Computer Engineering, McGill University, 2002.

Conclusion
----------

The Perceptual Evaluation of Audio Quality (PEAQ) measure, as implemented in the `distancia` package, provides a powerful tool for objectively assessing audio quality. By leveraging psychoacoustic models and neural network techniques, PEAQ offers a standardized approach to quantifying perceived audio quality, making it invaluable in various applications such as codec development, audio processing algorithm evaluation, and quality control in audio production and transmission systems.

