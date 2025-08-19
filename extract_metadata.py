from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

imagename = r""
image = Image.open(imagename)

print(f"{'Filename':25}: {image.filename}")
print(f"{'Size':25}: {image.size}")
print(f"{'Height':25}: {image.height}")
print(f"{'Width':25}: {image.width}")
print(f"{'Format':25}: {image.format}")
print(f"{'Mode':25}: {image.mode}")
print(f"{'Animated':25}: {getattr(image, 'is_animated', False)}")
print(f"{'Frames':25}: {getattr(image, 'n_frames', 1)}")

exif = image.getexif()
if exif:
    print("\nEXIF Metadata:")
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        if isinstance(value, bytes):
            value = value.decode(errors="ignore")
        print(f"{tag:25}: {value}")

    date_taken = exif.get(36867) or exif.get(306)  
    if date_taken:
        print("\nDate Taken: ", date_taken)

    gps_info = exif.get(34853)  
    if gps_info:
        print("\nGPS Data:")
        for key, val in gps_info.items():
            print(f"{GPSTAGS.get(key, key):25}: {val}")
else:
    print("\nNo EXIF data found.")