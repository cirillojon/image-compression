# image-compression

This Python script allows the user to select JPEG and PNG images via a graphical interface and compress them.

It compresses each selected image file by reducing its quality to a given amount. After compressing each image, it displays the size of the image before and after compression.

## Dependencies
To run this script, you need to install Pillow library:

pip install Pillow

## Usage 
1. Run the script using Python: `python image_compressor.py`
2. A file dialog will appear. Navigate to your images and select the ones you want to compress (you can select multiple images using Ctrl-click or Shift-click).
3. The selected images will be compressed in-place and their original versions will be replaced. 

Note: Always make sure to keep backups of your original images, as the compression process is lossy and the original images cannot be recovered after compression.

## Output
You should see output similar to the following for each image:

Successfully compressed example.jpg. Size before: 1000.00KB. Size after: 500.00KB.

In case of any errors during the compression process (for example, if an image file cannot be opened or saved), the script will display an error message for that image.

## Code
The code for this script can be found in `image_compressor.py`.
