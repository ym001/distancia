Kendall Tau Distance
=====================

Introduction
------------

The Kendall Tau distance is a metric used to measure the ordinal association between two ranked lists. Named after Maurice Kendall, it evaluates the number of pairwise disagreements between two rankings. This metric is widely used in statistics, especially in non-parametric tests, and has applications in fields such as information retrieval, bioinformatics, and social sciences.

The Kendall Tau distance provides a clear and interpretable measure of how much one ranking diverges from another, making it useful for comparing sequences, rankings, and ordered lists.

Formula
-------

The Kendall Tau distance between two rankings, `R1` and `R2`, is defined as:

.. math::

    \tau(R1, R2) = \frac{(\text{number of concordant pairs}) - (\text{number of discordant pairs})}{\binom{n}{2}}

Where:

- A pair of elements `(i, j)` is **concordant** if the order of `i` and `j` is the same in both rankings `R1` and `R2`.
- A pair of elements `(i, j)` is **discordant** if the order of `i` and `j` is different in the rankings `R1` and `R2`.
- `n` is the total number of elements in the rankings.

The formula effectively counts the number of pairs that are ordered consistently across the two rankings, normalizing by the total number of pairs.

Interpretation
--------------

The Kendall Tau distance is a normalized metric that ranges from -1 to 1:

- A value of `1` indicates perfect agreement between the two rankings (i.e., they are identical).
- A value of `-1` indicates perfect disagreement, where one ranking is the exact reverse of the other.
- A value of `0` suggests that the rankings are random or have no discernible correlation.

This metric is particularly effective when comparing rankings or sequences where the relative order of elements is important.

.. code-block:: python

    from distancia import KendallTau  # Assuming the KendallTau class is in the distancia package

    def main():
        # Create an instance of the KendallTau class
        kendall_tau = KendallTau()

        # Example 1: Identical rankings
        ranking1 = [1, 2, 3, 4, 5]
        ranking2 = [1, 2, 3, 4, 5]
        distance = kendall_tau.calculate(ranking1, ranking2)
        print(f"Kendall Tau distance between {ranking1} and {ranking2}: {distance}")

        # Example 2: Completely reversed rankings
        ranking1 = [1, 2, 3, 4, 5]
        ranking2 = [5, 4, 3, 2, 1]
        distance = kendall_tau.calculate(ranking1, ranking2)
        print(f"Kendall Tau distance between {ranking1} and {ranking2}: {distance}")

        # Example 3: Partially similar rankings
        ranking1 = [1, 2, 3, 4, 5]
        ranking2 = [1, 3, 2, 4, 5]
        distance = kendall_tau.calculate(ranking1, ranking2)
        print(f"Kendall Tau distance between {ranking1} and {ranking2}: {distance}")

        # Example 4: Random rankings
        ranking1 = [1, 2, 3, 4, 5]
        ranking2 = [3, 1, 4, 5, 2]
        distance = kendall_tau.calculate(ranking1, ranking2)
        print(f"Kendall Tau distance between {ranking1} and {ranking2}: {distance}")

    if __name__ == "__main__":
        main()

.. code-block:: bash

    >>>Kendall Tau distance between [1, 2, 3, 4, 5] and [1, 2, 3, 4, 5]: 0
    >>>Kendall Tau distance between [1, 2, 3, 4, 5] and [5, 4, 3, 2, 1]: 10
    >>>Kendall Tau distance between [1, 2, 3, 4, 5] and [1, 3, 2, 4, 5]: 1
    >>>Kendall Tau distance between [1, 2, 3, 4, 5] and [3, 1, 4, 5, 2]: 4

History
-------

The Kendall Tau distance was introduced by the British statistician Maurice Kendall in his 1938 paper "A New Measure of Rank Correlation." Kendall developed this metric as a method to measure the correspondence between two rankings, providing a non-parametric alternative to Pearson's correlation coefficient. Over the years, the Kendall Tau distance has become a staple in statistical analysis, particularly in non-parametric statistics, and has found applications in various scientific disciplines.

Academic Reference
------------------

The foundational work on Kendall Tau distance can be found in the following paper:

.. bibliography::

    KendallTau

Kendall, M. G. (1938). *A New Measure of Rank Correlation*. Biometrika, 30(1/2), 81-93.

Conclusion
----------

The Kendall Tau distance is a robust and widely-used metric for comparing ranked lists and sequences. Its ability to measure the degree of agreement or disagreement between two rankings makes it an invaluable tool in many areas of research, including statistics, information retrieval, and bioinformatics. By understanding and applying the Kendall Tau distance, users of the `distancia` package can gain deeper insights into the relationships between ordered data, making it a powerful addition to their analytical toolkit.

This documentation is provided by the creators of the `distancia` package to help users understand and effectively use the Kendall Tau distance in their projects.

