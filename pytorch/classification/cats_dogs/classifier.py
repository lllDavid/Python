import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms
from model import CNNModel
from dataset import ImageDataset
from pathlib import Path

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Running on {device}")

batch_size = 32
num_epochs = 10

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])


dataset = ImageDataset(folder_path='images', transform=transform)

train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size

train_set, test_set = torch.utils.data.random_split(dataset, [train_size, test_size])

train_loader = DataLoader(dataset=train_set, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_set, batch_size=batch_size, shuffle=False)

model = CNNModel().to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(params=model.parameters(), lr=0.001)  

for epoch in range(num_epochs):
    model.train()
    losses = []
    
    for data, targets in train_loader:
        data, targets = data.to(device), targets.float().to(device)

        scores = model(data)
        loss = criterion(scores.squeeze(), targets)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        losses.append(loss.item())

    print(f'Epoch {epoch}/{num_epochs}, Loss: {sum(losses)/len(losses):.4f}')

def check_accuracy(loader, model):
    model.eval()
    num_correct, num_samples = 0, 0
    
    with torch.no_grad():
        for data, targets in loader:
            data, targets = data.to(device), targets.float().to(device)

            scores = model(data)
            predictions = (torch.sigmoid(scores).squeeze() > 0.5).float()
            num_correct += (predictions == targets).sum().item()
            num_samples += predictions.size(0)

    accuracy = (num_correct / num_samples) * 100
    print(f'Test Accuracy: {accuracy:.2f}%')

check_accuracy(test_loader, model)

MODEL_PATH = Path("saved_models")
MODEL_PATH.mkdir(parents=True, exist_ok=True)
MODEL_NAME = "CNNModel.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

print(f"Saving model to: {MODEL_SAVE_PATH}")
torch.save(obj=model.state_dict(), f=MODEL_SAVE_PATH)
