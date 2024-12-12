NetSimile Class
================

Introduction
------------

The **NetSimile** class implements a graph similarity measure that compares two graphs based on their structural features. Unlike traditional distance metrics that directly compare adjacency matrices, **NetSimile** aggregates node-level features into graph-level descriptors, allowing for efficient and interpretable comparisons. It is particularly effective for graph classification and clustering tasks, providing robust results even for graphs with different sizes and node sets.

Utility
-------

The **NetSimile** distance is useful in several domains, including:

- **Social Network Analysis**: Comparing networks to identify structural similarities in community organization.
- **Biological Network Analysis**: Analyzing similarities between protein interaction networks or neural connectomes.
- **Molecular Graphs**: Understanding structural commonalities in chemical compounds.
- **Graph Summarization**: Providing interpretable summaries of graph similarities for visualization or downstream tasks.

Its ability to operate on summary statistics makes **NetSimile** computationally efficient and scalable for large datasets.

Formal Definition
-----------------

Let \( G_A \) and \( G_B \) represent two graphs. **NetSimile** operates in three main steps:

1. **Feature Extraction**:
   For each node \( v \) in a graph \( G \), compute a set of local structural features \( F(v) \), such as:
   - Degree of the node.
   - Clustering coefficient.
   - Average degree of neighbors.
   - Number of triangles.
   - Eccentricity.
   - Neighbor connectivity.

   The resulting feature matrix \( F \) for \( G \) has dimensions \( n \times f \), where \( n \) is the number of nodes and \( f \) is the number of features.

2. **Aggregation**:
   Compute statistical summaries of each feature across all nodes in the graph:
   - Mean (\( \mu \))
   - Standard deviation (\( \sigma \))
   - Skewness (\( \gamma \))
   - Median (\( m \))
   - Minimum (\( \text{min} \))
   - Maximum (\( \text{max} \))

   This yields a vector \( S(G) \) of aggregated statistics for each graph.

3. **Distance Calculation**:
   Compare the aggregated vectors \( S(G_A) \) and \( S(G_B) \) using a vector distance metric, such as the Canberra distance:
   \[
   d_{\text{NetSimile}}(G_A, G_B) = \sum_{i=1}^n \frac{|S_i(G_A) - S_i(G_B)|}{|S_i(G_A)| + |S_i(G_B)|}
   \]

   Here, \( n \) is the length of the summary vector.

Academic Reference
-------------------

NetSimile is introduced in:

Berlingerio, M., Koutra, D., Eliassi-Rad, T., & Faloutsos, C. (2013). *NetSimile: A Scalable Approach to Size-Independent Network Similarity*. Proceedings of the International Conference on Data Mining (ICDM).  
This paper details the feature extraction, aggregation, and comparison processes, demonstrating the approach's effectiveness in various domains.

Conclusion
----------

The **NetSimile** distance is a practical and efficient graph comparison technique, particularly well-suited for tasks where interpretability and scalability are key. By leveraging statistical summaries of graph features, it offers a robust yet computationally light approach to understanding structural similarities between graphs, making it a valuable tool in graph-based data analysis.
