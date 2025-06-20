import torch
from torch import nn
import numpy as np
import matplotlib.pyplot as plt

# === Setup known parameters ===
weight = 0.7
bias = 0.3

# === Generate synthetic data ===
X = torch.arange(0, 1, 0.02).unsqueeze(dim=1)
y = weight * X + bias

# === Train/Test split ===
split_index = int(0.8 * len(X))
X_train, y_train = X[:split_index], y[:split_index]
X_test, y_test = X[split_index:], y[split_index:]

# === Define Linear Regression Model ===
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1, dtype=torch.float, requires_grad=True))
        self.bias = nn.Parameter(torch.randn(1, dtype=torch.float, requires_grad=True))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias

# === Model initialization ===
torch.manual_seed(42)
model = LinearRegressionModel()

# === Loss function and optimizer ===
loss_fn = nn.L1Loss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# === Training loop setup ===
epochs = 200
epoch_log = []
train_losses = []
test_losses = []

# === Training loop ===
for epoch in range(epochs):
    model.train()
    y_pred = model(X_train)
    loss = loss_fn(y_pred, y_train)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Evaluation
    model.eval()
    with torch.inference_mode():
        test_pred = model(X_test)
        test_loss = loss_fn(test_pred, y_test.type(torch.float))

    if epoch % 10 == 0:
        epoch_log.append(epoch)
        train_losses.append(loss.item())
        test_losses.append(test_loss.item())
        print(f"Epoch: {epoch} | Train Loss: {loss.item():.4f} | Test Loss: {test_loss.item():.4f}")

# === Optional: Plot loss curves ===
"""
plt.plot(epoch_log, train_losses, label="Train Loss")
plt.plot(epoch_log, test_losses, label="Test Loss")
plt.title("Training and Test Loss Curves")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()
"""
