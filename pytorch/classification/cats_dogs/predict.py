import os
import torch
from torchvision import transforms
from PIL import Image
from model import CNNModel
from pathlib import Path
import pandas as pd

MODEL_PATH = Path("saved_models")
MODEL_NAME = "CNNModel.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CNNModel()
model.load_state_dict(torch.load(MODEL_SAVE_PATH, weights_only=True))
model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

labels_df = pd.read_csv("labels.csv") 
label_map = {row['filename']: row['label'] for _, row in labels_df.iterrows()}

def predict_image(image_path):
    image = Image.open(image_path).convert('RGB') 
    image = transform(image).unsqueeze(0)  
    image = image.to(device)

    with torch.no_grad():
        logits = model(image)
        prediction = torch.sigmoid(logits).item() > 0.5  
        
        return prediction

image_filenames = []
while True:
    user_input = input("Enter image paths (or type 'No' to finish): ")
    if user_input.lower() == "no":
        break
    image_filenames.append(user_input)

for image in image_filenames:
    image_path = f"images/{image}" 
    predicted_class = predict_image(image_path)

    class_names = {0: 'Dog', 1: 'Cat'}
    
    result_index = 1 if predicted_class else 0

    actual_label = label_map.get(image, "Unknown")

    resultString = f"The image {os.path.basename(image_path)} is a {class_names[result_index]}."
    print(resultString)
    print(f"Actual label from CSV: {actual_label}")
