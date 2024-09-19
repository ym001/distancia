Spectral Convergence
====================

Introduction
------------

The **Spectral Convergence** is a distance measure used to assess the similarity between the frequency spectra of two signals. It is particularly useful in audio processing, where the frequency content of signals plays a key role in distinguishing between different sounds.

Sense of the Distance
---------------------

Spectral Convergence measures the difference between the magnitudes of the frequency spectra of two signals. The closer the two spectra are, the smaller the spectral convergence, indicating that the signals are more similar in their frequency content.

Formal Definition
-----------------

Given two signals, `signal1` and `signal2`, their Spectral Convergence is computed as follows:

.. math::

   \text{Spectral Convergence} = \frac{\sum_{i} |M_1(i) - M_2(i)|}{\sum_{i} M_1(i)}

Where:
- :math:`M_1(i)` and :math:`M_2(i)` are the magnitudes of the frequency components of the FFT of `signal1` and `signal2`, respectively.
- The numerator computes the absolute differences between the magnitudes of the frequency components.
- The denominator normalizes the distance by the sum of the magnitudes of `signal1`.

.. code-block:: python

   def example(self):
        """
        Example usage of the Spectral Convergence class.
        """
        signal1: List[float] = [0.5, 0.1, 0.2, 0.4, 0.3, 0.2, 0.1, 0.0]
        signal2: List[float] = [0.4, 0.2, 0.2, 0.5, 0.3, 0.1, 0.2, 0.0]

        convergence: float = self.compute_spectral_convergence(signal1, signal2)
        print(f"Spectral Convergence: {convergence}")
   SpectralConvergence().example()

.. code-block:: bash

   >>>Spectral Convergence: 0.14673244459294343

Academic Reference
------------------

- Allen, J. B., & Rabiner, L. R. (1977). "A unified approach to short-time Fourier analysis and synthesis." Proceedings of the IEEE, 65(11), 1558-1564.

Conclusion
----------

The Spectral Convergence provides a practical way of comparing the frequency content of two signals, making it useful in audio analysis, speech processing, and signal comparison tasks.
