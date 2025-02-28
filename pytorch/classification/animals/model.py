import torch
from torch import nn

class AnimalCNNModel(nn.Module):
    def __init__(self, num_classes: int):
        super(AnimalCNNModel, self).__init__()
        
        self.conv_layers = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1),  
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  

            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),  
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  
            
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1), 
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)   
        )
        
        self.fc_layers = nn.Sequential(
            nn.Flatten(),  
            nn.Linear(128 * 16 * 16, 256),  
            nn.ReLU(),
            nn.Linear(256, num_classes)  
        )

    def forward(self, x):
        x = self.conv_layers(x) 
        x = self.fc_layers(x)     
        return x
