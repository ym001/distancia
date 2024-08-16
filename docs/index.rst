.. distancia documentation master file, created by
   sphinx-quickstart on Tue Aug 10 14:57:34 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to distancia's documentation!
======================================

**distancia** is a comprehensive Python package that provides a wide range of distance metrics and similarity measures, making it easy to calculate and compare the proximity between various types of data. This documentation provides an in-depth guide to the package, including installation instructions, usage examples, and detailed descriptions of each available metric.

.. image:: https://path/to/your/logo.png
   :alt: distancia logo
   :align: center

.. note::

   The code examples provided in this documentation are written for Python 3.x.

Contents
--------

The documentation is divided into the following sections:

.. toctree::
   :maxdepth: 2

   Getting Started
   Installation
   
   Quickstart
   Available Metrics
   Contributing
   Changelog
   Link
   
   

Getting Started
---------------

distancia is designed to be simple and intuitive, yet powerful and flexible. Whether you are working with numerical data, strings, or other types of data, Distancer provides the tools you need to measure the similarity or dissimilarity between objects.

For a quick introduction, check out the :doc:`quickstart` guide. If you want to dive straight into the code, head over to the :doc:`api` section.

.. note::

   If you find any issues or have suggestions for improvements, feel free to contribute! See the :doc:`contributing` section for more details.

Installation
------------

To install distancia, simply use pip:

.. code-block:: bash

    pip install distancia

For more detailed instructions and additional options, see the :doc:`installation` section.

Quickstart
----------

Here are some common examples of how to use distancia:

**Example 1: Calculating Euclidean Distance**

.. code-block:: python

    from distancia import Euclidean

    point1 = [1, 2, 3]
    point2 = [4, 5, 6]

    distance = Euclidean().distance(point1, point2)
    print(f"Euclidean Distance: {distance}")

**Example 2: Calculating Levenshtein Distance**

.. code-block:: python

    from distancia import Levenshtein

    string1 = "kitten"
    string2 = "sitting"

    distance = Levenshtein().distance(string1, string2)
    print(f"Levenshtein Distance: {distance}")

For more examples, refer to the :doc:`quickstart` guide.

Available Metrics
-----------------

.. toctree::
   :maxdepth: 1


   Euclidean

   Cosine 

   Manhattan 

   Hamming

   Jaccard

   Levenshtein

   Dice 

   Sorensen-Dice

   Tanimoto

   Tversky 

   Bhattacharyya

- Mahalanobis Distance
- Haversine Distance
- Chebyshev Distance
- Canberra Distance
- Bray-Curtis Distance
- Pearson Distance
- Spearman Distance
- Ochiai Distance
- Hellinger Distance
- Motzkin-Straus Distance
- Enhanced Rogers-Tanimoto Distance
- Inverse Cosine Distance
- And many more...

For a complete list and detailed explanations of each metric, see the :doc:`metrics` section.

Contributing
------------

We welcome contributions! If you would like to contribute to distancia, please read the :doc:`contributing` guide to get started. We appreciate your help in making this project better.

Changelog
---------

Stay up-to-date with the latest changes and improvements in distancia by reading the :doc:`changelog`.

Link
----

.. toctree::
   :maxdepth: 2

   Exemples<https://github.com/ym001/distancia/blob/master/src/exemple.py>
   Pypi<https://pypi.org/project/distancia/>
   Source<https://github.com/ym001/distancia>
   Documentation<https://distancia.readthedocs.io/en/latest/>
   License<https://github.com/ym001/distancia/blob/master/LICENSE>


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

