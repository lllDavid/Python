from PIL import Image

def to_bin(message):
    return ''.join(format(ord(c), '08b') for c in message) + '1111111111111110'

def encode(image_path, message, output_path):
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())
    binary = to_bin(message)
    if len(binary) > len(pixels) * 3:
        raise ValueError("Message too large for image")
    
    new_pixels = []
    i = 0
    for pixel in pixels:
        if i < len(binary):
            r, g, b = [int(format(c, '08b')[:-1] + binary[i+j], 2) if i+j < len(binary) else c 
                       for j, c in enumerate(pixel)]
            i += 3
            new_pixels.append((r, g, b))
        else:
            new_pixels.append(pixel)
    
    img.putdata(new_pixels)
    img.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def decode(image_path):
    img = Image.open(image_path).convert('RGB')
    binary = ''.join(format(c, '08b')[-1] for pixel in img.getdata() for c in pixel[:3])
    chars = []
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if byte == '11111110':
            break
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

encode('input.png', 'This is a secret message', 'output.png')
print(decode('output.png'))