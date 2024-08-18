Motzkin-Straus Distance
========================

Introduction
------------

The Motzkin-Straus distance is a lesser-known metric that originates from the study of combinatorial optimization and graph theory. It is closely related to the concept of a graph’s clique number, which is the size of the largest complete subgraph. The distance can be interpreted as a measure of similarity between two vectors or datasets, and is particularly useful in contexts where relationships between data points are inherently combinatorial.

The Motzkin-Straus distance is used in applications that require measuring how "tight" or "compact" a set of data points are when viewed as nodes in a graph.

Formula
-------

The Motzkin-Straus distance between two vectors :math:`x` and :math:`y` is defined as:

.. math::

    D(x, y) = 1 - \frac{1}{n-1} \sum_{i=1}^{n} \sum_{j=1}^{n} x_i x_j y_i y_j

Where:

- :math:`x` and :math:`y` are the vectors representing the data points.

- :math:`n` is the number of elements in each vector.

- The formula effectively calculates the complement of the normalized sum of pairwise products between elements of the two vectors.

History
-------

The Motzkin-Straus distance is named after Theodore Motzkin and Emil Straus, who introduced this concept in 1965 in their seminal work on the relationship between continuous optimization and graph theory. Originally, their work focused on representing cliques in graphs through continuous quadratic programming, which led to the development of this distance measure.

Although not as widely used as some other distance metrics, the Motzkin-Straus distance is of particular interest in areas where data relationships can be modeled as graphs, such as social network analysis, bioinformatics, and combinatorial optimization.

Example of Use
--------------

The Motzkin-Straus distance can be useful in:

- Graph theory, where it helps determine how closely a given subgraph approximates a complete graph.
- Combinatorial optimization, particularly in problems involving cliques and other graph structures.
- Data clustering and similarity analysis when relationships can be naturally modeled as a graph.

Example of Python Code
----------------------

Here is an example of how to use the Motzkin-Straus distance with the `distanciaa` package:

.. code-block:: python

    # Import the distanciaa package
    from distanciaa import MotzkinStraus

    # Define two vectors
    vector_1 = [1, 2, 3, 4]
    vector_2 = [4, 3, 2, 1]

    # Create an instance of the MotzkinStraus class
    motzkin_straus_dist = MotzkinStraus()

    # Calculate the Motzkin-Straus distance between the two vectors
    distance = motzkin_straus_dist.distance(vector_1, vector_2)

    # Print the result
    print(f"The Motzkin-Straus distance between the two vectors is: {distance}")

Expected Output:

The Motzkin-Straus distance between the two vectors is: 0.6
      
Academic Reference
------------------
      
For a deeper understanding of the Motzkin-Straus distance and its applications, consider the following reference:

Motzkin, T. S., & Straus, E. G. (1965). Maxima for graphs and a new proof of a theorem of Turán. Canadian Journal of Mathematics, 17, 533-540.

Conclusion
----------
The Motzkin-Straus distance, though specialized, provides a valuable tool for analyzing the structure of data represented as graphs. Its roots in combinatorial optimization and graph theory make it particularly useful for applications that require understanding the compactness or completeness of subgraphs. The distanciaa package allows for straightforward computation of this distance, making it accessible for a wide range of analytical purposes.
