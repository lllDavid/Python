import torch
import torch.nn as nn

# Defines a simple autoencoder that compresses 784-dimensional input into 32 features and reconstructs it back
class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Linear(784, 32)
        self.decoder = nn.Linear(32, 784)

    def forward(self, x):
        x = self.encoder(x)
        x = torch.relu(x)     
        x = self.decoder(x)
        x = torch.sigmoid(x)  
        return x

model = Autoencoder()
input_data = torch.randn(1, 784)  
output = model(input_data)
print(output.shape) 