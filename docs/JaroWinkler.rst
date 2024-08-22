Jaro-Winkler Distance
=====================

Introduction
------------

The Jaro-Winkler distance is an extension of the Jaro distance metric, which is specifically designed to give more favorable ratings to strings that match from the beginning. This characteristic makes it particularly useful in applications where the prefix similarity is important, such as in record linkage, spelling correction, and text mining.

The Jaro-Winkler distance was introduced as an enhancement to the original Jaro distance to better handle scenarios where the similarity is higher at the start of the strings, which often occurs in name matching tasks.

Formula
-------

The Jaro-Winkler distance `JW(s1, s2)` between two strings `s1` and `s2` is computed as follows:

.. math::

    JW(s1, s2) = J(s1, s2) + (l \cdot p \cdot (1 - J(s1, s2)))

Where:

- `J(s1, s2)` is the Jaro distance between `s1` and `s2`.
- `l` is the length of the common prefix at the start of the strings, up to a maximum of 4 characters.
- `p` is a constant scaling factor, typically set to 0.1, that adjusts the impact of the common prefix on the overall score.

The Jaro-Winkler distance increases as the common prefix length increases, making it a better fit for applications where the beginning of the strings is more significant in determining similarity.

Interpretation
--------------

The Jaro-Winkler distance metric returns a value between 0 and 1:

- A distance of 0 indicates that the strings are completely dissimilar.
- A distance of 1 indicates that the strings are identical.

The Jaro-Winkler distance is particularly well-suited for comparing short strings, such as names, where the prefix similarity is often a critical factor in determining the overall similarity.

.. code-block:: python

    from distancia import JaroWinkler  # Assuming the JaroWinkler class is in the distancia package

    def main():
        # Create an instance of the JaroWinkler class
        jaro_winkler = JaroWinkler()

        # Example 1: Identical strings
        s1 = "hello"
        s2 = "hello"
        distance = jaro_winkler.calculate(s1, s2)
        print(f"Jaro-Winkler distance between '{s1}' and '{s2}': {distance}")

        # Example 2: Completely different strings
        s1 = "hello"
        s2 = "world"
        distance = jaro_winkler.calculate(s1, s2)
        print(f"Jaro-Winkler distance between '{s1}' and '{s2}': {distance}")

        # Example 3: Strings with a common prefix
        s1 = "hello"
        s2 = "hellish"
        distance = jaro_winkler.calculate(s1, s2)
        print(f"Jaro-Winkler distance between '{s1}' and '{s2}': {distance}")

        # Example 4: One string is a prefix of the other
        s1 = "martha"
        s2 = "marhtax"
        distance = jaro_winkler.calculate(s1, s2)
        print(f"Jaro-Winkler distance between '{s1}' and '{s2}': {distance}")

        # Example 5: Completely dissimilar strings
        s1 = "abc"
        s2 = "xyz"
        distance = jaro_winkler.calculate(s1, s2)
        print(f"Jaro-Winkler distance between '{s1}' and '{s2}': {distance}")

    if __name__ == "__main__":
        main()

.. code-block:: bash

    >>>Jaro-Winkler distance between 'hello' and 'hello': 1.0
    >>>Jaro-Winkler distance between 'hello' and 'world': 0.4666666666666666
    >>>Jaro-Winkler distance between 'hello' and 'hellish': 0.8742857142857143
    >>>Jaro-Winkler distance between 'martha' and 'marhtax': 0.9277777777777778
    >>>Jaro-Winkler distance between 'abc' and 'xyz': 0.0

History
-------

The Jaro-Winkler distance was introduced by William E. Winkler in 1990 as an extension to the Jaro distance. Winkler recognized that many applications of the Jaro distance, particularly in the context of record linkage and name matching, could benefit from a metric that gives additional weight to strings that match at the beginning. This insight led to the development of the Jaro-Winkler distance, which has since become a popular choice for string comparison tasks where prefix similarity is important.

Academic Reference
------------------

The original research on the Jaro-Winkler distance can be found in the following paper:

.. bibliography::


Winkler, W. E. (1990). *String Comparator Metrics and Enhanced Decision Rules in the Fellegi-Sunter Model of Record Linkage*. Proceedings of the Section on Survey Research Methods, American Statistical Association, 354-359.

Conclusion
----------

The Jaro-Winkler distance is a powerful enhancement to the Jaro distance, particularly for tasks where the prefix similarity of strings is an important factor. Its ability to provide a more nuanced measurement of similarity makes it ideal for applications such as record linkage, name matching, and other text processing tasks. Understanding and applying the Jaro-Winkler distance can lead to improved accuracy in these fields, making it an essential tool in the `distancia` package.

This documentation is provided by the creators of the `distancia` package to help users understand and effectively use the Jaro-Winkler distance in their projects.

