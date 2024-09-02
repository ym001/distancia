Wasserstein Distance
=====================

Introduction
------------

The Wasserstein distance, also known as the Earth Mover's Distance (EMD), is a measure of the distance between two probability distributions over a given metric space. It quantifies the minimum amount of "work" required to transform one distribution into another, where "work" is defined as the amount of probability mass that must be moved, multiplied by the distance it has to be moved. The Wasserstein distance is widely used in fields such as image processing, machine learning, and economics, especially in problems involving optimal transport.

Formula
-------

For two probability distributions \( P \) and \( Q \) over a space \( \Omega \), the Wasserstein distance of order 1 (often called the 1-Wasserstein distance or EMD) is defined as:

.. math::

    W_1(P, Q) = \inf_{\gamma \in \Gamma(P, Q)} \mathbb{E}_{(x,y) \sim \gamma} [\|x - y\|]

where:

- \( \Gamma(P, Q) \) is the set of all joint distributions \(\gamma(x, y)\) whose marginals are \(P\) and \(Q\), respectively.
- \( \|x - y\| \) is the distance between points \(x\) and \(y\) in the metric space \( \Omega \).
- The infimum is taken over all possible joint distributions \( \gamma \).

In the case where \( P \) and \( Q \) are discrete distributions, the Wasserstein distance can be computed using linear programming methods.

Interpretation
--------------

The Wasserstein distance provides an intuitive way to compare distributions, particularly when the underlying metric space has a meaningful notion of distance. It captures the notion of minimal transportation cost needed to transform one distribution into another, making it particularly suitable for applications where the shape and structure of distributions are important.

A smaller Wasserstein distance indicates that the distributions are more similar, while a larger distance indicates greater dissimilarity.

.. code-block:: python

    # Import the Wasserstein class from the distancia package
    from distancia import Wasserstein

    def main():
        # Define two discrete probability distributions
        distribution1 = [0.1, 0.4, 0.5]
        distribution2 = [0.2, 0.3, 0.5]

        # Create an instance of the Wasserstein class
        wasserstein = Wasserstein()

        # Calculate the Wasserstein distance between the two distributions
        distance = wasserstein.calculate(distribution1, distribution2)

        # Print the calculated distance
        print(f"Wasserstein distance between the distributions: {distance:.4f}")

    if __name__ == "__main__":
        main()

.. code-block:: python

    >>>Wasserstein distance between the distributions: 0.1000

History
-------

The concept of Wasserstein distance originates from the field of optimal transport, with roots in the work of Gaspard Monge in the 18th century, who studied the problem of moving soil from one location to another with minimal cost. The formal mathematical framework for Wasserstein distances was later developed in the 20th century by Leonid Kantorovich, who introduced linear programming methods to the optimal transport problem.

The term "Wasserstein distance" is named after the Russian mathematician Leonid Vaseršteĭn (Wasserstein), who further advanced the study of these distances. The Wasserstein distance is now a fundamental concept in modern mathematical analysis, with applications in various scientific disciplines.

**Reference**:

:footcite:t:`wasserstein`

.. footbibliography::



Conclusion
----------

The Wasserstein distance is a powerful and versatile tool for measuring the dissimilarity between probability distributions. Its foundation in the theory of optimal transport allows it to capture the geometry and structure of the distributions being compared. The inclusion of the Wasserstein distance in the `distancia` package provides users with a robust method for comparing distributions in various applications, from machine learning to economics.

This documentation provides a detailed overview of the Wasserstein distance, its mathematical formulation, and its significance in comparing probability distributions.

