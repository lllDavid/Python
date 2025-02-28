import torch
from torchvision import transforms
from PIL import Image
from model import AnimalCNNModel 
from pathlib import Path
import pandas as pd

MODEL_PATH = Path("saved_models")
MODEL_NAME = "AnimalCNNModel.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AnimalCNNModel(num_classes=3)
model.load_state_dict(torch.load(MODEL_SAVE_PATH, weights_only=True))
model.to(device)
model.eval() 

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

labels_df = pd.read_csv("labels.csv") 
label_map = {row['fname']: row['label'] for _, row in labels_df.iterrows()}

def predict_image(image_path):
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)  
    image = image.to(device)

    with torch.no_grad():
        scores = model(image)
        _, predicted = scores.max(1)
        return predicted.item()

image_filenames = []
quit = None
while quit != "No":
    user_input = input("Enter image paths:")
    image_filenames.append(user_input)
    quit = input("Add more ? Yes/No:")
for image in image_filenames:
    image_path = f"images/{image}" 
    predicted_class = predict_image(image_path)

    class_names = {0: 'Bird', 1: 'Cat', 2: 'Dog'}

    actual_label = label_map.get(image, "Unknown")

    print(f"The predicted class is: {class_names[predicted_class]}")
    print(f"Actual label from CSV: {actual_label}")
