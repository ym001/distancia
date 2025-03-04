Environmental Sound Matching Distance
=====================================

Introduction
------------

The **Environmental Sound Matching Distance** is a specialized measure designed to quantify the similarity between environmental sounds. This metric is crucial for tasks such as environmental sound classification, acoustic scene analysis, and audio-based event detection. By capturing the unique characteristics of environmental sounds, this measure enables more accurate comparison and classification of audio samples from various real-world environments.

Purpose and Applications
------------------------

The Environmental Sound Matching Distance serves several key purposes in audio analysis and environmental monitoring:

1. **Sound Classification**: Categorizing environmental sounds into predefined classes (e.g., urban, nature, industrial).
2. **Acoustic Scene Analysis**: Identifying and characterizing different acoustic environments.
3. **Audio-based Event Detection**: Recognizing specific events or activities based on their acoustic signatures.
4. **Soundscape Ecology**: Studying the relationship between sound and ecological processes.
5. **Urban Planning**: Analyzing urban soundscapes for noise pollution monitoring and city planning.

Theoretical Background
----------------------

Environmental sounds are complex and often non-stationary, containing a mix of tonal and noise-like components. The Environmental Sound Matching Distance typically incorporates features that capture both spectral and temporal characteristics of the sounds. Common features used in this context include:

- Mel-frequency cepstral coefficients (MFCCs)
- Spectral centroid and spread
- Temporal envelope features
- Rhythmic patterns
- Pitch-based features

The distance measure may use a combination of these features, often weighted to emphasize the most discriminative aspects for environmental sound classification.

Formal Definition
-----------------

Given two environmental sound signals :math:`x(t)` and :math:`y(t)`, the Environmental Sound Matching Distance can be generally defined as:

.. math::

   D_{ESM}(x, y) = \sum_{i=1}^{N} w_i \cdot d_i(f_i(x), f_i(y))

Where:
- :math:`N` is the number of feature types considered
- :math:`w_i` is the weight assigned to the i-th feature
- :math:`f_i(\cdot)` is the function extracting the i-th feature from a signal
- :math:`d_i(\cdot, \cdot)` is the distance function for the i-th feature



   

Academic References
-------------------

1. Piczak, K. J. (2015). ESC: Dataset for environmental sound classification. In Proceedings of the 23rd ACM international conference on Multimedia (pp. 1015-1018).

2. Salamon, J., Jacoby, C., & Bello, J. P. (2014). A dataset and taxonomy for urban sound research. In Proceedings of the 22nd ACM international conference on Multimedia (pp. 1041-1044).

3. Barchiesi, D., Giannoulis, D., Stowell, D., & Plumbley, M. D. (2015). Acoustic scene classification: Classifying environments from the sounds they produce. IEEE Signal Processing Magazine, 32(3), 16-34.

4. Chu, S., Narayanan, S., & Kuo, C. C. J. (2009). Environmental sound recognition with time–frequency audio features. IEEE Transactions on Audio, Speech, and Language Processing, 17(6), 1142-1158.

5. Bello, J. P., Silva, C., Nov, O., Dubois, R. L., Arora, A., Salamon, J., ... & Mydlarz, C. (2019). SONYC: A system for monitoring, analyzing, and mitigating urban noise pollution. Communications of the ACM, 62(2), 68-77.

Conclusion
----------

The Environmental Sound Matching Distance measure, as implemented in the `distancia` package, provides a powerful tool for comparing and analyzing environmental sounds. By capturing the complex and varied nature of real-world acoustic environments, this measure enables more accurate classification and analysis of environmental audio data.

This metric is particularly valuable in fields such as urban planning, environmental monitoring, and soundscape ecology. It allows researchers and practitioners to quantify similarities between different acoustic environments, detect specific events or conditions based on their sound signatures, and analyze changes in soundscapes over time.

As environmental sound analysis continues to gain importance in various domains, from smart city development to ecological research, the Environmental Sound Matching Distance measure offers a robust method for extracting meaningful insights from acoustic data. Users of the `distancia` package can leverage this measure to develop more sophisticated environmental sound classification systems, contribute to noise pollution monitoring efforts, and advance our understanding of the acoustic characteristics of different environments.

