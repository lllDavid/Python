import torch
import torch.nn as nn
# Simplest possible linear regression model

# Input(x) and expected output(y) tensors
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]]) 
y = torch.tensor([[1.0], [2.0], [3.0], [4.0]]) 

# Define model
model = nn.Linear(1, 1)

# Loss and optimizer
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Train the model
for epoch in range(1000):
    optimizer.zero_grad()
    outputs = model(x)
    loss = loss_fn(outputs, y)
    loss.backward()
    optimizer.step()

# Check learned parameters
for name, param in model.named_parameters():
    print(f"{name}: {param.data}")

# Prediction for x = 5.0
input = torch.tensor([[5.0]])
prediction = model(input).item()
print(f"Predcition: {prediction:.2f}")