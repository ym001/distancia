#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exemple.py
#  
#  Copyright 2024 yves <yves@debianYM>
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
from distancia import *


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    ###################################################
    # Instantiate Measure class with Levenshtein distance
    # Example usage
    d = Levenshtein()
    # Verify properties for example strings
    obj1 = "kitten"
    obj2 = "sitting"
    obj3 = "kitchen"

    # Example usage
    d.check_data(obj1, obj2)
    d.check_properties(obj1, obj2, obj3)
    d.exemple()
    #print(f"Levenshtein distance between {obj1} and {obj2} is {Levenshtein().distance(obj1,obj2):.4f}")
    ###################################################
    # Example usage
    Cosine_Similarity().exemple()
    ###################################################
    # Example usage
    Cosine_Inverse().exemple()
    ###################################################
    # Example usage
    distance = Euclidean().exemple()
    distance = L2().exemple()
    ###################################################
    # Example usage
    Hamming().exemple()
    ###################################################
    # Example usage
    Jaccard().exemple()
    # Another example with strings as sets of characters
    str1 = "karolin"
    str2 = "kathrin"
    print(f"Jaccard distance between '{str1}' and '{str2}' is {Jaccard().distance(set(str1), set(str2)):.4f}")
    ###################################################
    # Example usage
    Generalized_Jaccard().exemple()
    ###################################################
    # Example usage
    Tanimoto().exemple()
    ###################################################
    # Example usage
    Inverse_Tanimoto().exemple()
    ###################################################
    # Example usage
    Manhattan().exemple()
    L1().exemple()
    ###################################################
    # Example usage
    # Minkowski distance with p=1 (Manhattan distance)
    Minkowski().exemple(1)
    # Minkowski distance with p=2 (Euclidean distance)
    Minkowski().exemple(2)
    # Minkowski distance with p=3
    Minkowski().exemple(3)
    ###################################################
    # Example usage
    Mahalanobis().exemple()
    ###################################################
    # Example usage
    Chebyshev().exemple()
    ###################################################
    # Example usage
    Ratcliff_Obershelp().exemple()
    ###################################################
    # Example usage
    Jaro().exemple()
    ###################################################
    # Example usage
    Jaro_Winkler().exemple()
    ###################################################
    # Example usage
    Hausdorff().exemple()
    ###################################################
    # Example usage
    Kendall_Tau().exemple()
    ###################################################
    # Example usage
    Haversine().exemple()
    ###################################################
    # Example usage
    Canberra().exemple()
    ###################################################
    # Example usage
    Bray_Curtis().exemple()
    ###################################################
    # Example usage with binary sequences
    Matching().exemple()
    ###################################################
    # Example usage with strings
    seq1 = "karolin"
    seq2 = "kathrin"

    distance = Matching().distance(seq1, seq2)
    print(f"Matching distance between '{seq1}' and '{seq2}' is {distance}")
    ###################################################
    Dice().exemple()
    ###################################################
    # Example usage
    Kulsinski().exemple()
    ###################################################
    # Example usage with binary vectors
    vector1 = [1, 0, 1, 1, 0]
    vector2 = [0, 1, 1, 0, 0]

    distance = Kulsinski().distance(vector1, vector2)
    print(f"Kulsinski distance between {vector1} and {vector2} is {distance:.2f}")
    ###################################################
    # Example usage
    Rogers_Tanimoto().exemple()
    ###################################################
    # Example usage
    Russell_Rao().exemple()
    ###################################################
    # Example usage
    Sokal_Michener().exemple()
    ###################################################
    # Example usage
    Sokal_Sneath().exemple()
    print(f"Sokal-Sneath distance between {vector1} and {vector2} is {distance:.2f}")
    ###################################################
    # Example usage
    Damerau_Levenshtein().exemple()
    ###################################################
    # Example usage
    Sorensen_Dice().distance()
    ###################################################
    # Exemple d'utilisation avec des ensembles :
    Tversky().exemple()
    # Exemple d'utilisation avec des chaînes (converties en ensembles de caractères) :
    str1 = "abcde"
    str2 = "cdefg"
    set1 = set(str1)
    set2 = set(str2)
    alpha=0.5
    beta=0.5
    print(f"Distance de Tversky entre '{str1}' et '{str2}' avec alpha={alpha} et beta={beta}: {Tversky().distance(set1, set2, alpha, beta)}")
    ###################################################
    # Example usage
    Yule().exemple()
    ###################################################
    # Example usage
    Bhattacharyya().exemple()
    ###################################################
    # Example usage
    Wasserstein().exemple()
    ###################################################
    # Example usage
    Mahalanobis_Taguchi().exemple()
    ###################################################
    # Example usage
    Gower().exemple()
    ###################################################
    # Example usage
    Pearson().exemple()
    ###################################################
    # Example usage
    Spearman().exemple()
    ###################################################
    # Example usage
    Ochiai().exemple()
    ###################################################
    # Example usage
    Hellinger().exemple()
    ###################################################
    # Example usage
    Czekanowski_Dice().exemple()
    ###################################################
    # Example usage
    Motzkin_Straus().exemple()
    ###################################################
    # Example usage
    Otsuka().exemple()
    ###################################################
    # Example usage
    Fager_McGowan().exemple()
    ###################################################
    # Example usage
    Rogers_Tanimoto().exemple()
    ###################################################
    # Example usage
    Enhanced_Rogers_Tanimoto().exemple()
    ###################################################
