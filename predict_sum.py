import torch
from torch import nn

num_samples = 1000
epochs = 1000
learning_rate = 0.01

X = []
y = []

for _ in range(num_samples):
    a = torch.randint(1, 10, (1,)).float() 
    b = torch.randint(1, 10, (1,)).float()  
    X.append(torch.cat((a, b)))  
    y.append(a + b) 

X = torch.stack(X)  
y = torch.stack(y)

class SumModel(nn.Module):
    def __init__(self):
        super(SumModel, self).__init__()
        self.fc = nn.Linear(2, 1)  

    def forward(self, x):
        return self.fc(x)

model = SumModel()
loss_fn = nn.MSELoss() 
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

for epoch in range(epochs):
    y_pred = model(X)
    loss = loss_fn(y_pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}')

with torch.no_grad():
    test_input = torch.tensor([[6.5, 8.3]])  
    predicted = model(test_input)
    print(f'Input: {test_input.flatten().tolist()}, Predicted Sum: {predicted.item()}')

with torch.no_grad():
    test_input2 = torch.tensor([[3.2, 7.9]]) 
    predicted2 = model(test_input2)
    print(f'Input: {test_input2.flatten().tolist()}, Predicted Sum: {predicted2.item()}')