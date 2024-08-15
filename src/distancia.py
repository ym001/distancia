#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  distancia.py
#  
#  Copyright 2024 yves <yves.mercadier@...>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from abc import ABC   # permet de définir des classes de base

class Distance(ABC):
	obj1_exemple=[1, 2, 3]
	obj2_exemple=[4, 5, 6]
	type1=list
	type2=list
	
	def distance(self,*args):
	#def distance(self, obj1, obj2):
		"""
		Calculate the distance between two objects.
		:param obj1: First object
		:param obj2: Second object
		....
		:return: Distance between obj1, obj2, ...
		"""
		if len(args)==2:
			return self.distance_function(args[0], args[1])
		if len(args)==3:
			return self.distance_function(args[0], args[1], args[2])
		if len(args)==4:
			return self.distance_function(args[0], args[1], args[2], args[3])

	def check_data(self, obj1, obj2):
		"""
		Verify the data of a distance measure: type, dimension.
		"""
		
		print(type(obj1))
		print(self.type1)
		properties = {
				f'collection1_type {self.type1}': type(obj1) is self.type1,
				f'collection2_type {self.type2}': type(obj2) is self.type2,
				f'data_type': True and True,
				f'association_rules': True and True,
		}
		print(f"Data verification: {properties}")
		
	def check_properties(self, obj1, obj2, obj3):
		"""
		Verify the properties of a distance measure: non-negativity, identity of indiscernibles, symmetry, and triangle inequality.
		:param obj1: First object
		:param obj2: Second object
		:param obj3: Third object
		:return: Dictionary indicating whether each property holds
		"""
		d12 = self.distance(obj1, obj2)
		d13 = self.distance(obj1, obj3)
		d23 = self.distance(obj2, obj3)

		properties = {
				'non_negativity': d12 >= 0 and d13 >= 0 and d23 >= 0,
				'identity_of_indiscernibles': (d12 == 0) == (obj1 == obj2) and (d13 == 0) == (obj1 == obj3) and (d23 == 0) == (obj2 == obj3),
				'symmetry': d12 == self.distance(obj2, obj1) and d13 == self.distance(obj3, obj1) and d23 == self.distance(obj3, obj2),
				'triangle_inequality': d12 <= d13 + d23 and d13 <= d12 + d23 and d23 <= d12 + d13,
		}
		print(f"Properties verification: {properties}")

	def exemple(self):
		# Example usage
		if not hasattr(self, 'obj3_exemple')and not hasattr(self, 'obj4_exemple'):
			print(f"{self.__class__.__name__} distance between {self.obj1_exemple} and {self.obj2_exemple} is {self.distance(self.obj1_exemple, self.obj2_exemple):.2f}")
		elif not hasattr(self, 'obj4_exemple'):
			print(f"{self.__class__.__name__} distance {self.obj3_exemple} between {self.obj1_exemple} and {self.obj2_exemple} is {self.distance(self.obj1_exemple, self.obj2_exemple, self.obj3_exemple):.2f}")
		else:
			print(f"{self.__class__.__name__} distance {self.obj3_exemple}, {self.obj4_exemple} between {self.obj1_exemple} and {self.obj2_exemple} is {self.distance(self.obj1_exemple, self.obj2_exemple, self.obj3_exemple, self.obj4_exemple):.2f}")

###################################################
class Levenshtein(Distance):
	def __init__(self):
		super().__init__()
		self.type1=str
		self.type2=str
	def distance_function(self,s1, s2):
		dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

		for i in range(len(s1) + 1):
			dp[i][0] = i
		for j in range(len(s2) + 1):
			dp[0][j] = j

		for i in range(1, len(s1) + 1):
			for j in range(1, len(s2) + 1):
				if s1[i - 1] == s2[j - 1]:
					cost = 0
				else:
					cost = 1
				dp[i][j] = min(dp[i - 1][j] + 1,        # Suppression
                           dp[i][j - 1] + 1,        # Insertion
                           dp[i - 1][j - 1] + cost) # Substitution

		return dp[len(s1)][len(s2)]
		
	def exemple(self):
		self.obj1_exemple = "kitten"
		self.obj2_exemple = "sitting"
		super().exemple()


class Cosine_Similarity(Distance):
	def __init__(self):
		super().__init__()
		
	def dot_product(self,vec1, vec2):
		"""
		Calculate the dot product between two vectors.
    
		:param vec1: First vector
		:param vec2: Second vector
		:return: Dot product of vec1 and vec2
		"""
		return sum(x * y for x, y in zip(vec1, vec2))

	def norm(self,vec):
		"""
		Calculate the norm (magnitude) of a vector.
    
		:param vec: Input vector
		:return: Norm of the vector
		"""
		return (sum(x * x for x in vec))**0.5

	def distance_function(self,vec1, vec2):
		"""
		Calculate the cosine similarity between two vectors.
    
		:param vec1: First vector
		:param vec2: Second vector
		:return: Cosine similarity between vec1 and vec2
		"""
		dot_prod = self.dot_product(vec1, vec2)
		norm_vec1 = self.norm(vec1)
		norm_vec2 = self.norm(vec2)
		if norm_vec1 == 0 or norm_vec2 == 0:
			# Handling edge case if any vector has zero length to avoid division by zero
			return 0.0
		return dot_prod / (norm_vec1 * norm_vec2)
		

class Cosine_Inverse(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,vec1, vec2):
		return 1-Cosine_Similarity().distance(vec1,vec2)


class Euclidean(Distance):
	def __init__(self):
		super().__init__()
		
	def distance_function(self,point1, point2):
		"""
		Calculate the Euclidean distance between two points.
    
		:param point1: First point as a list of coordinates
		:param point2: Second point as a list of coordinates
		:return: Euclidean distance between point1 and point2
		"""
		if len(point1) != len(point2):
			raise ValueError("Points must have the same dimensions")

		distance = 0.0
		for p1, p2 in zip(point1, point2):
			distance += (p1 - p2) ** 2
		return distance**0.5
		
class L2(Euclidean):
	def __init__(self):
		super().__init__()

class Hamming(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,str1, str2):
		"""
		Calculate the Hamming distance between two strings.
    
		:param str1: First string
		:param str2: Second string
		:return: Hamming distance between str1 and str2
		:raises ValueError: If the strings are not of the same length
		"""
		if len(str1) != len(str2):
			raise ValueError("Strings must be of the same length")
    
		return sum(el1 != el2 for el1, el2 in zip(str1, str2))
	def exemple(self):
		self.obj1_exemple = "1011101"
		self.obj2_exemple = "1001001"
		super().exemple()

class Jaccard(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,set1, set2):
		"""
		Calculate the Jaccard distance between two sets.
    
		:param set1: First set
		:param set2: Second set
		:return: Jaccard distance between set1 and set2
		"""
		intersection = len(set1.intersection(set2))
		union = len(set1.union(set2))
		if union == 0:
			return 0.0  # Both sets are empty
		return 1 - (intersection / union)
	def exemple(self):
		self.obj1_exemple = {1, 2, 3, 4}
		self.obj2_exemple = {3, 4, 5, 6}
		super().exemple()

class Generalized_Jaccard(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,x, y):
		"""
		Calcule la distance de Jaccard généralisée entre deux vecteurs.
    
		:param x: Premier vecteur (sous forme de liste ou d'array).
		:param y: Deuxième vecteur (sous forme de liste ou d'array).
		:return: Distance de Jaccard généralisée entre x et y.
		"""
		if len(x) != len(y):
			raise ValueError("Les vecteurs doivent avoir la même longueur.")
    
		min_sum = sum(min(x_i, y_i) for x_i, y_i in zip(x, y))
		max_sum = sum(max(x_i, y_i) for x_i, y_i in zip(x, y))
    
		if max_sum == 0:
			return 0.0  # Pour éviter la division par zéro
        
		return 1 - (min_sum / max_sum)
	def exemple(self):
		self.obj1_exemple = {1, 2, 3, 4}
		self.obj2_exemple = {3, 4, 5, 6}
		super().exemple()

class Tanimoto(Jaccard):
	def __init__(self):
		super().__init__()

class Inverse_Tanimoto(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,vector_a, vector_b):
		"""
		Calcule la distance Tanimoto inversée entre deux vecteurs binaires.
    
		:param vector_a: Premier vecteur (de type list).
		:param vector_b: Deuxième vecteur (de type list).
		:return: Distance Tanimoto inversée entre vector_a et vector_b.
		"""
		# Calcul de la similarité Tanimoto
		tanimoto = self.tanimoto_similarity(vector_a, vector_b)
    
		# Calcul de la distance Tanimoto inversée
		inverse_tanimoto = 1 - tanimoto
		return inverse_tanimoto
    
	def tanimoto_similarity(self,vector_a, vector_b):
		"""
		Calcule la similarité Tanimoto entre deux vecteurs binaires.
    
		:param vector_a: Premier vecteur (de type list).
		:param vector_b: Deuxième vecteur (de type list).
		:return: Similarité Tanimoto entre vector_a et vector_b.
		"""
		# Calcul du produit scalaire
		dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    
		# Calcul des sommes des carrés des vecteurs
		sum_square_a = sum(a * a for a in vector_a)
		sum_square_b = sum(b * b for b in vector_b)
    
		# Calcul de la similarité Tanimoto
		tanimoto = dot_product / (sum_square_a + sum_square_b - dot_product)
		return tanimoto
	def exemple(self):
		self.obj1_exemple = [1, 1, 0, 0]
		self.obj2_exemple = [1, 0, 1, 0]
		super().exemple()



class Manhattan(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,point1, point2):
		"""
		Calculate the Manhattan distance, taxicab or L1 between two points.
    
		:param point1: First point as a list of coordinates
		:param point2: Second point as a list of coordinates
		:return: Manhattan distance between point1 and point2
		:raises ValueError: If the points are not of the same dimension
		"""
		if len(point1) != len(point2):
			raise ValueError("Points must have the same dimensions")
    
		distance = sum(abs(p1 - p2) for p1, p2 in zip(point1, point2))
		return distance
		
class L1(Manhattan):
	def __init__(self):
		super().__init__()

class Minkowski(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,point1, point2, p):
		"""
		Calculate the Minkowski distance between two points.
    
		:param point1: First point as a list of coordinates
		:param point2: Second point as a list of coordinates
		:param p: The order of the Minkowski distance
		:return: Minkowski distance between point1 and point2
		:raises ValueError: If the points are not of the same dimension
		"""
		if len(point1) != len(point2):
			raise ValueError("Points must have the same dimensions")
    
		distance = sum(abs(p1 - p2) ** p for p1, p2 in zip(point1, point2)) ** (1 / p)
		return distance
	def exemple(self,p):
		self.obj3_exemple = p
		super().exemple()


class Mahalanobis(Distance):
	def __init__(self):
		super().__init__()
	def mean(self,data):
		"""
		Calculate the mean of each dimension in the dataset.
    
		:param data: A dataset as a list of points (list of lists)
		:return: Mean of each dimension as a list
		"""
		n = len(data)
		d = len(data[0])
		mean = [0] * d
    
		for point in data:
			for i in range(d):
				mean[i] += point[i]
    
		mean = [x / n for x in mean]
		return mean

	def covariance_matrix(self,data, mean):
		"""
		Calculate the covariance matrix of the dataset.
    
		:param data: A dataset as a list of points (list of lists)
		:param mean: Mean of each dimension as a list
		:return: Covariance matrix as a list of lists
		"""
		n = len(data)
		d = len(data[0])
		cov_matrix = [[0] * d for _ in range(d)]
    
		for point in data:
			diff = [point[i] - mean[i] for i in range(d)]
			for i in range(d):
				for j in range(d):
					cov_matrix[i][j] += diff[i] * diff[j]
    
		cov_matrix = [[x / (n - 1) for x in row] for row in cov_matrix]
		return cov_matrix

	def matrix_inverse(self,matrix):
		"""
		Calculate the inverse of a matrix using Gauss-Jordan elimination.
    
		:param matrix: A square matrix as a list of lists
		:return: Inverse of the matrix as a list of lists
		"""
		n = len(matrix)
		identity = [[float(i == j) for i in range(n)] for j in range(n)]
		augmented = [row + identity_row for row, identity_row in zip(matrix, identity)]
		for i in range(n):
			pivot = augmented[i][i]
			for j in range(2 * n):
				augmented[i][j] /= pivot
			for k in range(n):
				if k != i:
					factor = augmented[k][i]
					for j in range(2 * n):
						augmented[k][j] -= factor * augmented[i][j]
    
		inverse = [row[n:] for row in augmented]
		return inverse

	def distance_function(self,point, data):
		"""
		Calculate the Mahalanobis distance between a point and a dataset.
    
		:param point: A point as a list of coordinates
		:param data: A dataset as a list of points (list of lists)
		:return: Mahalanobis distance between the point and the dataset
		:raises ValueError: If the point dimensions do not match the dataset dimensions
		! lever une execption si la matrice est singulière
		"""
		if len(data[0]) != len(point):
			raise ValueError("Point dimensions must match dataset dimensions")
    
		mean_data = self.mean(data)
		cov_matrix = self.covariance_matrix(data, mean_data)
		cov_matrix_inv = self.matrix_inverse(cov_matrix)
    
		diff = [point[i] - mean_data[i] for i in range(len(point))]
    
		# Matrix multiplication: diff^T * cov_matrix_inv * diff
		result = 0
		for i in range(len(diff)):
			for j in range(len(diff)):
				result += diff[i] * cov_matrix_inv[i][j] * diff[j]
    
		return result**0.5
	def exemple(self):
		self.obj2_exemple = [
    [2, 1, 0],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
]
		super().exemple()

class Chebyshev(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,point1, point2):

		"""
		Calculate the Chebyshev distance between two points.
    
		:param point1: A list of coordinates for the first point
		:param point2: A list of coordinates for the second point
		:return: Chebyshev distance between the two points
		:raises ValueError: If the points do not have the same dimensions
		"""
		if len(point1) != len(point2):
			raise ValueError("Points must have the same dimensions")
    
		return max(abs(a - b) for a, b in zip(point1, point2))


class Ratcliff_Obershelp(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,str1, str2):
		"""
		ou Similarité Gestalt.
		Calculate the Ratcliff/Obershelp distance between two strings.
    
		:param str1: The first string
		:param str2: The second string
		:return: Ratcliff/Obershelp distance between the two strings
		"""
		def find_longest_common_substring(s1, s2):
			"""
			Helper function to find the longest common substring between two strings.
        
			:param s1: The first string
			:param s2: The second string
			:return: The longest common substring
			"""
			matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
			longest_length = 0
			lcs_end = 0

			for i in range(1, len(s1) + 1):
				for j in range(1, len(s2) + 1):
					if s1[i - 1] == s2[j - 1]:
						matrix[i][j] = matrix[i - 1][j - 1] + 1
						if matrix[i][j] > longest_length:
							longest_length = matrix[i][j]
							lcs_end = i

			return s1[lcs_end - longest_length: lcs_end]

		def recursive_match(s1, s2):
			"""
			Helper function to recursively match substrings.
        
			:param s1: The first string
			:param s2: The second string
			:return: The total length of matched substrings
			"""
			lcs = find_longest_common_substring(s1, s2)
			if not lcs:
				return 0

			lcs_length = len(lcs)
			lcs_start1 = s1.find(lcs)
			lcs_start2 = s2.find(lcs)

			return (
				lcs_length +
				recursive_match(s1[:lcs_start1], s2[:lcs_start2]) +
				recursive_match(s1[lcs_start1 + lcs_length:], s2[lcs_start2 + lcs_length:])
			)

		total_length = len(str1) + len(str2)
		if total_length == 0:
			return 0.0

		matched_length = recursive_match(str1, str2)
		similarity = (2 * matched_length) / total_length

		return 1 - similarity
	def exemple(self):
		self.obj1_exemple = "kitten"
		self.obj2_exemple = "sitting"
		super().exemple()

class Jaro(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,s1, s2):
		"""
		Calculate the Jaro similarity between two strings.
    
		:param s1: The first string
		:param s2: The second string
		:return: Jaro similarity between the two strings
		"""
		if s1 == s2:
			return 1.0

		len_s1 = len(s1)
		len_s2 = len(s2)

		if len_s1 == 0 or len_s2 == 0:
			return 0.0

		match_distance = max(len_s1, len_s2) // 2 - 1

		s1_matches = [False] * len_s1
		s2_matches = [False] * len_s2

		matches = 0
		transpositions = 0

		for i in range(len_s1):
			start = max(0, i - match_distance)
			end = min(i + match_distance + 1, len_s2)

			for j in range(start, end):
				if s2_matches[j]:
					continue
				if s1[i] != s2[j]:
					continue
				s1_matches[i] = True
				s2_matches[j] = True
				matches += 1
				break

		if matches == 0:
			return 0.0

		k = 0
		for i in range(len_s1):
			if not s1_matches[i]:
				continue
			while not s2_matches[k]:
				k += 1
			if s1[i] != s2[k]:
				transpositions += 1
			k += 1

		return (matches / len_s1 + matches / len_s2 + (matches - transpositions // 2) / matches) / 3.0
	def exemple(self):
		self.obj1_exemple = "martha"
		self.obj2_exemple = "marhta"
		super().exemple()

class Jaro_Winkler(Distance):
	def __init__(self):
		super().__init__()
	def Jaro(self,s1, s2):
		"""
		Calculate the Jaro similarity between two strings.
    
		:param s1: The first string
		:param s2: The second string
		:return: Jaro similarity between the two strings
		"""
		if s1 == s2:
			return 1.0

		len_s1 = len(s1)
		len_s2 = len(s2)

		if len_s1 == 0 or len_s2 == 0:
			return 0.0

		match_distance = max(len_s1, len_s2) // 2 - 1

		s1_matches = [False] * len_s1
		s2_matches = [False] * len_s2

		matches = 0
		transpositions = 0

		for i in range(len_s1):
			start = max(0, i - match_distance)
			end = min(i + match_distance + 1, len_s2)

			for j in range(start, end):
				if s2_matches[j]:
					continue
				if s1[i] != s2[j]:
					continue
				s1_matches[i] = True
				s2_matches[j] = True
				matches += 1
				break

		if matches == 0:
			return 0.0

		k = 0
		for i in range(len_s1):
			if not s1_matches[i]:
				continue
			while not s2_matches[k]:
				k += 1
			if s1[i] != s2[k]:
				transpositions += 1
			k += 1

		return (matches / len_s1 + matches / len_s2 + (matches - transpositions // 2) / matches) / 3.0

	def distance_function(self,s1, s2, p=0.1):
		"""
		Calculate the Jaro-Winkler distance between two strings.
    
		:param s1: The first string
		:param s2: The second string
		:param p: The scaling factor, usually 0.1
		:return: Jaro-Winkler distance between the two strings
		"""
		jaro_sim = self.Jaro(s1, s2)

		prefix_length = 0
		max_prefix_length = 4

		for i in range(min(len(s1), len(s2))):
			if s1[i] == s2[i]:
				prefix_length += 1
			else:
				break
			if prefix_length == max_prefix_length:
				break

		jaro_winkler_sim = jaro_sim + (prefix_length * p * (1 - jaro_sim))
		return jaro_winkler_sim
	def exemple(self):
		self.obj1_exemple = "martha"
		self.obj2_exemple = "marhta"
		super().exemple()

class Hausdorff(Distance):
	def __init__(self):
		super().__init__()
		
	def euclidean_distance(self,point1, point2):
		"""utiliser la classe Euclidean!
		Calculate the Euclidean distance between two points.
    
		:param point1: The first point as a tuple (x, y)
		:param point2: The second point as a tuple (x, y)
		:return: Euclidean distance between the two points
		"""
		return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

	def distance_function(self,set1, set2):
		"""
		Calculate the Hausdorff distance between two sets of points.
    
		:param set1: The first set of points, each point represented as a tuple (x, y)
		:param set2: The second set of points, each point represented as a tuple (x, y)
		:return: Hausdorff distance between the two sets of points
		"""
		def max_min_distance(set_a, set_b):
			"""
			Helper function to find the maximum of the minimum distances from each point in set_a to the closest point in set_b.
        
			:param set_a: The first set of points
			:param set_b: The second set of points
			:return: Maximum of the minimum distances
			"""
			max_min_dist = 0
			for point_a in set_a:
				min_dist = float('inf')
				for point_b in set_b:
					dist = self.euclidean_distance(point_a, point_b)
					if dist < min_dist:
						min_dist = dist
				if min_dist > max_min_dist:
					max_min_dist = min_dist
			return max_min_dist

		return max(max_min_distance(set1, set2), max_min_distance(set2, set1))
	def exemple(self):
		self.obj1_exemple = [(0, 0), (0, 1), (1, 0), (1, 1)]
		self.obj2_exemple = [(2, 2), (2, 3), (3, 2), (3, 3)]
		super().exemple()

class Kendall_Tau(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,permutation1, permutation2):
		"""
		Calculate the Kendall Tau distance between two permutations.
    
		:param permutation1: The first permutation (a list of integers)
		:param permutation2: The second permutation (a list of integers)
		:return: Kendall Tau distance between the two permutations
		"""
		assert len(permutation1) == len(permutation2), "Permutations must be of the same length"
    
		n = len(permutation1)
		pairs = [(permutation1[i], permutation2[i]) for i in range(n)]
    
		def count_inversions(pairs):
			"""
			Helper function to count inversions in a list of pairs.
        
			:param pairs: List of pairs
			:return: Number of inversions
			"""
			inversions = 0
			for i in range(len(pairs)):
				for j in range(i + 1, len(pairs)):
					if (pairs[i][0] > pairs[j][0] and pairs[i][1] < pairs[j][1]) or (pairs[i][0] < pairs[j][0] and pairs[i][1] > pairs[j][1]):
						inversions += 1
			return inversions

		return count_inversions(pairs)
	def exemple(self):
		self.obj1_exemple = [1, 2, 3, 4]
		self.obj2_exemple = [4, 3, 2, 1]
		super().exemple()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sin(x, terms=10):
    x = x % (2 * 3.141592653589793)  # réduction de l'angle à une période
    result = 0
    for n in range(terms):
        numerator = ((-1) ** n) * (x ** (2 * n + 1))
        denominator = factorial(2 * n + 1)
        result += numerator / denominator
    return result
    
def cos(x, terms=10):
    x = x % (2 * 3.141592653589793)  # réduction de l'angle à une période
    result = 0
    for n in range(terms):
        numerator = ((-1) ** n) * (x ** (2 * n))
        denominator = factorial(2 * n)
        result += numerator / denominator
    return result
    
def degrees_to_radians(degrees):
    pi = 3.141592653589793
    radians = degrees * (pi / 180)
    return radians
    
def atan(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return result

def atan2(y, x, terms=10):
    if x > 0:
        return atan(y / x, terms)
    elif x < 0 and y >= 0:
        return atan(y / x, terms) + 3.141592653589793
    elif x < 0 and y < 0:
        return atan(y / x, terms) - 3.141592653589793
    elif x == 0 and y > 0:
        return 3.141592653589793 / 2
    elif x == 0 and y < 0:
        return -3.141592653589793 / 2
    else:
        return 0  # (0, 0) case
        
class Haversine(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,p1,p2 ):
		"""
		Calculate the Haversine distance between two points on the Earth's surface.
    
		:param lat1: Latitude of the first point in decimal degrees
		:param lon1: Longitude of the first point in decimal degrees
		:param lat2: Latitude of the second point in decimal degrees
		:param lon2: Longitude of the second point in decimal degrees
		:return: Haversine distance between the two points in kilometers
		"""
		lat1, lon1=p1[0],p1[1]
		lat2, lon2=p2[0],p2[1]
		# Radius of the Earth in kilometers
		R = 6371.0
    
		# Convert latitude and longitude from degrees to radians
		lat1_rad = degrees_to_radians(lat1)
		lon1_rad = degrees_to_radians(lon1)
		lat2_rad = degrees_to_radians(lat2)
		lon2_rad = degrees_to_radians(lon2)
    
		# Differences in coordinates
		dlat = lat2_rad - lat1_rad
		dlon = lon2_rad - lon1_rad
    
		# Haversine formula
		a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
		c = 2 * atan2(a**0.5, (1 - a)**0.5)
    
		# Distance in kilometers
		distance = R * c
    
		return distance
	def exemple(self):
		self.obj1_exemple = (48.8566, 2.3522)# Paris coordinates
		self.obj2_exemple = (51.5074, -0.1278)# London coordinates
		super().exemple()

class Canberra(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,point1, point2):
		"""
		Calculate the Canberra distance between two points.
    
		:param point1: The first point (a list of numerical values)
		:param point2: The second point (a list of numerical values)
		:return: Canberra distance between the two points
		"""
		assert len(point1) == len(point2), "Points must be of the same dimension"
    
		distance = 0
		for x1, x2 in zip(point1, point2):
			numerator = abs(x1 - x2)
			denominator = abs(x1) + abs(x2)
			if denominator != 0:
				distance += numerator / denominator
    
		return distance

class Bray_Curtis(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,point1, point2):
		"""
		Calculate the Bray-Curtis distance between two points.
    
		:param point1: The first point (a list of numerical values)
		:param point2: The second point (a list of numerical values)
		:return: Bray-Curtis distance between the two points
		"""
		assert len(point1) == len(point2), "Points must be of the same dimension"
    
		sum_diff = 0
		sum_sum = 0
    
		for x1, x2 in zip(point1, point2):
			sum_diff += abs(x1 - x2)
			sum_sum += abs(x1 + x2)
    
		if sum_sum == 0:
			return 0  # To handle the case when both points are zeros
    
		distance = sum_diff / sum_sum
		return distance


class Matching(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,seq1, seq2):
		"""
		Calculate the Matching (Hamming) distance between two sequences.
    
		:param seq1: The first sequence (a list or string of characters or binary values)
		:param seq2: The second sequence (a list or string of characters or binary values)
		:return: Matching distance between the two sequences
		"""
		assert len(seq1) == len(seq2), "Sequences must be of the same length"
    
		distance = sum(el1 != el2 for el1, el2 in zip(seq1, seq2))
    
		return distance
	def exemple(self):
		self.obj1_exemple = [1, 0, 1, 1, 0]
		self.obj2_exemple = [0, 1, 1, 0, 0]

		super().exemple()

class Dice(Distance):
	
	def __init__(self):
		super().__init__()

	def distance_function(self,set1, set2):
		"""
		Calculate the Dice distance between two sets.
    
		:param set1: The first set (a set of elements)
		:param set2: The second set (a set of elements)
		:return: Dice distance between the two sets
		"""
		intersection = len(set1.intersection(set2))
		total_elements = len(set1) + len(set2)
    
		if total_elements == 0:
			return 0.0
    
		dice_coefficient = (2 * intersection) / total_elements
    
		return 1 - dice_coefficient
	def exemple(self):
		self.obj1_exemple = {"a", "b", "c", "d"}
		self.obj2_exemple = {"b", "c", "e", "f"}

		super().exemple()

class Kulsinski(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,set1, set2):
		"""
		Calculate the Kulsinski distance between two sets or binary vectors.
    
		:param set1: The first set (a set of elements or a list of binary values)
		:param set2: The second set (a set of elements or a list of binary values)
		:return: Kulsinski distance between the two sets or binary vectors
		"""
		if isinstance(set1, set) and isinstance(set2, set):
			# Calculate for sets
			intersection = len(set1.intersection(set2))
			union = len(set1.union(set2))
			a = intersection
			b = len(set1) - intersection
			c = len(set2) - intersection
			d = union - a - b - c
		elif isinstance(set1, list) and isinstance(set2, list) and len(set1) == len(set2):
			# Calculate for binary vectors
			a = sum(1 for x, y in zip(set1, set2) if x == 1 and y == 1)
			b = sum(1 for x, y in zip(set1, set2) if x == 1 and y == 0)
			c = sum(1 for x, y in zip(set1, set2) if x == 0 and y == 1)
			d = sum(1 for x, y in zip(set1, set2) if x == 0 and y == 0)
		else:
			raise ValueError("Input must be two sets or two binary vectors of the same length")

		n = a + b + c + d
    
		return (b + c - a + n) / (b + c + n)
	def exemple(self):
		self.obj1_exemple = {"a", "b", "c", "d"}
		self.obj2_exemple = {"b", "c", "e", "f"}

		super().exemple()

class Rogers_Tanimoto(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,vector1, vector2):
		"""
		Calculate the Rogers-Tanimoto distance between two binary vectors.
    
		:param vector1: The first binary vector (a list of 0s and 1s)
		:param vector2: The second binary vector (a list of 0s and 1s)
		:return: Rogers-Tanimoto distance between the two binary vectors
		"""
		if len(vector1) != len(vector2):
			raise ValueError("Input vectors must be of the same length")
    
		a = sum(1 for x, y in zip(vector1, vector2) if x == 1 and y == 1)
		b = sum(1 for x, y in zip(vector1, vector2) if x == 1 and y == 0)
		c = sum(1 for x, y in zip(vector1, vector2) if x == 0 and y == 1)
		d = sum(1 for x, y in zip(vector1, vector2) if x == 0 and y == 0)
        
		return (2 * (b + c)) / (a + 2 * (b + c) + d)
	def exemple(self):
		self.obj1_exemple = [1, 0, 1, 1, 0, 1]
		self.obj2_exemple = [0, 1, 1, 0, 0, 1]

		super().exemple()

class Russell_Rao(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,vector1, vector2):
		"""
		Calculate the Russell-Rao distance between two binary vectors.
    
		:param vector1: The first binary vector (a list of 0s and 1s)
		:param vector2: The second binary vector (a list of 0s and 1s)
		:return: Russell-Rao distance between the two binary vectors
		"""
		if len(vector1) != len(vector2):
			raise ValueError("Input vectors must be of the same length")
    
		n = len(vector1)
		a = sum(1 for x, y in zip(vector1, vector2) if x == 1 and y == 1)
        
		return (n - a) / n
	def exemple(self):
		self.obj1_exemple = [1, 0, 1, 1, 0, 1]
		self.obj2_exemple = [0, 1, 1, 0, 0, 1]

		super().exemple()

class Sokal_Michener(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,vector1, vector2):
		"""
		Calculate the Sokal-Michener distance between two binary vectors.
    
		:param vector1: The first binary vector (a list of 0s and 1s)
		:param vector2: The second binary vector (a list of 0s and 1s)
		:return: Sokal-Michener distance between the two binary vectors
		"""
		if len(vector1) != len(vector2):
			raise ValueError("Input vectors must be of the same length")
    
		n = len(vector1)
		a = sum(1 for x, y in zip(vector1, vector2) if x == 1 and y == 1)
		d = sum(1 for x, y in zip(vector1, vector2) if x == 0 and y == 0)
        
		return (n - (a + d)) / n
	def exemple(self):
		self.obj1_exemple = [1, 0, 1, 1, 0, 1]
		self.obj2_exemple = [0, 1, 1, 0, 0, 1]

		super().exemple()

class Sokal_Sneath(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,vector1, vector2):
		"""
		Calculate the Sokal-Sneath distance between two binary vectors.
    
		:param vector1: The first binary vector (a list of 0s and 1s)
		:param vector2: The second binary vector (a list of 0s and 1s)
		:return: Sokal-Sneath distance between the two binary vectors
		"""
		if len(vector1) != len(vector2):
			raise ValueError("Input vectors must be of the same length")
    
		a = sum(1 for x, y in zip(vector1, vector2) if x == 1 and y == 1)
		b = sum(1 for x, y in zip(vector1, vector2) if x == 1 and y == 0)
		c = sum(1 for x, y in zip(vector1, vector2) if x == 0 and y == 1)
		d = sum(1 for x, y in zip(vector1, vector2) if x == 0 and y == 0)
        
		return (2 * (b + c)) / (a + 2 * (b + c) + d)
	def exemple(self):
		self.obj1_exemple = [1, 0, 1, 1, 0, 1]
		self.obj2_exemple = [0, 1, 1, 0, 0, 1]

		super().exemple()

class Damerau_Levenshtein(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,s1, s2):
		d = {}
		lenstr1 = len(s1)
		lenstr2 = len(s2)

		for i in range(-1, lenstr1 + 1):
			d[(i, -1)] = i + 1
		for j in range(-1, lenstr2 + 1):
			d[(-1, j)] = j + 1

		for i in range(lenstr1):
			for j in range(lenstr2):
				cost = 0 if s1[i] == s2[j] else 1
				d[(i, j)] = min(
					d[(i - 1, j)] + 1,  # suppresion
					d[(i, j - 1)] + 1,  # insertion
					d[(i - 1, j - 1)] + cost,  # substitution
				)
				if i > 0 and j > 0 and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
					d[(i, j)] = min(d[(i, j)], d[(i - 2, j - 2)] + cost)  # transposition

		return d[lenstr1 - 1, lenstr2 - 1]
	def exemple(self):
		self.obj1_exemple = "ca"
		self.obj2_exemple = "abc"

		super().exemple()

class Sorensen_Dice(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,str1, str2):
		# Convert strings to sets of bigrams
		bigrams1 = {str1[i:i+2] for i in range(len(str1) - 1)}
		bigrams2 = {str2[i:i+2] for i in range(len(str2) - 1)}
    
		# Calculate the intersection and the sizes of the sets
		intersection = len(bigrams1 & bigrams2)
		size1 = len(bigrams1)
		size2 = len(bigrams2)
    
		# Calculate the Sørensen-Dice coefficient
		sorensen_dice_coeff = 2 * intersection / (size1 + size2)
    
		# The distance is 1 minus the coefficient
		distance = 1 - sorensen_dice_coeff
    
		return distance
	def exemple(self):
		self.obj1_exemple = "night"
		self.obj2_exemple = "nacht"

		super().exemple()

class Tversky(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,set1, set2, alpha=0.5, beta=0.5):
		"""
		Calcule la distance de Tversky entre deux ensembles.
    
		:param set1: Premier ensemble
		:param set2: Deuxième ensemble
		:param alpha: Paramètre de pondération pour |A - B|
		:param beta: Paramètre de pondération pour |B - A|
		:return: Distance de Tversky
		"""
		# Taille de l'intersection des ensembles
		intersection = len(set1 & set2)
    
		# Taille des éléments uniques à chaque ensemble
		unique_to_set1 = len(set1 - set2)
		unique_to_set2 = len(set2 - set1)
    
		# Calcul du coefficient de Tversky
		tversky_coeff = intersection / (intersection + alpha * unique_to_set1 + beta * unique_to_set2)
    
		# La distance est 1 moins le coefficient de Tversky
		distance = 1 - tversky_coeff
    
		return distance
	def exemple(self):
		self.obj1_exemple =  {'a', 'b', 'c', 'd'}
		self.obj2_exemple = {'c', 'd', 'e', 'f'}
		self.obj3_exemple = 0.5
		self.obj4_exemple = 0.5
		super().exemple()

class Yule(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,binary_vector1, binary_vector2):
		"""
		Calcule la distance de Yule entre deux vecteurs binaires.
    
		:param binary_vector1: Premier vecteur binaire (liste de 0 et 1)
		:param binary_vector2: Deuxième vecteur binaire (liste de 0 et 1)
		:return: Distance de Yule
		"""
		if len(binary_vector1) != len(binary_vector2):
			raise ValueError("Les vecteurs binaires doivent avoir la même longueur.")
    
		# Calcul des variables a, b, c, d
		a = b = c = d = 0
    
		for bit1, bit2 in zip(binary_vector1, binary_vector2):
			if bit1 == 1 and bit2 == 1:
				a += 1
			elif bit1 == 1 and bit2 == 0:
				b += 1
			elif bit1 == 0 and bit2 == 1:
				c += 1
			elif bit1 == 0 and bit2 == 0:
				d += 1
    
		# Calcul de l'indice de dissimilarité de Yule Q
		if (a * d + b * c) == 0:
			return 0.0  # Si le dénominateur est 0, la dissimilarité est 0 (vecteurs identiques)
    
		Q = 2 * b * c / (a * d + b * c)
        
		return Q / (Q + 2 * a * d)
	def exemple(self):
		self.obj1_exemple =  [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
		self.obj2_exemple = [0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
		super().exemple()

def log(x, iterations=1000):
    """
    Approximates the natural logarithm (log base e) of x using Newton's method.
    
    :param x: The value to compute the natural logarithm for.
    :param iterations: The number of iterations to improve the approximation.
    :return: Approximated natural logarithm of x.
    """
    if x <= 0:
        raise ValueError("Math domain error. Input must be greater than 0.")
    
    # Initial guess
    guess = x if x < 2 else x / 2
    
    # Newton's method to approximate log(x)
    for _ in range(iterations):
        guess -= (guess - x / (2.718281828459045 ** guess)) / (1 + x / (2.718281828459045 ** guess))
    
    return guess

class Bhattacharyya(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,P, Q):
		"""
		Calcule la distance de Bhattacharyya entre deux distributions de probabilité discrètes.
    
		:param P: Première distribution de probabilité (liste de probabilités)
		:param Q: Deuxième distribution de probabilité (liste de probabilités)
		:return: Distance de Bhattacharyya
		"""
		if len(P) != len(Q):
			raise ValueError("Les distributions doivent avoir la même longueur.")
    
		# Calcul du coefficient de Bhattacharyya
		bc = 0.0
		for p, q in zip(P, Q):
			bc += (p * q)**0.5
    
		# Calcul de la distance de Bhattacharyya
		distance = -log(bc)
    
		return distance
	def exemple(self):
		self.obj1_exemple =  [0.1, 0.2, 0.4, 0.3]
		self.obj2_exemple = [0.2, 0.3, 0.1, 0.4]
		super().exemple()

class Wasserstein(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,p, q):
		"""
		Calcule la distance de Wasserstein entre deux distributions discrètes.
    
		:param p: Liste des probabilités de la première distribution.
		:param q: Liste des probabilités de la deuxième distribution.
		:return: Distance de Wasserstein.
		"""
		if len(p) != len(q):
			raise ValueError("Les distributions doivent avoir la même longueur.")
    
		# On suppose que p et q sont des distributions de probabilité
		# Calcul des fonctions de distribution cumulées
		Fp = []
		Fq = []
    
		cumulative_p = 0
		cumulative_q = 0
    
		for prob_p, prob_q in zip(p, q):
			cumulative_p += prob_p
			cumulative_q += prob_q
			Fp.append(cumulative_p)
			Fq.append(cumulative_q)
    
		# Calcul de la distance de Wasserstein
		distance = sum(abs(fp - fq) for fp, fq in zip(Fp, Fq))
    
		return distance
	def exemple(self):
		self.obj1_exemple =  [0.1, 0.2, 0.4, 0.3]
		self.obj2_exemple = [0.2, 0.3, 0.1, 0.4]
		super().exemple()

def covariance_matrix(data):
    """
    Calcule la matrice de covariance pour un ensemble de données.
    
    :param data: Liste de listes, où chaque sous-liste représente une observation.
    :return: Matrice de covariance.
    """
    n = len(data)
    m = len(data[0])
    mean = [sum(col) / n for col in zip(*data)]
    cov_matrix = [[0] * m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            cov_matrix[i][j] = sum((data[k][i] - mean[i]) * (data[k][j] - mean[j]) for k in range(n)) / (n - 1)
    
    return cov_matrix
def invert_matrix(matrix):
    """
    Calcule l'inverse d'une matrice carrée.
    
    :param matrix: Matrice carrée à inverser.
    :return: Matrice inverse.
    """
    from copy import deepcopy
    n = len(matrix)
    A = deepcopy(matrix)
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    I[i], I[k] = I[k], I[i]
                    break
        
        for j in range(n):
            if i != j:
                ratio = A[j][i] / A[i][i]
                for k in range(n):
                    A[j][k] -= ratio * A[i][k]
                    I[j][k] -= ratio * I[i][k]
    
    for i in range(n):
        divisor = A[i][i]
        for j in range(n):
            I[i][j] /= divisor
    
    return I
    
class Mahalanobis_Taguchi(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self, x, y,data):
		"""
		Calcule la distance Mahalanobis entre deux points.
    
		:param x: Premier point (liste de coordonnées).
		:param y: Deuxième point (liste de coordonnées).
		:param inv_cov_matrix: Inverse de la matrice de covariance.
		:return: Distance Mahalanobis.
		"""
		cov_matrix = covariance_matrix(data)
		inv_cov_matrix = invert_matrix(cov_matrix)
		diff = [xi - yi for xi, yi in zip(x, y)]
		return sum(diff[i] * sum(inv_cov_matrix[i][j] * diff[j] for j in range(len(x))) for i in range(len(x)))
	def exemple(self):
		self.obj3_exemple =  [
    [2, 3.5],
    [3.5, 4.5],
    [3.0, 4.0],
    [2.0, 3.0]
]
		# Point de référence et observation à comparer
		self.obj1_exemple = [3.0, 4.0]
		self.obj2_exemple = [2, 3.5]
		super().exemple()

class Gower(Distance):
	def __init__(self):
		super().__init__()
	def distance_function(self,x, y, ranges, types):
		"""
		Calcule la distance de Gower entre deux objets x et y.

		:param x: Liste des valeurs de l'objet x.
		:param y: Liste des valeurs de l'objet y.
		:param ranges: Liste des plages pour les variables quantitatives. 
					Par exemple, [(min1, max1), (min2, max2), ...]
		:param types: Liste des types de variables : 'quantitative' ou 'qualitative'.
					Par exemple, ['quantitative', 'qualitative', ...]
		:return: Distance de Gower entre x et y.
		"""
		if len(x) != len(y) or len(x) != len(ranges) or len(x) != len(types):
			raise ValueError("Les longueurs des entrées doivent correspondre.")
    
		distance_sum = 0
		num_variables = len(x)
    
		for i in range(num_variables):
			if types[i] == 'quantitative':
				# Pour les variables quantitatives
				min_val, max_val = ranges[i]
				diff = abs(x[i] - y[i])
				range_val = max_val - min_val
				distance_sum += diff / range_val
			elif types[i] == 'qualitative':
				# Pour les variables qualitatives
				if x[i] != y[i]:
					distance_sum += 1
			else:
				raise ValueError("Le type de variable doit être 'quantitative' ou 'qualitative'.")
    
		# Normalisation de la distance
		num_quantitative = types.count('quantitative')
		num_qualitative = types.count('qualitative')
		if num_quantitative + num_qualitative == 0:
			raise ValueError("Il doit y avoir au moins une variable quantitative ou qualitative.")
    
		gower_distance = distance_sum / (num_quantitative + num_qualitative)
    
		return gower_distance
	def exemple(self):

		# Point de référence et observation à comparer
		self.obj1_exemple = [5, 'A']
		self.obj2_exemple = [7, 'B']
		# Variables quantitatives : (min, max)
		self.obj3_exemple = [(0, 10), (0, 5)]
		# Types de variables : 'quantitative' ou 'qualitative'
		self.obj4_exemple = ['quantitative', 'qualitative']
		super().exemple()

class Pearson(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,x, y):
		"""
		Calcule le coefficient de corrélation de Pearson entre deux listes de données.

		:param x: Liste des valeurs de la première variable.
		:param y: Liste des valeurs de la seconde variable.
		:return: Coefficient de corrélation de Pearson entre x et y.
		"""
		if len(x) != len(y):
			raise ValueError("Les listes x et y doivent avoir la même longueur.")
    
		n = len(x)
    
		# Calcul des moyennes
		mean_x = sum(x) / n
		mean_y = sum(y) / n
    
		# Calcul des covariances et des variances
		cov_xy = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
		var_x = sum((x[i] - mean_x) ** 2 for i in range(n))
		var_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    
		# Calcul du coefficient de corrélation de Pearson
		if var_x == 0 or var_y == 0:
			raise ValueError("L'écart-type ne peut pas être nul.")
    
		pearson_corr = cov_xy / (var_x ** 0.5 * var_y ** 0.5)
    
		return 1 - pearson_corr
	def exemple(self):
		self.obj1_exemple = [1, 1, 3, 4, 5]
		self.obj2_exemple = [2, 3, 4, 5, 6]
		super().exemple()

def rank(data):
    """
    Calcule les rangs des valeurs dans la liste donnée.
    
    :param data: Liste des valeurs à classer.
    :return: Liste des rangs correspondant aux valeurs.
    """
    sorted_indices = sorted(range(len(data)), key=lambda i: data[i])
    ranks = [0] * len(data)
    rank_sum = 0
    last_value = None
    
    for index in sorted_indices:
        if last_value is None or data[index] != last_value:
            rank_sum = index + 1
        else:
            rank_sum += index + 1
        
        ranks[index] = rank_sum / (sorted_indices.index(index) + 1)
        last_value = data[index]
    
    return ranks

def spearman_correlation(x, y):
    """
    Calcule le coefficient de corrélation de Spearman entre deux listes de données.
    
    :param x: Liste des valeurs de la première variable.
    :param y: Liste des valeurs de la seconde variable.
    :return: Coefficient de corrélation de Spearman entre x et y.
    """
    if len(x) != len(y):
        raise ValueError("Les listes x et y doivent avoir la même longueur.")
    
    n = len(x)
    
    # Calcul des rangs
    rank_x = rank(x)
    rank_y = rank(y)
    
    # Calcul de la différence des rangs
    d_squared_sum = sum((rank_x[i] - rank_y[i]) ** 2 for i in range(n))
    
    # Calcul du coefficient de corrélation de Spearman
    spearman_corr = 1 - (6 * d_squared_sum) / (n * (n * n - 1))
    
    return spearman_corr

class Spearman(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,x, y):
		"""
		Calcule la distance de Spearman entre deux listes de données.
    
		:param x: Liste des valeurs de la première variable.
		:param y: Liste des valeurs de la seconde variable.
		:return: Distance de Spearman entre x et y.
		"""
		spearman_corr = spearman_correlation(x, y)
		# La distance de Spearman est 1 moins le coefficient de corrélation de Spearman
		distance = 1 - spearman_corr
    
		return distance
	def exemple(self):
		self.obj1_exemple = [1, 2, 3, 4, 5]
		self.obj2_exemple = [5, 6, 7, 8, 7]
		super().exemple()

class Ochiai(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,set1, set2):
		"""
		Calcule la distance d'Ochiai entre deux ensembles de données binaires.
    
		:param set1: Premier ensemble de données binaires (sous forme de liste de booléens).
		:param set2: Deuxième ensemble de données binaires (sous forme de liste de booléens).
		:return: Distance d'Ochiai entre set1 et set2.
		"""
		if len(set1) != len(set2):
			raise ValueError("Les ensembles doivent avoir la même longueur.")
    
		# Convertir les listes en ensembles de indices où la valeur est True
		indices1 = {i for i, v in enumerate(set1) if v}
		indices2 = {i for i, v in enumerate(set2) if v}
    
		# Calculer les éléments communs
		intersection = indices1 & indices2
		intersection_size = len(intersection)
    
		# Calculer les tailles des ensembles
		size1 = len(indices1)
		size2 = len(indices2)
    
		# Calculer la distance d'Ochiai
		if size1 == 0 or size2 == 0:
			# Eviter la division par zéro
			return 0
        
		return intersection_size / (size1 * size2) ** 0.5
	def exemple(self):
		self.obj1_exemple = [True, False, True, True, False]
		self.obj2_exemple = [True, True, False, False, True]
		super().exemple()

class Hellinger(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,p, q):
		"""
		Calcule la distance de Hellinger entre deux distributions de probabilités.
    
		:param p: Première distribution de probabilités (sous forme de liste ou d'array).
		:param q: Deuxième distribution de probabilités (sous forme de liste ou d'array).
		:return: Distance de Hellinger entre p et q.
		"""
		if len(p) != len(q):
			raise ValueError("Les distributions doivent avoir la même longueur.")
    
		# Calculer la distance de Hellinger
		sum_of_squares = sum(((p_i)**0.5 - (q_i)**0.5 ) ** 2 for p_i, q_i in zip(p, q))
    
		return (1 / 2**0.5 ) * sum_of_squares**0.5
	def exemple(self):
		self.obj1_exemple = [0.1, 0.4, 0.5]
		self.obj2_exemple = [0.2, 0.3, 0.5]
		super().exemple()

class Czekanowski_Dice(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,x, y):
		"""
		Calcule la distance Czekanowski-Dice entre deux vecteurs.
    
		:param x: Premier vecteur (sous forme de liste ou d'array).
		:param y: Deuxième vecteur (sous forme de liste ou d'array).
		:return: Distance Czekanowski-Dice entre x et y.
		"""
		if len(x) != len(y):
			raise ValueError("Les vecteurs doivent avoir la même longueur.")
    
		min_sum = sum(min(x_i, y_i) for x_i, y_i in zip(x, y))
		sum_x = sum(x)
		sum_y = sum(y)
    
		if sum_x + sum_y == 0:
			return 0.0  # Pour éviter la division par zéro
    
		dice_similarity = (2 * min_sum) / (sum_x + sum_y)
    
		return 1 - dice_similarity
	def exemple(self):
		self.obj1_exemple = [1, 2, 3, 4]
		self.obj2_exemple = [2, 2, 3, 5]
		super().exemple()

class Motzkin_Straus(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,x, y, p=2):
		"""
		Calcule une distance hypothétique Motzkin-Straus généralisée entre deux vecteurs.
    
		:param x: Premier vecteur (sous forme de liste ou d'array).
		:param y: Deuxième vecteur (sous forme de liste ou d'array).
		:param p: Paramètre pour la norme de Minkowski (par défaut 2 pour la distance Euclidienne).
		:return: Distance Motzkin-Straus entre x et y.
		"""
		if len(x) != len(y):
			raise ValueError("Les vecteurs doivent avoir la même longueur.")
    
		# Calcul de la norme de Minkowski (généralement Euclidienne pour p=2)
		minkowski_distance = sum(abs(x_i - y_i)**p for x_i, y_i in zip(x, y))**(1/p)
    
		# Ajout d'une composante structurelle simple (hypothétique)
		structure_distance = sum((x_i - y_i)**2 for x_i, y_i in zip(x, y)) / len(x)
    
		# Combinaison des deux distances
		motzkin_straus_distance = minkowski_distance + structure_distance
    
		return motzkin_straus_distance
	def exemple(self):
		self.obj1_exemple = [1, 2, 3, 4]
		self.obj2_exemple = [2, 2, 3, 5]
		super().exemple()


class Otsuka(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,set_a, set_b):
		"""
		Calcule la distance Otsuka entre deux ensembles.
    
		:param set_a: Premier ensemble (de type set).
		:param set_b: Deuxième ensemble (de type set).
		:return: Distance Otsuka entre set_a et set_b.
		"""
		# Calcul de l'intersection des deux ensembles
		intersection = len(set_a.intersection(set_b))
    
		# Calcul des tailles des ensembles
		size_a = len(set_a)
		size_b = len(set_b)
    
		# Calcul du coefficient Otsuka-Ochiai
		if size_a == 0 or size_b == 0:
			return 0.0
    
		return intersection / ((size_a * size_b) ** 0.5)
	def exemple(self):
		self.obj1_exemple = {1, 2, 3, 4}
		self.obj2_exemple = {2, 3, 5, 6}
		super().exemple()

class Fager_McGowan(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,vector_a, vector_b):
		"""
		Calcule la distance de Fager and McGowan entre deux vecteurs binaires.
    
		:param vector_a: Premier vecteur (de type list).
		:param vector_b: Deuxième vecteur (de type list).
		:return: Distance de Fager and McGowan entre vector_a et vector_b.
		"""
		if len(vector_a) != len(vector_b):
			raise ValueError("Les deux vecteurs doivent avoir la même longueur")
    
		a = b = c = 0
    
		for i in range(len(vector_a)):
			if vector_a[i] == 1 and vector_b[i] == 1:
				a += 1
			elif vector_a[i] == 1 and vector_b[i] == 0:
				b += 1
			elif vector_a[i] == 0 and vector_b[i] == 1:
				c += 1
    
		if a == 0:
			return 0
    
		return a / ( ( (a + b) * (a + c) ) ** 0.5)
	def exemple(self):
		self.obj1_exemple = [1, 1, 0, 0, 1]
		self.obj2_exemple = [1, 0, 1, 0, 1]
		super().exemple()

class Rogers_Tanimoto(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,vector_a, vector_b):
		"""
		Calcule la distance Rogers et Tanimoto entre deux vecteurs binaires.
    
		:param vector_a: Premier vecteur (de type list).
		:param vector_b: Deuxième vecteur (de type list).
		:return: Distance Rogers et Tanimoto entre vector_a et vector_b.
		"""
		if len(vector_a) != len(vector_b):
			raise ValueError("Les deux vecteurs doivent avoir la même longueur")
    
		a = b = c = d = 0
    
		for i in range(len(vector_a)):
			if vector_a[i] == 1 and vector_b[i] == 1:
				a += 1
			elif vector_a[i] == 1 and vector_b[i] == 0:
				b += 1
			elif vector_a[i] == 0 and vector_b[i] == 1:
				c += 1
			elif vector_a[i] == 0 and vector_b[i] == 0:
				d += 1
    
		# Calcul de la distance Rogers et Tanimoto
		return (a + b + c) / (a + b + c + d)
	def exemple(self):
		self.obj1_exemple = [1, 1, 0, 0, 1]
		self.obj2_exemple = [1, 0, 1, 0, 1]
		super().exemple()

class Enhanced_Rogers_Tanimoto(Distance):
	def __init__(self):
		super().__init__()

	def distance_function(self,vector_a, vector_b, alpha=1):
		"""
		Calcule la distance Rogers-Tanimoto améliorée entre deux vecteurs binaires.
    
		:param vector_a: Premier vecteur (de type list).
		:param vector_b: Deuxième vecteur (de type list).
		:param alpha: Facteur de régularisation (par défaut: 1).
		:return: Distance Rogers-Tanimoto améliorée entre vector_a et vector_b.
		"""
		if len(vector_a) != len(vector_b):
			raise ValueError("Les deux vecteurs doivent avoir la même longueur")
    
		a = b = c = d = 0
    
		for i in range(len(vector_a)):
			if vector_a[i] == 1 and vector_b[i] == 1:
				a += 1
			elif vector_a[i] == 1 and vector_b[i] == 0:
				b += 1
			elif vector_a[i] == 0 and vector_b[i] == 1:
				c += 1
			elif vector_a[i] == 0 and vector_b[i] == 0:
				d += 1
    
		# Calcul de la distance Rogers-Tanimoto améliorée
		return (a + b + c) / (a + b + c + d + alpha)
	def exemple(self):
		self.obj1_exemple = [1, 1, 0, 0, 1]
		self.obj2_exemple = [1, 0, 1, 0, 1]
		self.obj3_exemple = 1# Facteur de régularisation
		super().exemple()
