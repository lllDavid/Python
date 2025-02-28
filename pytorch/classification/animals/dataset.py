import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from PIL import Image

class AnimalImageDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.root_dir = root_dir
        self.annotations = pd.read_csv(csv_file)
        self.transform = transform 
        
        unique_labels = self.annotations.iloc[:, 1].unique()
        self.label_map = {label: idx for idx, label in enumerate(unique_labels)}
        
        self.total_images_count = len(os.listdir(self.root_dir))
        self.loaded_images_count = 0

    def __len__(self):
        return len(self.annotations)
    
    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.annotations.iloc[index, 0])
        image = Image.open(img_path).convert("RGB")

        self.loaded_images_count += 1
        if self.loaded_images_count <= self.total_images_count:
            print(f"Loading image: {self.loaded_images_count} of {self.total_images_count}")

        y_label_str = self.annotations.iloc[index, 1]
        y_label = self.label_map.get(y_label_str)
        if y_label is None:
            raise ValueError(f"Unknown label: {y_label_str}")

        y_label = torch.tensor(y_label, dtype=torch.long)

        if self.transform:
            image = self.transform(image)

        return image, y_label
