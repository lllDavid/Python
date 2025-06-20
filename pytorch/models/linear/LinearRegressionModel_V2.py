import torch
from torch import nn
import matplotlib.pyplot as plt

# === Device configuration ===
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using: {device}")

# === Define true parameters and generate data ===
weight = 0.7
bias = 0.3

X = torch.arange(0, 1, 0.02).unsqueeze(dim=1)
y = weight * X + bias

# === Train/Test split ===
split_idx = int(0.8 * len(X))
X_train, y_train = X[:split_idx], y[:split_idx]
X_test, y_test = X[split_idx:], y[split_idx:]

# === Visualization ===
def plot_predictions(train_data=X_train,
                     train_labels=y_train,
                     test_data=X_test,
                     test_labels=y_test,
                     predictions=None):
    plt.figure(figsize=(10, 7))
    plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")
    plt.scatter(test_data, test_labels, c="g", s=4, label="Testing data")
    if predictions is not None:
        plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")
    plt.legend(prop={"size": 14})

plot_predictions(X_train, y_train, X_test, y_test)

# === Define model ===
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(in_features=1, out_features=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(x)

# === Initialize model ===
torch.manual_seed(42)
model = LinearRegressionModel().to(device)

# === Loss and optimizer ===
loss_fn = nn.L1Loss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# === Prepare data for training on selected device ===
X_train, y_train = X_train.to(device), y_train.to(device)
X_test, y_test = X_test.to(device), y_test.to(device)

# === Training loop ===
torch.manual_seed(42)
epochs = 1000

for epoch in range(epochs):
    model.train()
    y_pred = model(X_train)
    loss = loss_fn(y_pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    model.eval()
    with torch.inference_mode():
        test_pred = model(X_test)
        test_loss = loss_fn(test_pred, y_test)

    if epoch % 100 == 0:
        print(f"Epoch: {epoch} | Train Loss: {loss.item():.4f} | Test Loss: {test_loss.item():.4f}")

# === Final weights and bias ===
print("\nLearned model parameters:")
print(model.state_dict())
print("Original parameters:")
print(f"weights: {weight}, bias: {bias}")

# === Final predictions plot ===
model.eval()
with torch.inference_mode():
    y_preds = model(X_test)

plot_predictions(predictions=y_preds.cpu())
