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
    from distanciaa import Ochiai

    # Define two binary vectors representing data points
    binary_vector_1 = [1, 0, 1, 1, 0, 1, 0]
    binary_vector_2 = [1, 1, 0, 1, 0, 1, 1]

    # Create an instance of the OchiaiDistance class
    ochiai_dist = Ochiai()

    # Calculate the Ochiai distance between the two binary vectors
    distance = ochiai_dist.calculate(binary_vector_1, binary_vector_2)

    # Print the result
    print(f"The Ochiai distance between the two binary vectors is: {distance}")

Expected Output:

The Ochiai distance between the two binary vectors is: 0.292893

Academic Reference
------------------
                  
For further reading and a deeper understanding of the Ochiai distance and its applications, refer to the following academic paper:

.. bibliography::


Ochiai, M. (1957). Zoogeographic Studies on the Soleoid Fishes Found in Japan and Its Neighbouring Regions, II. Bulletin of the Japanese Society of Scientific Fisheries, 22(9), 526-530. DOI: 10.2331/suisan.22.526.

Conclusion
----------
The Ochiai distance is a robust and reliable measure for comparing binary vectors or sets, particularly in fields where the intersection between datasets is of interest. Its foundation in ecological studies and subsequent adoption in various scientific disciplines underscores its versatility and utility. The distanciaa package's implementation of the Ochiai distance allows for easy integration into analysis pipelines, enabling researchers to quantify dissimilarity with precision and efficiency.                
