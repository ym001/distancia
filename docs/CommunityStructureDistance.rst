CommunityStructureDistance
===========================

Introduction
------------
The `CommunityStructureDistance` class provides a method to measure the distance between the community structures of two graphs. Community detection is a fundamental aspect of graph analysis, aimed at uncovering the modular organization within networks. This class utilizes community detection algorithms to compare how nodes are grouped into communities in different graphs.

Idea
----
The primary objective of `CommunityStructureDistance` is to quantify the differences in community structures between two graphs. The distance metric is based on the comparison of detected communities, which are often represented as partitions or sets of nodes. By analyzing these structures, this distance metric can reveal how similar or different the underlying modular organizations of the graphs are.

Formal Definition
-----------------
The distance between the community structures of two graphs \( G_1 \) and \( G_2 \) is computed as follows:

1. **Community Detection**: Apply a community detection algorithm (e.g., Louvain method) to both graphs to identify the communities. Let \( C_1 \) and \( C_2 \) represent the detected communities in \( G_1 \) and \( G_2 \), respectively.

2. **Comparison Metric**: Use a comparison metric (e.g., Jaccard similarity, variation of information) to quantify the dissimilarity between the community structures \( C_1 \) and \( C_2 \).

For example, if \( C_1 \) and \( C_2 \) are partitions of the nodes, the distance can be computed as:
\[ \text{Distance}(G_1, G_2) = \text{ComparisonMetric}(C_1, C_2) \]

Here, `ComparisonMetric` could be a measure like the variation of information (VI) or normalized mutual information (NMI), depending on the specific implementation.

Significance
------------
Understanding the community structure of graphs is essential for various applications, including social network analysis, biological network study, and recommendation systems. The `CommunityStructureDistance` class helps in evaluating how changes in the graph's structure affect its modular organization. This can be particularly useful in scenarios where graphs evolve over time or when comparing different graph-based models.
Example
-------
.. code-block:: python

  import networkx as nx
  from community import community_louvain

  # Exemple de détection des communautés utilisant l'algorithme de Louvain
  def louvain_community_detection(graph):
      """
      Utilise l'algorithme de Louvain pour détecter les communautés dans un graphe.
    
      :param graph: Le graphe d'entrée.
      :return: Une liste de ensembles, où chaque ensemble représente une communauté.
      """
      partition = community_louvain.best_partition(graph)
      communities = {}
      for node, comm_id in partition.items():
          if comm_id not in communities:
              communities[comm_id] = set()
          communities[comm_id].add(node)
      return list(communities.values())

  # Créer deux graphes différents
  graph1 = nx.karate_club_graph()  # Exemple de graphe 1

  # Créer une copie de graph1 et ajouter des modifications pour changer la structure des communautés
  graph2 = graph1.copy()
  graph2.add_edge(0, 1)  # Ajout d'une arête entre deux nœuds dans différentes communautés
  graph2.add_edge(2, 3)  # Ajout d'une arête entre deux nœuds dans différentes communautés

  # Initialiser la classe de distance avec la détection de communautés de Louvain
  distance_calculator = CommunityStructureDistance(louvain_community_detection)

  # Calculer la distance entre les structures de communauté des deux graphes
  distance = distance_calculator.distance(graph1, graph2)

  print(f"The community structure distance between the two graphs is: {distance}")

.. code-block:: bash

  >>>The community structure distance between the two graphs is: 0.18091168091168086


Academic Reference
------------------
:footcite:t:`communitystructuredistance`:  
  
This reference describes the Louvain method, a popular algorithm for community detection, which can be used in conjunction with the `CommunityStructureDistance` class.

.. footbibliography::

Conclusion
----------
The `CommunityStructureDistance` class offers a valuable tool for analyzing and comparing community structures across different graphs. By leveraging community detection algorithms and various comparison metrics, it provides insights into the modular characteristics of networks. This distance measure is crucial for understanding structural similarities and differences in complex graph-based systems.

