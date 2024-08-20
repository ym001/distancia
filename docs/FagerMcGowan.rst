Fager Mc Gowan
============

Introduction
------------

The **Fager Mc Gowan** similarity coefficient is a statistical measure used primarily in ecological and biological studies to assess the similarity between two sets, particularly in species co-occurrence. Unlike other similarity measures, it is specifically designed to handle binary data, where the presence or absence of an attribute (such as a species in a habitat) is recorded. This metric is particularly useful in analyzing pairwise comparisons where the presence of a common attribute is more significant than its absence.

Formula
-------

The **Fager Mc Gowan** similarity coefficient is defined as follows:

.. math::

    S(X, Y) = \frac{|X \cap Y| - \frac{|X| \cdot |Y|}{N}}{\min(|X|, |Y|)}

where:

- :math:`X` and :math:`Y` are two sets (e.g., species in two different habitats).
- :math:`|X \cap Y|` represents the number of elements common to both sets :math:`X` and :math:`Y`.
- :math:`|X|` and :math:`|Y|` are the number of elements in sets :math:`X` and :math:`Y`, respectively.
- :math:`N` is the total number of elements in the universal set (e.g., total species surveyed).

Concept and Purpose
-------------------

The **FagerMc Gowan** coefficient is particularly effective in situations where the presence of common elements (e.g., species) between two sets is of interest, while the influence of rare or infrequent elements is minimized. The formula adjusts for the expected overlap due to random chance, providing a more accurate reflection of true similarity between two sets.

This coefficient is especially valuable in ecological studies, where understanding the co-occurrence patterns of species in different environments can reveal important insights about biodiversity, habitat preference, and environmental factors influencing species distribution.

.. code-block:: python

    # Importing the FagerMcGowan class from the distancia package
    from distancia import FagerMcGowan

    # Define a function to test the FagerMcGowan similarity coefficient
    def test_fager_mcgowan():
        # Create an instance of the FagerMcGowan class
        similarity_calculator = FagerMcGowan()

        # Test cases: Sets to compare
        test_cases = [
            ({"a", "b", "c"}, {"b", "c", "d"}),
            ({"apple", "banana"}, {"banana", "cherry"}),
            ({"cat", "dog"}, {"dog", "mouse"}),
            ({"python", "java", "c++"}, {"java", "c++", "ruby"}),
            ({"red", "blue", "green"}, {"yellow", "blue", "green", "purple"}),
        ]

        # Total number of unique elements in the universal set (for the purpose of these examples)
        universal_set_size = 10

        # Iterate through the test cases and compute the similarity
        for set1, set2 in test_cases:
            similarity = similarity_calculator.calculate(set1, set2, universal_set_size)
            print(f"Fager-McGowan similarity between {set1} and {set2}: {similarity:.4f}")

    if __name__ == "__main__":
        # Run the test function
        test_fager_mcgowan()

.. code-block:: python

    >>>Fager-McGowan similarity between {'a', 'b', 'c'} and {'c', 'b', 'd'}: 0.3667
    >>>Fager-McGowan similarity between {'apple', 'banana'} and {'banana', 'cherry'}: 0.3000
    >>>Fager-McGowan similarity between {'dog', 'cat'} and {'dog', 'mouse'}: 0.3000
    >>>Fager-McGowan similarity between {'python', 'c++', 'java'} and {'c++', 'ruby', 'java'}: 0.3667
    >>>Fager-McGowan similarity between {'green', 'blue', 'red'} and {'green', 'yellow', 'blue', 'purple'}: 0.2667

History
-------

The **Fager Mc Gowan** similarity coefficient was introduced by Eugene W. Fager and John A. McGowan in their 1963 study on species associations. Their work was part of a broader effort in the mid-20th century to develop more sophisticated measures for analyzing binary data, particularly in the field of ecology. The Fager-McGowan coefficient quickly gained recognition for its ability to account for chance co-occurrences, making it a preferred choice in ecological and environmental studies.

Academic Reference
------------------

For further reading on the **Fager-McGowan** similarity coefficient and its applications, consider the following academic reference:

- Fager, E. W., & McGowan, J. A. (1963). *Zooplankton species groups in the North Pacific*. Science, 140(3566), 453-460.

Conclusion
----------

The **Fager Mc Gowan** similarity coefficient offers a robust and nuanced approach to measuring the similarity between two sets, particularly in the context of binary data. By adjusting for random chance, it provides a more accurate assessment of true similarity, making it an essential tool in ecological research. As part of the `distancia` package, the Fager-McGowan coefficient is a valuable addition to any analysis involving species co-occurrence, habitat studies, or other fields where binary data plays a critical role.

