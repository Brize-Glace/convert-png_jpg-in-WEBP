from PIL import Image
import os

class Error(Exception):
    """Base class for other exceptions"""
    pass

def convert_image(image_path, image_type):
    # 1. Opening the image:
    im = Image.open(image_path)
    # 2. Converting the image to RGB colour:
    im = im.convert('RGB')
    # 3. Splitting the image path (to avoid the .jpg or .png being part of the image name):
    image_name = os.path.basename(image_path).split('.')[0]
    print(f"This is the image name: {image_name}")

    # Saving the images based upon their specific type:
    if image_type == 'jpg' or image_type == 'png':
        im.save(os.path.join('compressed', f"Converted-to-next-gen-format-{image_name}.webp"), 'webp')
    else:
        # Raising an error if we didn't get a jpeg or png file type!
        raise Error

# Create the directory if it doesn't exist
if not os.path.exists('compressed'):
    os.makedirs('compressed')

# Get all images in the directory
images = [file for file in os.listdir() if file.lower().endswith(('jpg', 'png'))]

# Loop through all images
for image in images:
    if image.lower().endswith('jpg'):
        convert_image(image, image_type='jpg')
    elif image.lower().endswith('png'):
        convert_image(image, image_type='png')
    else:
        raise Error