ResistanceDistance
=================

Introduction
------------
The ResistanceDistance class implements a method for comparing graphs based on electrical network theory. This distance measure, also known as the resistance distance or electrical distance, treats a graph as an electrical circuit where edges represent unit resistors. It provides a physically interpretable way to measure the dissimilarity between graph structures by analyzing how electrical current would flow through them.

Description
-----------
The resistance distance considers each edge in the graph as a unit resistor and measures the effective resistance between nodes. For comparing two graphs, it analyzes the differences in their resistance distances matrices. This approach provides a robust metric that captures both local and global connectivity patterns in the graphs.

Mathematical Formulation
-----------------------
For a graph G with adjacency matrix A, the resistance distance matrix R is computed as follows:

1. First, compute the Laplacian matrix L:
   .. math::
      L = D - A

   where D is the degree matrix (diagonal matrix with node degrees)

2. Compute the Moore-Penrose pseudoinverse L⁺ of L

3. The resistance distance between nodes i and j is:
   .. math::
      r_{ij} = L^+_{ii} + L^+_{jj} - 2L^+_{ij}

For two graphs G₁ and G₂ with resistance matrices R₁ and R₂, the distance can be computed as:

.. math::

   d(G_1, G_2) = ||R_1 - R_2||_F

where ||·||_F denotes the Frobenius norm.

Properties
---------
1. Non-negativity: d(G₁,G₂) ≥ 0
2. Identity of indiscernibles: d(G₁,G₂) = 0 iff G₁ and G₂ are isomorphic
3. Symmetry: d(G₁,G₂) = d(G₂,G₁)
4. Metric properties:
   - Triangle inequality
   - Invariance under node relabeling
   - Sensitivity to connectivity patterns

Implementation Features
---------------------
The class provides:
1. Efficient computation of resistance distances
2. Multiple normalizations options
3. Handling of disconnected graphs
4. Sparse matrix support
5. Numerical stability safeguards
6. Parallel computation options

Academic References
-----------------
1. Klein, D. J., & Randić, M. (1993). Resistance distance. Journal of Mathematical Chemistry, 12(1), 81-95.

2. Babić, D., Klein, D. J., Lukovits, I., Nikolić, S., & Trinajstić, N. (2002). Resistance-distance matrix: A computational algorithm and its application. International Journal of Quantum Chemistry, 90(1), 166-176.

3. Stevenson, D. E., & Winterrowd, E. (2010). Properties of resistance distances in graphs. arXiv preprint arXiv:1006.0741.

4. Xiao, W., & Gutman, I. (2003). Resistance distance and Laplacian spectrum. Theoretical Chemistry Accounts, 110(4), 284-289.

Applications
-----------
Resistance distances are particularly useful in:
- Network analysis (robustness assessment)
- Chemical graph theory (molecular similarity)
- Transportation networks (accessibility analysis)
- Power grid analysis (network vulnerability)
- Social network analysis (community detection)
- Communication networks (network planning)

Computational Considerations
--------------------------
1. Pseudoinverse Computation:
   - Choice of algorithm based on matrix size
   - Handling of numerical stability
   - Memory efficiency considerations

2. Optimizations:
   - Efficient handling of sparse graphs
   - Parallel computation for large networks
   - Approximation methods for very large graphs

Conclusion
----------
The ResistanceDistance class provides a robust implementation of electrical network-based distance measures for comparing graphs within the distancia package. Its foundation in physical principles makes it particularly suitable for applications where network flow and connectivity are important. The implementation balances computational efficiency with numerical stability, making it applicable to both small and large-scale network analysis problems.

Usage Notes
----------
- Consider graph size and density when choosing computation methods
- Normalize distances for comparing graphs of different sizes
- Be aware of computational complexity for large graphs
- Handle disconnected components appropriately
- Use sparse matrix representations for large, sparse graphs
