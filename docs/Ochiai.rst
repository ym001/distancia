Ochiai Distance
===============

Introduction
------------

The Ochiai distance, also known as the Ochiai coefficient, is a similarity measure that is often used to compare binary data or sets. It is derived from the Ochiai index, which was initially introduced in ecological studies to measure the similarity between species compositions. The Ochiai distance is particularly effective when comparing two binary vectors or sets, as it considers both the intersection and the size of the sets, making it a popular choice in fields such as bioinformatics, information retrieval, and ecology.

Formula
-------

The Ochiai coefficient between two binary vectors :math:`A` and :math:`B` is given by:

.. math::

    C(A, B) = \frac{|A \cap B|}{\sqrt{|A| \times |B|}}

Where:

- :math:`|A \cap B|` is the number of elements common to both sets :math:`A` and :math:`B`.

- :math:`|A|` and :math:`|B|` are the sizes of sets :math:`A` and :math:`B`, respectively.

The Ochiai distance :math:`D` is then calculated as:

.. math::

    D = 1 - C(A, B)

History
-------

The Ochiai coefficient was introduced by the Japanese botanist Masatoshi Ochiai in 1957 as a measure of the similarity between species compositions in ecology. It was later adopted in other fields such as bioinformatics and information retrieval for its effectiveness in comparing binary data. The Ochiai distance, derived from this coefficient, has become a standard tool for measuring dissimilarity between two binary vectors or sets.

Example of Use
--------------

The Ochiai distance is commonly used in:

- Comparing binary data in bioinformatics, such as gene presence or absence in different organisms.
- Information retrieval, where it measures the similarity between sets of retrieved documents and relevant documents.
- Ecology, to compare species compositions between different habitats.

Example of Python Code
----------------------

Here is an example of how to use the Ochiai distance with the `distanciaa` package:

.. code-block:: python

    # Import the distanciaa package
    from distancia import Ochiai

    ochiai = Ochiai()

    # Test with sets
    set1 = {1, 2, 3, 4}
    set2 = {2, 3, 4, 5}
    print(f"Sets test: {ochiai.compute(set1, set2)}")

    # Test with lists
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['b', 'c', 'd', 'e']
    print(f"Lists test: {ochiai.compute(list1, list2)}")

    # Test with mixed types
    mixed1 = {1, 2, 3}
    mixed2 = [2, 3, 4]
    print(f"Mixed types test: {ochiai.compute(mixed1, mixed2)}")

Expected Output:

.. code-block:: bash

    >>>Sets test: 0.25
    >>>Lists test: 0.25
    >>>Mixed types test: 0.33333333333333337

Academic Reference
------------------
                  
For further reading and a deeper understanding of the Ochiai distance and its applications, refer to the following academic paper: :footcite:t:`ochiai`

.. footbibliography::

    


Conclusion
----------
The Ochiai distance is a robust and reliable measure for comparing binary vectors or sets, particularly in fields where the intersection between datasets is of interest. Its foundation in ecological studies and subsequent adoption in various scientific disciplines underscores its versatility and utility. The distanciaa package's implementation of the Ochiai distance allows for easy integration into analysis pipelines, enabling researchers to quantify dissimilarity with precision and efficiency.                
