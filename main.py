from PIL import Image
import os

class Error(Exception):

    pass

def convert_image(image_path, image_type):

    im = Image.open(image_path)

    im = im.convert('RGB')
    image_name = os.path.basename(image_path).split('.')[0]
    print(f"This is the image name: {image_name}")

    if image_type == 'jpg' or image_type == 'png':
        im.save(os.path.join('compressed', f"Converted-to-next-gen-format-{image_name}.webp"), 'webp')
    else:
        raise Error

if not os.path.exists('compressed'):
    os.makedirs('compressed')

images = [file for file in os.listdir() if file.lower().endswith(('jpg', 'png'))]

for image in images:
    if image.lower().endswith('jpg'):
        convert_image(image, image_type='jpg')
    elif image.lower().endswith('png'):
        convert_image(image, image_type='png')
    else:
        raise Error