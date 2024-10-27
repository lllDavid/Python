from PIL import Image
import os

def resize_images(directory, size):
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            img_path = os.path.join(directory, filename)
            img = Image.open(img_path)
            img = img.resize(size)
            img.save(img_path)
            print(f"Resized {filename}")

if __name__ == "__main__":
    resize_images("/path/to/your/images", (800, 600))