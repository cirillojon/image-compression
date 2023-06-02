# image-compression

This Python script compresses all JPEG and PNG images in the 'images' directory (located in the same folder as the script). 

It compresses each image file by reducing its quality by a given amount.

After compressing each image, it displays the size of the image before and after compression.

## Imports
To run this script, you need to install Pillow library

pip install Pillow

## Usage 
Place your image files in a directory called 'images' located in the same directory as the script.

Adjust the quality variable as you see fit.

Run the script using Python: python image_compressor.py

## Ouput
You should see output similar to the following for each image:

Successfully compressed example.jpg. Size before: 1000.00KB. Size after: 500.00KB.

