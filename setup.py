from setuptools import setup

setup(
    name='DistanceMetrics',
    version='0.01',
    packages=['DistanceMetrics 0.01'],
    author='Yves Mercadier',
    author_email='yves.mercadier@example.com',
    description='The DistanceMetrics package is a comprehensive Python library designed to compute a wide variety of distance metrics between two vectors, set, matrix or sequences. This package includes implementations of several well-known distance metrics, each providing a unique measure of dissimilarity or similarity between data points. The toolkit is lightweight and does not rely on external dependencies such as NumPy, making it suitable for educational purposes, small-scale projects, or environments where minimal dependencies are preferred.',
    long_description='The DistanceMetrics package is a comprehensive Python library designed to compute a wide variety of distance metrics between two vectors, set, matrix or sequences. This package includes implementations of several well-known distance metrics, each providing a unique measure of dissimilarity or similarity between data points. The toolkit is lightweight and does not rely on external dependencies such as NumPy, making it suitable for educational purposes, small-scale projects, or environments where minimal dependencies are preferred.\nbash\n\nCopier le code\npip install DistanceMetrics\n\nUsage:\nHere is a detailed example of how to use the DistanceMetrics package:\n\npython\nCopier le code\nfrom DistanceMetrics import *\n# Example vectors\nvector_a = [1, 2, 3]\nvector_b = [4, 5, 6]\n# Create an instance of the DistanceMetrics class\nmetrics = DistanceMetrics()\n# Calculate various distances\neuclidean_distance = metrics.euclidean(vector_a, vector_b)\nmanhattan_distance = metrics.manhattan(vector_a, vector_b)\ncosine_similarity = metrics.cosine_similarity(vector_a, vector_b)\nprint(f"Euclidean Distance: {euclidean_distance}")\nprint(f"Manhattan Distance: {manhattan_distance}")\nprint(f"Cosine Similarity: {cosine_similarity}")',
    url='https://github.com/mon_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPL License',
    ],
)
