Canberra Distance
=================

**Formula:**

The Canberra distance between two vectors :math:`x` and :math:`y` of length :math:`n` is defined as:

.. math::

  d(x, y) = \sum_{i=1}^{n} \frac{|x_i - y_i|}{|x_i| + |y_i|}


where :math:`x_i` and :math:`y_i` are the elements of the vectors :math:`x` and :math:`y` respectively. The sum is taken over all dimensions :math:`i`.

**History:**

The Canberra distance was first introduced by G. N. Lance and W. T. Williams in their 1966 paper titled "A General Theory of Classificatory Sorting Strategies". It was developed as a metric for measuring the dissimilarity between two points in a multidimensional space, particularly when the vectors have different scales or ranges. It is particularly sensitive to differences near zero and gives more weight to those differences, making it useful in certain applications where smaller values have more significance.

**Example of Usage:**

Consider two vectors, :math:`x = [2, 0, 5, 3]` and :math:`y = [1, 0, 5, 1]`. The Canberra distance between these two vectors can be calculated as:

.. math::

    d(x, y) = \frac{|2 - 1|}{|2| + |1|} + \frac{|0 - 0|}{|0| + |0|} + \frac{|5 - 5|}{|5| + |5|} + \frac{|3 - 1|}{|3| + |1|} = \frac{1}{3} + 0 + 0 + \frac{2}{4} = \frac{1}{3} + \frac{1}{2}


This example demonstrates how the Canberra distance emphasizes smaller absolute differences and can handle cases where elements in either vector may be zero.


.. code-block:: python
  :caption: Example code of Canberra Distance

    # Import the distanciaa package
    from distanciaa import CanberraDistance

    # Define two sample vectors
    x = [2, 0, 5, 3]
    y = [1, 0, 5, 1]

    # Create an instance of the CanberraDistance class (or directly use the function if it is provided)
    canberra_dist = CanberraDistance()

    # Calculate the distance between the two vectors
    distance = canberra_dist.calculate(x, y)

    # Print the result
    rint(f"The Canberra distance between vectors x and y is: {distance}")

**Reference:**

Lance, G. N., & Williams, W. T. (1966). A General Theory of Classificatory Sorting Strategies: 1. Hierarchical Systems. *The Computer Journal*, 9(4), 373-380. doi:10.1093/comjnl/9.4.373

**Conclusion:**

The Canberra distance is a valuable metric when working with data that may have different ranges or when smaller values should be given more emphasis. Its sensitivity to changes near zero makes it particularly useful in applications such as clustering, anomaly detection, and various forms of classification. This distance metric can be an excellent choice when you need to capture the relative importance of smaller differences in data.

