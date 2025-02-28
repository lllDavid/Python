import torch
from torch import nn
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

### Setup
# Create known parameters
weight = 0.7
bias = 0.3

# Create data
start = 0
end = 1
step = 0.02
X = torch.arange(start, end, step).unsqueeze(dim=1)
y = weight * X + bias

# Create a train/test split
train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

len(X_train), len(y_train), len(X_test), len(y_test)

### Build model
# Create linear regression model class
class LinearRegressionModelV1(nn.Module): 
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))
        self.bias = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))
    
    # Forward method to define the computation in the model
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias  # Linear regression formula

# Create random seed
torch.manual_seed(42)

# Create an instance of the model
model_0 = LinearRegressionModelV1()

# Check parameters
# print(list(model_0.parameters()))
# print(model_0.state_dict())

### Train model
# Setup loss function
loss_fn = nn.L1Loss()

# Setup optimizer (stochastic gradient descent)
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.01)  # Learning rate 

### Train loop
# epochs = one loop through data
epochs = 200

# Track values
epoch_count = []
loss_values = []
test_loss_values = []

# Loop through data
for epoch in range(epochs):
    # Set model to training mode
    model_0.train()

    # 1. Forward pass
    y_pred = model_0(X_train)

    # 2. Calculate the loss
    loss = loss_fn(y_pred, y_train)

    # 3. Optimizer zero grad
    optimizer.zero_grad()

    # 4. Perform backpropagation on the loss with respect to parameters in model
    loss.backward()

    # 5. Step the optimizer (perform gradient descent)
    optimizer.step()

    ### Testing
    model_0.eval()

    with torch.inference_mode():
        # Forward pass
        test_pred = model_0(X_test)

        # Calculate the loss
        test_loss = loss_fn(test_pred, y_test.type(torch.float))

        if epoch % 10 == 0: 
            epoch_count.append(epoch)
            loss_values.append(loss)
            test_loss_values.append(test_loss)
            print(f"Epoch: {epoch} | Loss: {loss} | Test loss: {test_loss}")

            # Plot loss curves
            '''
            plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Train loss")
            plt.plot(epoch_count, test_loss_values, label="Test loss")
            plt.title("Training and test loss curves")
            plt.ylabel("Loss")
            plt.xlabel("Epochs")
            plt.legend();
            plt.show()
            '''


