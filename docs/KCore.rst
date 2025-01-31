===========================
K-Core in Distancia
===========================

Introduction
-----------
The ``KCoreDecomposition`` class implements algorithms for computing the k-core decomposition of graphs. K-cores provide insights into the hierarchical structure of networks by identifying cohesive subgroups and the most densely connected regions, which is crucial for understanding network resilience and community structure.

Conceptual Framework
------------------
A k-core is a maximal subgraph in which each vertex has at least degree k within the subgraph. The k-core decomposition process progressively identifies shells of the network from the periphery (low k) to the core (high k). Each node's core number is the highest k value of a k-core containing that node.

Key Applications:
- Network visualization
- Community detection
- Network robustness analysis
- Influence spread modeling

Formal Definition
---------------
For a graph G = (V,E), a subgraph H ⊆ G is a k-core if:

.. math::

    \forall v \in H: deg_H(v) \geq k

    \nexists H' \supset H: \forall v \in H': deg_{H'}(v) \geq k

where:
- deg_H(v) is the degree of vertex v in subgraph H
- k is the coreness value

The core number of a vertex v is defined as:

.. math::

    c(v) = max\{k | v \in k\text{-core}\}

For weighted graphs, we use the weighted degree:

.. math::

    deg_w(v) = \sum_{u \in N(v)} w(v,u)

Implementation
-------------
.. code-block:: python

    from distancia import KCoreDecomposition

    # Initialize decomposition
    kcore = KCoreDecomposition()

    # Example graph
    graph = {
        'A': {'B': 1.0, 'C': 1.0},
        'B': {'C': 1.0, 'D': 1.0},
        'C': {'D': 1.0},
        'D': {'E': 1.0},
        'E': {}
    }

    # Calculate k-cores
    core_numbers = kcore.decompose(graph)
    shells = kcore.get_shells(graph)

Complexity Analysis
-----------------
The implementation uses an efficient algorithm with the following complexities:

* Time complexity: O(max(|E|, |V|))
* Space complexity: O(|V|)

For weighted graphs:
* Time complexity: O(|E| log |V|)
* Space complexity: O(|V| + |E|)

Academic References
-----------------
1. Seidman, S. B. (1983). "Network structure and minimum degree."
   Social Networks, 5(3), 269-287.
   *Original formulation of k-core decomposition.*

2. Batagelj, V., & Zaversnik, M. (2003). "An O(m) Algorithm for Cores Decomposition of Networks."
   arXiv preprint cs/0310049.
   *Presents the efficient algorithm used in this implementation.*

3. Alvarez-Hamelin, J. I., Dall'Asta, L., Barrat, A., & Vespignani, A. (2008).
   "K-core decomposition of internet graphs: hierarchies, self-similarity and measurement biases."
   Networks and Heterogeneous Media, 3(2), 371-393.
   *Applications in network analysis.*

4. Gaertler, M., & Patrignani, M. (2004).
   "Dynamic Analysis of the Autonomous System Graph."
   IPS 2004, 13-24.
   *Extensions to weighted networks.*

Special Cases and Properties
-------------------------
1. **Nested Structure**:
   - k-cores form a hierarchical structure
   - (k+1)-core is always contained in k-core

2. **Edge Cases**:
   - Empty graph: all vertices have core number 0
   - Complete graph of n vertices: all vertices have core number n-1
   - Tree: all vertices have core number 1 (except leaves: 0)

3. **Properties**:
   - Core numbers are unique
   - Process is deterministic
   - Robust to small perturbations

Conclusion
---------
The ``KCoreDecomposition`` implementation in Distancia provides:

* Efficient computation of core numbers
* Support for both weighted and unweighted graphs
* Shell decomposition functionality
* Robust handling of special cases

Potential future enhancements:
* Parallel implementation for large networks
* Dynamic updates for evolving networks
* Approximate k-core decomposition for massive graphs
* Specialized versions for directed networks

This implementation is particularly useful for:
* Network visualization and analysis
* Finding cohesive subgroups
* Identifying network hierarchy
* Studying network robustness

The combination of computational efficiency and mathematical rigor makes it suitable for both research and practical applications in network analysis.
