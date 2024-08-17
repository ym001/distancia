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
X_train, Y_train, context_train = torch.tensor(X, dtype=torch.float32), torch.tensor(Y, dtype=torch.float32), torch.tensor(context, dtype=torch.float32)

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
