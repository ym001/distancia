MFCCProcessor
=============

Introduction
------------
The **MFCCProcessor** class is designed to compute the Mel-frequency cepstral coefficients (MFCCs), a widely used feature in speech and audio signal processing. MFCCs capture the spectral characteristics of a sound by simulating the human ear's response to different frequencies, making them a powerful tool for comparing audio signals in various applications such as speech recognition, music analysis, and sound classification.

Sense of the Distance
---------------------
The distance calculated using MFCCs aims to measure the dissimilarity between two audio signals based on their cepstral representation. By evaluating how closely the spectral properties of two signals match, the MFCC distance provides an objective measure of similarity, making it particularly useful in tasks involving audio signal comparison.

Formal Representation
----------------------
The MFCC calculation involves the following steps:
1. Apply a short-time Fourier transform (STFT) to the signal to obtain its frequency representation.
2. Use a Mel filterbank to transform the frequency scale into the Mel scale, which mimics human perception of sound.
3. Take the logarithm of the Mel-scaled spectrogram to simulate the human ear's sensitivity to loudness.
4. Finally, apply the discrete cosine transform (DCT) to compress the resulting data into a small set of coefficients (MFCCs).

Given two sets of MFCC vectors, the distance between them can be computed using a variety of distance metrics such as Euclidean distance or dynamic time warping (DTW) to account for temporal misalignments.

.. code-block:: python

  import math
  from typing import List
  import librosa
  ##################

  import math

  def generate_test_signals(duration: float = 1.0, sample_rate: int = 16000) -> tuple[list[float], list[float]]:
      """
      Génère deux signaux audio de test.

      Args:
          duration (float): Durée du signal en secondes. Par défaut 1.0 seconde.
          sample_rate (int): Taux d'échantillonnage en Hz. Par défaut 16000 Hz.

      Returns:
          tuple[list[float], list[float]]: Deux signaux audio de test.
      """
      num_samples = int(duration * sample_rate)

      # Signal 1: Combinaison de deux sinusoïdes (440 Hz et 880 Hz)
      signal1 = [
          0.5 * math.sin(2 * math.pi * 440 * t / sample_rate) +
          0.3 * math.sin(2 * math.pi * 880 * t / sample_rate)
          for t in range(num_samples)
      ]

      # Signal 2: Combinaison de trois sinusoïdes (330 Hz, 660 Hz et 990 Hz)
      signal2 = [
          0.4 * math.sin(2 * math.pi * 330 * t / sample_rate) +
          0.3 * math.sin(2 * math.pi * 660 * t / sample_rate) +
          0.2 * math.sin(2 * math.pi * 990 * t / sample_rate)
          for t in range(num_samples)
      ]

      return signal1, signal2

  # Générer les signaux de test
  test_signal1, test_signal2 = generate_test_signals()

  # Afficher les 10 premiers échantillons de chaque signal
  print("10 premiers échantillons du signal 1:", test_signal1[:10])
  print("10 premiers échantillons du signal 2:", test_signal2[:10])

  # Informations sur les signaux
  print(f"Nombre d'échantillons dans chaque signal: {len(test_signal1)}")
  print(f"Fréquence d'échantillonnage: 16000 Hz")
  print(f"Durée de chaque signal: 1.0 seconde")


  # Créer une instance de MFCCProcessor
  processor = MFCCProcessor()

  # Calculer les MFCC pour les deux signaux
  mfcc1, mfcc2 = processor.compute_mfcc(test_signal1, test_signal2)

  # Comparer les MFCC
  distance = processor.compare_mfcc(test_signal1, test_signal2)

  print(f"Nombre de trames MFCC pour chaque signal: {len(mfcc1)}")
  print(f"Nombre de coefficients MFCC par trame: {len(mfcc1[0])}")
  print(f"Distance moyenne entre les MFCC des deux signaux: {distance}")

  # Afficher les premiers coefficients MFCC de la première trame pour chaque signal
  print("Premiers coefficients MFCC du signal 1:", mfcc1[0][:5])
  print("Premiers coefficients MFCC du signal 2:", mfcc2[0][:5])

.. code-block:: bash

  >>>10 premiers échantillons du signal 1: [0.0, 0.1875859262132922, 0.3605961570472526, 0.5059519423173868, 0.6133981700929515,   
  >>>0.6765094849785568, 0.6932630175151309, 0.6661155750120292, 0.6015809911697477, 0.5093615439642688]
  >>>10 premiers échantillons du signal 2: [0.0, 0.20438860983483298, 0.39145963493709207, 0.5459418258086269, 0.6563814019704781, 0.7164019346692834, 0.7252895158905303, 0.687835184778397, 0.6134709666303622, 0.5148340607737458]
  >>>Nombre d'échantillons dans chaque signal: 16000
  >>>Fréquence d'échantillonnage: 16000 Hz
  >>>Durée de chaque signal: 1.0 seconde
  >>>Nombre de trames MFCC pour chaque signal: 14
  >>>Nombre de coefficients MFCC par trame: 13
  >>>Distance moyenne entre les MFCC des deux signaux: 20.184593753832043
  >>>Premiers coefficients MFCC du signal 1: [15.923779200605054, 9.83322863572527, -3.845832597620646, -13.142400019412856, -11.848251033422947]
  >>>Premiers coefficients MFCC du signal 2: [19.99216500253236, 12.156240075081715, -4.210556501678201, -14.207220023885315, -11.081603255491393]

Academic Reference
------------------
Davis, S., & Mermelstein, P. (1980). Comparison of parametric representations for monosyllabic word recognition in continuously spoken sentences. **IEEE Transactions on Acoustics, Speech, and Signal Processing, 28**(4), 357-366. doi:10.1109/TASSP.1980.1163420

Conclusion
----------
The **MFCCProcessor** class provides an efficient way to extract and compare MFCCs from audio signals, making it a versatile tool in the analysis of audio data. By simulating the human ear's perception of sound, this method allows for meaningful comparisons between signals in various applications such as speech recognition, music retrieval, and audio classification.
