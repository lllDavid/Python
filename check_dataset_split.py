import pandas as pd

from torch.utils.data import random_split
from torchvision import transforms

transform = transforms.ToTensor()
csv_file = "PyTorch/test/labels.csv"
# dataset = "dataset"(csv_file= csv_file,root_dir="", transform=transform)

dataset_length = len(dataset)
print(f"Dataset length: {dataset_length}")

train_size = int(0.8 * dataset_length)  
val_size = dataset_length - train_size 

if train_size + val_size == dataset_length:
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
    print("Dataset split successfully.")
else:
    print(f"Error: train_size + val_size does not equal dataset_length! ({train_size + val_size} != {dataset_length})")
