Vector-Based Distances
======================

Introduction
============
When comparing vectors, it is crucial to understand the different mathematical principles and methods that can be applied depending on the type of data and the context. The **Distancia** package provides a comprehensive suite of vector-based distance measures that allow for the evaluation of similarity or dissimilarity between vectors. These methods can be applied in domains such as machine learning, signal processing, and data clustering, among others.


List of Vector-Based Distances
==============================

**Metric Distances**
--------------------

Metric distances follow mathematical properties such as symmetry, non-negativity, and the triangle inequality. These distances are often used when a precise, geometrically consistent measurement is required between vectors.
Vector-Based Distance Measures
==============================

This section organizes vector-based distance measures into distinct categories for better clarity and understanding. Each measure is linked to its respective documentation or mathematical definition.

**1. Euclidean and Minkowski Family**  
These distances are based on geometric norms and are widely used in various applications.

#. `Euclidean`_  
   The straight-line distance between two points in Euclidean space.
#. `Manhattan`_ 
   The sum of absolute differences between vector components, also known as L1 norm.
#. `Chebyshev`_  
   The maximum absolute difference between vector components, corresponding to L∞ norm.
#. `Canberra`_  
   A weighted metric emphasizing small differences between components.

**2. Similarity Measures**  
These metrics quantify similarity rather than dissimilarity between vectors.

5. `Jaccard`_  
   The intersection over the union of two binary vectors.
#. `GeneralizedJaccard`_  
   Extends Jaccard to weighted vectors.
#. `Tanimoto`_ 
   A similarity metric similar to Jaccard, used in chemistry and information retrieval.
#. `Ochiai`_   
   A cosine-like measure for binary overlaps.
#. `CzekanowskiDice`_ 
   A similarity measure emphasizing common elements.
#. `Pearson`_ 
   Measures linear correlation between two vectors.
#. `Spearman`_ 
   A rank-based correlation metric.

**3. Probabilistic and Divergence Measures**  
Metrics designed for comparing probability distributions or statistical properties.

12. `Bhattacharyya`_ 
    Quantifies similarity between two probability distributions.
#. `KullbackLeibler`_ 
   A divergence metric for comparing probability distributions, often asymmetric.
#. `Hellinger`_  
   Computes the divergence based on the Bhattacharyya coefficient.
#. `Wasserstein`_ 
   Also known as Earth Mover's Distance, measures the effort required to transform one distribution into another.

**4. Binary and Categorical Measures**  
Specialized for binary vectors and categorical data.

16. `RogersTanimoto`_  
    Focuses on binary matches and mismatches.
#. `RussellRao`_   
   Measures binary similarity based on shared ones.
#. `SokalMichener`_ 
   Evaluates binary dissimilarity using equal weighting for matches.
#. `SokalSneath`_ 
   A variant of SokalMichener with different weighting.
#. `EnhancedRogersTanimoto`_  
   An improved version of RogersTanimoto.
#. `FagerMcGowan`_  
   Derived from ecological studies, adapted for binary data.
#. `Otsuka`_   
   Measures binary similarity, emphasizing shared proportions.

**5. Geometric and Contextual Measures**  
Metrics designed for spatial and contextual data.

23. `Haversine`_ 
    Computes spherical distances, useful for geographic coordinates.
#. `ContextualDynamicDistance`_ 
   Adapts dynamically based on data properties.
#. `Gestalt`_ 
   Captures overall alignment between two vectors.

**6. Graph and Miscellaneous Measures**  
Unique metrics for specialized applications, including graph theory.

26. `MotzkinStraus`_   
    Used in graph-theoretic contexts, adapted for vectors.
#. `BrayCurtis`_ 
   Measures compositional dissimilarity in ecology.
#. `Gower`_   
   A general similarity measure applicable to mixed-type data.

This categorized approach facilitates better navigation and understanding of vector-based distance measures, aligning them with specific domains and applications. 

   
Conclusion
==========
The **Distancia** package provides a versatile and robust collection of vector-based distance measures, allowing users to compare vectors in various ways depending on their specific needs. By categorizing distances into metric, non-metric, probabilistic, and information-theoretic types, **Distancia** enables flexible and accurate vector comparisons. Whether you need to compute exact geometric distances or probabilistic differences, **Distancia** offers a comprehensive toolkit for analyzing the relationships between vectors in your data.

.. _Euclidean: https://distancia.readthedocs.io/en/latest/Euclidean.html
.. _Manhattan: https://distancia.readthedocs.io/en/latest/Manhattan.html
.. _Jaro: https://distancia.readthedocs.io/en/latest/Jaro.html
.. _KendallTau: https://distancia.readthedocs.io/en/latest/KendallTau.html
.. _Bhattacharyya: https://distancia.readthedocs.io/en/latest/Bhattacharyya.html
.. _Haversine: https://distancia.readthedocs.io/en/latest/Haversine.html
.. _Chebyshev: https://distancia.readthedocs.io/en/latest/Chebyshev.html
.. _ContextualDynamicDistance: https://distancia.readthedocs.io/en/latest/ContextualDynamicDistance.html
.. _Canberra: https://distancia.readthedocs.io/en/latest/Canberra.html
.. _BrayCurtis: https://distancia.readthedocs.io/en/latest/BrayCurtis.html
.. _RogersTanimoto: https://distancia.readthedocs.io/en/latest/RogersTanimoto.html
.. _RussellRao: https://distancia.readthedocs.io/en/latest/RussellRao.html
.. _SokalMichener: https://distancia.readthedocs.io/en/latest/SokalMichener.html
.. _SokalSneath: https://distancia.readthedocs.io/en/latest/SokalSneath.html
.. _Wasserstein: https://distancia.readthedocs.io/en/latest/Wasserstein.html
.. _Gower: https://distancia.readthedocs.io/en/latest/Gower.html
.. _CzekanowskiDice: https://distancia.readthedocs.io/en/latest/CzekanowskiDice.html
.. _Hellinger: https://distancia.readthedocs.io/en/latest/Hellinger.html
.. _MotzkinStraus: https://distancia.readthedocs.io/en/latest/MotzkinStraus.html
.. _EnhancedRogersTanimoto: https://distancia.readthedocs.io/en/latest/EnhancedRogersTanimoto.html
.. _KullbackLeibler: https://distancia.readthedocs.io/en/latest/KullbackLeibler.html
.. _Jaccard: https://distancia.readthedocs.io/en/latest/Jaccard.html
.. _GeneralizedJaccard: https://distancia.readthedocs.io/en/latest/GeneralizedJaccard.html
.. _Tanimoto: https://distancia.readthedocs.io/en/latest/Tanimoto.html
.. _InverseTanimoto: https://distancia.readthedocs.io/en/latest/InverseTanimoto.html
.. _Ochiai: https://distancia.readthedocs.io/en/latest/Ochiai.html
.. _CzekanowskiDice: https://distancia.readthedocs.io/en/latest/CzekanowskiDice.html
.. _Pearson: https://distancia.readthedocs.io/en/latest/Pearson.html
.. _Spearman: https://distancia.readthedocs.io/en/latest/Spearman.html
.. _FagerMcGowan: https://distancia.readthedocs.io/en/latest/FagerMcGowan.html
.. _Otsuka: https://distancia.readthedocs.io/en/latest/Otsuka.html
.. _Gestalt: https://distancia.readthedocs.io/en/latest/Gestalt.html
