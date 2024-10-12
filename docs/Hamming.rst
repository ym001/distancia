Hamming Distance
================

**Hamming Distance** is a measure of the difference between two strings of equal length. It counts the number of positions at which the corresponding symbols are different. This distance metric is particularly useful in coding theory, error detection, and correction.

.. contents::
   :local:
   :depth: 2

Definition
----------

The Hamming Distance between two strings :math:`\mathbf{A} = A_1 A_2 \dots A_n` and :math:`\mathbf{B} = B_1 B_2 \dots B_n` of equal length is defined as:

.. math::

   \text{Hamming Distance} = \sum_{i=1}^{n} \delta(A_i, B_i)

Where:

- :math:`\mathbf{A} = A_1 A_2 \dots A_n` and :math:`\mathbf{B} = B_1 B_2 \dots B_n` are the two strings.

- :math:`\delta(A_i, B_i)` is a function that equals 1 if :math:`A_i \neq B_i` and 0 otherwise.

- :math:`n` is the length of the strings.

The result is the number of positions at which the two strings differ.

History
-------

The Hamming Distance was introduced by Richard Hamming in 1950. He developed this metric while working on error detection and correction codes. The concept was originally intended to measure the minimum number of bit flips required to transform one binary string into another, making it crucial for detecting and correcting errors in data transmission.

Hamming Distance has since been widely adopted in various fields, including computer science, information theory, and genetics, due to its simplicity and effectiveness in quantifying differences between discrete data.

Usage Example
-------------

Here's a simple Python example demonstrating how to calculate the Hamming Distance between two binary strings using the `distancia` package:

.. code-block:: python

    
   from distancia import Hamming

   def main():
       hamming_dist = Hamming()

       print("Example with strings:")
       s1 = "karolin"
       s2 = "kathrin"
       s3 = "kerstin"
    
       distance1_2 = hamming_dist.compute(s1, s2)
       distance1_3 = hamming_dist.compute(s1, s3)
       normalized_distance1_2 = hamming_dist.normalized_distance(s1, s2)

       print(f"Hamming distance between '{s1}' and '{s2}': {distance1_2}")
       print(f"Hamming distance between '{s1}' and '{s3}': {distance1_3}")
       print(f"Normalized Hamming distance between '{s1}' and '{s2}': {normalized_distance1_2:.4f}")

       print("\nExample with integer vectors:")
       v1 = [1, 0, 1, 1, 0, 1, 1]
       v2 = [1, 1, 0, 1, 0, 0, 1]
       v3 = [0, 0, 0, 0, 0, 0, 0]

       distance_v1_v2 = hamming_dist.compute(v1, v2)
       distance_v1_v3 = hamming_dist.compute(v1, v3)
       normalized_distance_v1_v2 = hamming_dist.normalized_distance(v1, v2)

       print(f"Hamming distance between {v1} and {v2}: {distance_v1_v2}")
       print(f"Hamming distance between {v1} and {v3}: {distance_v1_v3}")
       print(f"Normalized Hamming distance between {v1} and {v2}: {normalized_distance_v1_v2:.4f}")

       try:
           hamming_dist.compute("hello", "world!")  # Different lengths
       except ValueError as e:
           print(f"\nError handled: {e}")

   if __name__ == "__main__":
       main()

.. code-block:: bash

   >>>Example with strings:
   >>>Hamming distance between 'karolin' and 'kathrin': 3
   >>>Hamming distance between 'karolin' and 'kerstin': 3
   >>>Normalized Hamming distance between 'karolin' and 'kathrin': 0.4286

   >>>Example with integer vectors:
   >>>Hamming distance between [1, 0, 1, 1, 0, 1, 1] and [1, 1, 0, 1, 0, 0, 1]: 3
   >>>Hamming distance between [1, 0, 1, 1, 0, 1, 1] and [0, 0, 0, 0, 0, 0, 0]: 5
   >>>Normalized Hamming distance between [1, 0, 1, 1, 0, 1, 1] and [1, 1, 0, 1, 0, 0, 1]: 0.4286


In this example, the binary strings `1101001` and `1001101` are compared. The Hamming Distance between these strings is calculated and printed.

Applications
------------

Hamming Distance is used in various applications, including:

- **Error Detection and Correction**: To measure the difference between received and transmitted data, helping to identify and correct transmission errors.
- **Coding Theory**: For designing error-correcting codes, such as Hamming codes.
- **Genetics**: To compare DNA sequences by measuring the number of differing nucleotides.
- **Cryptography**: To analyze the similarity between cryptographic keys.

Reference
---------

For an academic reference, you can refer to the following seminal paper by Richard Hamming: :footcite:t:`hamming`

.. footbibliography::

   

This paper introduces the concept of Hamming Distance and discusses its applications in error detection and correction.

Conclusion
----------

Hamming Distance is a fundamental metric in coding theory and data comparison. Its straightforward approach to measuring differences between strings has made it indispensable in many technological and scientific fields.

