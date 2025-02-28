from torch.utils.data import Dataset
import os
from PIL import Image

class ImageDataset(Dataset):
    def __init__(self, folder_path, transform=None):
        self.folder_path = folder_path
        self.transform = transform
        self.images = []
        self.labels = []
        self.total_images_count = os.listdir(folder_path)

        for filename in self.total_images_count:
            if filename.endswith(('.jpg', '.png')):
                self.images.append(os.path.join(folder_path, filename))
                label = 1 if 'cat' in filename.lower() else 0 if 'dog' in filename.lower() else None
                if label is not None:
                    self.labels.append(label)

        self.loaded_images_count = 0

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = self.images[idx]
        image = Image.open(img_path).convert('RGB')
        self.loaded_images_count += 1
        if self.loaded_images_count <= len(self.total_images_count):
            print(f"Loading image: {self.loaded_images_count} of {len(self.total_images_count)}")
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label
