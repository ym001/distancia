**distancia** - A Comprehensive Distance Metrics Package for Python

distancia is a Python package that provides an extensive collection of distance metrics and similarity measures, making it easy to calculate and compare the proximity between various types of data. Whether you're working with strings, vectors, or other data types, distancia offers the tools you need for your analysis.

**Features**
Diverse Range of Metrics: Calculate distances using a variety of algorithms including Euclidean, Manhattan, Cosine Similarity, Hamming, Jaccard, Levenshtein, and many more.
Ease of Use: Simple and intuitive API design, making it easy to integrate into your existing projects.
Customizable: Easily extend the package with your own custom distance metrics.
Well-Documented: Each function is well-documented, providing clear explanations and examples of use.

**Installation**
You can install distancia via pip:
[distancia on Pypi](https://pypi.org/project/distancia/)


bash
Copier le code
pip install distancia

**Usage**
Below are some examples of how to use the Distancer package to calculate various distance metrics.

**Example 1:** Calculating Euclidean Distance
python
Copier le code :

```python

from distancia import Euclidean

point1 = [1, 2, 3]
point2 = [4, 5, 6]

distance = Euclidean().distance(point1, point2)
print(f"Euclidean Distance: {distance}")
```

**Example 2: Calculating Cosine Similarity**
python
Copier le code :

from distancia import Cosine_Similarity

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

similarity = Cosine_Similarity().distance(vector1, vector2)
print(f"Cosine Similarity: {similarity}")

**Example 3: Calculating Levenshtein Distance**
python
Copier le code :

from distancia import Levenshtein

string1 = "kitten"
string2 = "sitting"

distance = Levenshtein().distance(string1, string2)
print(f"Levenshtein Distance: {distance}")

**Available Metrics**
distancia includes the following distance metrics (and more):

* Euclidean
* Minkowski
* Hamming
* Cosine_Similarity 
* Cosine_Inverse 
* L1 
* L2 
* Jaccard 
* Generalized_Jaccard 
* Tanimoto 
* Inverse_Tanimoto 
* Manhattan 
* Mahalanobis 
* Chebyshev 
* Ratcliff_Obershelp 
* Jaro 
* Jaro_Winkler 
* Hausdorff 
* Kendall_Tau
* Haversine 
* Canberra 
* Bray_Curtis 
* Matching 
* Dice 
* Kulsinski 
* Rogers_Tanimoto 
* Russell_Rao 
* Sokal_Michener 
* Sokal-Sneath 
* Damerau_Levenshtein 
* Tversky 
* Yule 
* Bhattacharyya 
* Wasserstein 
* Mahalanobis_Taguchi 
* Gower 
* Pearson 
* Spearman 
* Ochiai 
* Hellinger 
* Czekanowski_Dice 
* Motzkin_Straus 
* Otsuka 
* Fager_McGowan 
* Rogers_Tanimoto 
* Enhanced_Rogers_Tanimoto 


And many more...
Contributing
Contributions are welcome! If you'd like to contribute to Distancia, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

**License**
distancia is licensed under the MIT License. See LICENSE for more information.

**Authors**
distancia was developed and maintained by YvesMercadier and the open-source community.

**Acknowledgments**
This package was inspired by the need for a comprehensive and easy-to-use library for distance metrics. We would like to thank all the contributors and users who have provided feedback and improvements to the project.

This README file provides an overview of the package, how to install it, usage examples, and other relevant information. It serves as an introduction and guide for new users who want to understand what the package does and how to use it effectively.

