Spectral Distance Class
=======================

Introduction
------------

The Spectral Distance class is a Python implementation for measuring the similarity between graphs based on their spectral properties. This method leverages the eigenvalues of the graph Laplacian matrix to quantify structural differences between graphs. It's particularly useful in various fields such as network analysis, bioinformatics, and machine learning on graphs.

Understanding Spectral Distance
-------------------------------

The spectral distance between two graphs is defined as the Euclidean distance between the eigenvalues of their respective Laplacian matrices. Mathematically, for two graphs G1 and G2, the spectral distance D is given by:

.. math::

   D(G1, G2) = \sqrt{\sum_{i=1}^k (\lambda_i^{G1} - \lambda_i^{G2})^2}

Where:
- λ_i^G1 and λ_i^G2 are the i-th eigenvalues of the Laplacian matrices of G1 and G2, respectively.
- k is the number of eigenvalues considered (can be all eigenvalues or a subset).

Key properties:
- It's invariant to node permutations, making it suitable for comparing graphs with different node labelings.
- It captures global structural properties of the graphs.
- The use of normalized Laplacian makes it less sensitive to differences in graph sizes.

Usage Example
-------------

Here's a basic example of how to use the SpectralDistance class:

.. code-block:: python

  import networkx as nx

  def create_sample_graphs():
      # Create a path graph
      P10 = nx.path_graph(10)
    
      # Create a cycle graph
      C10 = nx.cycle_graph(10)
    
      # Create a complete graph
      K10 = nx.complete_graph(10)
    
      # Create two random graphs
      G1 = nx.gnm_random_graph(10, 20)
      G2 = nx.gnm_random_graph(10, 20)
    
      return P10, C10, K10, G1, G2

  def compare_graphs(graphs, names):
      # Initialize SpectralDistance object
      sd = SpectralDistance(k=5, normalized=True)
    
      print("Spectral distances between graphs:")
      for i, (G1, name1) in enumerate(zip(graphs, names)):
          for j, (G2, name2) in enumerate(zip(graphs[i+1:], names[i+1:])):
              distance = sd.calculate(G1, G2)
              print(f"{name1} vs {name2}: {distance:.4f}")

  def main():
      # Create sample graphs
      P10, C10, K10, G1, G2 = create_sample_graphs()
      graph_names = ["Path", "Cycle", "Complete", "Random1", "Random2"]
    
      # Compare the graphs
      compare_graphs([P10, C10, K10, G1, G2], graph_names)

  if __name__ == "__main__":
      main()

This example compares a cycle graph with a path graph, both having 10 nodes. The spectral distance quantifies how different these graphs are structurally.

.. code-block:: bash

  Spectral distances between graphs:
  Path vs Cycle: 1.0351
  Path vs Complete: 1.0969
  Path vs Random1: 0.7070
  Path vs Random2: 0.7057
  Cycle vs Complete: 1.9245
  Cycle vs Random1: 1.5880
  Cycle vs Random2: 1.5554
  Complete vs Random1: 0.6507
  Complete vs Random2: 0.6727
  Random1 vs Random2: 0.0611


Academic Citation
-----------------

When using this implementation in academic work, please cite the seminal paper on spectral graph theory: :footcite:t:`spectraldistance1`

For the specific use of spectral distance in graph comparison, you may also reference: :footcite:t:`spectraldistance2`


.. footbibliography::

Conclusion
----------

The Spectral Distance class provides a powerful tool for graph comparison based on spectral properties. Its strengths lie in its ability to capture global structural similarities and differences between graphs, making it valuable in various applications of network analysis.

Key advantages:
1. Invariance to node permutations
2. Capture of global graph properties
3. Flexibility in the number of eigenvalues used

However, users should be aware of its limitations:
1. Computational complexity for large graphs
2. Potential loss of information when using only a subset of eigenvalues
3. Sensitivity to minor structural changes in some cases

Future work could explore optimizations for large-scale graphs and extensions to weighted or directed graphs. Despite its limitations, the spectral distance remains a fundamental and widely-used method in the field of graph analysis and comparison.
