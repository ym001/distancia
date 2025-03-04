Chord Similarity Distance
==========================

Introduction
------------

The **Chord Similarity Distance** is a measure designed to evaluate the harmonic similarity between two audio signals by analyzing their chordal content. This measure is particularly useful in music information retrieval (MIR) tasks, where understanding and comparing harmonic structures is crucial. It can be applied to tasks such as chord recognition, harmonic progression analysis, and music recommendation systems.

The measure works by extracting the harmonic features of audio signals (e.g., chord representations) and quantifying their similarity using a well-defined distance metric. By focusing on harmonic content, it provides a meaningful way to compare musical pieces or segments based on their perceived harmonic characteristics.

Purpose and Applications
------------------------

The Chord Similarity Distance is widely used in the following applications:

1. **Music Recommendation**: Comparing songs based on their harmonic similarity for playlist generation.
2. **Chord Recognition Evaluation**: Measuring the accuracy of chord recognition algorithms by comparing predicted and ground truth chord sequences.
3. **Musicological Analysis**: Analyzing harmonic progressions in classical or popular music.
4. **Cover Song Detection**: Identifying different versions of the same song based on their harmonic structure.

Theoretical Background
-----------------------

Harmonic similarity is based on the idea that chords represent the fundamental building blocks of harmony in Western music. Chords are typically represented as pitch class sets (e.g., C major = {C, E, G}) or chroma vectors—a 12-dimensional representation where each dimension corresponds to one of the 12 semitones in an octave.

The **Chord Similarity Distance** compares two sequences of chords or chroma vectors using a distance function that accounts for both pitch content and temporal alignment. Common methods for computing chord similarity include:

1. **Pitch Class Overlap**: Measures the overlap between pitch classes of two chords.
2. **Tonal Centroid Distance (TCD)**: Projects chords into a continuous tonal space (e.g., Tonnetz) and computes their Euclidean distance.
3. **Dynamic Time Warping (DTW)**: Aligns two sequences of chords to handle tempo variations.

Formal Definition
-----------------

Given two audio signals :math:`x(t)` and :math:`y(t)`, the Chord Similarity Distance can be computed as:

.. math::

   CSD(x, y) = \frac{1}{N} \sum_{i=1}^{N} d(c_x(i), c_y(i))

Where:
- :math:`c_x(i)` and :math:`c_y(i)` are the chord representations (e.g., chroma vectors or pitch class sets) at time frame :math:`i` for signals :math:`x` and :math:`y`, respectively.
- :math:`d(\cdot, \cdot)` is a distance function between two chords (e.g., cosine distance or Euclidean distance).
- :math:`N` is the total number of frames.

For sequences with different lengths (e.g., due to tempo differences), Dynamic Time Warping (DTW) can be applied to align the sequences before computing the distance.

Usage Example
-------------

Here's an example of how to use the Chord Similarity Distance measure in `distancia`:

.. code-block:: python

   from distancia import ChordSimilarityDistance

   chord_distance = ChordSimilarityDistance()

   chord1 = ['C', 'E', 'G']  # Accord de Do majeur
   chord2 = ['C', 'E', 'G#']  # Accord de Do augmenté

   distance = chord_distance.calculate_distance(chord1, chord2)
   print(f"Distance entre les accords : {distance}")

Academic References
-------------------

1. Harte, C., Sandler, M., & Gasser, M. (2006). Detecting harmonic change in musical audio. In Proceedings of the 1st ACM workshop on Audio and music computing multimedia (pp. 21-26).

2. Müller, M., & Ewert, S. (2011). Chroma Toolbox: MATLAB implementations for extracting variants of chroma-based audio features. In Proceedings of the 12th International Society for Music Information Retrieval Conference (ISMIR 2011) (pp. 215-220).

3. Mauch, M., & Dixon, S. (2010). Simultaneous estimation of chords and musical context from audio. IEEE Transactions on Audio, Speech, and Language Processing, 18(6), 1280-1289.

4. Bartsch, M. A., & Wakefield, G. H. (2005). To catch a chorus: Using chroma-based representations for audio thumbnailing. In IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (pp. 15-18).

5. Bello, J. P., & Pickens, J. (2005). A robust mid-level representation for harmonic content in music signals. In Proceedings of the 6th International Conference on Music Information Retrieval (ISMIR 2005) (pp. 304-311).

Conclusion
----------

The Chord Similarity Distance measure, as implemented in the `distancia` package, provides a powerful tool for comparing the harmonic content of audio signals. By leveraging chroma features and advanced distance metrics, it offers a musically meaningful way to assess similarity between chord progressions or entire musical pieces.

This measure is particularly valuable in various music information retrieval tasks, including chord recognition evaluation, cover song detection, and music recommendation systems. Its ability to capture harmonic similarities aligns well with human perception of musical structure, making it an essential tool for researchers and developers working in the field of music technology.

The flexibility of the implementation, allowing for different distance metrics and the option to use Dynamic Time Warping, makes it adaptable to various use cases and musical genres. As the field of MIR continues to evolve, measures like the Chord Similarity Distance will play a crucial role in advancing our understanding and analysis of musical harmony.

Researchers and developers using the `distancia` package can leverage this measure to gain deeper insights into harmonic structures, improve music classification systems, and develop more sophisticated music analysis tools. The Chord Similarity Distance thus stands as a valuable contribution to

