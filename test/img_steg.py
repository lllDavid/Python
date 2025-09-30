import cv2
import numpy as np

def text_to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text)

def hide_text(image_path, output_path, text):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img.shape[2] == 3:
        alpha_channel = np.ones((img.shape[0], img.shape[1], 1), dtype=np.uint8) * 255
        img = np.concatenate([img, alpha_channel], axis=2)

    binary_text = text_to_bin(text) + '1111111111111110' 
    data_index = 0
    rows, cols, _ = img.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(3): 
                if data_index < len(binary_text):
                    img[i, j, k] = np.bitwise_or(np.bitwise_and(img[i, j, k], 254), int(binary_text[data_index]))

                    data_index += 1

    cv2.imwrite(output_path, img)
    print(f"Text hidden in {output_path}")

def extract_text(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    binary_text = ''
    rows, cols, _ = img.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                binary_text += str(img[i, j, k] & 1)

    chars = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    text = ''
    for char in chars:
        if char == '11111111':
            break
        text += chr(int(char, 2))
    return text

hide_text("image.PNG", "output.png", "A secret")
message = extract_text("output.png")
print("Extracted message:", message)