import pandas as pd
from custom_dataset import ImageDataset


from torch.utils.data import random_split
from torchvision import transforms

# Initialize your dataset
transform = transforms.ToTensor()
csv_file = "PyTorch/test/labels.csv"
dataset = ImageDataset( csv_file= csv_file,root_dir="PyTorch/test/cats_dogs_images", transform=transform)

# Check the length of the dataset
dataset_length = len(dataset)
print(f"Dataset length: {dataset_length}")

# Verify that the split sizes add up to the dataset length
train_size = int(0.8 * dataset_length)  # 80% training
val_size = dataset_length - train_size   # 20% validation

# Ensure they sum up correctly
if train_size + val_size == dataset_length:
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
    print("Dataset split successfully.")
else:
    print(f"Error: train_size + val_size does not equal dataset_length! ({train_size + val_size} != {dataset_length})")
