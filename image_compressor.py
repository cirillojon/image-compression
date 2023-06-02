# To run this script, you need to install Pillow library
# pip install Pillow

# To run:
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
    filepath = os.path.join(directory, filename)
    try:
        # Get the file size before compression
        size_before = os.path.getsize(filepath)
        
        # Compress and save each image
        with Image.open(filepath) as image:
            # Adjust quality to control the compression level
            image.save(filepath, optimize=True, quality=50)
        
        # Get the file size after compression
        size_after = os.path.getsize(filepath)

        # Print the success message with sizes before and after compression
        print(f"Successfully compressed {filename}. Size before: {size_before / 1024:.2f}KB. Size after: {size_after / 1024:.2f}KB.")
    except Exception as e:
        print(f"Failed to compress image {filename}. Error: {str(e)}")
