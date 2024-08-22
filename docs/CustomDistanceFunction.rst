CustomDistanceFunction
=======================

Introduction
------------

The `CustomDistanceFunction` class in the `distancia` package allows users to define their own custom distance functions. It is designed to provide flexibility for users who require specific distance metrics that are not commonly available or implemented in standard libraries. This is particularly useful in research or specialized applications where conventional distance measures do not suffice.

Concept and Utility
-------------------

The main idea behind the `CustomDistanceFunction` is to empower users to compute distances between data points based on their specific needs. By accepting a user-defined Python function, this class facilitates the creation of tailored distance metrics, which can then be seamlessly integrated into various machine learning workflows or analytical tasks.

For instance, in some cases, traditional metrics like Euclidean or Manhattan distances may not capture the nuances of the data being analyzed. By using `CustomDistanceFunction`, users can encode domain-specific knowledge directly into the distance computation, potentially improving the performance of algorithms that rely on these metrics, such as clustering, nearest neighbors, or other forms of instance-based learning.

Usage Example
-------------

Here’s a brief example of how to use the `CustomDistanceFunction` class:

```python
from distancia.distance_metrics import CustomDistanceFunction

# Define a custom distance function
def my_custom_function(p, q):
    return sum(abs(p_i - q_i) for p_i, q_i in zip(p, q))

# Create an instance of CustomDistanceFunction
custom_distance = CustomDistanceFunction(func=my_custom_function)

# Example points
point1 = (1, 2, 3)
point2 = (4, 2, 3)

# Compute the custom distance
distance = custom_distance.compute(point1, point2)
print(f"Custom distance: {distance}")


Academic Reference
------------------

Custom distance functions are often used in specialized fields where standard metrics are inadequate. For example, in the work by 
*Grauman, K., & Darrell, T. (2005)* titled "The Pyramid Match Kernel: Discriminative Classification with Sets of Image Features," 
a custom distance metric was devised to compare unordered sets of image features, showing the power of tailored metrics in improving classification tasks.

Conclusion
----------

The `CustomDistanceFunction` class is a versatile tool for anyone needing to go beyond standard distance metrics. It allows the user to encode their specific requirements into a distance function, making it suitable for a wide range of applications from academic research to industry-specific data analysis. By providing this level of customization, the `distancia` package enhances its utility for users with unique and specialized needs.

