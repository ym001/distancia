WeisfeilerLehman Class
======================

Introduction
------------

The **WeisfeilerLehman** class implements a distance metric inspired by the Weisfeiler-Lehman graph kernel, a method widely used in graph theory and machine learning. This metric is based on iterative neighborhood aggregation, where node features are recursively updated based on their neighbors' features. The result is a powerful, scalable approach to comparing the structure of graphs or their matrix representations.

The **WeisfeilerLehman** distance is especially effective for comparing graphs with rich structural properties, capturing both local and global similarities.

Utility
-------

The **WeisfeilerLehman** distance is applicable in various scenarios, such as:

- **Graph Classification**: Measuring similarities between graph structures for supervised or unsupervised learning.
- **Molecular Graph Analysis**: Comparing chemical compounds or molecular structures represented as graphs.
- **Social Network Analysis**: Identifying communities or similar structures in large networks.
- **Pattern Recognition**: Supporting graph-based feature extraction and matching.

This metric is widely used in machine learning pipelines, especially when working with graph kernels or graph neural networks.

Formal Definition
-----------------

Let \( A \) and \( B \) be the adjacency matrices of two graphs \( G_A \) and \( G_B \). The Weisfeiler-Lehman distance is computed by iteratively refining node labels and comparing the resulting graphs. Formally:

1. **Initialization**:
   Each node \( v \) in \( G_A \) and \( G_B \) is assigned an initial label \( l_0(v) \), often derived from its degree or other features.

2. **Neighborhood Aggregation**:
   At iteration \( k \), the label of each node \( v \) is updated as:
   \[
   l_k(v) = \text{hash}\left(l_{k-1}(v), \{l_{k-1}(u) \,|\, u \in \text{neighbors}(v)\}\right)
   \]
   Here, \( \text{hash} \) is a function that maps the node's previous label and its neighbors' labels into a new label.

3. **Distance Computation**:
   After \( K \) iterations, the distance between \( G_A \) and \( G_B \) is computed by comparing the distributions of node labels:
   \[
   d_{\text{WL}}(G_A, G_B) = \sum_{k=0}^{K} \text{Divergence}(\text{LabelDist}_k(G_A), \text{LabelDist}_k(G_B))
   \]
   Where \( \text{LabelDist}_k \) is the distribution of labels at iteration \( k \), and \( \text{Divergence} \) is a measure such as the Wasserstein distance or Jensen-Shannon divergence.

Academic Reference
-------------------

The Weisfeiler-Lehman graph kernel is a foundational method in graph machine learning. A key reference is:

Shervashidze, N., Vishwanathan, S. V. N., Petri, T., Mehlhorn, K., & Borgwardt, K. M. (2011). Weisfeiler-Lehman Graph Kernels. *Journal of Machine Learning Research*, 12, 2539-2561.  
This work formalizes the Weisfeiler-Lehman framework and demonstrates its effectiveness in graph classification tasks.

Conclusion
----------

The **WeisfeilerLehman** distance is a versatile and robust metric for graph comparison, capable of capturing structural nuances while remainin
