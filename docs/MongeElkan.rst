MongeElkanDistance
===================

Introduction
------------
The **MongeElkanDistance** class computes the similarity between two text sequences by comparing their individual components (such as words or characters) through a recursive distance calculation. This method is widely used in fields such as natural language processing, where flexible and partial matching is required.

Distance Meaning
----------------
The **Monge-Elkan** distance measures the similarity between two sequences by evaluating the closest match between each element in one sequence and the elements in the other sequence. Instead of treating each element as an atomic unit, this distance allows for the comparison of elements based on a chosen underlying distance metric, enabling more nuanced and flexible matching.

Formal Definition
-----------------
Given two sequences :math:`X = \{x_1, x_2, ..., x_n\}` and :math:`Y = \{y_1, y_2, ..., y_m\}`, the Monge-Elkan distance is defined as:

.. math::
   D_{ME}(X, Y) = \frac{1}{n} \sum_{i=1}^{n} \min_{j} d(x_i, y_j)

where:
- :math:`d(x_i, y_j)` represents the distance between elements :math:`x_i` and :math:`y_j` using an underlying distance function,
- The distance for each element :math:`x_i` in :math:`X` is determined by the closest corresponding element :math:`y_j` in :math:`Y`,
- :math:`n` is the number of elements in sequence :math:`X`.

.. code-block:: python

   from distancia import MongeElkan,Levenshtein
   from typing import List, Callable


   # Exemple d'utilisation
   text1: str = "the quick brown fox"
   text2: str = "the quick brown dog"

   # Convertir les textes en listes de mots
   set1: List[str] = text1.split()
   set2: List[str] = text2.split()

   # Créer une instance de la classe Monge-Elkan avec la distance de Levenshtein comme distance de base
   monge_elkan = MongeElkan(base_distance=Levenshtein())

   # Calculer la distance Monge-Elkan
   distance: float = monge_elkan.compute(set1, set2)
   print(f"Monge-Elkan Distance: {distance}")

Academic Reference
------------------
The Monge-Elkan distance was first introduced in the context of name matching and entity resolution. A key reference is:
:footcite:t:`MongeElkanDistance`

.. footbibliography::

Conclusion
----------
The **MongeElkanDistance** class provides a powerful technique for comparing sequences with flexible matching criteria. By applying an underlying distance function to compare sub-elements, this distance is well-suited for text comparison tasks where partial matches and inexact alignments are important.
