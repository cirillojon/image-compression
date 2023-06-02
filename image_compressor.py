# to run
# python image_compressor.py

import os
from PIL import Image

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Set the directory containing the images
directory = os.path.join(current_directory, 'images')

# only these file types will be compressed
valid_extensions = ['jpg', 'jpeg', 'png']

image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) 
               and f.lower().split('.')[-1] in valid_extensions]

for filename in image_files:
    try:
        # Compress and save each image
        with Image.open(os.path.join(directory, filename)) as image:
            image.save(os.path.join(directory, filename), optimize=True, quality=85)
    except Exception as e:
        print(f"Failed to compress image {filename}. Error: {str(e)}")
