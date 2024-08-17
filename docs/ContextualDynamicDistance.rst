Contextual Dynamic Distance
===========================

Introduction
------------

The **Contextual Dynamic Distance (CDD)** is a novel distance measure proposed by Yves Mercadier in the context of his research in artificial intelligence (AI). This distance metric is designed to account for the contextual similarities between objects, making it especially useful in tasks where context plays a critical role, such as sentiment analysis, recommendation systems, and personalized learning algorithms.

Formula
-------

The CDD is calculated using a combination of traditional distance metrics and a context-aware weighting function. The formula can be expressed as:

.. math::

    \text{CDD}(x, y) = \sqrt{\sum_{i=1}^{n} w(x_i, y_i, C_x, C_y) \cdot (x_i - y_i)^2}

Where:

- :math:`x` and :math:`y` are the objects being compared, each represented by an n-dimensional vector.

- :math:`C_x` and :math:`C_y` represent the contextual information associated with :math:`x` and :math:`y`, respectively.

- :math:`w(x_i, y_i, C_x, C_y)` is a context-aware weighting function that dynamically adjusts based on the Galois Lattice of the contexts.

### Galois Lattice-Based Context Weighting

The context-aware weighting function :math:`w(x_i, y_i, C_x, C_y)` is computed based on the similarities and relationships identified through a Galois Lattice constructed over the contextual attributes. The Galois Lattice captures the inherent structure of the context, providing a more meaningful distance measure that considers the underlying relationships between the contexts.

History
-------

The Contextual Dynamic Distance was proposed by Yves Mercadier as a result of his work on incorporating context into AI systems. Traditional distance measures often ignore the rich contextual information available in many applications, leading to suboptimal performance. By integrating context into the distance calculation, CDD offers a more nuanced and accurate measure of similarity, particularly in applications where context significantly influences the data.

Example of Usage
----------------

Let's consider a simple example where we use the Contextual Dynamic Distance in a sentiment analysis task. Below is an illustration of how CDD can be integrated into a neural network:

.. code-block:: python
   :caption: Example 1

    from distancia import ContextualDynamicDistance

    # Feature vectors
    x = [1.0, 2.0, 3.0]
    y = [4.0, 5.0, 6.0]

    # Context vectors
    context_x = [0.2, 0.3, 0.5]
    context_y = [0.1, 0.4, 0.6]

    # Calculate Cosine Similarity
    similarity = ContextualDynamicDistance().distance(x,y,context_x, context_y)

    print(f"Contextual Dynamic Distance: {similarity}")

.. code-block:: bash
        >>> Contextual Dynamic Distance: 5.196152417906096


.. code-block:: python
   :caption: Example 2

    import torch
    import torch.nn as nn
    import torch.optim as optim
    import numpy as np
    import matplotlib.pyplot as plt

    # Step 1: Create a simple synthetic dataset with contexts
    def generate_data(num_samples):
        np.random.seed(42)
        X = np.random.rand(num_samples, 2)
        Y = (X[:, 0] + X[:, 1] > 1).astype(np.float32)
        context = np.random.rand(num_samples, 2)  # Random context for each point
        return X, Y, context

    X, Y, context = generate_data(100)
    X_train, Y_train, context_train = torch.tensor(X, dtype=torch.float32), torch.tensor(Y, dtype=torch.float32), torch.tensor(context,     dtype=torch.float32)

    # Step 2: Define the Neural Network
    class SimpleNN(nn.Module):
        def __init__(self):
            super(SimpleNN, self).__init__()
            self.fc1 = nn.Linear(2, 10)
            self.fc2 = nn.Linear(10, 1)
        
        def forward(self, x):
            x = torch.relu(self.fc1(x))
            x = torch.sigmoid(self.fc2(x))
            return x

    # Custom loss function incorporating CDD
    def cdd_loss(output, target, context, model):
        cdd = ContextualDynamicDistance(convolution_context_weight_func)
        distance_sum = 0.0
    
        for i in range(len(output)):
            for j in range(len(output)):
                if i != j:
                    distance_sum += cdd.calculate(output[i].detach().numpy(), output[j].detach().numpy(), 
                                              context[i].detach().numpy(), context[j].detach().numpy())
    
        binary_cross_entropy = nn.BCELoss()(output.squeeze(), target)
        return binary_cross_entropy + 0.01 * distance_sum  # Adding CDD as regularization

    # Instantiate the network, optimizer, and train
    model = SimpleNN()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    num_epochs = 100
    for epoch in range(num_epochs):
        model.train()
        optimizer.zero_grad()
        output = model(X_train)
        loss = cdd_loss(output, Y_train, context_train, model)
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    # Step 3: Visualization of Decision Boundary
    def plot_decision_boundary(model, X, context):
        x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
        y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
        grid = np.c_[xx.ravel(), yy.ravel()]
    
        with torch.no_grad():
            context_test = np.random.rand(len(grid), 2)  # Random context for test points
            context_test = torch.tensor(context_test, dtype=torch.float32)
            grid_tensor = torch.tensor(grid, dtype=torch.float32)
            Z = model(grid_tensor).reshape(xx.shape)
    
        plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.RdYlBu)
        plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolor='k', cmap=plt.cm.RdYlBu)
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('Decision Boundary with Contextual Dynamic Distance')
        plt.show()

    # Plot the decision boundary
    plot_decision_boundary(model, X, context)



References
----------

Wille, R. (1982). Restructuring lattice theory: an approach based on hierarchies of concepts. In I. Rival (Ed.), Ordered sets (pp. 445-470). Dordrecht: Reidel.

***How Galois Lattices Contribute to Contextual Dynamic Distance**

The reference you mentioned on the relationship between Galois lattices and context plays a crucial role in enhancing the Contextual Dynamic Distance (CDD) measure, especially in the way context is incorporated into the similarity computation. Here’s how:

1. Enhanced Context Sensitivity

Galois Lattice-Based Context Weighting: Galois lattices are used to structure and analyze the relationships between different contexts in the data. By employing a Galois lattice, we can more effectively model the hierarchical and multi-dimensional nature of context. This allows the CDD to adjust the weights applied to different contextual factors dynamically, depending on the relationship between contexts.

Contextual Interactions: The Galois lattice framework makes it possible to identify and leverage complex interactions between contexts, something traditional distance measures typically overlook. This enhances the ability of CDD to differentiate between similar and dissimilar objects based on nuanced contextual cues.

2. Improved Flexibility and Accuracy

Dynamic Weight Adjustment: The use of a Galois lattice enables dynamic adjustment of the weights used in the distance computation. Unlike static weight assignment, which may not adapt well to all contexts, Galois lattices allow the CDD to fine-tune the influence of each context based on the specific data being analyzed.

Precision in Contextual Representation: The precise, formal structure provided by Galois lattices ensures that all relevant contexts are considered and represented accurately in the distance computation. This reduces the risk of context oversimplification and enhances the overall precision of the distance measure.

3. Application in Sentiment Analysis

Contextual Sentiment Analysis: In sentiment analysis, for instance, the application of Galois lattices allows the CDD to more accurately capture the influence of surrounding words (context) on the sentiment of a target word or phrase. This leads to a more nuanced understanding of sentiment that can adapt to various contexts, thereby improving classification accuracy.

4. Scholarly Foundation

Academic Reference: The integration of Galois lattices into the CDD is backed by academic research that has established the effectiveness of Galois lattices in representing and analyzing complex contextual relationships. This scholarly foundation not only lends credibility to the CDD but also opens avenues for further research and refinement.
In summary, the incorporation of Galois lattices into the Contextual Dynamic Distance provides a sophisticated mechanism for weighting and adjusting the influence of different contexts in similarity computations. This results in a more accurate, flexible, and context-sensitive distance measure that can be particularly beneficial in applications such as sentiment analysis and beyond.

Conclusion
----------

The Contextual Dynamic Distance is a powerful tool that brings contextual awareness into distance calculations, providing significant benefits in areas where context matters. Its integration into AI systems offers a more accurate and effective way to measure similarity, leading to improved performance in a variety of applications, from sentiment analysis to recommendation systems.

As with any new measure, it's essential to carefully consider the specific requirements and characteristics of your data and application. The CDD offers a unique approach to distance calculation, and its impact on your models can be significant, particularly in context-rich environments.
