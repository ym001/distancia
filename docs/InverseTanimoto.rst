Inverse Tanimoto
===============

Introduction
------------

The Inverse Tanimoto coefficient is a similarity measure derived from the Tanimoto coefficient, which is widely used in various fields, particularly in cheminformatics, bioinformatics, and text analysis. Unlike the standard Tanimoto coefficient, which measures similarity, the Inverse Tanimoto coefficient is focused on highlighting dissimilarities between two datasets or feature sets. It is particularly useful in contexts where the differences between two entities are more significant than their commonalities.

Formula
-------

The formula for calculating the Inverse Tanimoto coefficient is:

.. math::

    \text{Inverse Tanimoto}(A, B) = \frac{|A \cup B| - |A \cap B|}{|A \cup B|}

where:
- :math:`A` and :math:`B` are sets representing the features or attributes of the two entities being compared.
- :math:`|A \cup B|` is the cardinality (size) of the union of sets :math:`A` and :math:`B`.
- :math:`|A \cap B|` is the cardinality of the intersection of sets :math:`A` and :math:`B`.

This formula computes the proportion of features that are not shared between the two sets, thereby emphasizing dissimilarity.

Concept and Idea
----------------

The Inverse Tanimoto coefficient serves as a complementary measure to the traditional Tanimoto coefficient. While the Tanimoto coefficient is adept at identifying the proportion of shared features between two entities, the Inverse Tanimoto focuses on the portion of features that differ. This is particularly valuable in scenarios where dissimilarity is more critical to assess than similarity. For example, in drug design, identifying compounds that are structurally different from known active compounds can be as important as finding similar ones.

By subtracting the intersection from the union, the Inverse Tanimoto coefficient provides a normalized measure of how much two sets differ relative to their combined size.

# Instantiate the InverseTanimoto class
inverse_tanimoto = InverseTanimoto()

# Define two sets for testing
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Calculate the Inverse Tanimoto coefficient between the two sets
result = inverse_tanimoto.distance(set_a, set_b)

# Print the result
print(f"Inverse Tanimoto coefficient between {set_a} and {set_b}: {result:.4f}")

# Additional test cases
test_cases = [
    ({1, 2, 3}, {3, 4, 5}),
    ({'apple', 'banana', 'cherry'}, {'banana', 'cherry', 'date'}),
    ({1, 2}, {1, 2, 3, 4}),
    ({'cat', 'dog'}, {'dog', 'mouse'}),
    ({10, 20, 30}, {40, 50, 60})
]

# Run additional test cases
for a, b in test_cases:
    result = inverse_tanimoto.distance(a, b)
    print(f"Inverse Tanimoto coefficient between {a} and {b}: {result:.4f}")
Inverse Tanimoto coefficient between {1, 2, 3, 4} and {3, 4, 5, 6}: 0.6667
Inverse Tanimoto coefficient between {1, 2, 3} and {3, 4, 5}: 0.8000
Inverse Tanimoto coefficient between {'apple', 'cherry', 'banana'} and {'date', 'cherry', 'banana'}: 0.5000
Inverse Tanimoto coefficient between {1, 2} and {1, 2, 3, 4}: 0.5000
Inverse Tanimoto coefficient between {'cat', 'dog'} and {'mouse', 'dog'}: 0.6667
Inverse Tanimoto coefficient between {10, 20, 30} and {40, 50, 60}: 1.0000

History
-------

The Tanimoto coefficient was first introduced by Tanimoto in the context of binary attributes to measure the similarity between two sets. Over time, the concept has been adapted and extended to various fields, including text analysis, where it is used to compare the overlap between document feature sets.

The Inverse Tanimoto coefficient has emerged as a variant to address scenarios where dissimilarity is of greater interest than similarity. While not as widely known or used as its predecessor, it has found its niche in fields like anomaly detection, diversity analysis, and any application where differences between entities are key to understanding the data.

Academic Reference
------------------

For a detailed exploration of the Tanimoto coefficient and its applications, refer to:

- Tanimoto, T. T. "An Elementary Mathematical Theory of Classification and Prediction." IBM Internal Report, 1958.

Conclusion
----------

The Inverse Tanimoto coefficient offers a unique perspective in similarity and dissimilarity analysis. By focusing on the differences rather than the commonalities between sets, it provides valuable insights in contexts where divergence is more important than convergence. This measure is particularly useful in fields such as cheminformatics, text analysis, and bioinformatics, where understanding the distinctions between entities can lead to significant discoveries.

As the creator of this implementation, I hope that the Inverse Tanimoto coefficient becomes a valuable tool in your data analysis toolkit, helping you uncover insights that might be overlooked by traditional similarity measures.

