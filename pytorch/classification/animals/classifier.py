import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms
from model import AnimalCNNModel 
from dataset import AnimalImageDataset
from pathlib import Path

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Running on {device}")

batch_size = 32
num_epochs = 10
num_classes = 3  

transform = transforms.Compose([
    transforms.Resize((128, 128)), 
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  
])

dataset = AnimalImageDataset(csv_file="labels.csv", root_dir="images", transform=transform)

train_set, test_set = torch.utils.data.random_split(dataset, [25000, 5000]) 

train_loader = DataLoader(dataset=train_set, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_set, batch_size=batch_size, shuffle=True)

model = AnimalCNNModel(num_classes=num_classes)
model.to(device)
criterion = nn.CrossEntropyLoss()  
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(num_epochs):
    model.train()
    losses = []
    
    for batch_idx, (data, targets) in enumerate(train_loader):
        data, targets = data.to(device), targets.to(device)

        scores = model(data)
        loss = criterion(scores, targets)
        losses.append(loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    avg_loss = sum(losses) / len(losses)
    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}')

def check_accuracy(loader, model):
    model.eval()
    num_correct = 0
    num_samples = 0

    with torch.no_grad():
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum().item()
            num_samples += predictions.size(0)

    accuracy = float(num_correct / num_samples) * 100
    print(f"{num_correct} / {num_samples} correct ({accuracy:.2f}%)")

print("Accuracy on training set:")
check_accuracy(train_loader, model)

print("Accuracy on test set:")
check_accuracy(test_loader, model)

MODEL_PATH = Path("saved_models")
MODEL_PATH.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "AnimalCNNModel.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

print(f"Saving model to: {MODEL_SAVE_PATH}")
torch.save(obj=model.state_dict(), f=MODEL_SAVE_PATH)

loaded_model_1 = AnimalCNNModel(3)
loaded_model_1.load_state_dict(torch.load(MODEL_SAVE_PATH,weights_only=True))
loaded_model_1.to(device)
