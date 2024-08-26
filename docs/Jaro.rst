Jaro Distance
=============

Introduction
------------

The Jaro distance is a metric used to measure the similarity between two strings. It is particularly useful in applications such as record linkage, spell checking, and natural language processing, where determining the similarity between two strings is essential. The Jaro distance is designed to account for differences in character position and the presence of transpositions, making it well-suited for comparing short strings like names.

The Jaro distance is named after Matthew A. Jaro, who introduced the metric in the context of record linkage and matching algorithms.

Formula
-------

The Jaro distance between two strings `s1` and `s2` is calculated using the following formula:

.. math::

    J(s1, s2) = \frac{1}{3} \left( \frac{|m|}{|s1|} + \frac{|m|}{|s2|} + \frac{|m| - |t|}{|m|} \right)

Where:

- `m` is the number of matching characters (characters that are the same and within a certain distance from each other).
- `t` is half the number of transpositions (characters that match but are out of order).
- `|s1|` and `|s2|` are the lengths of the strings `s1` and `s2`.

Matching characters are defined as characters that are the same and no further than `floor(max(|s1|, |s2|) / 2) - 1` positions apart in the two strings.

Interpretation
--------------

The Jaro distance metric returns a value between 0 and 1:

- A distance of 0 indicates that the strings are completely dissimilar.
- A distance of 1 indicates that the strings are identical.

In practice, the Jaro distance is often used to compare names and short text strings, where it performs well due to its sensitivity to transpositions and character positions.

.. code-block:: python

    from distancia import Jaro  # Assuming the Jaro class is in the distancia package

    def main():
        # Create an instance of the Jaro class
        jaro = Jaro()

        # Example 1: Identical strings
        s1 = "hello"
        s2 = "hello"
        distance = jaro.calculate(s1, s2)
        print(f"Jaro distance between '{s1}' and '{s2}': {distance}")

        # Example 2: Completely different strings
        s1 = "hello"
        s2 = "world"
        distance = jaro.calculate(s1, s2)
        print(f"Jaro distance between '{s1}' and '{s2}': {distance}")

        # Example 3: Partially matching strings
        s1 = "dixon"
        s2 = "dicksonx"
        distance = jaro.calculate(s1, s2)
        print(f"Jaro distance between '{s1}' and '{s2}': {distance}")

        # Example 4: One empty string
        s1 = ""
        s2 = "nonempty"
        distance = jaro.calculate(s1, s2)
        print(f"Jaro distance between '{s1}' and '{s2}': {distance}")

        # Example 5: Both strings empty
        s1 = ""
        s2 = ""
        distance = jaro.calculate(s1, s2)
        print(f"Jaro distance between '{s1}' and '{s2}': {distance}")

    if __name__ == "__main__":
        main()

.. code-block:: bash

    >>>Jaro distance between 'hello' and 'hello': 1.0
    >>>Jaro distance between 'hello' and 'world': 0.4666666666666666
    >>>Jaro distance between 'dixon' and 'dicksonx': 0.7666666666666666
    >>>Jaro distance between '' and 'nonempty': 0.0
    >>>Jaro distance between '' and '': 1.0


History
-------

The Jaro distance was first introduced by Matthew A. Jaro in the 1989 paper titled *Advances in Record-Linkage Methodology as Applied to Matching the 1985 Census of Tampa, Florida*. The method was developed to improve the accuracy of record linkage, which is the process of identifying records that refer to the same entity across different datasets. Over time, the Jaro distance has become a standard tool in fields such as data cleaning, deduplication, and text processing.

Academic Reference
------------------

The seminal paper by Matthew A. Jaro: :footcite:t:`jaro`

.. footbibliography::

    

Conclusion
----------

The Jaro distance is a powerful metric for string comparison, particularly when dealing with short strings or names. Its ability to account for transpositions and character positions makes it a robust choice in many applications. Understanding and implementing the Jaro distance can significantly improve the accuracy of tasks such as record linkage, deduplication, and text comparison.

This documentation is provided by the creators of the `distancia` package to assist users in understanding and utilizing the Jaro distance in their projects. We encourage further exploration and application of this metric in various fields of study.

