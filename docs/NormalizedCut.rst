===================================
Normalized Cut Distance
===================================

Introduction
-----------
Normalized Cut Distance is a graph similarity metric that compares networks based on their partition quality. Unlike simple cut measures, normalized cut considers both the separation between communities and the size of the communities, providing a balanced measure of partition quality. This distance metric is particularly valuable for analyzing image segmentation, data clustering, and community detection problems.

Formal Definition
---------------
For two graphs G1 and G2, the normalized cut distance uses the normalized cut measure Ncut(A,B):

Let Ncut(A,B) be the normalized cut for a partition of graph G into sets A and B:
Ncut(A,B) = cut(A,B)/assoc(A,V) + cut(A,B)/assoc(B,V)

where:
* cut(A,B) is the sum of weights of edges between A and B
* assoc(A,V) is the total connection from A to all nodes in the graph
* V is the set of all vertices

For multiple partitions, the overall normalized cut score NC(G) is:
NC(G) = average(Ncut(Ai,V-Ai)) for all partitions i

The distance is then defined as:
D(G1, G2) = |NC(G1) - NC(G2)|

Intuition and Significance
------------------------
This metric captures:
* Balanced partition quality
* Community separation strength
* Size-normalized division quality
* Natural cluster boundaries

Applications
-----------
Normalized Cut Distance finds applications in various domains:

1. Image Processing
   * Comparing segmentation results
   * Analyzing region boundaries
   * Evaluating partition quality

2. Social Networks
   * Analyzing community structures
   * Evaluating group divisions
   * Studying network partitions

3. Data Mining
   * Comparing clustering results
   * Analyzing data partitions
   * Evaluating segmentation quality

Usage Example
------------
```python
from distancia import NormalizedCutDistance

# Create example graphs with partitions
G1 = nx.Graph()
G1.add_weighted_edges_from([
    (0,1,1), (1,2,1), (0,2,1),  # Partition 1
    (3,4,1), (4,5,1), (3,5,1),  # Partition 2
    (2,3,0.1)                   # Weak bridge
])
partitions1 = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1}

G2 = nx.Graph()
G2.add_weighted_edges_from([
    (0,1,1), (1,2,1), (0,2,1),  # Partition 1
    (3,4,1), (4,5,1), (3,5,1),  # Partition 2
    (2,3,0.5), (1,4,0.5)        # Strong bridges
])
partitions2 = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1}

# Calculate normalized cut distance
ncut_calculator = NormalizedCutDistance()
distance = ncut_calculator.compute(G1, G2, partitions1, partitions2)
print(f"Normalized Cut Distance: {distance}")
```

Computational Complexity
----------------------
The computational complexity for comparing two graphs:
* Time complexity: O(|E|) for normalized cut calculation
* Space complexity: O(|V|) for partition storage
* Overall comparison complexity: O(|E|)

where |V| is the number of vertices and |E| is the number of edges.

Academic References
-----------------
1. Shi, J., & Malik, J. (2000). "Normalized cuts and image segmentation." IEEE PAMI, 22(8), 888-905.
2. von Luxburg, U. (2007). "A tutorial on spectral clustering." Statistics and Computing, 17(4), 395-416.
3. Yu, S. X., & Shi, J. (2003). "Multiclass spectral clustering." ICCV '03.
4. Wagner, D., & Wagner, F. (1993). "Between min cut and graph bisection." MFCS '93.

Conclusion
---------
Normalized Cut Distance provides a balanced way to compare networks based on their partition quality. This metric is particularly effective for:
* Comparing segmentation results
* Evaluating clustering quality
* Analyzing community boundaries
* Studying network divisions

Key considerations:
* Balance between cut and association
* Sensitivity to partition size
* Handling of weighted edges
* Multiple partition comparison

Best practices include:
* Using consistent partitioning methods
* Considering edge weights when available
* Normalizing for network size
* Combining with other structural metrics

The metric is most useful when combined with other distance measures, as it specifically captures partition quality while potentially missing other important network properties.
