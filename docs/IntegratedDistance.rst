IntegratedDistance
===================

Introduction
------------

The `IntegratedDistance` class is a versatile tool designed for seamless integration with popular data science libraries such as `pandas`, `scikit-learn`, and `numpy`. It provides a flexible interface for calculating distances between data points using a custom or predefined distance function, such as the Euclidean distance. This functionality is particularly useful for data analysis workflows where distance computations are a critical part of tasks like clustering, classification, or nearest neighbor search.

Concept and Utility
-------------------

The primary idea behind the `IntegratedDistance` class is to facilitate the application of distance metrics directly to data structures commonly used in data science. By allowing users to compute distances within `pandas` DataFrames or `numpy` arrays and integrate these computations within `scikit-learn` pipelines, the class enhances the usability of distance metrics in real-world applications.

**Utility:**

- **Pandas Integration:** Users can apply distance computations to columns in a DataFrame, making it easier to analyze relationships between data points.
  
- **Scikit-learn Integration:** The class can be used within `scikit-learn` pipelines, providing a seamless way to incorporate custom distance functions into machine learning workflows.
  
- **Numpy Support:** The class handles `numpy` arrays efficiently, making it suitable for large-scale data analysis.

**Example Use Case:**

A typical use case could be calculating the Euclidean distance between rows in two columns of a DataFrame, where each row represents a point in a multi-dimensional space. This can be directly applied in tasks such as clustering or anomaly detection.



# Example usage:
if __name__ == "__main__":
    # Example DataFrame
    data = {
        'point1': [(1, 2), (3, 4), (5, 6)],
        'point2': [(7, 8), (9, 10), (11, 12)]
    }
    df = pd.DataFrame(data)

    # Initialize the distance class with Euclidean distance
    distance_calculator = IntegratedDistance()

    # Apply to DataFrame
    df = distance_calculator.apply_to_dataframe(df, 'point1', 'point2')
    print(df)

    # Example numpy array
    X = np.array([[1, 2], [3, 4], [5, 6]])
    Y = np.array([[7, 8], [9, 10], [11, 12]])

    # Apply within a scikit-learn pipeline context
    distances = distance_calculator.apply_to_sklearn(X, Y)
    print(distances)

    def apply_to_sklearn(self, X, Y=None):
        """
        Apply the distance function within a scikit-learn pipeline.
        
        Parameters:
        X (numpy array or pandas DataFrame): The data for which to compute distances.
        Y (numpy array or pandas DataFrame, optional): Another data set to compare with.
        
        Returns:
        numpy.array: An array of computed distances.
        """
        if Y is None:
            Y = X
        
        distances = np.zeros((X.shape[0], Y.shape[0]))
        for i in range(X.shape[0]):
            for j in range(Y.shape[0]):
                distances[i, j] = self.compute(X[i], Y[j])
                
        return distances

# Example usage:
if __name__ == "__main__":
    # Example DataFrame
    data = {
        'point1': [(1, 2), (3, 4), (5, 6)],
        'point2': [(7, 8), (9, 10), (11, 12)]
    }
    df = pd.DataFrame(data)

    # Initialize the distance class with Euclidean distance
    distance_calculator = IntegratedDistance()

    # Apply to DataFrame
    df = distance_calculator.apply_to_dataframe(df, 'point1', 'point2')
    print(df)

    # Example numpy array
    X = np.array([[1, 2], [3, 4], [5, 6]])
    Y = np.array([[7, 8], [9, 10], [11, 12]])

    # Apply within a scikit-learn pipeline context
    distances = distance_calculator.apply_to_sklearn(X, Y)
    print(distances)


   point1    point2  distance
0  (1, 2)    (7, 8)  8.485281
1  (3, 4)   (9, 10)  8.485281
2  (5, 6)  (11, 12)  8.485281
[[ 8.48528137 11.3137085  14.14213562]
 [ 5.65685425  8.48528137 11.3137085 ]
 [ 2.82842712  5.65685425  8.48528137]]
   point1    point2  distance
0  (1, 2)    (7, 8)  8.485281
1  (3, 4)   (9, 10)  8.485281
2  (5, 6)  (11, 12)  8.485281
[[ 8.48528137 11.3137085  14.14213562]
 [ 5.65685425  8.48528137 11.3137085 ]
 [ 2.82842712  5.65685425  8.48528137]]

Academic Reference
-------------------

The concept of distance metrics is fundamental in many areas of data science, particularly in machine learning and statistical analysis. The use of customizable distance metrics allows researchers and practitioners to tailor their analyses to the specific needs of their data. A relevant academic reference discussing the importance of distance metrics in clustering algorithms is:

- Aggarwal, C. C., & Reddy, C. K. (2013). *Data Clustering: Algorithms and Applications*. Chapman and Hall/CRC. This book provides an in-depth discussion of various distance metrics and their applications in clustering algorithms.

Conclusion
----------

The `IntegratedDistance` class in the `distancia` package is a powerful tool for those who need to apply custom distance metrics within their data analysis workflows.
