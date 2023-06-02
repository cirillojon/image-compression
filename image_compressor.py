import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def compress_image(filepath):
    try:
        # Get the file size before compression
        size_before = os.path.getsize(filepath)
        
        # Compress and save each image
        with Image.open(filepath) as image:
            # Adjust quality to control the compression level
            image.save(filepath, optimize=True, quality=25)
        
        # Get the file size after compression
        size_after = os.path.getsize(filepath)

        # Print the success message with sizes before and after compression
        print(f"Successfully compressed {os.path.basename(filepath)}. Size before: {size_before / 1024:.2f}KB. Size after: {size_after / 1024:.2f}KB.")
    except Exception as e:
        print(f"Failed to compress image {os.path.basename(filepath)}. Error: {str(e)}")

# Create a Tk root widget
root = Tk()

# Hide the main window
root.withdraw()

# Raise the file dialog to the front of screen
root.lift()
root.attributes('-topmost',True)

# Only these file types will be opened
filetypes = [('JPEG files', '*.jpg'), ('JPEG files', '*.jpeg'), ('PNG files', '*.png')]

# Open the file dialog
filepaths = askopenfilenames(filetypes=filetypes)

# Compress each selected image
for filepath in filepaths:
    compress_image(filepath)

# Destroy the root widget
root.destroy()
