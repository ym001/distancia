Markov Chain Distances
======================

Introduction
============
Markov chains are widely used to model stochastic processes where the next state depends only on the current state. Comparing two Markov chains can help us understand differences in their behavior, transition probabilities, and steady-state distributions. The **Distancia** package provides various methods for calculating distances between two Markov chains, each capturing different aspects of their structures and dynamics. These measures are useful in fields like statistical modeling, machine learning, and decision-making processes.

Markov Chain Distance Measures
------------------------------

Categorized Distance Measures
-----------------------------
#. `Euclidean`_ :

#. `L1 Distance`_ : Computes the element-wise \( L1 \) distance (Manhattan distance) between the transition matrices of two Markov Chains.
#. `L2 Distance`_ : Computes the element-wise \( L2 \) distance (Euclidean distance) between the transition matrices.
#. `MarkovChainFrobenius`_ : Measures the norm of the difference between the transition matrices.
#. `Matrix Divergence`_ : A general measure comparing two matrices in terms of divergence metrics.
#. `Spectral Norm Distance`_ : Focuses on the spectral properties of the transition matrices.

Stationary Distribution-Based Measures
-----------------------------

#. `MarkovChainKullbackLeibler`_ : Measures the information gain or loss between the stationary distributions.
#. `MarkovChainJensenShannon`_ : A symmetric version of the Kullback-Leibler divergence.
#. `Hellinger Distance`_ : Measures the similarity between two stationary distributions using a probabilistic approach.
#. `Total Variation Distance`_ : Calculates the maximum probability difference across all states between two stationary distributions.

Graph-Theoretic Measures
-----------------------------

#. `Commute Time Distance`_ : Measures the average time taken for a random walk to move between two states.
#. `Hitting Time Distance`_ : The expected time for a random walk to first reach a particular state.
#. `Resistance Distance`_ : Interprets the Markov Chain as an electrical network and computes resistances.
#. `Graph Laplacian Distance`_ : Uses properties of the Laplacian matrix of the graph induced by the Markov Chain.

Entropy and Information-Based Measures
-----------------------------

#. `Relative Entropy Rate`_ : Measures the divergence between the entropy rates of two Markov Chains.
#. `Cross-Entropy Distance`_ : Combines entropy rates to evaluate the distance between chains.
#. `Entropy-Based Similarity`_ : Quantifies similarity using entropy principles.

Behavioral or State-Sequence Measures
-----------------------------

#. `Levenshtein Distance on Paths`_ : Measures the edit distance between state sequences generated by two Markov Chains.
#. `Dynamic Time Warping (DTW)`_ : Measures alignment between state sequences with different lengths.
#. `Sequence Probability Divergence`_ : Compares the likelihood of sequences under two different Markov Chains.

Customized Measures
-----------------------------

#. `Wasserstein Distance`_ : Computes the cost of transforming one stationary distribution into another, using the structure of the state space.
#. `Markov Earth Mover's Distance (MEMD)`_ : A variation of Wasserstein designed for Markov Chains.
#. `Bhattacharyya Distance for Markov Chains`_ : Measures overlap between stationary distributions.
#. `Cosine Similarity on Transition Matrices`_ : Treats the transition matrices as vectors and computes cosine similarity.
#. `MarkovChainSpectral`_

Conclusion
-----------------------------

Markov Chain distances provide a versatile toolkit for comparing stochastic processes, whether through transition matrices, stationary distributions, or state-sequence behaviors. Choosing the right distance depends on the specific application, such as analyzing stationary distributions, comparing paths, or investigating graph-based properties.

This categorized approach simplifies the selection process and ensures you have access to the most relevant methods for your analysis.






**Transition Probability Distances**
------------------------------------

These distances focus on comparing the transition matrices of two Markov chains. They are primarily concerned with how likely it is to move from one state to another in each Markov chain.

1. :doc:`L1`

   - Measures the element-wise difference between the transition matrices of two Markov chains, providing a simple comparison of transition probabilities.

2. :doc:`Kullback-LeiblerDivergence`

   - Compares the transition probabilities by calculating the divergence between probability distributions over transitions in each chain.

3. :doc:`TotalVariation`

   - Measures the maximum difference between transition probabilities, capturing the largest deviation in state transitions between two chains.

**State Distribution Distances**
--------------------------------

These distances evaluate the differences in steady-state or marginal distributions between two Markov chains, helping to capture differences in long-term behavior.

1. :doc:`Steady-StateDistribution`

   - Compares the steady-state distributions of two Markov chains, evaluating the long-term behavior differences.

2. :doc:`Wasserstein`

   - Measures the “cost” of transforming one steady-state distribution into another, capturing the distributional differences between two chains.

3. :doc:`JensenShannonDivergence`

   - Symmetrized version of the Kullback-Leibler divergence that compares the steady-state distributions of the two chains.

**Structural Distances**
------------------------

Structural distances assess the overall architecture of the Markov chains, including how the states are connected and whether there are differences in the structure of the state transitions.

1. :doc:`GraphEditDistance`

   - Calculates the minimal number of edits (additions, deletions, substitutions) required to transform the state transition graph of one Markov chain into another.

2. :doc:`Hamming`

   - Compares the state sequences generated by two Markov chains by calculating the number of positions where the sequences differ.

3. :doc:`SpectralDistance`

   - Compares the eigenvalues of the transition matrices, capturing the differences in the dynamics of the chains, such as mixing times and convergence rates.

Conclusion
==========
The **Distancia** package provides an extensive set of tools to compare Markov chains using various distance measures. Whether you're interested in comparing transition probabilities, state distributions, or the overall structure, **Distancia** offers methods tailored to different analysis needs. By understanding these distances, you can gain valuable insights into the behavior of stochastic systems, making **Distancia** a versatile tool for applications ranging from machine learning to operations research.

    - `MarkovChainWasserstein`_
    - `MarkovChainTotalVariation`_
    - `MarkovChainHellinger`_

.. _MarkovChaine: https://distancia.readthedocs.io/en/latest/markovChainDistance.html
.. _MarkovChainKullbackLeibler: https://distancia.readthedocs.io/en/latest/MarkovChainKullbackLeibler.html
.. _MarkovChainWasserstein: https://distancia.readthedocs.io/en/latest/MarkovChainWasserstein.html
.. _MarkovChainTotalVariation: https://distancia.readthedocs.io/en/latest/MarkovChainTotalVariation.html
.. _MarkovChainHellinger: https://distancia.readthedocs.io/en/latest/MarkovChainHellinger.html
.. _MarkovChainJensenShannon: https://distancia.readthedocs.io/en/latest/MarkovChainJensenShannon.html
.. _MarkovChainFrobenius: https://distancia.readthedocs.io/en/latest/MarkovChainFrobenius.html
.. _MarkovChainSpectral: https://distancia.readthedocs.io/en/latest/MarkovChainSpectral.html
